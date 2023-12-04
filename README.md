# Project Name: Community Center Booking System
#Problem Statement  : Local community centers are not imformative about what events are being held and a booking system for them does not exist that is avialable to the public. 
#Purpose : Provides a platform for community venue to increase public engagement and public awareness of ongoing events. To allow instructors to host events and provide a venue for education, businesses and individuals . 
#Target Audience  : Government officials , members of the public and instructors 
## Overview
This project is a web application for managing bookings at a community center. It provides interfaces for different user personas including general users , instructors  and government officials to interact with the system based on their roles.

#MVP Features: User registration + login , task entry editing , deleting , submitting for instructors and officials . General Users can view events and the schedule . General users can save events to their schedule . 

#Iteration 1 and 2 : Category filtering , images uploaded to gallery , downloading resources , payment system. Liking and commenting on events . 

## Personas

### General User Persona
**Name:** Alex Johnson  
**Age:** 29  
**Occupation:** Freelancer  
**Tech Savviness:** High  
**Goals:** Wants to find and book community events easily.  
**Frustrations:** Complex booking systems and lack of clear information.

### Government Official Persona
**Name:** Sarah Wang  
**Age:** 41  
**Occupation:** Government Employee  
**Tech Savviness:** Moderate  
**Goals:** Needs to manage educational courses and utilize community spaces effectively.  
**Frustrations:** Inefficiency in event management and reporting.


## Project Setup

### Requirements
- Python 
- Django 
- PostgreSQL
- Heroku CLI

### Local Development Setup
1. Clone the repository:
2. Navigate to the project directory:
3. Install dependencies:
4. Set up your PostgreSQL database and update `settings.py` with your database credentials.
5. Run migrations to create database schema:
6. Start the development server:

### Deploying to Heroku
1. Log in to your Heroku account and create a new app.
2. Connect your GitHub repository to Heroku.
3. Configure environment variables in Heroku's settings.
4. Deploy the main branch to Heroku.
5. Run migrations on Heroku:
6. Access the live site using your Heroku app's URL.

# Progress Report

## Day 1: Nov 14, 2023
- **Started the Project**: Initial commit and set up Django project and app.
- **Base Setup**: Created base template and linked the home page.
- **Deployment Initiatives**: Worked on deploying to Heroku and resolving application errors.
- **Configuration**: Set up Whitenoise for static files and fixed BASE_DIR and path issues in wsgi.

## Day 2: Nov 15, 2023
- **Admin and User Management**: Worked on the admin interface and user creation, rectifying user creation errors.
- **Authentication**: Implemented basic login functionality.
- **User Roles**: Developed a model for different user types.
- **Registration System**: Displayed and indicated correct login details and views for registration.

## Day 3: Nov 16, 2023
- **Signup Functionality**: Completed signup forms and addressed form submission errors.
- **Event Management**: Began creating event models, views, and forms.
- **Testing**: Conducted initial form testing.
- **MVT Implementation**: Started working on the Model-View-Template for events.

## Day 4: Nov 17, 2023
- **Login and Registration**: Resolved login page errors and confirmed the effective functioning of event registration.
- **Booking System Development**: Initiated the development of the booking system, focusing on rendering and functionality.

## Day 5: Nov 18, 2023
- **Gallery and Media**: Addressed errors in displaying media files and added functionality to the gallery.
- **Styling**: Completed preliminary styling on the about page.
- **Booking System Enhancement**: Worked on refining the booking system, ensuring proper rendering and addressing double booking issues.

## Day 6: Nov 19, 2023
- **Admin Interface Upgrade**: Implemented Summernote in the admin section to enhance content management.
- **Cloud Integration**: Added Cloudinary for improved media management.
- **System Check**: Resolved issues identified during system checks.
- **Readme Update**: Updated the project README file.

## Day 7:Nov 20, 2023
- **Fixed Media Upload Errors**: Corrected issues with uploading media and the correct use of static files.
- **Styling Home Page**: Began the process of enhancing the home page styling.

## Day 8: Nov 21, 2023
- **Rough Styling of Pages**: Applied initial styling to various pages excluding forms.
- **Styling the Booking Page**: Focused on refining the booking page appearance.
- **Styling the About Page**: Made several commits to improve the layout and style of the about page.

## Day 9: Nov 22, 2023
- **Testing**: Added `tests.py` ensuring all tests pass.
- **Code Commenting**: Improved code documentation to adhere to industry standards.
- **Migrations and Updates**: Kept database migrations up to date and made minor updates.
- **MVP Achieved**: Reached a minimal viable product with current features.
- **Form Styling**: Enhanced the styling of forms and updated the event updating form.

