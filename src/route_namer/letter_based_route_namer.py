from nltk.corpus import words
from random import choices

class LetterBasedRouteNamer:
    def __init__(self):
        # Get a Python list of all english words
        self.word_list = words.words()

        self.analyseWordList()

    def considerWordLength(self, word_length):
        if word_length not in self.word_lengths.keys():
            self.word_lengths[word_length] = 1
        else:
            self.word_lengths[word_length] += 1

    def considerFirstLetter(self, letter):
        if not letter in self.first_letter_counts.keys():
            self.first_letter_counts[letter] = 1
        else:
            self.first_letter_counts[letter] += 1

    def considerBigraph(self, last_letter, letter):
        if not last_letter in self.bigraph_counts.keys():
            self.bigraph_counts[last_letter] = {}

        if not letter in self.bigraph_counts[last_letter].keys():
            self.bigraph_counts[last_letter][letter] = 1
        else:
            self.bigraph_counts[last_letter][letter] += 1

    def analyseWordList(self):
        ''' Count number of occurrences of english letters as well as bigraph letter
            counts and word lengths.
            All these are used for probabilistic word construction.
        '''
        self.first_letter_counts = {}
        self.letter_counts = {}
        self.bigraph_counts = {}
        self.word_lengths = {}

        for word in self.word_list:
            self.considerWordLength(len(word))

            last_letter = None
            for pos, letter in enumerate(word):

                if pos == 0:
                    self.considerFirstLetter(letter)

                if last_letter is None:
                    last_letter = letter
                    continue

                self.considerBigraph(last_letter, letter)

                last_letter = letter

        # For being eable to use the random.choices function, we need
        # to separate keys and values of our newly established dictionaries.
        self.first_letter_list = list(self.first_letter_counts.keys())
        self.first_letter_weights = list(self.first_letter_counts.values())

        self.word_length_list = list(self.word_lengths.keys())
        self.word_length_weights_list = list(self.word_lengths.values())

    def listBigraphWeights(self):
        print("bigraphs:")
        for letter, next_letter_stats in sorted(self.bigraph_counts.items()):
            print(f"{letter}:")
            for next_letter, count in sorted(next_letter_stats.items(), key=lambda x: x[1]):
                print(f"   {next_letter}: {count}")

    def generateName(self, num_generated_words):
        # First we determine the lengths of our words based on the properties
        # of english language in a probabilistic fashion.
        generated_word_lengths = choices(self.word_length_list, weights = self.word_length_weights_list, k = num_generated_words)

        # Initialize words as empty string to enable concatenation later on.
        generated_words = [""] * num_generated_words

        for i in range(0, num_generated_words):
            word_length = generated_word_lengths[i]

            current_letter = None
            for j in range(0, word_length):
                if current_letter is None:
                    # First letter is chosen based on english first letter occurrence
                    # probabilities.
                    current_letter = choices(self.first_letter_list, weights = self.first_letter_weights, k = 1)[0]
                else:
                    # Subsequent letters are chosen on bigraph probabilities
                    bc = self.bigraph_counts[current_letter]
                    current_letter = choices(list(bc.keys()), weights = list(bc.values()), k = 1)[0]
                generated_words[i] += current_letter

        for i in range(0, num_generated_words):
            generated_words[i] = generated_words[i].capitalize()

        name = " ".join(generated_words)

        return name
