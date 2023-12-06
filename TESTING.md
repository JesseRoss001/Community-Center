# Testing

Return back to the [README.md](README.md) file.

## Responsiveness

You can watch the video [here](https://youtu.be/NTsB_5O4eM4).



# Feature Testing

- **Instructor Signup**: Instructors signing up should provide a 4-digit card number or lower. This is to demonstrate the concept initially, with plans to later restrict the accepted card numbers and implement in-person verification for added security.

#### Screenshots
![Screenshot 2023-12-06 010515](https://github.com/JesseRoss001/Community-Center/assets/79084912/3e78ed32-e1b5-47d4-a887-2f725f4f0a7f)
![Screenshot 2023-12-06 021733](https://github.com/JesseRoss001/Community-Center/assets/79084912/49ed6c04-9efb-4a51-8c56-fbeaac090859)
![Screenshot 2023-12-06 021750](https://github.com/JesseRoss001/Community-Center/assets/79084912/153f62f9-06a5-42ac-8683-49274f3f5e38)

- **Event Search and Creation**: Instructors can search for events for inspiration, held by other instructors or officials. 
    - On clicking 'Create Event', instructors can schedule a new event. The date and time combination must be unique to prevent double bookings. Event time cannot be set in the past, and the capacity limit is 60. 
    - Optional event details or an image can be added.

    **Note**: An error related to image upload has been identified and will be addressed.

#### Screenshots
![Screenshot 2023-12-06 021945](https://github.com/JesseRoss001/Community-Center/assets/79084912/ec48c201-053e-4f13-89d8-0b35c2f58536)
![Screenshot 2023-12-06 022045](https://github.com/JesseRoss001/Community-Center/assets/79084912/73badd18-c0ab-423f-80ac-f13ea47fb9f1)

- **Image Upload and Management**: Images uploaded will be directly added to the gallery, with options for deletion if needed.

#### Screenshots
![Screenshot 2023-12-06 022224](https://github.com/JesseRoss001/Community-Center/assets/79084912/e3a705b8-c627-4a6d-9f6b-64c42745ad6a)
![Screenshot 2023-12-06 022327](https://github.com/JesseRoss001/Community-Center/assets/79084912/e182aed1-7846-464d-ace8-b858b7c535fc)
![Screenshot 2023-12-06 022357](https://github.com/JesseRoss001/Community-Center/assets/79084912/219f126a-cee1-4cc6-95b2-53c87e2f127d)
![Screenshot 2023-12-06 025130](https://github.com/JesseRoss001/Community-Center/assets/79084912/6337b208-0af4-4748-95c0-df73645cd2a2) – Successful Image Deletion
![Screenshot 2023-12-06 025241](https://github.com/JesseRoss001/Community-Center/assets/79084912/c57b93f5-eb72-432c-a87f-7aa207529df6)

- **Event Management for Instructors**: Created events are displayed on the instructor's homepage. Events can be updated, provided the capacity isn't reduced below the number of already joined members. Images can also be re-uploaded during updates.

#### Screenshots
![Screenshot 2023-12-06 025155](https://github.com/JesseRoss001/Community-Center/assets/79084912/b425f3a8-2829-40ad-983d-f37bbdd7408b)
![Screenshot 2023-12-06 025344](https://github.com/JesseRoss001/Community-Center/assets/79084912/8639717a-0f47-4ded-abfa-fc9c8640cac6)
![Screenshot 2023-12-06 025406](https://github.com/JesseRoss001/Community-Center/assets/79084912/b888a7de-6d1e-40c1-bcf1-abfbb635d9d5)

- **Event Cancellation and Refunds**: Events can be deleted, and refunds issued if no users have joined. However, events cannot be deleted once a member has joined. The system also includes a graphical representation of balance statements.

#### Screenshots
![Screenshot 2023-12-06 025553](https://github.com/JesseRoss001/Community-Center/assets/79084912/a91ad8b6-2c91-454f-9d8c-9d8cd02e72ea)

- **User Registration and Permissions**: Users can register without providing card number, badge, or staff ID. They are not permitted to create events.

#### Screenshots
![Screenshot 2023-12-06 025850](https://github.com/JesseRoss001/Community-Center/assets/79084912/5a2af9e2-31d7-482c-9857-9daa6ddd452a)
![Screenshot 2023-12-06 025914](https://github.com/JesseRoss001/Community-Center/assets/79084912/a1d20fa8-b4fd-4437-a092-700be79d06d4)

- **Event Joining and User Homepage**: Users can join events from the booking page. This information, along with a history of transactions and a graphical display, will be shown on their homepage.

#### Screenshots
![Screenshot 2023-12-06 025945](https://github.com/JesseRoss001/Community-Center/assets/79084912/61ca3ebb-bf59-4687-bfce-5e6e2516579e)
![Screenshot 2023-12-06 025959](https://github.com/JesseRoss001/Community-Center/assets/79084912/8ba1a296-2eda-46c8-af1c-5ae99eca1db1)
![Screenshot 2023-12-06 030007](https://github.com/JesseRoss001/Community-Center/assets/79084912/d1ebe7b2-b845-43d2-ab1a-287d6aa4e408)

- **Event Participation Restrictions**: Users cannot join the same event more than once.

#### Screenshot
![Screenshot 2023-12-06 030037](https://github.com/JesseRoss001/Community-Center/assets/79084912/51cd884f-ffca-48a2-a98c-0bc62c20813d)

- **Event Likes and Ratings**: Users can like any event, even if they haven't joined, and can unlike at will. Only users who have joined an event can rate the instructor.

#### Screenshots
![Screenshot 2023-12-06 030054](https://github.com/JesseRoss001/Community-Center/assets/79084912/2aa994e5-075a-46fb-ad96-a7dcb06d3f69)
![Screenshot 2023-12-06 030144](https://github.com/JesseRoss001/Community-Center/assets/79084912/2fb49614-c8c0-4385-ab7c-db3650ddad81)

- **Budget Limitations and Corrections**: Users' budgets cannot exceed a deficit of -28 before receiving in-person credits from staff members. This bug has been addressed and fixed.

#### Screenshot
![Screenshot 2023-12-06 031653](https://github.com/JesseRoss001/Community-Center/assets/79084912/0a50233d-0a6b-4e7c-af3f-3381389621f1)

- **Event Search Functionality**: Known issue - clicking 'Find Event' redirects to the page where the event is located, but not to the specific event itself. Time constraints have prevented fixing this issue. The search works with tags, instructor rankings, and sorting by like counts and time of day.

#### Screenshots
![Screenshot 2023-12-06 031820](https://github.com/JesseRoss001/Community-Center/assets/79084912/9fefced5-a5b7-4104-a848-c2e520bb1f6c)
![Screenshot 2023-12-06 031845](https://github.com/JesseRoss001/Community-Center/assets/79084912/12b7107b-a35a-4773-b74e-2784414e4f0b)
![Screenshot 2023-12-06 031912](https://github.com/JesseRoss001/Community-Center/assets/79084912/9a0a11ae-ba51-4a0f-967f-b6803ce08549)
![Screenshot 2023-12-06 031949](https://github.com/JesseRoss001/Community-Center/assets/79084912/71a82ec0-907b-41c8-87c4-448d5a6301c2)
![Screenshot 2023-12-06 032059](https://github.com/JesseRoss001/Community-Center/assets/79084912/592a849f-ab1a-4559-a269-cc1e63a8ef0d)
![Screenshot 2023-12-06 032120](https://github.com/JesseRoss001/Community-Center/assets/79084912/c27892cb-f36a-46f1-980e-8a67966dcaa6)


- **Government Instructor Testing**: Government official testing requires a badge number of 5 digits or less for registration.

#### Screenshot
![Screenshot 2023-12-06 034105](https://github.com/JesseRoss001/Community-Center/assets/79084912/66322813-7dbc-4da2-9a72-ee499deedaba)

- **Direct Booking for Officials and Instructors**: Officials and instructors can book events directly from the booking page.

#### Screenshot
![Screenshot 2023-12-06 034138](https://github.com/JesseRoss001/Community-Center/assets/79084912/5160a30c-5b2c-470d-afd3-4e8ab63a7b13)

- **Redirection Issue After Creating Instructors**: A bug concerning redirection after creating instructor profiles has been identified.

#### Screenshot
![Screenshot 2023-12-06 034858](https://github.com/JesseRoss001/Community-Center/assets/79084912/696654fa-7f26-4b60-bce2-2b85201ca3f3)

- **Joining Fee for Official Events**: A bug where the joining fee incorrectly cost users for official events has been fixed. The joining fee should be zero for officials.

- **Staff Member Requirements**: Staff members are required to have a staff ID of 6 digits or less.

#### Screenshot
![Screenshot 2023-12-06 040756](https://github.com/JesseRoss001/Community-Center/assets/79084912/6424191d-abaa-4699-89b5-6f46b98fa74b)

- **Staff Member Budget Management**: Staff members can view all users' budgets and credit them following in-person payments.

#### Screenshots
![Screenshot 2023-12-06 035549](https://github.com/JesseRoss001/Community-Center/assets/79084912/2a0a4cf2-5441-4bc3-9e04-603db0703f27)
![Screenshot 2023-12-06 035626](https://github.com/JesseRoss001/Community-Center/assets/79084912/525fa976-ee18-4b9a-81ea-94c9c46a6287)
![Screenshot 2023-12-06 035634](https://github.com/JesseRoss001/Community-Center/assets/79084912/ddf23bd4-4d35-46c3-acf2-cf88574963f8)
![Screenshot 2023-12-06 035645](https://github.com/JesseRoss001/Community-Center/assets/79084912/cb376479-228e-40a9-b53f-e0ea2e9a6b0e)

- **Admin Login and Management Capabilities**: 
    - Admins can view all balance changes and amounts and have the authority to delete specific transfers.
    - Admins can view, update, and delete events, including filtering events to identify system errors. They can also manage event images.
    - Admins have access to user roles, budgets, and can filter users by roles.

#### Screenshots
![Screenshot 2023-12-06 041015](https://github.com/JesseRoss001/Community-Center/assets/79084912/524581a2-8fcd-4178-9092-1c5dc7563b75)
![Screenshot 2023-12-06 041034](https://github.com/JesseRoss001/Community-Center/assets/79084912/5fd515fe-2a8d-4685-9f56-aa838262a8d4)
![Screenshot 2023-12-06 041114](https://github.com/JesseRoss001/Community-Center/assets/79084912/17852022-01e2-4864-a716-4744d0efa39d)
![Screenshot 2023-12-06 041226](https://github.com/JesseRoss001/Community-Center/assets/79084912/8416959c-1e02-47ac-b066-d15fded6bed9)

# Defensive Programming Test: Join Event

## Overview
This report evaluates the security and user experience aspects of the `join_event` functionality in the Community Center project.

## Test Scenarios

### Non-Logged-In Member Access
- **Objective**: Verify access control for non-logged-in users.
- **Expected Behavior**: Redirection to login page.
- **Result**: ![Non-logged-in Access Test](https://github.com/JesseRoss001/Community-Center/assets/79084912/d02c91fc-7ab5-4124-a8dd-6f201257914a)

### Search Event Access
- **Objective**: Confirm that non-logged-in members cannot search events.
- **Expected Behavior**: Restricted access.
- **Result**: (Provide screenshot or test result link)

### Event Booking Visibility
- **Objective**: Assess if event booking details are hidden from non-logged-in members.
- **Expected Behavior**: Booking details should not be visible.
- **Result**: ![Event Booking Test](https://github.com/JesseRoss001/Community-Center/assets/79084912/d02c91fc-7ab5-4124-a8dd-6f201257914a)

### Credit Issuance Authorization
- **Objective**: Ensure that only authorized members can issue credits.
- **Expected Behavior**: Access denied for unauthorized roles.
- **Result**: ![Credit Issuance Test](https://github.com/JesseRoss001/Community-Center/assets/79084912/d5e14c3e-36c5-43f2-8971-9b7c5a34dc00)

### Token Generation for Event Joining
- **Objective**: Validate the token generation mechanism for event joining.
- **Expected Behavior**: Unique tokens for each join event request.
- **Results**: 
  - ![Token Test 1](https://github.com/JesseRoss001/Community-Center/assets/79084912/959d2e93-a591-4df4-89dd-6af71e188d54)
  - ![Token Test 2](https://github.com/JesseRoss001/Community-Center/assets/79084912/ab115db9-b825-4c07-92c0-2dc90393ab88)
  - ![Token Test 3](https://github.com/JesseRoss001/Community-Center/assets/79084912/5a2d8a90-c1df-41fa-825b-e9fc2e5ea1a0)

### Budget Restriction Compliance
- **Objective**: Check the effectiveness of budget restrictions.
- **Expected Behavior**: Restrict event joining based on budget.
- **Result**: ![Budget Restriction Test](https://github.com/JesseRoss001/Community-Center/assets/79084912/fb0f5054-db3c-48fc-9df2-0866ff6e00aa)

## Conclusion
The tests conducted illustrate robust access control, effective budgetary restrictions, and secure token-based event joining mechanisms. These results affirm the application's adherence to defensive programming principles.
