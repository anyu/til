# Python Environment Management

[Pyenv](https://github.com/pyenv/pyenv) is useful for managing python versions.
- `brew install pyenv`
- update .zshrc (see pyenv section; in general read the ReadMe if hit version issues)

[Virtualenv](https://virtualenv.pypa.io/en/stable/) is useful for managing python virtual environments.

## Updating virtualenv Python version

1. Install Python 3.10
    ```sh
    pyenv install 3.10
    ```

2. Get location
    ```sh
    which python3.10
    ```

3. Overwrite virtual env named `venv` with new path
    ```sh
    virtualenv -p /Users/anyu/.pyenv/shims/python3.10 venv

    # or if it's in /versions:
    virtualenv -p /Users/anyu/.pyenv/versions/3.8.18/bin/python venv
    ```

4. Check that `venv` now has the new version:
    ```sh
    ls venv/bin
    ```

5. Activate venv
    ```sh
    source venv/bin/activate
    ```

6. Check python version being used
    ```sh
    $ python -V
    Python 3.10.0
    ```

## Troubleshooting

If get `FileExistsError`, remove existing `venv` dir before running `virtualenv` step:

```sh
ls | grep venv
rm -rf venv
```

### venv

Or just use venv, which comes with pip installed
```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

### Requirements file

Generate from existing deps via `pip freeze > requirements.txt`

Install reqs from reqs file
```sh
pip install -r requirements.txt
```

### Dependency Trees

[pipdeptree](https://pypi.org/project/pipdeptree/) can be handy for viewing pip package dependencies:
```sh
pip install pipdeptree
```
