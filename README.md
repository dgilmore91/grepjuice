# GrepJuice - Find questions to answers!

Currently uses two files:
- A skimmer that pulls in data `skimmer.py`
- A cleaner that cleans up results obtained via the skimmer `*cleaner.py`

## Requirements before setup

Must have the latest version of Python (>2.7) installed as this project requires pip to install packages.

## Usage
We will be using a virtual environment for Python so that we can manage Python packages properly. To install virtualenv run (may require sudo at the start if permissions are a problem):
```bash
pip install virtualenv
```
To create a virtual environment after virtualenv is installed change to the project directory and run:
```bash
virtualenv .
```

To start the virtual environment that you have created within the project run from project root:
```bash
source bin/activate
```

To install all requirements onto the virtualenv run:
```bash
pip install -r requirements.txt
```

To obtain a set of results just run from project root:
```bash
python data-gathering/skimmer.py
```

There should be an output file called search_results.txt in the project root folder.
