# Building sphinx documentation

## Initial steps
1. Fork the 
2. Clone the repository to your local machine


## Building Adding a sphinx build configuration to PyCharm
1. Open Pycharm.
2. File -> Open -> Navigate to your project folder -> Click Ok.
3. Run -> Edit configurations. 
4. Click the + button and selected `python docs` -> `sphinx` and complete the 
following fields:
    1. Name: `Sphinx`
    2. Input: Select the source directory in the documentation folder
    3. Output: Select the build directory in the documentation folder
    4. Python interpreter: Select your interpreter
    5. Options: `-E -a` (This options forces rebuild of html)
5. Click ok.

<!---
## Updating documentation
-->





