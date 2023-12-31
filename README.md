# Setup

Run

```
python3 -m venv env/
```

in your terminal.

Then, restart your terminal or run

```
source env/bin/activate
```

# Installation

Run

```
pip list
pip install -r requirements.txt
pip list
```

in your terminal to install the packages listed in
[`requirements.txt`](requirements.txt).

To install a new package, run

```
pip list
pip install autopep8 # replace `autopep8` with the package name
pip list
pip freeze > requirements.txt
```

in your terminal.

# Running

Run

```
python3 p.py
```

in your terminal.

# Formatting

Run

```
autopep8 p.py --in-place
```

in your terminal to format the file `p.py`.
