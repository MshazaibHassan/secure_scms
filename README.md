READ.md 
The Student Course Management System is a multi-user web-based application that is created to offer regulated access, effective management of courses and administrative management.
The platform provides role-based access to administrators and students, allowing secure interaction and CRUD access on students, courses, and enrolments. The system was developed with Flask, SQLAlchemy.
Bootstrap 5 and includes security improvements, password hashing, access control and CSRF.
The application shows how usable software can be hardened against the common vulnerabilities without being rendered unusable. Functionality and security testing ensured that the system achieves its goals and provides a strong foundation of secure educational management.
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