## Day 10: Nov 23, 2023
- **Correcting Styling Errors**: Made adjustments to fix prominent styling issues across the platform.
- **Finalizing Home Page Design**: Worked on finalizing the home page design, ensuring responsiveness across all device sizes.
- **Footer Layout Improvement**: Reverted footer styling to its original design and enhanced the layout.

### Day 11: Nov 24, 2023
- **HTML Validation**: Began the process of validating HTML to ensure code quality.
- **UI Enhancements**: Made improvements to the user interface for better usability.

### Day 12: Nov 25, 2023
- **Code Documentation**: Enhanced code documentation for better clarity and maintenance.
- **Bug Fixes**: Addressed minor bugs to improve overall system stability.

### Day 13: Nov 26, 2023
- **Refactoring Code**: Continued cleaning and refactoring parts of the codebase.
- **Security Updates**: Implemented additional security measures for robustness.

### Days 14-16: Nov 27-29, 2023
- **No Commits**: Attended a Hackathon, hence no progress on this project.

### Day 17: Nov 30, 2023
- **Deploy to Heroku**: Redeployed project to Heroku, recycling keys for security.
- **Feature Addition for Staff**: Added a 'coming soon' feature to the staff graph display and fixed a bug related to staff crediting.

### Day 18: Dec 1, 2023
- **Improvement in Functionality**: Worked on enhancing various functionalities, including instructor rating and staff roles.

### Day 19: Dec 2, 2023
- **Search Functionality Enhancement**: Improved basic search functions and added features like searching by tags and filters.

### Day 20: Dec 3, 2023
- **Accessibility Improvements**: Focused on improving accessibility features, like adding semantic headers and visually hidden classes.
- **Layout Improvements**: Made improvements in the layout of views and other elements for better user experience.

### Day 21: Dec 4, 2023
- **Bug Fixing and Updates**: Addressed several bugs, particularly in search functionality and event management.
- **Testing and Documentation**: Updated testing procedures and documentation to reflect recent changes.

## Contributing
This project is aimed at meeting assessment criteria and therefore contributions are not welcome.

## Contact 
For any questions or concerns , please contact me at jesseross001@gmail.com

## User Stories

1. **Homepage Access for Guest Users**:
   As a guest user, I want to view the homepage with a clear indication of the website's purpose, so I can understand what the site offers without logging in.

2. **Event Browsing for Guest Users**:
   As a guest user, I want to browse upcoming events, so I can decide if I want to participate or register.

3. **Account Login for Registered Users**:
   As a registered user, I want to log in to my account, so I can access user-specific features.

4. **Government Portal Access**:
   As a government official, I want to log in through a government portal, so I can manage courses and events sponsored by the government.

5. **Instructor Dashboard Access**:
   As an instructor, I want to log in to access the instructor dashboard, so I can manage my bookings and courses.

6. **Event Booking for Users**:
   As a user, I want to book available slots for events, so that I can ensure my attendance.

7. **Booking Details for Users**:
   As a user, I want to see the price and time for each booking, so I can choose the most suitable option for me.

8. **Course Pricing for Instructors**:
   As an instructor, I want to set prices for my courses, so that I can be compensated for my services.

9. **Course Addition for Government Officials**:
   As a government official, I want to add free courses, so I can provide educational services to the community.

10. **Event Calendar for Users**:
    As a user, I want to see a calendar of events, so I can plan my schedule accordingly.

11. **User Management for Admins**:
    As an admin, I want to manage all user logins and roles, so I can ensure proper access control.

12. **Gallery Management for Admins**:
    As an admin, I want to manage the gallery section, so I can curate the content displayed.

13. **Feedback Submission for Users**:
    As a user, I want to provide feedback on courses and events, so I can share my experiences with the community.

14. **Booking and Transaction Oversight for Admins**:
    As an admin, I want to view all bookings and transactions, so I can monitor community center usage.

15. **Event Modification for Instructors/Government Officials**:
    As an instructor or government official, I want to cancel or reschedule events, so I can adapt to changes as needed.

16. **Venue Booking for Personal Events**:
    As a user, I want to rent out the venue for personal events, so I can utilize the community space for private functions.

17. **Event Notifications for Users**:
    As a user, I want to sign up for notifications about upcoming events, so I don't miss any opportunities.

18. **Material Uploads for Instructors**:
    As an instructor, I want to upload course materials, so attendees can access necessary resources.

19. **Site Usage Reporting for Admins**:
    As an admin, I want to run reports on site usage, so I can make data-driven decisions for future planning.

20. **Event Search by Keywords for Users**:
    As a user, I want to search for events by keywords, so I can quickly find events that interest me.

#USE CASES How each use case contributes to allecviating the indentified problem 

## Project Wireframes

