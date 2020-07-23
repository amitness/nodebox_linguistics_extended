# Nodebox Linguistics Extended (Python 3 Version) [![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
## Overview 
This repository is a modified fork of Tom De Smedt's [Nodebox English Linguistics library](https://www.nodebox.net/code/index.php/Linguistics), which bundles WordNet, NLTK, and other useful modules.

It is used as part of the openly-available Python version of the Rensa framework, which was introduced in the following paper:

```
@phdthesis{harmon2017narrative,
  title={Narrative Encoding for Computational Reasoning and Adaptation},
  author={Harmon, Sarah M},
  year={2017},
  school={University of California, Santa Cruz}
}
```

## Installation 
To install, download the repository and install using setup.py:
```
python setup.py install
```

You can also install it directly from the repo as:
```
pip install git+https://github.com/amitness/nodebox_linguistics_extended
```

## Usage
For convenience, import in python as follows:
```
import nodebox_linguistics_extended as nle
```

You can then call the original Nodebox commands.  For example:
```
print nle.verb.infinitive("swimming")
```
...will print the word "swim".
