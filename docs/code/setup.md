# Setup

## Asitop
NVTOP like for M1 Mac

## isort
use isort to sort python imports
- install `pipx install isort`


## Npm & NodeJS
NPM is a package manager for javascript (like [pdm](#pdm) for python)

[What is npm video](https://www.youtube.com/watch?v=P3aKRdUyr0s)

- install with NodeJs via official website
- use:
  - `npm -v` get the version
  - `npm init` start new project
  - `npm list` list all dependencies
  - `npm install X` install locally. If package `X`not provided, install all packages from the `package-lock.json`, or `package.json`
  - `npm install -g X` install globally (available everywhere on the computer)

### package.json
`package.json` gets updated with each new dependancy

### package-lock.json
`package-lock.json` avoid dependency or compatibility issues by storing exact versions of packages

### node_modules
store all packages after an `npm install`

## Oh my zsh
- install via `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- TODO: custom aliases

### dotfiles
[What should/shouldn't go in .zshenv, .zshrc, .zlogin, .zprofile, .zlogout?](https://unix.stackexchange.com/a/71258)

#### `.zshenv`
You can put environment variable in `.zshenv`

```sh title=".zshenv"
export MY_KEY="<key>"
OTHER_KEY="<other_key>"
```

???+ tip
    When `export` is used, it makes the variable available to subprocessed as well

???+ warning
    It will most of the time **override** environment variables in `.env` file

## Pdm
Use [pdm](https://pdm.fming.dev/2.9/) as python package and dependency manager

- install `pipx install pdm`
- use:
    - `pdm init` for new projects
    - `pdm install` for existing projects
    - `pdm info`, `pdm config`
- do not fill name, version etc in the `pyproject.toml` to avoid editable package issues
- store environment variable in `.env`; only works if run command with `pdm run mycmd`
- using the src layout, just make a `pdm add .` to editably install the project

```python title="pyproject.toml"
[tool.pdm]

[project]
name =""
version = ""
description = ""
authors = [
    {name = "Magsen Chebini", email = "magsen.che@gmail.com"},
]
dependencies = [
    "black>=23.3.0",
    "numpy>=1.24.3",
    "matplotlib>=3.7.1",
]
requires-python = ">=3.11"
license = {text = "MIT"}

[tool.pdm.scripts._]
env_file = ".env"

[tool.pdm.scripts.hello]
cmd = "python3 hello_world.py"

[tool.black]
line-length = 88

[tool.isort]
profile = "black"
```

## Pipx
Use [pipx](https://pypa.github.io/pipx/) for python tools used on several projects, e.g. pdm ([more](https://python.land/virtual-environments/pipx))

- install `brew install pipx`
- add to $PATH `pipx ensurepath` (in `~/.zshrc` so that it's loaded with the shell)

## Python 3.11.5
- download https://www.python.org/ftp/python/3.11.5/python-3.11.5-macos11.pkg
- install using mac software manager
- accept root certificate (double-click)

## VsCode
- [download](https://code.visualstudio.com/download)
- install using mac software manager
- can also be installed using `brew install code`

Extensions:

- Python
- Path intellisense
- Black formatter
- isort
- Even Better TOML
- Jupyter
- Markdown all in one
- Markdowon preview enhanced
- YAML
