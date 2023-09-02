# keyChecker
Personal project for data quality checks in plain text files

There is a beta version for a function that checks business key duplicates: business_key_checker.ipynb


Current objectives:

1. **main.py**: parameterize file path, separator, header and column informations so users will have to write only these to the code (easier usage)
2. **ReadFile.py**: read the file that contains data the user wants to check - **into a format** as optimized as possible
3. **KeyChecker.py**: write the key check in python (python exercise and cleaner code)
4. **KeyChecker.py + main.py**: return result of check in a user-friendly readable format (easier usage)


Learning objectives:

- OOP: push different functionalities into different classes and main class will call these from their respective classes
- GitHub: such small functions may not be useful to push out into different classes and files but in this project our purpose is to get familiar with using git repository, file management, branching, cloning, pull, push, merge etc.


Code should be made easily expandable for functional extensions. These long-term objectives include:

- get user parameters without user having to write into code
- data type checks
- null value checks
- data length checks

