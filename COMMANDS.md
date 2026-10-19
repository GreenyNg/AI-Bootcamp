# Command Log: AI Engineering Bootcamp

This file documents the terminal commands I use while learning Python and preparing for AI engineering.

## 1. Installing and checking Python

| Command | Purpose | Result |
|---|---|---|
| `python --version` | Check the Python version | Python was not recognized |
| `py --version` | Check Python using the Windows Python launcher | Worked. Reported Python 3.15.0 |
| `py` | Open the interactive Python interpreter | Worked. Tested Python using `print(2 + 3)` |

## 2. First Python experiment

Command entered inside the Python interpreter:

```python
print(2 + 3)
```

**Purpose:** Test a simple calculation.

**Result:** Printed `5`.

## 3. Installing Jupyter Notebook

Python 3.15 encountered compatibility problems when installing Jupyter-related packages, particularly PyYAML.

| Command | Purpose | Result |
|---|---|---|
| `py -m pip install notebook` | Install Jupyter Notebook. | Installation failed because a compatible PyYAML build was unavailable without additional C++ build tools. |
| `py -m pip install --only-binary=:all: PyYAML` | Check for compatible PyYAML. | No compatible PyYAML binary was found for that Python version. |
| `py -m pip install jupyterlab` | Install JupyterLab. | Installation encountered the same PyYAML build problem. |

**Note:** I installed Python 3.13 alongside Python 3.15 to use a version compatible with the packages I needed. Both versions can coexist, and `py -3.13` explicitly selects Python 3.13.

## 4. Using Python 3.13

| Command | Purpose | Result |
|---|---|---|
| `py -3.13 --version` | Check the Python 3.13 installation. | Checked before installing Jupyter Notebook. |
| `py -3.13 -m pip install notebook` | Installed Jupyter Notebook. | Successfully installed Jupyter Notebook. |
| `py -3.13 -m notebook` | Launch Jupyter Notebook in the browser. | Worked |

## 5. Running Python files

```bash
py day1_exercise1.py
```

**Purpose:** Execute a Python script from the terminal.

**Result:** Worked after the file contained code that printed output.

## Notes

- `py` is the Windows Python launcher.
- `-m pip` runs pip using the selected Python interpreter.
- `-3.13` selects Python 3.13.
- Commands entered inside the Python interpreter are different from commands entered in the terminal.
- I will add new commands and record their results as I learn.