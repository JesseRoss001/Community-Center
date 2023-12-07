
# PEP 8 Validation Report

## Introduction
This document details the PEP 8 compliance validation performed on the Django project. It outlines the initial findings, actions taken to resolve issues, and a final overview of the remaining issues with justifications for why they were not resolved. Disclaimer this is my first project using python code.

## Initial Findings
The initial validation identified several hundred issues across multiple files, including all python files like `urls.py`, `models.py`, `forms.py`,`views.py` , `settings.py` etc . Issues ranged from whitespace errors, line length exceedances, to more complex structural concerns.

## Actions Taken
A concerted effort was made to address the vast majority of these issues. This involved:
- Refactoring code for better compliance with line length requirements.
- Adjusting whitespace and indentation to meet PEP 8 standards.
- Renaming variables and functions for better clarity and consistency with naming conventions.



## Conclusion
The codebase now adheres  to PEP 8 standards.

[PEP8 Validation for manage.py](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/manage.py)

[PEP8 Validation for settings.py](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/my_project/settings.py)

[PEP8 Validation for urls.py in my_project](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/my_project/urls.py)

[PEP8 Validation for admin.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/admin.py)

[PEP8 Validation for forms.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/forms.py)

[PEP8 Validation for models.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/models.py)

[PEP8 Validation for signals.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/signals.py)

[PEP8 Validation for urls.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/urls.py)

[PEP8 Validation for views.py in community](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/Community-Center/main/community/views.py)

![Screenshot 2023-12-07 115501](https://github.com/JesseRoss001/Community-Center/assets/79084912/041b9dc4-ba65-410e-a48a-52cc48960049)
![Screenshot 2023-12-07 115511](https://github.com/JesseRoss001/Community-Center/assets/79084912/9cdddcff-c9b6-49f8-a9aa-f123d18d2f2c)
![Screenshot 2023-12-07 115519](https://github.com/JesseRoss001/Community-Center/assets/79084912/ad7cb842-c06a-4528-a530-798609b32eda)
![Screenshot 2023-12-07 115527](https://github.com/JesseRoss001/Community-Center/assets/79084912/b6865287-cd7e-4a72-9654-259a3a4e8463)
![Screenshot 2023-12-07 115537](https://github.com/JesseRoss001/Community-Center/assets/79084912/fb3096c6-01aa-4d25-a868-e81829183d79)
![Screenshot 2023-12-07 115546](https://github.com/JesseRoss001/Community-Center/assets/79084912/22866218-c683-45a3-a6e6-d14e194ec0e1)
![Screenshot 2023-12-07 115559](https://github.com/JesseRoss001/Community-Center/assets/79084912/b3694f62-bb58-4789-b58d-8d19e736bc3e)
![Screenshot 2023-12-07 115608](https://github.com/JesseRoss001/Community-Center/assets/79084912/aa9a4d04-0596-42a7-9e62-c296fec023f8)
![Screenshot 2023-12-07 115616](https://github.com/JesseRoss001/Community-Center/assets/79084912/06aaa844-80b3-4a9a-9cb1-0bc4ba49580b)
![Screenshot 2023-12-07 115622](https://github.com/JesseRoss001/Community-Center/assets/79084912/2869d9c3-cdf3-460f-a4a4-060cc3fcd5b9)


## JavaScript File Metrics (Analyzed with JSHint)

- Total Functions: 25
- Largest Function Signature: 3 arguments
- Median Function Signature: 1 argument
- Largest Function Statements: 12
- Median Function Statements: 1
- Most Complex Function Cyclomatic Complexity: 7
- Median Cyclomatic Complexity: 1
- Warnings: 27

    - 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
    - 'template literal syntax' is only available in ES6 (use 'esversion: 6').
    - Unrecoverable syntax error. (80% scanned).

- Unused Variables: 5

    - eventDate
    - eventGraph
    - instructorEventDates
    - governmentEventDates
    - eventParticipationGraph

## CSS Validation - Zero Errors Achieved!



### What This Means
- **Compliance with Standards**: My CSS meets the rigorous standards set by the W3C for CSS level 3 + SVG.
- **Cross-Browser Compatibility**: This validation ensures that my stylesheets are more likely to be rendered consistently across different web browsers.
- **Optimized Performance**: Error-free CSS can help to speed up page loading times, providing a better user experience.

