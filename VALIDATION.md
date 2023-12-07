## HTML Validation Errors
Return back to the [README.md](README.md) file.


### Known Validation Error

An error has been detected by the Nu Html Checker due to the use of Crispy Forms tags which are not standard HTML elements. The error message is as follows:

> Error: Element `ul` not allowed as child of element `small` in this context.

This is a known issue associated with the use of Crispy Forms and will not be resolved as it pertains to the implementation specifics of the Crispy Forms Django package. The error is documented but does not affect the functionality of the forms or the website.


![Screenshot 2023-12-07 120315](https://github.com/JesseRoss001/Community-Center/assets/79084912/ee0c318a-6b57-4403-b0a7-a426a941c923)
![Screenshot 2023-12-07 120726](https://github.com/JesseRoss001/Community-Center/assets/79084912/96023eec-a26b-4c26-af63-abb8a7aa6627)
![Screenshot 2023-12-07 120742](https://github.com/JesseRoss001/Community-Center/assets/79084912/e2c72992-e69b-4811-b040-3fa28aaf7e9d)
![Screenshot 2023-12-07 120754](https://github.com/JesseRoss001/Community-Center/assets/79084912/e69c5dfc-bfee-40cc-98a4-c96eab5b17a3)
![Screenshot 2023-12-07 120809](https://github.com/JesseRoss001/Community-Center/assets/79084912/f346136e-26ae-4988-ae44-02fb09f6b692)
![Screenshot 2023-12-07 120823](https://github.com/JesseRoss001/Community-Center/assets/79084912/c2e041ff-c82e-4b94-b84b-c53c2009727e)
![Screenshot 2023-12-07 120844](https://github.com/JesseRoss001/Community-Center/assets/79084912/c65b48cd-9cb1-4d6e-9221-80fee6e6eaa6)
![Screenshot 2023-12-07 120853](https://github.com/JesseRoss001/Community-Center/assets/79084912/ecc3308d-4411-4481-bbcf-347c6b7a034c)


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


# JavaScript Validation Report  /JS HINT 
![Screenshot 2023-12-07 121455](https://github.com/JesseRoss001/Community-Center/assets/79084912/bb3937f7-fd35-46b4-8086-0d8fdf2ddfe9)

## Overview

I've conducted a static analysis of the JavaScript code using a linter, which has helped to highlight areas for improvement and confirm good practices already in place. The tool has been instrumental in detecting errors and potential issues.

## Metrics Observed

In my code, I have a total of 25 functions, indicating a modular approach to scripting. The largest function signature takes 3 arguments, slightly above the median of 1, which suggests some functions might be doing more complex tasks. The most extensive function consists of 12 statements, again indicating more elaborate logic than the median of 1 statement per function. The cyclomatic complexity measures the code's complexity, with the most intricate function having a value of 7, while the median complexity is 1.

## Identified Issues and Explanations

The linter has pointed out two undefined variables, `Chart` and `$`. These are not errors in the code but rather indicators of external dependencies. The variable `Chart` is utilized in conjunction with the Chart.js library, which is a separate script included in the project for rendering charts and graphs. The `$` symbol is a common alias for jQuery, another external library that simplifies DOM manipulation and event handling.

Additionally, four variables have been marked as unused: `eventDate`, `eventGraph`, `instructorEventDates`, and `governmentEventDates`. These variables are placeholders for future features where event data will be dynamically rendered on the page, and thus, they are necessary for the planned scalability of the application.





### What This Means
- **Compliance with Standards**: My CSS meets the rigorous standards set by the W3C for CSS level 3 + SVG.
- **Cross-Browser Compatibility**: This validation ensures that my stylesheets are more likely to be rendered consistently across different web browsers.
- **Optimized Performance**: Error-free CSS can help to speed up page loading times, providing a better user experience.

![Screenshot 2023-12-07 120315](https://github.com/JesseRoss001/Community-Center/assets/79084912/01201b0c-4494-4f37-b87a-f71f7fc7f17f)
