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