# Notes

## Github
1. After creating a new repository add project description to README.md
2. Include how-to install and use project in README.md
3. Check .gitignore file, verify that files with sensitive data won't be
    published to repostory. (See [Removing sensitive data]
    (https://help.github.com/articles/removing-sensitive-data-from-a-repository/))

## Code Style
1. Follow [pep8](https://www.python.org/dev/peps/pep-0008/) - use
    (flake8)[http://flake8.pycqa.org/en/latest/] in editor and with tests.
2. Don't go past 80 characters in line - easier side by side code comparison

## Project management
1. Use `make` for building project, running tests...
2. Specify requirements versions to avoid possible bugs and compatibility issues
    in newer versions. [pip tools](https://github.com/jazzband/pip-tools)

## Pyramid
1. Use [basemodel](https://github.com/thruflo/pyramid_basemodel) for easier
    work with SQLAlchemy.
2. Write script for populating database with dummy data. Use it instead of
    production database data and in tests.
3. Use `mock` for mocking objects in tests. (An Introduction to Mocking in
    Python)[https://www.toptal.com/python/an-introduction-to-mocking-in-python]