The wireframes for this project are detailed in the following document. This document includes the layout and design considerations for our application's interface.
[View the Project Wireframes](https://drive.google.com/file/d/1Aa_hGM3fGi_G6RnyrY9oSEWahFzyjGzW/view?usp=sharing)


## Examples of model view template planning 
This file shows a rough demonstration on how the MVT was planned to be ready to implement.
[View template examples here ](https://drive.google.com/file/d/1kkD_z-1SnDRcn4Hx_sx1PzzE5_1qTAbX/view?usp=sharing)

## Time boxing 
The intitial time boxing document can be found below 
[View time boxing here] (https://drive.google.com/file/d/1ZcLm_VVa5sJz3wZoFjCXrjSpz_SdAryr/view?usp=sharing)


# Community Center Booking System
## Chosen User Stories and their Implementations 

### Homepage Access for Guest Users
- **Contribution**: Simplifies discovery of community offerings without the barrier of forced registration.
- **Implementation**: A welcoming homepage with clear CTAs and information about the community center's offerings.

### Event Browsing for Guest Users
- **Contribution**: Engages the public by showcasing events and encourages registration.
- **Implementation**: Publicly accessible events page with filters for dates and categories.

### Account Login for Registered Users
- **Contribution**: Personalizes the experience and unlocks full platform features.
- **Implementation**: Secure login system with personalized dashboard reflecting bookings and interests.

### Government Portal Access
- **Contribution**: Streamlines event management for government-sponsored activities.
- **Implementation**: Separate login portal for government officials with additional event management tools.

### Instructor Dashboard Access
- **Contribution**: Enables instructors to manage their offerings and engage with the community.
- **Implementation**: Instructor dashboard for course management, scheduling, and communication with attendees.

### Event Booking for Users
- **Contribution**: Facilitates community participation in events.
- **Implementation**: Intuitive booking system with confirmation and calendar integration.

### Booking Details for Users
- **Contribution**: Informs users to make educated decisions about event participation.
- **Implementation**: Detailed event pages with cost, duration, and other relevant information.

### Course Pricing for Instructors
- **Contribution**: Provides instructors with a revenue stream for their services.
- **Implementation**: Pricing options during event creation with secure payment processing.

### Course Addition for Government Officials
- **Contribution**: Offers educational opportunities to the community.
- **Implementation**: Special privileges for government officials to create and manage free courses.

### Event Calendar for Users
- **Contribution**: Assists users in planning their schedules around community events.
- **Implementation**: Interactive calendar view of events that users can subscribe to.

### User Management for Admins
- **Contribution**: Ensures appropriate access and maintains platform integrity.
- **Implementation**: Admin panel for user role assignment and access control.

### Gallery Management for Admins
- **Contribution**: Enhances the visual appeal and informational value of the platform.
- **Implementation**: Admin tools for curating and managing the event gallery.

### Feedback Submission for Users
- **Contribution**: Collects community input for continuous improvement.
- **Implementation**: Feedback forms and rating systems for events and courses.

### Booking and Transaction Oversight for Admins
- **Contribution**: Monitors the financial and operational health of the community center.
- **Implementation**: Dashboard with reports on bookings, cancellations, and financial transactions.

### Event Modification for Instructors/Government Officials
- **Contribution**: Adds flexibility to event management to adapt to unforeseen circumstances.
- **Implementation**: Tools to edit, reschedule, or cancel events with automated attendee notifications.

# [COMMUNITY CENTER](https://community-centre-71f077e09006.herokuapp.com)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you will include a few paragraphs providing an overview of your project.
Essentially, this part is your "sales pitch".

At this stage, you should have a name for your project so use it!
Don't introduce the project as a "portfolio project" for the diploma.

In this section, describe what the project hopes to accomplish, who it is intended to target, and how it will be useful to the target audience.

Consider adding a mockup image using the "Am I Responsive" website.
Here's your deployed site as an example:
https://ui.dev/amiresponsive?url=https://community-centre-71f077e09006.herokuapp.com

Screenshots for the README and testing should not be inside of `assets/` or `static/` image folders.
(reminder: `assets/` and `static/` are for files used on the live site, not documentation)
Consider adding a new folder called `documentation`, and add the amiresponsive screenshot inside of that folder.
To add the image into your README, use this format:
(assuming you have a new folder called `documentation` with an image called "mockup.png")

![screenshot](documentation/mockup.png)

Note: Markdown files (.md) should not contain HTML elements like `img`, `br`, `div`, `a`, etc, only Markdown formatting.
Find out more about using Markdown elements here:
https://pandao.github.io/editor.md/en.html

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## UX

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you will briefly explain your design processes.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Colour Scheme

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Explain your colours and the colour scheme.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- `#000000` used for primary text.
- `#E84610` used for primary highlights.
- `#4A4A4F` used for secondary text.
- `#009FE3` used for secondary highlights.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a link and screenshot for your colour scheme using "coolors".
https://coolors.co/generate

When you add a colour to the palette, the URL is dynamically updated, making it easier for you to return back to your colour palette later if needed.

Example:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate my colour palette.

![screenshot](documentation/coolors.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you've used CSS `:root` variables, consider also including a code snippet here!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    /* P = Primary | S = Secondary */
    --p-text: #000000;
    --p-highlight: #E84610;
    --s-text: #4A4A4F;
    --s-highlight: #009FE3;
    --white: #FFFFFF;
    --black: #000000;
}
```

### Typography

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Explain any fonts and icon libraries used, like Google Fonts and/or Font Awesome.

Consider adding a link to each font used, and the Font Awesome site if used (or similar icon library).

Example:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.

- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, list all of your user stories for the project.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### New Site Users

- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.

### Returning Site Users

- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.

### Site Admin

- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.
- As a site administrator, I should be able to ____________, so that I can ____________.

## Wireframes

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, display your wireframe screenshots using a Markdown `table`.
Instructions on how to do Markdown `tables` start on line #213 on this site: https://pandao.github.io/editor.md/en.html

Alternatively, dropdowns are a way to condense several wireframes into a collapsible menu to save space.
Dropdowns in Markdown are considered some of the only acceptable HTML components that are allowed for assessment purposes.

**IMPORTANT**! **IMPORTANT**! **IMPORTANT**!
The example below uses the `details` and `summary` code elements.
However, for these scripts to work, I've had to add spaces within the `< >` elements.

You MUST remove these spaces for it to work properly on your own README/TESTING files.
Remove the spaces within the `< >` brackets for the `details` and `summary` code elements,
for the Mobile, Tablet, and Desktop wireframes.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

< details >
< summary > Click here to see the Mobile Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/mobile-home.png)

About
  - ![screenshot](documentation/wireframes/mobile-about.png)

Contact
  - ![screenshot](documentation/wireframes/mobile-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/mobile-gallery.png)

etc.
  - repeat for any remaining mobile wireframes

< / details >

### Tablet Wireframes

< details >
< summary > Click here to see the Tablet Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/tablet-home.png)

About
  - ![screenshot](documentation/wireframes/tablet-about.png)

Contact
  - ![screenshot](documentation/wireframes/tablet-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/tablet-gallery.png)

etc.
  - repeat for any remaining tablet wireframes

< / details >

### Desktop Wireframes

< details >
< summary > Click here to see the Desktop Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)

About
  - ![screenshot](documentation/wireframes/desktop-about.png)

Contact
  - ![screenshot](documentation/wireframes/desktop-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

etc.
  - repeat for any remaining desktop wireframes

< / details >

## Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should go over the different parts of your project,
and describe each in a sentence or so.

You will need to explain what value each of the features provides for the user,
focusing on who this website is for, what it is that they want to achieve,
and how your project is the best way to help them achieve these things.

For some/all of your features, you may choose to reference the specific project files that implement them.

IMPORTANT: Remember to always include a screenshot of each individual feature!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Existing Features

- **Title for feature #1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature01.png)

- **Title for feature #2**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature02.png)

- **Title for feature #3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Future Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Title for future feature #1
    - Any additional notes about this feature.
- Title for future feature #2
    - Any additional notes about this feature.
- Title for future feature #3
    - Any additional notes about this feature.

## Tools & Technologies Used

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Codeanywhere](https://codeanywhere.com) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Materialize](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Using your defined models (one example below), create an ERD with the relationships identified.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

A couple recommendations for building free ERDs:
- [Draw.io](https://draw.io)
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/erd.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Using Markdown formatting to represent an example ERD table using the Product model above:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | category | ForeignKey | FK to **Category** model |
    | | sku | CharField | |
    | | name | CharField | |
    | | description | TextField | |
    | | has_sizes | BooleanField | |
    | | price | DecimalField | |
    | | rating | DecimalField | |
    | | image_url | URLField | |
    | | image | ImageField | |

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/JesseRoss001/Community-Center/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a basic screenshot of your Projects Board.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/JesseRoss001/Community-Center/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a screenshot of your Open and Closed Issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [Open Issues](https://github.com/JesseRoss001/Community-Center/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/JesseRoss001/Community-Center/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT:**

- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

The live deployed application can be found deployed on [Heroku](https://community-centre-71f077e09006.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: Community-Center).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JesseRoss001/Community-Center) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JesseRoss001/Community-Center.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JesseRoss001/Community-Center)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JesseRoss001/Community-Center)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Credits

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Content

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
