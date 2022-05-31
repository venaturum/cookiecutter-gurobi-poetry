# cookiecutter-gurobi-poetry

_An "opinionated" cookiecutter for creating optimisation projects in Python with Gurobi and Poetry._

### Requirements:
-----------
 - Python 3.8+
 - Gurobi solver, with valid license
 - [Cookiecutter]((http://cookiecutter.readthedocs.org/en/latest/installation.html))
 - [Poetry](https://python-poetry.org/docs/#installation)

### Quickstart

To start a new project, open a terminal and navigate to the folder in which you want to create the new project, then run

    cookiecutter https://github.com/venaturum/cookiecutter-gurobi-poetry.git

Change into the newly created directory then run

    poetry install

which will download and install the required dependencies, in addition to making the project an editable install.

The virtual environment can be activated with

    poetry shell

### Features

**TODO**
- reproducability
- editable install
- command line
- root directory reference
- template model

**An example project using this cookiecutter template can be found here: [knapsack-example-gurobi-cookiecutter](https://github.com/venaturum/knapsack-example-gurobi-cookiecutter).**

### The resulting directory structure
------------

The directory structure of your new project will look like this: 

```
<project_slug>/
|
├── <project_slug>/
│   │
│   ├── __init__.py             <- Makes project_slug a Python module
│   ├── cli.py                  <- command line interface (optional)
│   │
│   └── models/                 <- Scripts to download or generate data
│       ├── __init__.py         <- Makes "models" a Python module
│       └── base.py             <- Contains a base class, from which to extend
│
├── logs/                       <- A folder for log files produced by Gurobi solver
│
├── model_files/                <- A place for your model files (.lp .mps etc)
│
├── notebooks/                  <- Jupyter notebooks (optional) 
|
├── problem_files/              <- user defined file formats for problem instances
│
├── .pre-commit-config.yaml     <- pre-commit configuration (optional)
├── pyproject.toml              <- Project specification
├── setup.cfg                   <- Config for flake8 (optional)
├── LICENSE                     <- (optional)
└── README.md                   <- The top-level README describing your project
```

## Acknowledgements

Inspired by [cookiecutter-poetry](https://github.com/johanvergeer/cookiecutter-poetry).