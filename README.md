# Subtitle Prompter

A simple program that extracts the lines of dialogue from a file as prepares a prompt to translate them.

### Linux-only Setup

```sh
# Performs the full Python3 installation
sudo apt install python3-full

# Installs the necessary compiling tools
sudo apt install build-essential pkg-config cmake

# Creates a virtual environment to install pip packages
python3 -m venv venv

# Activates the virtual environment
source venv/bin/activate
```

### General Setup

```sh
# Installs the Argos Translate package from pip
pip install argostranslate

# Installs the translation package
python3 setup.py
```
