
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

## Remaining Issues
After extensive work, some issues remain unresolved due to reasons such as maintaining existing functionality, ensuring readability, or specific project requirements that diverge from PEP 8 standards.

### Examples of Unresolved Issues:
- **urls.py**: Whitespace before commas remained in certain cases to align with existing codebase patterns.
- **forms.py**: Some lines remain longer than the PEP 8 recommendation to avoid breaking strings that are URLs or database queries.

## Conclusion
The codebase now adheres much more closely to PEP 8 standards, which will aid in maintainability and readability. The remaining issues have been left intentionally and do not detract from the overall quality of the code. Future work on this project will continue to strive for PEP 8 compliance while balancing practical considerations.

## Exempler Images
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/Appspyfile_tn46ex.png)
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/Adminpy_i6or1e.png)
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/views_validation_biy8mm.png)
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/validate_urls_q34mfg.png)
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/settings_wrrg1n.png)
![screenshot](https://res.cloudinary.com/dwz6t9jry/image/upload/v1701752147/Validation/formspy_ldrcpo.png)


**** HTML CHECKER 
Base.html 

Parse Errors for Django Template Tags: The checker points out parse errors for lines where you use Django template tags, such as {% extends 'community/base.html' %}, {% load static %}, {% block content %}, and so on. These tags are not standard HTML and will not be recognized by a generic HTML validator.

Use of Django Template Variables: Similarly, the checker flags lines where you use Django template variables like {{ user.profile }}. These are Django-specific and won't be understood by a standard HTML checker.

Meta Tags and Links: The checker doesn't seem to recognize the {% block title %} and {% endblock title %} syntax used in your <title> tag, which is a Django template feature. This might be why it's reporting an issue with the <title> tag.

CSS and JavaScript Loading: The checker doesn't understand the {% static 'styles/style.css' %} syntax used to load static CSS files. Again, this is specific to Django and not standard HTML.

Conditionals and Loops: The checker may flag constructs like {% if ... %} and {% for ... %} because they are not part of standard HTML.



First iteration of validation largely involed adding docstrings and removing whitespace . Removing trailing divs and unclosed p tags. 