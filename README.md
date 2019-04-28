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
```bash
python manage.py test <module_pattern> 
```

For example, to run all the tests in the `test_models` module:

```bash
python manage.py test tests.test_models
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

### How to deploy?

<WIP>