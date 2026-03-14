# Mignonnesaurus Blog

[![CircleCI](https://circleci.com/gh/eliflores/mignonnesaurus-blog.svg?style=svg)](https://circleci.com/gh/eliflores/mignonnesaurus-blog)
[![Code Coverage](https://qlty.sh/gh/eliflores/projects/mignonnesaurus-blog/coverage.svg)](https://qlty.sh/gh/eliflores/projects/mignonnesaurus-blog)
[![Maintainability](https://qlty.sh/gh/eliflores/projects/mignonnesaurus-blog/maintainability.svg)](https://qlty.sh/gh/eliflores/projects/mignonnesaurus-blog)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

I :yellow_heart: the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/). After [following it](https://github.com/mignonnesaurus/my-first-blog), I continued the fun by:
* Adding Tests 
* Setting up Continuous Integration with [circleci](https://circleci.com/)
* Setting up [Qlty](https://qlty.sh/)

## Table of Contents

- [How to run the project locally?](#how-to-run-the-project-locally)
- [Testing](#testing)
  - [Running a single test](#running-a-single-test)
  - [Modify the verbosity level](#modify-the-verbosity-level)
  - [Code coverage](#code-coverage)
  - [Coverage report](#coverage-report)
  - [E2E Tests](#e2e-tests)
    - [Troubleshooting E2E Tests](#troubleshooting-e2e-tests)
  - [Demos](#demos)

## How to run the project locally?

1. Install the version of Python the [.tool-versions](.tool-versions) file.
  * You may want to use [asdf](https://asdf-vm.com/) for this purpose.

2. Make sure you have [GNU Make](https://www.gnu.org/software/make/) installed on your machine.
  * A [Makefile](Makefile) was added to the project to simplify some tasks.

3. The project uses [pipenv](https://github.com/pypa/pipenv) to manage the Python dependencies and facilitate the 
   workflow when working with a virtualenv. You'll need to [install pipenv](https://github.com/pypa/pipenv#installation) 
   before getting started.

4. Setup dev environment: 
```bash
make dev_setup
```

5. Make sure things are healthy by running the tests: 
```bash
make test
```

6. Start the server:
```bash
make runserver
```

## Testing

The tests that are run as part of CI are: 
- `tests.forms`
- `tests.models`
- `tests.views`
- `tests.functional`: these are run as E2E tests with Selenium and Firefox in headless mode.

You can run all of these tests with: `make test` or with the following command:

```bash
python manage.py test tests.forms tests.models tests.views tests.functional
```

### Running a single test

You can pass the module or test case:

```bash
python manage.py test <module_pattern> 
```

For example, to run all the tests in the `models` module:

```bash
python manage.py test tests.models
```

And you can also use the `--pattern` or `-p` argument. For example:

```bash
python manage.py test --pattern="*_forms.py"
```

```bash
python manage.py test -p "*_forms.py"
```

### Modify the verbosity level

You can get more details about the test execution by passing the argument `--verbosity` or `-v`. For the value you can choose from: `0, 1, 2, 3`.

For example, to pass verbosity of 2: 
```bash
python manage.py test tests.functional -v 2
```

### Code coverage

```bash
make test_coverage
```

### Coverage report

```bash
coverage html -d coverage-report
```

### E2E Tests

E2E Tests that open a visible browser are currently run separately from the rest of the tests. To run them, make sure 
you have Firefox installed and run:

```bash
make test_e2e
```

#### Troubleshooting E2E Tests

E2E tests use the shared Firefox WebDriver factory in `tests/webdriver.py`.
If Firefox is installed in a non-standard path, set `FIREFOX_BINARY` before running the tests.

```bash
export FIREFOX_BINARY=/path/to/firefox
```


### Demos

A visual demo of the blog, implemented with [SeleniumBase](https://pypi.org/project/seleniumbase/) can be run with:

```bash
make rundemo
```

ℹ️ The development server needs to already be running and a superuser needs to also exist with credentials that need to
be exposed as environment variables: 

```bash
export MY_BLOG_USERNAME=myusername
export MY_BLOG_PASSWORD=mypassword
```

---
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

The tutorial that was followed for the creation of this blog is attributed to [Django Girls](https://djangogirls.org/) and it can be found [here](https://tutorial.djangogirls.org/).

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
