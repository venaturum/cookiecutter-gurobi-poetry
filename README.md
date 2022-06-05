# cookiecutter-gurobi-poetry

_An "opinionated" Cookiecutter for creating optimisation projects in Python with Gurobi and Poetry._

**An example project using this Cookiecutter template can be found here: [knapsack-example-gurobi-cookiecutter](https://github.com/venaturum/knapsack-example-gurobi-cookiecutter).**

## Requirements:
-----------
 - Python 3.8+
 - Gurobi solver, with valid license
 - [Cookiecutter]((http://cookiecutter.readthedocs.org/en/latest/installation.html))
 - [Poetry](https://python-poetry.org/docs/#installation)

## Quickstart

To start a new project, open a terminal and navigate to the folder in which you want to create the new project, then run

    cookiecutter https://github.com/venaturum/cookiecutter-gurobi-poetry.git

Change into the newly created directory then run

    poetry install

which will download and install the required dependencies, in addition to making the project an editable install.

The virtual environment can be activated with

    poetry shell

## Features

Poetry is regular member of modern Python workflows.  There are many advantages to using Poetry to manage your project, including thorough dependency resolution, virtual environments, reproducibility and editable installs - some of which are discussed below.

The template is intended to be used with object-oriented programming, which provides several benefits. It also encourages model definition to be separated away from code that uses is, such as notebooks or scripts that perform experiments with the models.  Cookiecutter also makes it easy to bake-in small, but handy features into the project, which are discussed further below.

### Dependencies

This template project has one required Python dependency: `gurobipy`.
If you wish to use the "matrixapi" functionality of `gurobipy` then `numpy` and `scipy` will also be required, but Cookiecutter will take care of this for you. The optional dependencies include:

[**gurobipy_exceptions**](https://github.com/venaturum/gurobipy_exceptions): a package available on github for patching and extending functionality related to exceptions in `gurobipy`

[**numpy**](numpy.org/): a library providing support for multi-dimensional arrays and matrices, and related functionality.

[**scipy**](https://scipy.org/): a library with many modules for scientific and technical computing, including optimisation and linear algebra.

[**pandas**](https://pandas.pydata.org/): the most popular Python package for data manipulation and analysis.

[**matplotlib**](https://matplotlib.org/): the de-facto standard library for data visualisation and graphical plotting in Python.

[**seaborn**](https://seaborn.pydata.org/): a high level interface for plotting with tidy data, based on matplotlib.

[**isort**](https://pycqa.github.io/isort/): a utility for sorting import statements according to the Python Style Guide (PEP8).

[**black**](https://github.com/psf/black): an "opinionated" code formatter which, popular among Python developers.

[**flake8**](https://flake8.pycqa.org/en/latest/): a utility for checking code against the Python Style Guide (PEP8).

[**precommit**](https://pre-commit.com/): a framework for managing and maintaining git hooks (only useful if you're using git).


The other question regarding dependencies you will be asked when using this template with Cookiecutter is whether you wish to "*use notebooks*".  This of course is referring to Jupyter notebooks, which have become a very popular tool, particular among data analysts/scientists for prototyping solutions, exploratory analysis and documenting experiments.  Note that answering "y" to this prompt will only install `ipykernel` which is the execution backend for Jupyter notebooks.  It does not install products published by Project Jupyter, such as JupyterLab or Jupyter Notebook, as there are several alternatives to these products available for working with notebooks. 


### Based on pyproject.toml

The *pyproject.toml* file has been officially adopted as the standard for project specification in Python.  It's specifications range from project metadata, to dependencies, to configuration of tools.  There are several modern tools for managing Python projects which base their functionality around the pyproject.toml file, but Poetry is arguably emerging as the clear winner.

The contents of the pyproject.toml in your `cookiecutter-gurobi-poetry` project will be dependent on the the options chosen when running Cookiecutter.  Sometimes the inclusion of two particular packages may require configuration specified in the pyproject.toml file so that they work in harmony.  This template (through Cookiecutter) will take care of that for you.

### Reproducability

Dependency resolution is not a trivial problem to solve.  Given a set of packages, and their permitted versions for the project, the problem of dependency resolution is to find a set of versions for those dependencies which are compatible.  But this also includes dependencies of dependencies (i.e. transitive dependencies).  Dependency resolution in Python has not always been thorough, and it was weaknesses in Python's offical package manager *pip* that in part motivated the creation of the Conda package manager.  Poetry uses `pip` "under the hood" but applies it's own algorithms and rules for dependency resolution.

More importantly, once dependencies are resolved, they are "pinned" in a lock file (*poetry.lock*), meaning the exact version of all dependencies, including transitive dependencies, are recorded in this file.  Whenever Poetry has access to a lock file it can reproduce the Python environment exactly.  This means that results and behaviour can be reproduced, independent of by whom, on what, or how.  Reproducible analysis is a particularly hot topic in the data analysis/science community and does not exist by default.  Coupled with [git](https://git-scm.com/) it also enables users to maintain a history of their Python environments and restore previous configurations.

### Editable install

Another nice feature of Poetry, by default, is that the project will be installed as a editable package in your environment.  This means changes made to the source code are immediately reflected by restarting the Python shell (or ipykernel if using Jupyter notebooks) - there is no need to build the project and reinstall with each change.

Thinking of the project as a package may be a leap for newcomers, but it provides several advantages, especially when it comes to importing modules that have been developed in other directories.  With respect to a project generated with this template, developers can use `from myproj.models.base import GurobiBaseModel`, for example (assuming the project slug is *myproj*), from anywhere in the code and from any directory in the shell provided the Python executable used is the one local to the virtual environment created by Poetry.

Another advantage of the project being installed as a package is discussed in the next section (`root directory reference`).

### Root directory reference

Any code that is in the top level *\_\_init\_\_.py* file can be accessed as attributes and functions on the editable installed package.  Currently this file contains a variable called `root_dir` which holds a `pathlib.Path` object corresponding to the very top level directory.  For example, if you project is called *myproj* and the root directory for the project (the one containing the pyproject.toml) has a folder called "data", which contains a file called "saved.csv", then you can access this folder with either of the two following alternatives

    import myproj
    data_folder = myproj.root_dir / "data" / "saved.csv"  # using pathlib.Path functionality

or 

    from myproj import root_dir
    data_folder = root_dir / "data" / "saved.csv"  # using pathlib.Path functionality


This is very handy for accessing input data, writing logs, saving models etc.

### Template class (and object-oriented programming)

As mentioned above, it is intended that projects produced with this template utilise object-oriented programming (OOP).  One of the main benefits, or goals, of OOP - which is shared and reinforced by templating with Cookiecutter - is "code reuse".  In OOP this is achieved through inheritance; deriving new classes from another (subclassing).  This is the idea behind the `GurobiBaseModel` (super)class, which includes features such as  

- hiding away boiler plate code
- permitting Gurobi parameters to be set as keyword arguments in the constructor
- using [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) to enable callback method to access/alter the state of objects created from subclasses of `GurobiBaseModel`
- a class method (`run`) for building and optimising model with one function call
- a class method (`make_model`) for utilising subclasses of `GurobiBaseModel` as a pipeline for producing `gurobipy.Model` objects


The nature of modelling often means several alternative models arise which share very similar structure (i.e. variables and constraints).  For example, model perfomance may want to be evaluated under different objective functions, or perhaps with the addition of tight constraints or adding a cutting plane method as a callback.  These use cases don't require the OOP approach proposed by this template but they can be handled nicely using it.


### The resulting directory structure
------------

The directory structure of your new project is created through a combination of the files and folders which can be seen in this repository, and the use of a *hook* (*hooks/post_gen_project.py*) to add and remove directories.
The resulting structure will be a subset (depending on options chosen during Cookiecutter prompt) of the following: 

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
├── problem_files/              <- User defined file formats for problem instances
|
├── scripts/                    <- A folder for .py scripts as an alternative to CLI
│
├── .pre-commit-config.yaml     <- pre-commit configuration (optional)
├── pyproject.toml              <- Project specification
├── setup.cfg                   <- Config for flake8 (optional)
├── LICENSE                     <- (optional)
└── README.md                   <- The top-level README describing your project
```

**An example project using this Cookiecutter template can be found here: [knapsack-example-gurobi-cookiecutter](https://github.com/venaturum/knapsack-example-gurobi-cookiecutter).**

## Acknowledgements

Inspired by [cookiecutter-poetry](https://github.com/johanvergeer/cookiecutter-poetry).