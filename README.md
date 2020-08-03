[![CircleCI](https://circleci.com/gh/eliflores/mignonnesaurus-blog/tree/master.svg?style=svg)](https://circleci.com/gh/mignonnesaurus/mignonnesaurus-blog/tree/master)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6ed84ae41b3695a8af27/test_coverage)](https://codeclimate.com/github/eliflores/mignonnesaurus-blog/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ed84ae41b3695a8af27/maintainability)](https://codeclimate.com/github/eliflores/mignonnesaurus-blog/maintainability)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

# Mignonnesaurus Blog

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
* Setting up [Code Climate](https://codeclimate.com/) for Code Quality and Code Coverage
* Setting up a delivery pipeline to run the blog in a staging and production environment in [Heroku](https://www.heroku.com/).

## How to run the project locally?
1. Create a virtual env
```bash
python -m venv venv
```

1. Active the virtual env:
```bash
source venv/bin/activate
```

2. Start the web server:
```bash
python manage.py runserver localhost:8000
```

3. Development server will run at: `http://localhost:8000/`

## How to run tests?

### Test suite

The test suite currently includes _unit_ and _integration_ tests and can be run with:

```bash
python runtests.py
```

It does not include _E2E_ / _UI_ tests, they can be run separately, see the [E2E Tests](#e2e-tests) section.

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

#### Pre-requirements

* Install [geckodriver](https://github.com/mozilla/geckodriver) - The [Web Driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) for Firefox.

```bash
brew install geckodriver
```

#### Running E2E Tests 

E2E Tests are currently run separately from the main [test suite](#how-to-run-tests) and can be run with:

```bash
python manage.py test e2e.local
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

### Demo Tests

Demo tests are E2E selenium tests that run with [SeleniumBase](https://pypi.org/project/seleniumbase/) to provide a visual blog tour of this project.

#### Pre-requirements

* Install [geckodriver](https://github.com/mozilla/geckodriver) - The [Web Driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) for Firefox.

```bash
brew install geckodriver
```

#### Run the demo tests
```bash
./tour.sh
```

## Continuous Integration

Continuous Integration (CI) is managed with the help of [CircleCI](https://circleci.com/gh/mignonnesaurus/mignonnesaurus-blog/tree/master).

Every time a PR is opened all tests - _except E2E Functional tests_ - are run. Passing tests are required to merge a PR to master.

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
