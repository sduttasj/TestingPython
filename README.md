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

7



