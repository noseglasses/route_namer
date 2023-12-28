from nltk.corpus import words
from random import choices
import os
import inspect

class SyllableBasedRouteNamer:
    def __init__(self):
        # Get a Python list of all english words
        self.word_list = words.words()

        self.analyseWordList()

    def considerWordLength(self, word_length):
        if word_length not in self.word_lengths.keys():
            self.word_lengths[word_length] = 1
        else:
            self.word_lengths[word_length] += 1

    def considerFirstSyllable(self, syllable):
        if not syllable in self.first_syllable_counts.keys():
            self.first_syllable_counts[syllable] = 1
        else:
            self.first_syllable_counts[syllable] += 1

    def considerBiSyllable(self, last_syllable, syllable):
        if not last_syllable in self.bisyllable_counts.keys():
            self.bisyllable_counts[last_syllable] = {}

        if not syllable in self.bisyllable_counts[last_syllable].keys():
            self.bisyllable_counts[last_syllable][syllable] = 1
        else:
            self.bisyllable_counts[last_syllable][syllable] += 1

    def analyseWordList(self):
        ''' Count number of occurrences of english syllables as well as bisyllable syllable
            counts and word lengths.
            All these are used for probabilistic word construction.
        '''
        self.first_syllable_counts = {}
        self.syllable_counts = {}
        self.bisyllable_counts = {}
        self.word_lengths = {}

        module_path = os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))
        syllable_file = module_path + "/../../25K-syllabified-sorted-alphabetically.txt"
        with open(syllable_file, "r") as f:
            lines = f.readlines()

        for line in lines:
            syllables = line.rstrip().split(";")
            if len(syllables) < 2:
                continue

            word = "".join(syllables)

            #print(word)

            self.considerWordLength(len(word))

            last_syllable = None

            for pos, syllable in enumerate(syllables):
                #print(f"  {syllable}")

                if pos == 0:
                    self.considerFirstSyllable(syllable)

                if last_syllable is None:
                    last_syllable = syllable
                    continue

                self.considerBiSyllable(last_syllable, syllable)

                last_syllable = syllable

        # For being eable to use the random.choices function, we need
        # to separate keys and values of our newly established dictionaries.
        self.first_syllable_list = list(self.first_syllable_counts.keys())
        self.first_syllable_weights = list(self.first_syllable_counts.values())

        self.word_length_list = list(self.word_lengths.keys())
        self.word_length_weights_list = list(self.word_lengths.values())

    def listBigraphWeights(self):
        print("bisyllables:")
        for syllable, next_syllable_stats in sorted(self.bisyllable_counts.items()):
            print(f"{syllable}:")
            for next_syllable, count in sorted(next_syllable_stats.items(), key=lambda x: x[1]):
                print(f"   {next_syllable}: {count}")

    def generateName(self, num_generated_words, word_length):
        # First we determine the lengths of our words based on the properties
        # of english language in a probabilistic fashion.
        generated_word_lengths = choices(self.word_length_list, weights = self.word_length_weights_list, k = num_generated_words)

        # Initialize words as empty string to enable concatenation later on.
        generated_words = [""] * num_generated_words

        for i in range(0, num_generated_words):
            #word_length = generated_word_lengths[i]

            last_syllable = None
            next_syllable = None
            for j in range(0, word_length):
                if last_syllable is None:
                    # First syllable is chosen based on english first syllable occurrence
                    # probabilities.
                    next_syllable = choices(self.first_syllable_list, weights = self.first_syllable_weights, k = 1)[0]
                else:
                    # Subsequent syllables are chosen on bisyllable probabilities
                    if last_syllable in self.bisyllable_counts.keys():
                        bc = self.bisyllable_counts[last_syllable]
                        next_syllable = choices(list(bc.keys()), weights = list(bc.values()), k = 1)[0]
                    else:
                        break
                if next_syllable == last_syllable:
                    continue

                generated_words[i] += next_syllable
                last_syllable = next_syllable

                if len(generated_words[i]) >= word_length:
                    break

        for i in range(0, num_generated_words):
            generated_words[i] = generated_words[i].capitalize()

        name = " ".join(generated_words)

        return name
