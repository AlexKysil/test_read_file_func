# Test Read File Return Lines

## Overview
* Given: Function/method that will get on an input a path to a file destination and N integer number. This method on the output should print N last lines from file in the correct order.
* Task:  Create tests, which will test this function.

## Project Structure:
    .
    ├── .github                 # directory with github templates like: PR template
    │   ├── workflows           # directory with GitHub Actions flow: Runs flake8 and pylint check on each PR 
    ├── function                # folder with read_file_return_lines function, the function that need to be tested
    ├── function_tests          # mian folder for tests and tests data
    │   ├── src                 # folder with test files 
    │   ├── tests_negative      # holds negative tests and necessary constants files
    │   ├── tests_positive      # holds positive tests and necessary constants files
    ├── helpers                 # folder for help methods and classes
    ├── .flake8                 # config file for flake8  
    ├── .gitignore              # config file for git, which defines what files to ignore  
    ├── .pylintrc               # config file for pylint     
    ├── conftest.py             # file with global fixtures  
    ├── pytest.ini              # config file for pytest     
    ├── README.md               # readme file  
    ├── requirements.txt        # file with requirements list
    
## Before you get started:
1. Install [python](https://www.python.org/downloads/) 3.7 or higher  
2. Create [virtual environment](https://docs.python.org/3/library/venv.html) if there is a need
3. In local terminal or in vevn run next script to install requirements:
`pip3 install -r requirements.txt` ([pip help](https://help.dreamhost.com/hc/en-us/articles/115000699011-Using-pip3-to-install-Python3-modules))

## How to Run tests:
**Note:** We are using [pytest](https://docs.pytest.org/en/stable/getting-started.html) as test framework, so follow [basic pytest rules](https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test) to run tests.

* Example how to run single test:
`
pytest -s -v -k test_read_by_wrong_path
`
* Example how to run tests by mark
`
pytest -s -v -m positive
`
* Example how to execute all tests:
`
pytest -s -v
`