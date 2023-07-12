# sphinx-docs

## How to use Sphinx

Create a `docs` directory inside the project to hold the documentation.

```python
cd /path/to/project
mkdir docs
```

Run `sphinx-quickstart` inside the `docs` directory.

```python
cd docs
sphinx-quickstart
```

This sets up a source directory, walks you through some basic configurations, and creates an `index.rst` file as well as a `conf.py` file.

You can add some information about your project in `index.rst`, then build them:

```python
make html
```

> Guide: <https://docs.python-guide.org/writing/documentation/>
>
> Import docs on Read The Docs: <https://docs.readthedocs.io/en/latest/intro/import-guide.html>

## Automatically publishing gh-pages

Changes made in the `docs/` folder are automatically published to [yungng07.github.io/sphinx-docs/](https://yungng07.github.io/sphinx-docs/) using GitHub workflows.
