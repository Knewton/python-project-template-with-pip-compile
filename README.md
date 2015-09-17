python-project-template-with-pip-compile
========================================
This project is an explanatory template showing how to do effective dependency management in Python
with pip-compile.

This template is minimal, including only the ingredients that you'll need to do dependency
management effectively. In almost all cases, you'll want to add in additional tools for unit
testing, linting, documentation generation, build automation, and many other things. Sean Fisk's
[python-project-template](https://github.com/seanfisk/python-project-template) is a great place to
start for incorporating more build tools into your project.

Usage
-----
To use this as a template, clone it, modify the files to your liking, and you're good to go! Each
file is documented to explain how it works, so you can also browse the files to learn more about how
to set up dependency management for a Python project.

To install dependencies and run tests, run `tox`. Running `tox -r` will recreate all virtualenvs.

If you want to add a tool that's only needed to test this project, add it to
`requirements.testing.in`, then run `tox -e pip-compile` to update your `requirements.txt` file.

If you want to add a Python library that is needed by the code itself, add it to `requirements.in`,
then run `tox -e pip-compile` to update your `requirements.txt` file.

Philosophy
----------
For a more detailed explanation of how this project works, see [this blog post](link to second blog post).
