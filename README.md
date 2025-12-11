READ.md 

The youtube video link that helped with flusk login https://www.youtube.com/watch?v=cYWiDiIUxQc ( This is not my youtube video link MY LINK IS IN THE WORD FILE>>>>) 

Overall, the tutorials acted as learning guides to understand core Flask concepts. 
The code from them was not copied directly but was adapted, expanded, and combined into a more complete and secure student course management system. Each video contributed a different part: user login logic, CRUD operations, and database design. These pieces were then integrated to create a fully functioning system with role-based access and secure handling of user and course data.


Introduction (Overview)

The Student Course Management System is a multi-user web-based application that is created to offer regulated access, effective management of courses and administrative management.
The platform provides role-based access to administrators and students, allowing secure interaction and CRUD access on students, courses, and enrolments. The system was developed with Flask, SQLAlchemy.
Bootstrap 5 and includes security improvements, password hashing, access control and CSRF.
The application shows how usable software can be hardened against the common vulnerabilities without being rendered unusable. Functionality and security testing ensured that the system achieves its goals and provides a strong foundation of secure educational management.

(Features And Objectives)

The project was developed in an iterative approach, which focused on incremental system building, testing, and improvement.
This method was chosen since secure code involves continuous evaluation of new functionality to detect vulnerabilities and add safeguards at the right points.
The process started with a first outline of the key features, which comprised authentication, role separation, and course management.
Security considerations re-escalated in every cycle, to evaluate the impact of new functionality on the overall system posture.
he iterative approach enabled the developer to verify and modify architectural choices and remain receptive to address problems encountered during initial tests.
Security has been introduced and implemented in all the development cycles to identify, rectify and remove any form of vulnerability in the initial stages so that the system design and its execution would be fully correct and be able to withstand the threats that were to be encountered.
The iterative method also resulted in incremental progress where progress was made add by add and features were tested each time added to be functional, consistent, and be security compliant.
The foundational functionalities, including the authentication, user registration, role-based access control, student and course management, and the course assignment process, were the main focus of the cycles as in this way the developers could verify the functional correctness as well as the secure DBA. SQLAlchemy relationships,
database integrity and data flow between parts and the ability to adjust backend logic, user interface design and system architecture were validated by the use of modular testing and prototyping.
Bootstrap 5 was chosen specifically due to the fact that it is geared towards responsive and accessible interfaces, and practicality was evaluated in relation to different devices, screen sizes, and user requirements.
The efficiency and completeness of security measures like route protection, CSRF tokens, input checks, and password hashing were reviewed periodically.
his solution allowed programmers to detect and fix potential vulnerabilities when they happened, rather than being an afterthought. Using iterative testing, modular planning, sustained security testing and systematic
development practices, the finished application came to a development/ usability/ reliability/ safe operation trade-off that provided a sound multi-user platform that satisfies both the functional as well as safety needs in totality.

(Project Structure) 

The code for this project was developed by using three YouTube tutorials as the main learning references. 
The first video, which explained how to build a registration and login system in Flask, was used to understand how to create user accounts, store passwords securely, and manage user login sessions. 
From this video, the patterns for the register, login, and logout functions were adapted and expanded. Password hashing, form validation, and the use of Flask-Login were also learned from this tutorial. 
These ideas were then applied to build a secure authentication system for the student, instructor, and admin users in this project.
The second video provided a practical example of how to perform basic CRUD operations in Flask. CRUD refers to creating, reading, updating, and deleting records.
This tutorial helped in structuring the admin functions such as adding courses, editing course details, deleting courses, and listing all available courses. 
The route structure, the use of forms, and the template layout used in the admin pages were based on the CRUD patterns demonstrated in the video. 
These ideas were then adjusted to work with role-based access so that only instructors and admins could change course information.
The third video focused on how to use Flask-SQLAlchemy to design a database, create models, and interact with the database through Python code. 
This tutorial guided the structure of the User, Course, and Enrollment models in the project. It also helped in setting up the database connection, creating tables, and using ORM methods for querying data. 
The migration process, which allows database changes to be tracked over time, follows the approach shown in the video.
All three tutorials were combined to create a complete system. The authentication code was connected with the database models so that user accounts and passwords are stored securely. 
The CRUD functions were connected with the course model so instructors and admins could create or update course records. 
Role-based access control was added on top of this structure to ensure that only authorised users could access certain pages. For example, students can only view their dashboard and profile, while instructors can manage courses.
Security features were added to improve the code beyond what the tutorials provided. 
These include password hashing, CSRF protection on forms, login protection using decorators, and environment-based configuration for sensitive values such as the secret key. 
The final application structure keeps the admin, student, and authentication functions separated into different files and folders, which makes the system organised, readable, and easier to maintain.
The rollout of the Student Course Management System was a systematic process whereby each feature would be introduced to enable modularity, readability, and testability.
It was written in Flask, with an application factory pattern that enabled configuration, database initialization, and blueprint registration to be structured.
The authentication blueprint was used to deal with login, registration, and log out functions. The passwords were encrypted using the bcrypt library which saved hashed passwords in place of plain text passwords.
This method meant that password disclosure was unlikely even in a situation where the database was compromised.
Role based redirection was applied in the login feature with a conditional test to redirect the administrators and the students to their own dashboard.
The administrative blueprint introduced the CRUD functions of the students and courses. Student creation involved the generation of a related user record using SQLAlchemy models
The course creation encompassed entry of new courses. Enrolment was made using an association table which formed the association between the courses and the students.


Usage And GuideLines Instructions.


First any normal user can creat an account with a name and user email, whcih they will later uses to login and log out of the system, while creatring the account user can choose to be either student or Admin. Secondly they can login very easily using that password and email what they can do now is very simple. There are two kind of privilleges that are assigned to the users one as student and other is Admin role.
The Admin can easily make any certain kind of changes like adding or removing studnets, the admin can also assign the courses to the students, the admin can also creat the courses. 
On the other hand student have few privilages compared to the Admin role. Their privileges are decideded by the Admin.

Testing 

The system was tested to ensure that operations were as intended and that security improvements worked. 
Functional testing was started by testing the authentication process that includes successful login to both roles and proper redirection to the corresponding dashboard. 
Administrative CRUD operations were checked by creating student accounts, adding courses, assigning courses and ensuring that the database showed the expected changes. 
Student testing was aimed at the dashboard display accuracy and the visibility of assigned courses.



