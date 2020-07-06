# E713 - PyView


## Setup

This package uses venv module.

    python -m venv .venv

To acrivate the environment using PowerShell

    # optionally allo remote signed scripts for current user
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    .venv/Scripts/Activate.ps1

### Requirements

Install anything you need to your newly created environment

    pip install -r requirements.txt

Adding Packages can ba done via pip.

        pip install <some_package>

Requirements might be frozen to document dependencies.

        pip freeze > requirements.txt
