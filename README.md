# Route Namer

A simple climbing route name generator.

## Preparation
Install the required python packages via the `requirements.txt` file.

### Install Required Python Packages

#### Linux
```sh
> python3 -m pip install -r ./requirements.txt
```

#### Windows
```sh
> py -m pip install -r ./requirements.txt
```

### Setup ntlk Word List
To install the required list of ~200000 english words do the following.

#### Linux
```sh
> python3
```

#### Windows
```
> py
```

At the Python interpreter type the following to open nltk's GUI that enables installation of
separate packages.

```
>>> import nltk
>>> nltk.download()
```

## Generate Route Names

#### Linux
```sh
> python3 ./route_namer.py
```

#### Windows
```sh
> py route_namer.py
```

## Argumument Help
To output a help text that explains command argmuents, add the command line parameter `-h`.

## Generate Route Names with Multiple Words
Use the command line arg `-w` to supply the integer number of words that the route name should consist of.

## Generate Multiple Names
Use the command line argument `-n` to generate multiple route names as follows.
```sh
> python3 ./route_namer.py -n 10
Middlebarreneven
Installmentedness
Intronomics
Falselycenarrow
Equiv
Motionallaxalent
Leveralliogracial
Perfluorganityro
Staticinglyingness
Putteratedlying
```

## Acknowledgements
A list of 25000 syllabified english words coming with this repo was found at [https://github.com/gautesolheim/25000-syllabified-words-list/blob/master/25K-syllabified-sorted-alphabetically.txt](https://github.com/gautesolheim/25000-syllabified-words-list/blob/master/25K-syllabified-sorted-alphabetically.txt).
