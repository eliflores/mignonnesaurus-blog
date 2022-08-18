# Mignonnesaurus Blog

[![CircleCI](https://circleci.com/gh/eliflores/mignonnesaurus-blog.svg?style=svg)](https://circleci.com/gh/eliflores/mignonnesaurus-blog)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6ed84ae41b3695a8af27/test_coverage)](https://codeclimate.com/github/eliflores/mignonnesaurus-blog/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ed84ae41b3695a8af27/maintainability)](https://codeclimate.com/github/eliflores/mignonnesaurus-blog/maintainability)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


- [Introduction](#Introduction)
- [How to run the project locally?](#How-to-run-the-project-locally)
- [How to run tests?](#How-to-run-tests)
  - [Test suite](#Test-suite)
  - [Single test case(s)](#Single-test-cases)
  - [Modify the verbosity level](#Modify-the-verbosity-level)
  - [Code coverage](#Code-coverage)
    - [Coverage report](#Coverage-report)
  - [E2E Tests](#E2E-Tests)
  - [On a local machine :computer:](#On-a-local-machine-computer)
    - [Pre-requirements](#Pre-requirements)
    - [Running E2E Tests](#Running-E2E-Tests)
  - [On a remote machine :cloud:](#On-a-remote-machine-cloud)
    - [Pre-requirements](#Pre-requirements-1)
    - [Running E2E Tests](#Running-E2E-Tests-1)
- [Continuous Integration](#Continuous-Integration)
- [Deployment](#Deployment)
  - [Review Apps](#Review-Apps)

## Introduction

I :yellow_heart: the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/). After [following it](https://github.com/mignonnesaurus/my-first-blog), I continued the fun by:
* Adding Tests 
* Setting up Continuous Integration with [circleci](https://circleci.com/)
* Setting up [Code Climate](https://codeclimate.com/)
* Setting up a delivery pipeline to run the blog in a staging and production environment in [Heroku](https://www.heroku.com/)

## Getting started

### How to run the project locally?

1. Make sure you have [GNU Make](https://www.gnu.org/software/make/) installed on your machine.
  * A [Makefile](Makefile) was added to the project to simplify some tasks.

2. The project uses [pipenv](https://github.com/pypa/pipenv) to manage the Python dependencies and facilitate the 
   workflow when working with a virtualenv. So, please [install pipenv](https://github.com/pypa/pipenv#installation) 
   before getting started:
```bash
brew install pipenv
```

3. Setup dev environment: 
```bash
make dev_setup
```

4. Make sure things are healthy by running the tests: 
```bash
make test
```

5. Start the server:
```bash
make runserver
```

## How to run tests?

### Test suite

All the tests that are run as part of CI are in the [tests](tests) folder and you can run them locally with:

```bash
python manage.py test tests
```

ℹ️ Additionally, you can run: `make test`

The execution includes _E2E_ Functional Tests that run on Firefox in headless mode. 

_E2E_ / _UI_ tests that do not run in headless mode, can be run separately, see the [E2E Tests](#e2e-tests) section.

### Single test case(s)

You can pass the module or test case:

```bash
python manage.py test <module_pattern> 
```

For example, to run all the tests in the `test_models` module:

```bash
python manage.py test tests.test_models
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
python manage.py test tests -v 2
```

### Code coverage

```bash
coverage run manage.py test tests
```

#### Coverage report

```bash
coverage html -d coverage-report
```

### E2E Tests 

:mag_right: It is also possible to run a single E2E test by using the options described [here](#single-test-cases).

### On a local machine :computer:

#### Running E2E Tests 

E2E Tests that do not run in headless mode are currently run separately from the main [test suite](#how-to-run-tests) 
and can be run with:

```bash
python manage.py test e2e.local
```

#### Troubleshooting E2E Tests

E2E tests by default run in _headless_ mode, this means that if you want to 
troubleshoot via the browser and the driver doing its magic, you will need 
to modify the test you would like to troubleshoot and change:

```python
firefox_options.headless = True
```

to 

```python
firefox_options.headless = False
```

### On a remote machine :cloud:

Remote E2E Tests - tests that run _on the cloud_ - are setup to run on [Sauce Labs](https://saucelabs.com/) :zap:.

#### Pre-requirements

* A _username_ and _API Key_ is needed to run the tests on the Sauce Labs Testing Cloud. 

#### Running E2E Tests 

Tests that run on the cloud can be run with:

```bash
python manage.py test e2e.remote
```

### Demos

A visual demo of the blog, implemented with [SeleniumBase](https://pypi.org/project/seleniumbase/) can be run with:

```bash
sh demo.sh
```

ℹ️ Make sure that your development server is already started, before running the demo.

#### Pre-requirements

* Install [geckodriver](https://github.com/mozilla/geckodriver) - The [Web Driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) for Firefox.

## Continuous Integration

Continuous Integration (CI) is managed with the help of [CircleCI](https://app.circleci.com/pipelines/github/eliflores/mignonnesaurus-blog).

Every time a PR is opened all tests inside [tests](tests) are run. Passing tests are required to merge a PR to master.

## Deployment

The application runs in [Heroku](https://heroku.com/).

There are 2 different environments:

1. [Staging](https://mignonnesaurus-staging.herokuapp.com/)
2. [Production](https://mignonnesaurus.herokuapp.com/)

Deployment is managed with the help of [CircleCI](https://circleci.com/gh/mignonnesaurus/mignonnesaurus-blog) and after a PR is merged, the change is _automagically_ deployed to the [staging](https://mignonnesaurus-staging.herokuapp.com/) environment. 

Once changes are verified in _staging_, they can be _promoted_ to _production_ using [Heroku Pipelines](https://devcenter.heroku.com/articles/pipelines).

Here is how the UI to promote changes looks like in Heroku: 

![pipeline](https://user-images.githubusercontent.com/615127/60803185-ef09f500-a17a-11e9-9b84-5eebe0189381.png)

### Review Apps 

Heroku has a [Review Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) feature that could be used if you would like to see or test a feature or a fix under development. 
You can create an _ad-hoc_ app for a PR that is open, review the changes and then delete the app. 

Here is how Review Apps UI looks like in Heroku: 

![review_apps](https://user-images.githubusercontent.com/615127/60805001-2ed2db80-a17f-11e9-9f43-723592b9ed21.png)

---
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

The tutorial that was followed for the creation of this blog is attributed to [Django Girls](https://djangogirls.org/) and it can be found [here](https://tutorial.djangogirls.org/).

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
