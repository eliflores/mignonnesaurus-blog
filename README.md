[![CircleCI](https://circleci.com/gh/mignonnesaurus/my-first-blog/tree/master.svg?style=svg)](https://circleci.com/gh/mignonnesaurus/my-first-blog/tree/master)
[![Test Coverage](https://api.codeclimate.com/v1/badges/88f1f4084f20c55eaf01/test_coverage)](https://codeclimate.com/github/mignonnesaurus/my-first-blog/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/88f1f4084f20c55eaf01/maintainability)](https://codeclimate.com/github/mignonnesaurus/my-first-blog/maintainability)  


# My First Blog - Django Girls Tutorial

This is the result of me following the Django Girls Tutorial [here](https://tutorial.djangogirls.org/en/) and also: 
* Adding Tests 
* Adding a setup to run the blog in a staging and production environment in Heroku 
    * To show an example of a delivery pipeline.
* Adding SonarQube analysis and fixing issues found by the scanner.

### How to run the project locally?
1. Active the virtual env:
```bash
source myvenv/bin/activate
```

2. Start the web server:
```bash
python manage.py runserver
```

3. Development server will run at: `http://127.0.0.1:8000/`

### How to run tests?

#### Test suite

The test suite currently includes _unit_ and _integration_ tests and can be run with:

```bash
python runtests.py
```

It does not include _E2E_ / _UI_ tests, they can be run separately, see the [E2E Tests](#e2e-tests) section.

#### Single test case(s)

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

#### Modify the verbosity level 

You can get more details about the test execution by passing the argument `--verbosity` or `-v`. For the value you can choose from: `0, 1, 2, 3`.

For example, to pass verbosity of 2: 
```bash
python manage.py test tests -v 2
```

#### Code coverage

```bash
coverage run manage.py test tests
```

##### Coverage report

```bash
coverage html -d coverage-report
```

#### E2E Tests 

#### Pre-requirements

* Install [geckodriver](https://github.com/mozilla/geckodriver) - The [Web Driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) for Firefox.

```bash
brew install geckodriver
```

#### Running E2E Tests 

E2E Tests are currently run separately from the main [test suite](#how-to-run-tests) and can be run with:

```bash
python manage.py test e2e
```

The options to run single test case(s) are also available as described [here](#single-test-cases).

### Continuous Integration

Continuous Integration (CI) is managed with the help of [CircleCI](https://circleci.com/gh/mignonnesaurus/my-first-blog/tree/master).

Every time a PR is opened all tests, except E2E Functional tests, are run. Passing tests are required to merge a PR to master.

### Deployment

The application runs in [Heroku](https://heroku.com/).

There are 2 different environments:

1. [Staging](https://mignonnesaurus-staging.herokuapp.com/)
2. [Production](https://mignonnesaurus.herokuapp.com/)

Deployment is managed with the help of [CircleCI](https://circleci.com/gh/mignonnesaurus/my-first-blog) and after a PR is merged, the change is _automagically_ deployed to the [staging](https://mignonnesaurus-staging.herokuapp.com/) environment. 

Once changes are verified in _staging_, they can be _promoted_ to _production_ using [Heroku Pipelines](https://devcenter.heroku.com/articles/pipelines).

Here is how the UI to promote changes looks like in Heroku: 

![pipeline](https://user-images.githubusercontent.com/615127/60803185-ef09f500-a17a-11e9-9b84-5eebe0189381.png)

#### Review Apps 

Heroku has a [Review Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) feature that could be used if you would like to see or test a feature or a fix under development. 
You can create an _ad-hoc_ app for a PR that is open, review the changes and then delete the app. 

Here is how Review Apps UI looks like in Heroku: 

![review_apps](https://user-images.githubusercontent.com/615127/60805001-2ed2db80-a17f-11e9-9f43-723592b9ed21.png)
