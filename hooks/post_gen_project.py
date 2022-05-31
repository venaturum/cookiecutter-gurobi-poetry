#!/usr/bin/env python
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(".").absolute()


def add(filepath):
    target = PROJECT_DIRECTORY / filepath
    target.mkdir(parents=True, exist_ok=True)


def remove(filepath):
    target = PROJECT_DIRECTORY / filepath

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


if __name__ == "__main__":

    if "none" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = Path(".") / "{{ cookiecutter.project_slug }}" / "cli.py"
        remove(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove("LICENSE")

    remove("licenses")

    if "{{ cookiecutter.use_flake8 }}" == "n":
        remove("setup.cfg")

    if "{{ cookiecutter.use_precommit }}" == "n":
        remove(".pre-commit-config.yaml")

    add("logs")
    add("model_files")
    if "{{ cookiecutter.use_notebooks }}" == "y":
        add("notebooks")
    add("problem_files")
