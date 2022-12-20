# GALACTICA Playground

The GALACTICA playground is the place to experiment with the [GALACTICA][galactica-paper] language model.

## ☑️ Requirements

Before starting the project make sure these requirements are available:

- [python][python]. For executing the code in this project.
- [git][git]. For versioning your code.

## 🛠️ Setup

### Create a python environment

First create the virtual environment where the service will store all the modules.

#### Using virtualenv

Using the `virtualenv` command, run the following commands:

```bash
# install the virtual env command
pip install virtualenv

# create a new virtual environment
virtualenv -p python ./.venv

# activate the environment (UNIX)
./.venv/bin/activate

# activate the environment (WINDOWS)
./.venv/Scripts/activate

# deactivate the environment (UNIX & WINDOWS)
deactivate
```

#### Using conda

Install [conda][conda], a program for creating python virtual environments. Then run the following commands:

```bash
# create a new virtual environment
conda create --name galactica python=3.8 pip

# activate the environment
conda activate galactica

# deactivate the environment
deactivate
```

### Install

To install the requirements run:

```bash
pip install -e .
```

### Configuration

The project can be configured using the `.env` file. To configure the project copy the `.env.example` file to `.env` and change the values.

## 🚀 Start the service

To start the service run:

```bash
python scripts/start_demo.py
```

This will start the service on port `7654` or on the port specified in the `.env` file.

To stop the service press `Ctrl+C` in the terminal.

## 📚 Related Papers

**[Galactica: A Large Language Model for Science.][galactica-paper]**
Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic,
arXiv, 2022.

[python]: https://www.python.org/
[conda]: https://www.anaconda.com/
[git]: https://git-scm.com/
[galactica-paper]: https://arxiv.org/abs/2211.09085
