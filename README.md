# Testing Python
Trying out simple continuous integration with python

1. First we are going to set up virtual env in windows using the following command:
-->Windows
py -m venv venv envname

2. Activate the virtual env by
--> Windows
.\virtual_environment_name\Scripts\activate

3. Next we pick a leetcode problem to solve: 
https://leetcode.com/problems/letter-case-permutation/

4. We keep the solution in LetterCasePermutation.py

5. To test the code we need a few tools such as a unit testing library and code coverage tool. We are picking pytest and flake for those..use the following command in the virtual env for these:
pip install flake8 pytest pytest-cov

6. Store the dependencies in requirements.txt:
pip freeze > requirements.txt

7.Next we add a test file under the same directory (main directory)

8. We run the test coverage. pytest -v --cov

(venv) C:\DEV\LeetCode-Problems\TestingPython>pytest -v --cov
================================================= test session starts =================================================
platform win32 -- Python 3.10.1, pytest-7.0.1, pluggy-1.0.0 -- C:\DEV\LeetCode-Problems\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\DEV\LeetCode-Problems\TestingPython
plugins: cov-3.0.0
collected 1 item

test_LetterCasePermution.py::Test::test_letterCasePermutation PASSED                                             [100%]

---------- coverage: platform win32, python 3.10.1-final-0 -----------





