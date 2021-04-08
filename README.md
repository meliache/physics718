# Programming for Physicists

## Prerequisites

## Conda Installation

We use [conda](https://www.anaconda.com) to provide a python environment with
all packages that you need for the exercises. Follow [these
instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
from the conda documentation to download and install Miniconda for your system.
On a linux 64 bit system, the following should work:

``` bash
# download the latest linux installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# run the installer and follow the instructions
sh Miniconda3-latest-Linux-x86_64.sh
```

When prompted for

```
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
```

answer yes. Then you can create the conda environment for the exercises via

``` bash
conda env create --file environment.yml
```

Then, you should be able to activate the conda environment with

``` bash
conda activate pfp
```

With future exercise sheets, we might add python-packages to the
`environment.yml`. Then, we will ask you to update your environment via

``` bash
conda env update --file environment.yml
```

For more help on working with conda, read [getting started with
conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

## Materials for further reading

- [Software Carpentry](https://software-carpentry.org/lessons/) is a website
  which offers basic software skills for researchers. I really recommend their
  courses on
    - [Programming in Python](https://swcarpentry.github.io/python-novice-inflammation):
      Do this course if you your python is rusty, as we require familarity with the language.
    - [The Unix Shell](https://swcarpentry.github.io/shell-novice):
      I recommend working with python from a linux environment, which often
      involves working with the shell, so a basic familiarity with it is helpful.
    - [Version Control with git](https://swcarpentry.github.io/git-novice/):
      Nowadays `git` is the de-facto standard version-control system used for
      most software projects.
- [PyHEP resources](https://github.com/hsf-training/PyHEP-resources):
  Includes a python reading list that is maintained by the HEP Software
  Foundation and a list of useful python packages.

## Contributors

- [Michael Eliachevitch](meliache@uni-bonn.de)
