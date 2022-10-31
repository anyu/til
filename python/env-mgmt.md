# Python Environment Management

[Pyenv](https://github.com/pyenv/pyenv) is useful for managing python versions.
- `brew install pyenv`
- update .zshrc

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