# Root Namer

A simple climbing route name generator.

## Preparation
Install the required python packages via the `requirements.txt` file.

### Install Required Python Packages

#### Linux
```sh
> python3 -m pip install ./requirements.txt
```

#### Windows
```sh
> py -m pip install ./requirements.txt
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

## Generate Route Names with Multiple Words
Use the command line arg `-n` to supply the integer number of words that the route name should consist of.
