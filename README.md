[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mignonnesaurus_my-first-blog&metric=alert_status)](https://sonarcloud.io/dashboard?id=mignonnesaurus_my-first-blog) 


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

### How to deploy?

Deployment is managed with the help of [Heroku](https://heroku.com/) 

There are 3 environments used for testing and deploying the application: 

1. [Dev](https://mignonnesaurus-dev.herokuapp.com/)
2. [Staging](https://mignonnesaurus-staging.herokuapp.com/)
3. [Production](https://mignonnesaurus.herokuapp.com/)

After a PR is merged, the change is _automagically_ deployed the  [Dev](https://mignonnesaurus-dev.herokuapp.com/). 
Once changes are verified in _Dev_, they can be _promoted_ to _staging_ and then to _production_ using the [Heroku Pipelines](https://devcenter.heroku.com/articles/pipelines)

Here is how the UI to promote changes looks like in Heroku: 

![pipeline](https://user-images.githubusercontent.com/615127/56868332-49efd500-69f1-11e9-8c3e-03141452dca0.png)