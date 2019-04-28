# My First Blog - Django Girls Tutorial

This is the result of me following the Django Girls Tutorial [here](https://tutorial.djangogirls.org/en/).

## Table of Contents

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
```bash
python runtests.py
```

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

### How are changes deployed?

Deployment is managed with the help of [Heroku](https://heroku.com/) 

There are 3 environments used for testing and deploying the application: 

1. [Dev](https://mignonnesaurus-dev.herokuapp.com/)
2. [Staging](https://mignonnesaurus-staging.herokuapp.com/)
3. [Production](https://mignonnesaurus.herokuapp.com/)

After a PR is merged, the change is _automagically_ deployed the  [Dev](https://mignonnesaurus-dev.herokuapp.com/). 
Once changes are verified in _Dev_, they can be _promoted_ to _staging_ and then to _production_ using the [Heroku Pipelines](https://devcenter.heroku.com/articles/pipelines)

Here is how the UI to promote changes looks like in Heroku: 

![pipeline](https://user-images.githubusercontent.com/615127/56868332-49efd500-69f1-11e9-8c3e-03141452dca0.png)