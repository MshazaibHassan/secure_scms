READ.md
Muhammad ShazaIb Hassan (24225541)
Introduction (Overview)
The youtube video link that helped with flusk login https://www.youtube.com/watch?v=cYWiDiIUxQc ( This is not my youtube video link MY LINK IS IN THE WORD FILE>>>>) 

The code for this project was developed by using three YouTube tutorials as the main learning references. 
The first video, which explained how to build a registration and login system in Flask, was used to understand how to create user accounts, store passwords securely, and manage user login sessions. 
From this video, the patterns for the register, login, and logout functions were adapted and expanded. Password hashing, form validation, and the use of Flask-Login were also learned from this tutorial. 
These ideas were then applied to build a secure authentication system for the student, instructor, and admin users in this project.

The second video provided a practical example of how to perform basic CRUD operations in Flask. 
CRUD refers to creating, reading, updating, and deleting records. 
This tutorial helped in structuring the admin functions such as adding courses, editing course details, deleting courses, and listing all available courses. 
The route structure, the use of forms, and the template layout used in the admin pages were based on the CRUD patterns demonstrated in the video. 
These ideas were then adjusted to work with role-based access so that only instructors and admins could change course information.

The third video focused on how to use Flask-SQLAlchemy to design a database, create models, and interact with the database through Python code. 
This tutorial guided the structure of the User, Course, and Enrollment models in the project. It also helped in setting up the database connection, creating tables, and using ORM methods for querying data. 
The migration process, which allows database changes to be tracked over time, follows the approach shown in the video.

Structure 
All three tutorials were combined to create a complete system. The authentication code was connected with the database models so that user accounts and passwords are stored securely. 
The CRUD functions were connected with the course model so instructors and admins could create or update course records. Role-based access control was added on top of this structure to ensure that only authorised users could access certain pages. 
For example, students can only view their dashboard and profile, while instructors can manage courses.

Security Improvements / Testing 

Security features were added to improve the code beyond what the tutorials provided. These include password hashing, CSRF protection on forms, login protection using decorators, and environment-based configuration for sensitive values such as the secret key. 
The final application structure keeps the admin, student, and authentication functions separated into different files and folders, which makes the system organised, readable, and easier to maintain.



(Usage And GuideLines Instructions)


First any normal user can creat an account with a name and user email, whcih they will later uses to login and log out of the system,  Secondly they can login very easily using that password and email what they can do now is very simple. There are two kind of privilleges that are assigned to the users one as student and other is Admin role.
The Admin can easily make any certain kind of changes like adding or removing studnets, the admin can also assign the courses to the students, the admin can also creat the courses. 
On the other hand student have few privilages compared to the Admin role. Their privileges are decideded by the Admin.


Overview

Overall, the tutorials acted as learning guides to understand core Flask concepts. 
The code from them was not copied directly but was adapted, expanded, and combined into a more complete and secure student course management system. 
Each video contributed a different part: user login logic, CRUD operations, and database design. These pieces were then integrated to create a fully functioning system with role-based access and secure handling of user and course data.




