
Pysvenska: learn new words
===

Overview
---
Very basic command line utility to learn new words.
Works with csv's with two columns only.


Installation
---
```
git clone https://bitbucket.org/lk16/pysvenska
cd pysvenska
virtualenv -p `which python3` venv
. venv/bin/activate
pip install -r requirements.txt
```

Usage
---
```
# first csv column is used for questions
./quiz.py yourfile.csv

# second csv column is used for questions
./quiz.py yourfile.csv --swap
```