import sqlite3

DB = 'internship.db'

ENTRIES = [
    # ── PHASE 1 ──
    {
        "date": "2026-02-02", "hours": 6, "phase": "Phase 1",
        "work_summary": "The first internship session focused on providing an introduction to mobile application development using Flutter and setting the context for the overall internship. The session began with an overview of the organization, followed by a discussion on internship objectives, duration, rules, guidelines, and expected outcomes from the interns. This helped in understanding the structure of the program and the professional expectations throughout the internship period. A high-level introduction to Flutter and the Dart programming language was provided, explaining their roles in building modern mobile applications. The mentor discussed the concept of cross-platform development and how Flutter enables developers to create applications for both Android and iOS using a single codebase. The session also included an overview of the development tools, frameworks, and workflow that will be used during the internship, giving a clear picture of how projects will be planned, developed, tested, and improved over time.",
        "learning_outcome": "Developed a clear understanding of the fundamentals of Flutter and Dart and how they work together to build cross-platform mobile applications from a single codebase. Gained better clarity on the structure of the internship, the planned learning roadmap, and the expectations for upcoming tasks and projects. Was introduced to real-world mobile app development practices, including how applications are planned, designed, and implemented in a professional environment. Also learned the importance of UI/UX principles such as layout design, user interaction, and responsiveness, and how Flutter helps in creating scalable, efficient, and maintainable mobile applications through its widget-based architecture and modern development approach.",
        "skills": "Flutter",
        "blockers": "No Blockers or Risks are faced since it was an Introductory session."
    },
    {
        "date": "2026-02-03", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session focused on building a strong foundation in Flutter and the Dart programming language. The session began with the installation and configuration of the Flutter development environment, including setting up the Flutter SDK, configuring the IDE, and ensuring that the emulator/device setup was working properly. An introduction to Dart programming was provided, covering basic syntax, variable declaration, data types, functions, and control statements such as conditional and looping structures. The mentor also explained the basic structure of a Flutter project, including important files and directories, and how the application execution starts from the main function. Additionally, the concept of widgets was introduced, emphasizing that everything in Flutter is built using widgets. The difference between various types of widgets and their role in designing the user interface was discussed.",
        "learning_outcome": "Gained a strong understanding of the fundamentals of Dart programming and its significance in Flutter app development. Understood how Dart serves as the core language for building application logic, managing state, and handling user interactions within Flutter applications. Explored the basic structure of a Flutter project, including key folders and files such as main.dart, and learned how the application execution begins from the main function and runs through the widget tree. Developed a clear understanding of the widget-based architecture of Flutter and how every UI element is created using widgets. Learned the difference between Stateless and Stateful widgets and identified appropriate scenarios for using each type.",
        "skills": "Flutter",
        "blockers": "No Risks faced."
    },
    {
        "date": "2026-02-04", "hours": 5, "phase": "Phase 1",
        "work_summary": "The session began with a detailed overview of Flutter's origin, purpose, and its relevance in the current technology landscape. The mentor explained how Flutter was introduced to overcome the challenges of developing separate applications for Android and iOS, which traditionally required different codebases, tools, and development teams. A comparative discussion was held between Flutter, native Android development using Android Studio with Kotlin, and React Native. Key differences were highlighted in terms of performance, development speed, UI consistency, hot reload feature, and code reusability. The session also addressed Flutter's growing demand in the industry, explaining why startups prefer it for faster product development and cost efficiency, and how enterprises are adopting it for scalable and maintainable applications.",
        "learning_outcome": "Gained a clear understanding of the scope and importance of Flutter in modern mobile app development and how it compares with other approaches. Understood the difference between Flutter and native Android development using Kotlin, which is limited to Android-only applications, and React Native, which relies on React concepts for cross-platform development. This helped in recognizing why Flutter is widely preferred for building applications for both Android and iOS using a single codebase. Developed clarity on Flutter's evolution, its growing industry adoption, and the advantages it offers in terms of performance, UI consistency, faster development, and maintainability.",
        "skills": "Flutter, React, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-05", "hours": 6, "phase": "Phase 1",
        "work_summary": "The session focused on understanding the Android emulator structure. The mentor demonstrated how to configure and run a virtual device using Android Studio and explained how the emulator integrates seamlessly with the Flutter development environment. A brief introduction to APIs was also provided, explaining their importance in modern mobile applications. The mentor discussed how applications communicate with external services through APIs and how data is exchanged in JSON format. A sample Flutter application was executed to understand the complete development workflow—from writing code to building and running the app on the emulator. The session also introduced Git and version control concepts, including repositories, commits, and pushing code to remote platforms. It was explained that VS Code would be primarily used for writing Flutter code, while Android Studio would mainly be used for emulator management.",
        "learning_outcome": "Learned how to set up and manage Android emulators such as Pixel 6 and Pixel 9 Pro for testing Flutter applications, including configuring virtual devices and ensuring proper integration with the Flutter environment. Understood the basic concept of APIs and their significance in mobile app development, particularly how applications communicate with external servers and exchange data using formats like JSON. Gained hands-on experience in running a sample Flutter application, which helped in understanding the complete workflow from writing code to executing it on the emulator. Additionally, developed a foundational understanding of Git version control.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers or Risks till now."
    },
    {
        "date": "2026-02-06", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's work focused on building a strong foundation in the Dart programming language. The session covered core Dart concepts such as data types, variables, and basic syntax. Key differences between final and const, as well as var and dynamic, were explained in detail to understand how Dart manages memory, ensures type safety, and handles immutability in different scenarios. Basic programming constructs were also discussed, including functions, conditional statements, and simple example programs to strengthen logical thinking and coding structure. Towards the end of the session, the mentor assigned practice tasks related to Dart fundamentals and basic Flutter usage to be completed over the weekend.",
        "learning_outcome": "Developed a clear understanding of fundamental Dart programming concepts, including data types and variable declarations used in Flutter development. Learned the key differences between final and const, as well as var and dynamic, and understood when each should be used based on immutability, type safety, and runtime behavior. Strengthened overall programming basics through discussion of simple examples and logic-building exercises. Received practice assignments to work on over the weekend to reinforce these concepts through hands-on coding.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers found."
    },
    {
        "date": "2026-02-07", "hours": 6, "phase": "Phase 1",
        "work_summary": "During the weekend, I continued working on the assignments provided by my internship mentor to strengthen my understanding of Dart programming concepts. The tasks involved solving coding problems based on the seven basic data types in Dart, including int, double, String, bool, List, Map, and Set, along with concepts such as var, dynamic, final, and const. I practiced writing small programs to understand how each data type is declared, initialized, and used within Dart and Flutter applications. These exercises helped me improve my familiarity with syntax, variable handling, and basic program structure.",
        "learning_outcome": "Strengthened my understanding of Dart's seven core data types through consistent hands-on coding practice and repeated problem-solving exercises. Improved confidence in writing structured Dart programs by correctly applying concepts usage in different scenarios. Practiced working with collections like lists, maps, and sets to understand how data is stored, accessed, and modified within a program. Enhanced logical thinking and debugging skills by completing the mentor-assigned tasks.",
        "skills": "Flutter",
        "blockers": "Initially faced minor confusion while differentiating between var and dynamic while working on practice programs. These challenges were resolved through repeated practice, referring to documentation, and testing programs in the IDE."
    },
    {
        "date": "2026-02-08", "hours": 5, "phase": "Phase 1",
        "work_summary": "I continued working on the assignments given by my internship mentor to further improve my understanding of Dart programming concepts. I revised the seven basic data types in Dart — int, double, String, bool, List, Map, and Set — and practiced additional coding exercises to strengthen my logic and syntax clarity. I also focused on concepts like var, dynamic, final, and const to better understand when and where each should be used in real Flutter applications.",
        "learning_outcome": "Strengthened my understanding of Dart concepts by continuing the mentor-assigned assignments and practicing additional problems on data types and variables. Gained better clarity on using var, dynamic, final, and const in different scenarios within Dart programs. Improved coding confidence and logical thinking through consistent practice and debugging. Developed a deeper understanding of how these fundamental Dart concepts support Flutter app development.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-09", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session focused on understanding Dart operators and control flow statements used in everyday programming. The mentor explained arithmetic, comparison, and logical operators with simple examples. We also explored basic list handling and practiced using operators while working with list elements. The session then covered control flow concepts such as if–else, switch statements, and looping constructs like for, while, and do-while. Special attention was given to the ternary operator for writing short conditional expressions and the assert operator for debugging and validating assumptions during development. Additional assignments were provided to further strengthen understanding.",
        "learning_outcome": "Learned how to use arithmetic, comparison, and logical operators in Dart and understood how they help perform calculations, comparisons, and decision-making within programs. Gained clarity on implementing conditional statements such as if–else and switch, along with looping constructs like for, while, and do-while. Also understood how operators can be applied while working with lists and simple data handling tasks. Developed a better understanding of the ternary operator and the assert operator for debugging.",
        "skills": "Flutter",
        "blockers": "No Blockers found."
    },
    {
        "date": "2026-02-10", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session focused on understanding functions in Dart and their different types. The mentor explained the concept and importance of functions in structuring and reusing code. Various types of functions were discussed, including named functions, anonymous functions, arrow functions, the main function, recursive functions, and higher-order functions. The session also covered function parameters, including the difference between positional and named parameters, use of optional parameters, and default parameter values. Practical examples were demonstrated to show how these function types and parameters are used in real Flutter applications.",
        "learning_outcome": "Developed a clear understanding of the different types of functions in Dart and how they are used to structure and organize code efficiently. Learned the differences between positional, named, and optional parameters, along with the use of default parameter values to make functions more flexible and readable. Gained deeper insight into advanced concepts such as recursive functions and higher-order functions, and understood their practical relevance in real programming scenarios. Improved overall coding skills through hands-on problem-solving exercises.",
        "skills": "Flutter",
        "blockers": "No Blockers found."
    },
    {
        "date": "2026-02-11", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session focused on the fundamentals of Object-Oriented Programming (OOP) in Dart and how these concepts are applied in Flutter development. We learned about classes and objects, along with constructors such as default and parameterized constructors used to initialize object properties. Core OOP principles including encapsulation, inheritance, polymorphism, and abstraction were explained with simple examples. The session also introduced the use of interfaces in Dart through the implements keyword and explained the purpose of the this and super keywords while working with classes and inheritance.",
        "learning_outcome": "Gained a clear understanding of Object-Oriented Programming concepts in Dart and their importance in building structured Flutter applications. Learned how to create and use classes, objects, and constructors effectively. Understood key OOP principles such as encapsulation, inheritance, polymorphism, and abstraction, and how these concepts support modular, reusable, and maintainable code in real-world app development. Developed knowledge of implementing interfaces using the implements keyword and learned the proper usage of this and super keywords.",
        "skills": "Flutter",
        "blockers": "No Risks."
    },
    {
        "date": "2026-02-12", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session focused on understanding the difference between Stateless and Stateful widgets in Flutter and their roles in building user interfaces. The mentor explained that Stateless widgets are used when the UI does not change after being built, while Stateful widgets are required when the interface needs to update dynamically based on user interaction or data changes. A detailed walkthrough and live demonstration helped in understanding how state is created, managed, and updated within a Flutter application. We also gained hands-on experience by running a basic Hello World application on the emulator and built a simple counter application with increment and decrement buttons.",
        "learning_outcome": "Developed a clear understanding of the difference between Stateless and Stateful widgets and identified appropriate scenarios for using each in Flutter development. Learned how state changes directly impact the user interface and gained clarity on how the setState() method triggers UI updates by rebuilding the widget tree when data changes occur. Gained practical experience in running Flutter applications on the emulator and building simple interactive applications such as a counter app.",
        "skills": "Flutter, Android Studio",
        "blockers": "Initially faced minor confusion while understanding how setState() updates the UI and how Stateful widgets manage dynamic data. These issues were resolved through practice and guidance during the session."
    },
    {
        "date": "2026-02-13", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session featured an interactive quiz activity designed to review and evaluate our understanding of the topics covered so far during the internship. The quiz acted as a comprehensive recap of key concepts from Dart programming, Flutter fundamentals, widgets, Object-Oriented Programming principles, and development tools. It was conducted in an engaging and participative manner, encouraging interns to answer questions, explain their reasoning, and actively contribute to discussions. At the end of the activity, points were awarded based on performance, and I secured 3rd place in the quiz.",
        "learning_outcome": "Reinforced and revised previously learned concepts from Dart and Flutter through an interactive quiz-based recap session. Strengthened understanding of key topics by actively recalling answers, participating in discussions, and applying theoretical knowledge in a time-bound setting. The activity also encouraged healthy competition and peer learning. It helped identify specific areas that require further revision and practice.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-14", "hours": 6, "phase": "Phase 1",
        "work_summary": "Today's session was dedicated to working on assignments: developing two Flutter applications — a My Digital Card app and a Click Counter game app. I began by planning the UI structure and layout for the Digital Card app, designing a simple interface to display personal details using widgets such as Text, Container, Row, Column, and Image. After completing the layout design, I worked on the Click Counter game application, implementing interactive buttons to increment and decrement the count value. I tested both applications on the emulator and made minor adjustments to improve layout and responsiveness.",
        "learning_outcome": "Improved understanding of Flutter UI widgets and layout structures by designing and implementing the Digital Card application. Practiced arranging widgets, applying basic styling, and structuring the interface to create a clean and responsive layout. Strengthened knowledge of Stateful widgets and the use of setState() through the Click Counter game. Gained hands-on experience in building simple interactive applications and testing them on the emulator.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor issues while aligning UI elements in the Digital Card layout and managing button logic in the counter app. These were resolved through debugging, revising widget structure, and testing the app multiple times."
    },
    {
        "date": "2026-02-15", "hours": 5, "phase": "Phase 1",
        "work_summary": "Today, I was assigned to develop a Quote of the Day application using Flutter. The task involved creating a list containing five different quotes and displaying one quote on the screen at a time. I implemented a button labeled 'Next Quote' that allows users to navigate through the quotes sequentially. The logic was designed to ensure that once all quotes are displayed, the application loops back to the first quote, maintaining a continuous cycle. While working on this assignment, I used a Stateful widget to manage the current quote index and dynamically update the user interface whenever the button was pressed.",
        "learning_outcome": "Enhanced understanding of using lists in Dart to store, access, and manage data efficiently within a Flutter application. Gained practical experience working with Stateful widgets and learned how to update the user interface dynamically based on user interactions such as button presses. Developed clarity on implementing button-driven logic, maintaining an index, and looping through data to create a smooth and continuous user experience.",
        "skills": "Flutter, Android Studio",
        "blockers": "Initially faced slight confusion while implementing the looping logic to return to the first quote after reaching the last one. Also required some debugging to correctly update the quote index and refresh the UI. These issues were resolved through testing and revising the logic."
    },
    {
        "date": "2026-02-16", "hours": 6, "phase": "Phase 1",
        "work_summary": "Session focused on deepening understanding of Stateful and Stateless widgets — learning the key differences and how to identify situations where a widget needs to be converted from stateless to stateful based on dynamic data changes and user interaction requirements. Revisited how Flutter rebuilds the UI when state changes occur and how to structure widgets accordingly. Continued practicing state management through small assignments.",
        "learning_outcome": "Gained a clearer and more in-depth understanding of the differences between Stateful and Stateless widgets and their specific roles in Flutter UI development. Learned how to identify situations where a widget needs to be converted from stateless to stateful based on dynamic data changes and user interaction requirements. Improved understanding of basic state management concepts, including how data is stored within a widget and how UI updates are triggered.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    # ── PHASE 2 ──
    {
        "date": "2026-02-17", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today's session focused on implementing user input fields in Flutter applications. We learned how to use TextField widgets to take input from users and how to style them for a clear and user-friendly interface. The mentor demonstrated how to customize text fields with labels, hints, borders, and alignment to improve the overall UI. We also learned how to create a password input field where the entered text is hidden using the obscure text feature for security. We implemented a simple username and password input system, where user input was taken through text fields and handled within a Stateful widget.",
        "learning_outcome": "Learned how to implement and style TextField inputs in Flutter applications, including customizing properties such as decoration, labels, hints, and borders to create a clean and user-friendly interface. Understood how to configure secure password fields using obscured text to protect sensitive input. Improved knowledge of handling user input using Stateful widgets by connecting UI components with underlying logic and managing state updates effectively.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-18", "hours": 5, "phase": "Phase 2",
        "work_summary": "Today's session focused on understanding navigation in Flutter, including the use of push and pop methods to move between screens. We learned how navigation works in multi-screen applications and how data can be passed between pages. The mentor then introduced various UI feedback components such as Dialog, Alert Dialog, SnackBar, Bottom Sheet, and Toast messages, explaining their purpose and when to use each in real applications. Navigation was added between login and home screens, and UI feedback elements like alert dialogs and snack bars were integrated. The mentor also gave a quick live task to add additional features under certain constraints.",
        "learning_outcome": "Understood how to implement navigation in Flutter using push and pop methods to move between screens and manage the app's navigation stack effectively. Learned how to use dialog boxes, snack bars, bottom sheets, and toast messages to provide user feedback, confirmations, and alerts. Gained practical experience by integrating these features into an existing login application. Also strengthened problem-solving and implementation skills by completing a live task within given constraints.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Risks."
    },
    {
        "date": "2026-02-19", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today's session focused on understanding ListView and GridView in Flutter. We learned the basics of creating a simple ListView and also how to build dynamic lists that display data using builder methods. After this, we explored GridView and its use in designing layouts such as image galleries and product displays. We continued working on the existing login app, where we integrated a GridView example on the home page. This involved adding images to the assets folder, updating the pubspec.yaml file, and displaying images in a grid layout similar to a photo gallery. The mentor also introduced the physics property in Flutter to control scroll behavior and demonstrated the Stack widget.",
        "learning_outcome": "Gained a strong understanding of ListView and GridView and how they are used to display scrollable and grid-based data in Flutter applications. Learned how to implement dynamic lists using builder methods and how to structure UI for efficient rendering. Understood how to integrate images into an app using the assets folder and pubspec.yaml configuration. Improved knowledge of navigation and UI structuring by extending the login app with a gallery-style grid screen. Learned how the physics property affects scrolling behavior and how the Stack widget can be used to overlay widgets.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor issues while configuring the assets path in pubspec.yaml and aligning grid items properly within the layout. Also required some practice to understand scroll physics behavior and widget layering using Stack."
    },
    {
        "date": "2026-02-20", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today's session focused on understanding Inherited Widgets and Provider in Flutter and how they are used for state management across multiple widgets. The mentor explained how Inherited Widgets help share data efficiently down the widget tree without manually passing data through constructors. We also discussed the limitations of basic state management and why more structured approaches like Provider are preferred in larger applications. A detailed explanation was given on how Provider works internally, its advantages such as better scalability, cleaner code structure, and improved performance. The mentor demonstrated the practical implementation of Provider by integrating it into our existing login app.",
        "learning_outcome": "Gained a clear understanding of Inherited Widgets and their role in data sharing within Flutter applications. Learned how Provider simplifies state management compared to manually managing state. Understood the advantages of Provider such as improved code maintainability, separation of concerns, and better scalability for larger apps. Developed practical knowledge of implementing Provider in a real project by extending the login app with additional functionality.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-21", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today I worked on the assignment to build a Contact Manager Flutter application that demonstrates real-world multi-screen features. The task involved creating a two-screen app using navigation, ListView, dialogs, and SnackBar components. On the first screen, I implemented a contact list page displaying at least five dummy contacts using a ListView and ListTile widgets, each showing a name, phone number, and a leading person icon. A FloatingActionButton was added to navigate to the second screen for adding new contacts. When a contact item is tapped, an AlertDialog was implemented to display the contact details. On the second screen, I created an Add Contact page with TextFields and a Save button.",
        "learning_outcome": "Gained strong hands-on experience in building a multi-screen Flutter application. Learned how to use Navigator.push and pop for screen transitions and how to implement AlertDialog and SnackBar for user feedback. Improved understanding of ListView and ListTile for displaying structured data. Strengthened skills in handling user input through TextFields and managing UI interactions across screens.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor issues while passing data between screens and managing navigation flow after saving a contact. Also required some debugging to correctly display dialogs and snack bars at the right time."
    },
    {
        "date": "2026-02-22", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today I worked on the second assignment — building a Photo Gallery Flutter application using GridView, Stack, BottomSheet, and Navigation concepts. On the first screen (Gallery Grid Page), I implemented a GridView.count with crossAxisCount: 2 to display six colored containers representing photos. Each grid item was designed using a Stack widget, where the background color container was overlaid with a Positioned text widget showing labels like 'Photo 1', 'Photo 2'. When a grid item was tapped, I implemented a Modal BottomSheet that displayed three options: View Full, Share, and Delete, each with respective icons. Selecting 'View Full' navigated to the second screen where the selected colored container was displayed in full-screen mode.",
        "learning_outcome": "Gained practical experience in using GridView.count to create structured grid-based layouts. Improved understanding of the Stack and Positioned widgets to layer UI elements and design visually organized components like photo cards. Learned how to implement and customize a Modal BottomSheet to provide interactive options. Strengthened knowledge of screen navigation using Navigator and passing data between screens for full-view display.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor issues with positioning text correctly inside the Stack and handling BottomSheet interactions properly. Also needed careful handling of navigation to ensure the correct photo data was displayed on the full-screen page."
    },
    {
        "date": "2026-02-23", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today's session was focused on refining the previously developed applications and improving overall code structure. I revisited the Contact Manager and Photo Gallery apps to enhance UI alignment, spacing, and responsiveness. Minor improvements were made to widget structuring to ensure cleaner code and better readability. The mentor also discussed best practices for organizing Flutter projects, such as separating widgets into different files, maintaining proper naming conventions, and structuring folders efficiently. Additionally, small enhancements were implemented in the existing apps, such as improving button styling, refining layout spacing using Padding and SizedBox, and optimizing navigation flow.",
        "learning_outcome": "Improved understanding of writing clean and maintainable Flutter code. Learned the importance of proper project structure and file organization. Strengthened UI design skills by refining layouts and improving responsiveness. Gained confidence in debugging and optimizing previously built applications. This session helped in understanding that app development is not only about building features but also about improving code quality, structure, and user experience for long-term scalability.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor challenges in restructuring widgets without affecting functionality. Also needed to carefully test navigation flow after making modifications."
    },
    {
        "date": "2026-02-24", "hours": 7, "phase": "Phase 2",
        "work_summary": "Today's session introduced the fundamentals of networking in Flutter and how mobile applications fetch data from the internet using REST APIs. We learned how apps communicate with servers and how data is requested and received through API calls. The mentor explained the structure of a URL and API endpoint, including protocol, domain, endpoint path, and ID parameters. We also discussed common REST operations such as GET, POST, PUT, and DELETE, and their role in real-world applications. The session covered the use of the http package in Flutter. We explored JSON data format, how servers send responses in JSON, and how to perform JSON parsing. Important concepts like Future, async, and await were explained. For hands-on practice, we implemented API integration using free public APIs to fetch random jokes and user profiles displayed in the UI using FutureBuilder.",
        "learning_outcome": "Gained a strong understanding of REST API concepts and how mobile apps communicate with servers over the internet. Learned how to use the http package to make API calls and how to structure URLs and endpoints properly. Developed clarity on asynchronous programming using Future, async, and await, and how these concepts ensure smooth UI performance. Improved knowledge of JSON format and parsing, including handling lists of objects and displaying dynamic data in the UI using FutureBuilder. Understood common HTTP status codes and their meaning in API responses.",
        "skills": "Flutter, Android Studio",
        "blockers": "Initially found it slightly challenging to understand asynchronous flow using Future and async/await, and how data loads into the UI using FutureBuilder. Also needed some practice to correctly parse JSON data and display it properly."
    },
    {
        "date": "2026-02-25", "hours": 6, "phase": "Phase 2",
        "work_summary": "Today's session focused on implementing form validation and introducing animations in Flutter. We learned how to use a GlobalKey to manage form state and how to wrap input fields inside a Form widget. The mentor explained the difference between TextField and TextFormField, and how to add a validator function to validate user input such as empty fields, password length, and proper formatting. These validations were implemented in our existing login app. The session then moved to Flutter animations, where we explored basic animation types such as Fade, Scale, and Slide animations. We also integrated Lottie animations into the login app by adding the required dependency and updating the pubspec.yaml file.",
        "learning_outcome": "Gained practical understanding of implementing form validation using Form, GlobalKey, and TextFormField. Learned how to apply validator functions to ensure proper user input handling. Developed knowledge of basic Flutter animations such as fade, scale, and slide, and understood their importance in enhancing user experience. Improved confidence in integrating third-party packages like Lottie by updating pubspec.yaml and using animation assets effectively.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-26", "hours": 5, "phase": "Phase 2",
        "work_summary": "Today's session focused on a comprehensive recap of all Phase 2 concepts covered so far. The mentor revised important topics including navigation operations, ListView, GridView, TextFormField with validators, Stack widget, Provider and its setup methods, Inherited Widgets, Alert Dialog, SnackBar, and BottomSheet. We also revisited networking concepts such as REST API integration, JSON parsing, async/await, and animations in Flutter. After the revision, the mentor conducted an online quiz-based assessment through a selected website. The quiz consisted of 30 questions, with 30 seconds allotted per question. I was able to secure 2nd place with a score of 27/30, which was both motivating and encouraging.",
        "learning_outcome": "Revised and strengthened understanding of key Phase 2 Flutter concepts including navigation, ListView, GridView, form validation, Stack, Provider setup, and UI feedback components like dialogs, snack bars, and bottom sheets. Refreshed knowledge of REST API integration, JSON parsing, async/await, and basic animations. The quiz helped improve quick recall of concepts, time management, and confidence in answering technical questions under pressure. Securing 2nd place boosted confidence since I got 3rd place last time.",
        "skills": "Flutter, Android Studio",
        "blockers": "The time limit of 30 seconds per question required quick decision-making, which was challenging for some scenario-based questions. However, consistent revision and practice helped in answering most questions correctly."
    },
    {
        "date": "2026-02-27", "hours": 5, "phase": "Phase 2",
        "work_summary": "Today's session involved a quiz-based assessment on REST API, JSON, JSON parsing, and FutureBuilder — 30 questions with 30 seconds per question. I secured 3rd place in the quiz. After a short break, the mentor informed us about a surprise MCQ quiz focusing on the topic Splash Screen in Flutter. Before starting the test, the mentor briefly revised the key highlights related to splash screen implementation. I was able to secure 3rd place again. The session concluded with the mentor assigning weekend tasks related to the concepts learned.",
        "learning_outcome": "Strengthened understanding of REST API integration, JSON data handling, JSON parsing, and the use of FutureBuilder through a competitive quiz assessment. The timed format improved quick thinking, concept recall, and the ability to answer technical questions efficiently. The surprise quiz helped reinforce knowledge about Splash Screen implementation and encouraged quick preparation and adaptability. Securing 3rd place in both quizzes reflected consistent understanding of the topics.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-02-28", "hours": 5, "phase": "Phase 2",
        "work_summary": "Today's session involved working on an assignment where we were asked to develop a simple Flutter application of our own choice, applying the concepts learned during the internship. I chose to build a Decision Maker App (Spin the Choice). The app was designed to help users make quick decisions by randomly selecting an option from a predefined list. I implemented basic UI components using Flutter widgets such as Container, Text, Button, and layout widgets to structure the interface. The logic of the app was built to randomly choose an option whenever the user presses the spin or decision button. I tested the application on the emulator and refined the layout to ensure smooth functionality.",
        "learning_outcome": "This assignment helped strengthen understanding of Flutter widget structuring and UI design principles. It improved confidence in independently designing a small application from scratch and applying previously learned concepts such as state management, button interactions, and layout widgets. Working on this custom app also enhanced problem-solving skills by implementing random decision logic and managing UI updates dynamically. This was great experience in finding and creating our own application of choice with proper use of all knowledges learnt till now.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially required some experimentation to design the UI layout and implement the random decision logic effectively. Minor adjustments were needed to ensure the UI updated correctly when the decision button was pressed."
    },
    # ── PHASE 3 ──
    {
        "date": "2026-03-01", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I decided to work on a unique and advanced project idea to further improve my practical Flutter development skills. I began exploring concepts related to Firebase backend integration and studied how APIs can be used to handle dynamic data in mobile applications. This involved understanding how backend services support features such as data storage, authentication, and real-time updates in modern apps. Along with this, I started researching and planning the structure for a project titled 'Digital Twin City Simulator', which is an advanced application concept that simulates a virtual representation of a city using interactive components and data-driven features.",
        "learning_outcome": "Gained introductory understanding of Firebase as a backend service and how it can be used in Flutter applications for storing and retrieving data. Learned how APIs interact with mobile applications to provide dynamic information and services. This exploration helped expand knowledge beyond basic UI development and introduced the importance of backend integration in building scalable and real-world mobile applications.",
        "skills": "Flutter, Android Studio",
        "blockers": "As this project involves advanced concepts, it required additional research to understand backend integration and API handling effectively. Some complexity was encountered while planning how to structure such a large-scale application."
    },
    {
        "date": "2026-03-02", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session marked the beginning of Phase 3 concepts, where the mentor introduced Firebase and backend development concepts. Session started with a brief theoretical overview covering the history of Firebase and its role as a Backend-as-a-Service (BaaS) platform. We learned about Firebase services such as database management, hosting, authentication, analytics, cloud storage, notifications, and serverless backend logic. The mentor also explained the difference between traditional backend architectures and Firebase's serverless approach. The session further covered database concepts such as the difference between SQL and NoSQL databases. Additionally, we explored Firebase database options, including Realtime Database (RTDB) and Cloud Firestore, understanding their differences, use cases, and suitability for large-scale applications.",
        "learning_outcome": "Gained a strong conceptual understanding of Firebase as a Backend-as-a-Service platform and how it supports modern mobile and web application development. Learned about the various Firebase services that provide backend functionalities such as authentication, storage, analytics, and notifications without requiring server management. Improved understanding of database structures and scaling techniques, including the differences between SQL and NoSQL databases and how data is stored and managed in Firebase. Also learned about Realtime Database and Cloud Firestore, their architecture, use cases, and how Firestore queries such as filtering, sorting, and pagination are applied to manage large datasets efficiently.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-03", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on the complete Firebase setup process for integrating backend services into our Flutter application. The mentor demonstrated step-by-step how to create a Firebase project, register the Android application, and configure it properly. We learned how to copy and add the required Firebase plugin and project ID into the gradle.kts (project-level) file and how to configure the app-level gradle.kts file with necessary dependencies. The process also included downloading and placing the google-services.json file correctly inside the Android app directory. Further, we updated the pubspec.yaml file by adding dependencies for Firebase Authentication and Cloud Firestore. The mentor also briefly discussed CRUD operations in theory.",
        "learning_outcome": "Gained practical understanding of the complete Firebase setup process in a Flutter project. Learned how to configure gradle files, integrate google-services.json, and manage dependencies in pubspec.yaml. Understood how Firebase Authentication and Firestore connect with a Flutter application. Strengthened backend integration knowledge by testing Firebase within the existing login app. Also developed conceptual clarity about CRUD operations in Firestore.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially faced minor confusion while configuring the gradle.kts files and ensuring the Firebase plugin was added at the correct project and app levels. Also required careful attention while placing the google-services.json file in the correct directory, as incorrect placement caused build errors."
    },
    {
        "date": "2026-03-04", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on understanding CRUD operations in Firebase Cloud Firestore. The mentor explained how data can be managed in Firestore using different operations such as Create, Read, Update, and Delete. We first learned about the create operation, where new data can be added to a collection using the .add() method. For the read operation, the mentor demonstrated how to retrieve data using .get() to fetch all stored data and .snapshots() to receive real-time updates. The session also covered update operations, where specific fields within a document can be modified. Finally, we discussed the delete operation. The mentor mentioned that in the next session we will implement these CRUD operations practically.",
        "learning_outcome": "Gained a clear understanding of Firestore CRUD operations and how they are used to manage application data. Learned how to add new data using .add(), retrieve data using .get() and .snapshots(), update specific fields within documents, and delete records when required. This session helped build foundational knowledge for implementing real-time database operations in Flutter applications. It also improved understanding of how Firestore collections and documents are structured and how data flows between the Flutter application and the backend database.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-05", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on setting up and integrating Firebase Authentication and Cloud Firestore with our existing Flutter login application. We went through the complete configuration process and ensured that Firebase services were correctly connected to the project. The mentor demonstrated how CRUD operations can be applied using Firestore and how authentication services work alongside database storage. As part of the implementation, we added a Register feature to the existing login app where users can enter their username, email, and password. These credentials were stored in Firestore as well as Firebase Authentication, allowing users to later log in using their email and password.",
        "learning_outcome": "Gained hands-on experience in integrating Firebase Authentication and Cloud Firestore within a Flutter application. Learned how to create a user registration system where user credentials are securely stored and used for authentication. Improved understanding of how Firestore CRUD operations interact with authentication workflows in real-world applications. This session strengthened backend integration skills and helped in understanding how user data management and login systems are implemented in mobile apps.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially required careful configuration of Firebase services and dependencies to ensure both authentication and Firestore worked correctly with the existing login app. Minor issues occurred while verifying the registration and login flow, but they were resolved through testing and mentor guidance."
    },
    {
        "date": "2026-03-06", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on the practical implementation of CRUD operations using Firebase Cloud Firestore. The mentor demonstrated how to manage dynamic data within the application by integrating CRUD functionality into our existing login app. For better understanding, a Student List View feature was developed where users can manage student records directly within the application. An Elevated Button was added that allows users to add new student details. On clicking the button, a form appears where users can enter information such as student name, email, age, and ID. Once saved, the student record is stored in Firestore and displayed in the ListView dynamically. The list included edit and delete icons beside each student entry.",
        "learning_outcome": "Gained hands-on experience implementing Firestore CRUD operations in a real Flutter application. Learned how to create, display, update, and delete dynamic data using Firestore collections and documents. Improved understanding of integrating backend database functionality with interactive UI components such as ListView, buttons, and icons. This exercise also helped in understanding how modern mobile applications manage dynamic lists and user-generated data, combining clean UI design with backend data management.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially required careful handling of data updates to ensure the list refreshed correctly after adding or editing student records. Minor debugging was needed while connecting UI actions with Firestore operations."
    },
    {
        "date": "2026-03-07", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I spent time revising the topics previously covered during the internship sessions to strengthen my understanding. I reviewed key Flutter and Firebase concepts and ensured better clarity on their implementation and workflow within mobile applications. Along with revision, I also worked on self-study related to my advanced project idea — Digital Twin City Model Application. I explored various sources and collected relevant datasets that could potentially be used for this project. The focus was on understanding the structure of the datasets, analyzing different attributes, and examining how multiple datasets could be merged together.",
        "learning_outcome": "Strengthened conceptual understanding by revising previously learned Flutter and Firebase concepts, reinforcing knowledge of application structure, backend integration, and database operations. Additionally, gained initial exposure to dataset collection, exploration, and preprocessing, which are important for building data-driven applications. Learned to analyze dataset attributes, evaluate their relevance, and study how multiple datasets can be merged and structured for future machine learning model training.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-08", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I continued exploring Flutter development concepts, particularly focusing on the process of building APK files. I learned the difference between debug builds and release builds, where debug builds are mainly used for developer testing and debugging, while release builds (--release) are optimized for production and application distribution. In addition to this, I spent time gaining further insights into Firebase features. I also continued working on my self-learning project — Digital Twin City Model application, where I focused on improving and cleaning the datasets that I previously collected.",
        "learning_outcome": "Gained a clearer understanding of Flutter build processes, particularly the difference between debug and release builds and their role in application testing and deployment. Improved awareness of Firebase capabilities and how backend services integrate with mobile applications. Also enhanced knowledge of dataset cleaning and preparation, which is an essential step for future machine learning model development.",
        "skills": "Flutter",
        "blockers": "Working with raw datasets required careful analysis and restructuring to make the data suitable for future model training. Understanding how to optimize and clean the dataset effectively required additional research and experimentation."
    },
    {
        "date": "2026-03-09", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on revising the concepts discussed in the previous class and clearing doubts at the code level. The mentor provided a detailed explanation of several lines of code that previously caused confusion. We learned about the use of constructors in Dart, especially the usage of 'required this' for initializing class variables properly. The mentor also explained how JSON data is stored in Dart using Map<String, dynamic> and why proper formatting is important to safely create object instances. In this context, the use of a factory constructor was discussed as a translator mechanism that converts JSON data into Dart objects. We also encountered an issue while running the application, which the mentor assigned as a debugging task, and after analyzing the problem, we identified a small mistake in the setState() definition and corrected it.",
        "learning_outcome": "Improved understanding of Dart constructors and object initialization, particularly the use of required this for assigning values to class properties. Learned how JSON data is handled in Dart using Map<String, dynamic> and how factory constructors help convert JSON responses into Dart objects safely. Gained clarity on the role of the underscore (_) in Dart for defining private members. The debugging activity enhanced problem-solving and troubleshooting skills.",
        "skills": "Flutter, Android Studio",
        "blockers": "Initially faced difficulty understanding how JSON data maps to Dart objects and how factory constructors simplify object creation. Additionally, identifying the exact issue causing the application to fail required careful code review, but the problem was resolved after correcting the setState() implementation."
    },
    {
        "date": "2026-03-10", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on reviewing and refining the existing Firebase Firestore CRUD implementation in the Flutter login application. The mentor explained how the Student List feature works with Firestore, where student details such as name, email, age, and grade are stored and displayed in real time using StreamBuilder. We also revised how edit, update, and delete operations function through the icons provided in each student entry. Additionally, the mentor explained the use of modal bottom sheets for adding and editing student records. Some UI concepts were also clarified, including the use of EdgeInsets.symmetric and EdgeInsets.fromLTRB for proper padding and spacing.",
        "learning_outcome": "Gained a clearer understanding of the existing Firestore CRUD implementation in the Flutter application. Reviewed how StreamBuilder is used to display real-time data from Firestore and how documents are converted into Dart objects using factory constructors. Also improved understanding of how edit, update, and delete operations interact with Firestore documents through service methods. Additionally, developed better knowledge of Flutter UI layout design, including padding and spacing.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially required careful understanding of how Firestore streams update the UI in real time and how document IDs are used when updating or deleting records."
    },
    {
        "date": "2026-03-11", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session included a Phase 3 assessment quiz based on Firebase and backend concepts covered in recent classes. Before the quiz, we were given some time to revise the topics, after which the mentor conducted a test consisting of 40 questions with about 15 seconds per question. The questions included a mix of easy, medium, and some scenario-based problems related to Firebase setup, CRUD operations, NoSQL concepts, and database structures in RTDB and Cloud Firestore. Some questions required understanding JSON data structures and document–collection models. I was able to score 33 out of 40 marks and successfully secured 1st place in the test.",
        "learning_outcome": "This quiz helped reinforce understanding of Firebase database structures, NoSQL concepts, JSON data representation, and CRUD operations in Firestore and RTDB. It also improved quick decision-making and time management skills, as each question had a strict time limit. The activity helped evaluate my current level of understanding and boosted confidence in applying backend concepts learned during Phase 3. First place in the Phase 3 assessment marked my first top position in the ongoing assessments.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-12", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on adding a search feature to the existing Student List in the Flutter login application. A search icon was added to the AppBar, which converts the title into a TextField when activated, allowing users to search student records by name or email. We implemented search logic using _searchQuery and _isSearching, where the _applySearch() method filters the student list based on the entered text and displays matching results dynamically. The mentor also explained how to handle cases where no matching student is found and how to display the number of filtered results.",
        "learning_outcome": "Developed a better understanding of implementing search functionality in Flutter applications using state variables and filtering logic. Learned how to dynamically filter lists using the where() method and update the UI using setState() when user input changes. Also improved knowledge of AppBar actions, TextField integration, and conditional UI rendering based on search states. The session also strengthened understanding of real-time UI updates and list filtering techniques.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-13", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on adding a grade-based filtering feature to the existing Student List in the Flutter login application. We implemented ChoiceChip widgets placed horizontally to allow users to filter students based on grades such as A, B, C, D, or view all records. When a grade is selected, the application retrieves the corresponding student data from Firestore using a filtered query. The mentor explained how the where() query in Firestore is used along with orderBy() to filter students by grade and display the results dynamically through StreamBuilder. The existing search functionality was also integrated with the grade filter. Additionally, we learned about Firebase indexing requirements when combining where and orderBy queries.",
        "learning_outcome": "Improved understanding of Firestore query operations, especially filtering data using where() conditions and sorting results using orderBy(). Learned how to implement UI filtering using ChoiceChip widgets and manage state changes with setState() to update the displayed data dynamically. Also gained knowledge about Firestore indexing, which is required for complex queries combining filtering and sorting. This session strengthened skills in building interactive data-driven interfaces in Flutter.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-14", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today I worked on an assignment to develop an Employee Management Page using Flutter integrated with Firebase Firestore. I created an Employee model class with fields such as id, name, age, department, salary, and email, along with methods like toMap() and fromFirestore() for storing and retrieving data from Firestore. An EmployeeService class was implemented to perform CRUD operations. The UI was designed to display employee details using Flutter cards with edit and delete options. A Floating Action Button with a form and validation was implemented to add new employees. Additionally, a search feature in the AppBar was added to filter employees by name or email, and department-based filtering using ChoiceChips was implemented. A salary summary bar was also developed to display total employees and average salary.",
        "learning_outcome": "Gained hands-on experience in building a data-driven Flutter application integrated with Firebase Firestore. Learned how to structure model classes, implement CRUD operations, and display real-time data in the UI. Improved understanding of search and filtering techniques, form validation, and UI components such as ChoiceChips, Cards, and FloatingActionButton. This task also strengthened knowledge of Firestore queries, state management for filtering/searching, and calculating dynamic data summaries within Flutter applications.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-15", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I worked on enhancing the Employee Management application by adding additional improvements and bonus features suggested by the mentor. These updates were focused on refining the functionality and improving the overall user interface of the page. I also spent some time working on self-improvement tasks, further optimized certain parts of the application, and explored ways to make the UI and functionality better. Along with this, I revised previously learned Flutter and Firebase concepts and explored new features that will be covered in the upcoming class.",
        "learning_outcome": "Improved understanding of how to enhance an existing Flutter application by adding additional features and UI refinements. Strengthened knowledge of Firestore integration, CRUD workflows, and UI component usage through revision and practical implementation. Also developed better awareness of optimizing application structure and improving usability while working on self-assigned improvements.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-16", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on enhancing the existing Student List feature in the Flutter login application by adding advanced filtering and sorting options. We implemented a 'Show More Options' feature that allows users to dynamically load additional student records using a limit-based query. The mentor explained how Firestore queries can combine filters, sorting, and limits for efficient data retrieval. We added age-based sorting functionality with ascending and descending options using an icon toggle. Additionally, a RangeSlider was implemented to filter students based on an age range. A 'Show More' button was also implemented to load additional students in batches, improving the usability of the list and demonstrating how pagination-like behavior can be achieved using Firestore query limits.",
        "learning_outcome": "Gained deeper understanding of advanced Firestore query operations, including combining where, orderBy, and limit conditions in a single query. Learned how to implement dynamic filtering and sorting in Flutter using state variables and UI controls such as RangeSlider, ChoiceChips, and toggle icons. Improved knowledge of handling multiple filters simultaneously. Also understood how limit-based queries can be used to implement 'Show More' functionality, which is useful for handling large datasets efficiently.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-17", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on revision of previous Firebase and Firestore concepts, along with learning the difference between Spark and Blaze plans. The mentor explained how the Spark plan provides free usage limits, while the Blaze plan follows a pay-as-you-go model, including details about billing, free credits, budget alerts, and how usage is tracked. We also learned about Firebase CLI integration, which provides an alternative way to connect Firebase with a Flutter project. Additionally, some video demonstrations were shown to strengthen understanding of Firestore and Flutter integration. At the end of the session, a surprise quiz of 40 questions was conducted. I scored 34/40 and secured 1st place, as bonus points were awarded for quick responses.",
        "learning_outcome": "Gained a clear understanding of the difference between Spark and Blaze plans in Firebase, including when to use each based on project requirements. Learned how Blaze plan billing works, including pay-as-you-go pricing, budget alerts, and usage monitoring. Improved knowledge of Firebase CLI integration as an alternative to manual setup. This session enhanced awareness of cost management in Firebase projects and improved conceptual clarity through revision.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-18", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on Firebase Storage concepts and file handling in Flutter. The mentor explained the difference between Firestore and Firebase Storage, where Firestore is used as a database to store structured data while Storage is used to store files such as images, videos, and PDFs using ref() as a pointer to file locations. The session covered Firebase Storage rules, permissions setup in Android Manifest, and how files are uploaded and accessed securely. The mentor explained key operations such as putFile(), getDownloadURL(), delete(), and getMetadata(), along with the step-by-step image upload flow. Additionally, we were introduced to useful packages like image_picker, file_picker, cached_network_image, and url_launcher.",
        "learning_outcome": "Gained a clear understanding of the difference between Firestore and Firebase Storage and when to use each for storing structured data vs media files. Learned how to use Storage references (ref()) and perform file operations like upload, download, delete, and metadata retrieval. Improved knowledge of handling media in Flutter applications, including image selection, file picking, caching images for better performance, and opening external resources like PDFs and videos.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-19", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I worked on the Firebase Storage implementation by upgrading the existing setup in the application. I referred to tutorials to better understand the configuration and improve the file handling features. Along with this, I did a brief revision of all topics covered so far. I also focused on enhancing previous assignment projects by adding extra features and refining the UI to make them more professional and practical. This included improving structure, usability, and overall presentation of the applications.",
        "learning_outcome": "Improved understanding of Firebase Storage setup and integration through self-learning and practical exploration. Strengthened overall knowledge by revising previously learned Flutter and Firebase concepts. Enhanced skills in refining and upgrading existing projects by adding new features and improving UI/UX. This session helped in building a more professional approach towards application development and continuous improvement.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-20", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on the practical implementation of Firebase Storage in Flutter applications. The mentor explained in detail how file storage works, including uploading and managing images, PDFs, and videos using Firebase Storage. We implemented a FileModel class to handle file details such as name, URL, type, size, and upload time. A FileService class was created to handle file upload operations using methods like putFile() and putData(). We also integrated packages such as image_picker, file_picker, cached_network, and url_launcher. Additionally, it was discussed that Firebase Storage requires a credit card setup (Blaze plan) for full usage. As an alternative, the mentor suggested using Supabase Storage in the upcoming sessions.",
        "learning_outcome": "Gained practical understanding of Firebase Storage integration in Flutter, including uploading and retrieving files using storage references. Learned how to manage different file types like images, PDFs, and videos and handle their metadata effectively. Improved knowledge of using external packages such as image_picker and file_picker for file selection. Also understood the importance of file size handling and storage organization in real-world applications. This session also provided insight into Firebase billing requirements and alternative backend solutions like Supabase.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced some difficulty while setting up Firebase Storage, as it requires upgrading to the Blaze plan with a credit card, which limited full implementation during practice."
    },
    {
        "date": "2026-03-21", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on revising key Flutter and Firebase concepts to strengthen my understanding. I also attempted to set up and explore Firebase Storage with billing enabled. Additionally, I started studying Supabase as an alternative backend solution, particularly its SQL-based structure, which differs from Firebase's NoSQL approach. I explored the differences in data structure, syntax, and usage patterns, and tried to understand how Supabase handles storage and database operations. I also compared how queries and data relationships are managed differently in SQL vs NoSQL systems.",
        "learning_outcome": "Improved understanding of Flutter and Firebase concepts through revision and practical exploration. Gained initial exposure to Firebase Storage setup with billing considerations. Also developed basic knowledge of Supabase architecture and SQL-based data handling, and how it differs from Firebase's NoSQL model. This session helped in understanding different backend approaches and choosing appropriate technologies based on project needs.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-22", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on learning Flutter concepts and working on existing projects and assignments. I spent time improving the implementation and refining the features of my ongoing work. Additionally, I identified and resolved issues related to cache accumulation, which was causing system slowdown. I cleared unnecessary cached data and optimized the environment to ensure smoother performance. I also continued enhancing my projects to make them more efficient and better structured.",
        "learning_outcome": "Improved understanding of Flutter development through continuous practice and project work. Learned the importance of managing cache and system resources to maintain smooth performance during development. Enhanced skills in optimizing existing applications, debugging issues, and refining project structure.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-23", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session focused on learning Supabase as an alternative backend solution to Firebase. We started with video lectures explaining how Supabase works, including a small to-do list example. The mentor explained how Supabase, being a SQL-based system, can still handle images, files, and media using URLs. Further, we were introduced to Supabase features and basic CRUD workflow, followed by a hands-on setup where we created an organization and configured a storage bucket. We connected Supabase with our Flutter project by updating pubspec.yaml and configuring Supabase URL and anon key in main.dart. Additionally, we worked on a partial implementation for uploading images, PDFs, and videos using Supabase Storage.",
        "learning_outcome": "Gained a clear understanding of Supabase architecture and how it differs from Firebase, especially in terms of SQL vs NoSQL data handling. Learned how Supabase Storage manages files using buckets and public URLs for accessing media. Improved knowledge of integrating Supabase with Flutter, including setup, configuration, and basic file upload operations.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Initially required some time to understand the difference in structure and syntax between Firebase and Supabase, especially due to SQL-based handling. Also needed careful setup of Supabase credentials and bucket configuration to ensure proper connectivity."
    },
    {
        "date": "2026-03-24", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on revising previous sessions, especially concepts related to Supabase and backend integration. The mentor conducted a surprise presentation activity where we were asked to explain Supabase concepts. It was an interactive session where everyone shared their understanding, and I also presented my points. Additionally, we worked on fixing errors in the existing Supabase-Flutter integration, ensuring proper connectivity and resolving configuration issues.",
        "learning_outcome": "Strengthened understanding of Supabase concepts through revision and presentation. Improved communication and presentation skills by explaining technical concepts clearly in front of others. Also gained better clarity in debugging and resolving integration issues between Supabase and Flutter.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-25", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today's session started with a revision of yesterday's Supabase Storage concepts. After that, we worked on implementing a File Manager UI design in Flutter, where we handled file operations like uploading, displaying, opening, and deleting files using Supabase Storage. The design included features such as listing uploaded files, displaying file size, using icons based on file type (image, PDF, video), and implementing floating action buttons for selecting and uploading different file formats. We also handled operations like refreshing data, opening files using URLs, and deleting files from storage.",
        "learning_outcome": "Gained better understanding of Supabase Storage integration with Flutter UI, including handling multiple file types like images, PDFs, and videos. Learned how to design a complete file manager interface with dynamic data display and user interaction. Improved knowledge of file handling operations such as upload, fetch, open, and delete, along with managing file metadata like size and type.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-26", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on revising previous concepts and improving the Supabase setup. We updated the configuration by applying new storage policies for read and insert operations in the bucket to properly handle media files. This helped in resolving earlier issues related to file access and uploads. Additionally, the existing code was enhanced and refined, including better handling of file uploads and UI improvements in the File Manager application. We also worked on setting up Gmail in the emulator, where I initially faced issues due to device compatibility. After trying different devices (Pixel 6, Pixel 9a), I finally switched to a stable Pixel 6a with Android 13, which resolved the issue.",
        "learning_outcome": "Gained better understanding of Supabase storage policies, especially how read and insert permissions work for secure media handling. Learned how to troubleshoot backend configuration issues and fix access-related errors effectively. Also understood the importance of choosing the right emulator/device configuration for proper app functionality.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced issues with Supabase storage access due to missing or incorrect policy configuration, which initially prevented file uploads and retrieval. Also encountered problems with emulator compatibility, as Pixel 6 did not support Google Play services properly. These challenges were resolved by correcting storage policies and using a stable emulator configuration (Pixel 6a with Android 13)."
    },
    {
        "date": "2026-03-27", "hours": 6, "phase": "Phase 3",
        "work_summary": "Today I focused on the completion and enhancement of the existing Supabase File Manager application. I added several modern UI improvements, making the interface more attractive and user-friendly with better layout, colors, and structured components. New features were implemented such as file preview for images, proper display of file size, and improved file cards with icons based on file type. I also added support for PDF and video uploads, along with proper handling and access through URLs. Additionally, a delete functionality with confirmation dialog was implemented to manage files efficiently.",
        "learning_outcome": "Gained deeper understanding of building complete file management systems using Supabase Storage and Flutter UI. Learned how to implement advanced UI components, file previews, and dynamic data display effectively. Improved knowledge of handling multiple file types (images, PDFs, videos) along with managing file metadata like size and type. Also strengthened skills in CRUD operations for storage, including upload, fetch, and delete functionalities.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-28", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on improving the UI widgets in the existing login page, making the design more clean, structured, and user-friendly. I worked on refining layouts, spacing, and overall component arrangement to enhance the visual appearance and usability of the application. Along with this, I spent time revising all the concepts learned this week, especially understanding how the code flows, how different widgets interact, and how data moves between UI and backend.",
        "learning_outcome": "Improved understanding of Flutter widget structuring and UI design principles, including layout management and component organization. Gained better clarity on application flow, state handling, and interaction between frontend and backend logic. Strengthened conceptual knowledge by revising weekly topics and applying them in real code scenarios.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-29", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on revising the complete learning journey from Dart basics to Flutter application development, covering all concepts from Phase 1, Phase 2, and Phase 3. As we are nearing the end of the learning phase, I prepared myself for the upcoming comprehensive test by reviewing key topics and previously implemented work. Along with revision, I also spent time practicing on learning platforms to strengthen my hands-on experience.",
        "learning_outcome": "Strengthened overall understanding of Dart, Flutter, and backend integration concepts through complete revision. Improved confidence in handling end-to-end application development, from basic programming to advanced features like Firebase and Supabase integration. Enhanced ability to connect theoretical concepts with practical implementation.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-30", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today I focused on learning how to deploy a Flutter application on the Google Play Store, including the steps involved in preparing the app for release. I explored how apps can be updated after deployment, such as version updates, bug fixes, and feature enhancements. Additionally, I researched ways to improve application quality post-deployment, including performance optimization and user experience improvements. I also explored testing and project management tools like GitHub and Jira.",
        "learning_outcome": "Gained understanding of the app deployment process on the Play Store, including release management and update cycles. Learned how continuous improvements and updates are handled after an app is published. Improved knowledge of testing strategies and tools, including how platforms like GitHub and Jira support debugging, issue tracking, and team collaboration.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-03-31", "hours": 5, "phase": "Phase 3",
        "work_summary": "Today's session focused on revising the image picker and file upload concepts, with a deeper understanding of how they work with the Supabase backend (SQL-based). The mentor explained the practical workflow of handling media files and how they are stored and accessed through Supabase storage. We also worked on updating Supabase storage policies, where new rules were written to fix issues related to the delete functionality, which was not working earlier. After proper configuration, the delete feature was successfully implemented. Additionally, the mentor discussed that the learning phase is now complete, and we are moving towards the project phase.",
        "learning_outcome": "Strengthened understanding of image picker integration with Supabase storage and how backend operations work in a SQL-based system. Learned how to write and manage storage policies to control access for operations like upload and delete. Improved knowledge of debugging permission-related issues and ensuring proper backend configuration. This session marked the completion of the learning phase and prepared me for the upcoming project phase.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    # ── APRIL ──
    {
        "date": "2026-04-01", "hours": 5, "phase": "April",
        "work_summary": "Today's session focused on discussions regarding the upcoming project phase, including how teams will be formed and responsibilities will be assigned. We had an interactive discussion about team allocation, and currently we are waiting for the final team formation to begin the project work. The mentor also provided a Supabase-based assignment to be completed soon. Additionally, we were informed about upcoming recorded sessions that will cover more advanced concepts. It was also emphasized that once the project phase begins, we need to maintain discipline, collaboration, and consistent contribution.",
        "learning_outcome": "Gained clarity on how the project phase will be structured, including team collaboration and task distribution. Understood the importance of working in teams, communication, and responsibility sharing in real-world development environments. Also became aware of the need for discipline and consistent effort during project development.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-02", "hours": 5, "phase": "April",
        "work_summary": "Today's session focused on project phase discussions and team formation. The mentors decided to form teams of 4 members. We were also addressed by the Chief Director of the company, who spoke about our performance, expectations, and the importance of discipline in the project phase. A brief interaction session was conducted where our communication and presentation skills were evaluated. Additionally, various project ideas were introduced and explained by mentors, covering domains such as smart retail systems, live bus tracking, collaborative learning platforms, freelance marketplaces, alumni networking systems, and smart city issue reporting applications.",
        "learning_outcome": "Gained clear understanding of how the project phase will be structured, including team collaboration, idea evaluation, and execution planning. Improved communication and presentation skills through interaction with mentors and leadership. Also understood the importance of selecting the right project idea based on real-world impact, technical feasibility, and scalability.",
        "skills": "Flutter",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-03", "hours": 6, "phase": "April",
        "work_summary": "Today's session involved working on the assigned Flutter learning task from the O'Reilly platform, where I started progressing through the course as instructed to complete it within 10 days. Additionally, I worked on the Shop Product Page assignment, which was successfully implemented as per the given requirements. The application included features like uploading product images, PDF price lists, and videos, displaying them with file details such as name, size, and type, and managing them through a clean UI. The assignment also included file preview, external opening using URL launcher, and delete functionality.",
        "learning_outcome": "Gained practical experience in building a real-world product management page using Flutter and Supabase. Learned how to handle different file types (images, PDFs, videos) with proper upload techniques and storage handling. Improved understanding of file management workflows, including displaying file metadata, previewing content, and deleting files efficiently.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced minor challenges in handling different file upload types and understanding when to use withData options. Also had some issues with managing storage paths correctly for deletion and retrieval."
    },
    {
        "date": "2026-04-04", "hours": 5, "phase": "April",
        "work_summary": "Today I began the 10-day trial Flutter course assigned by the mentor. I successfully completed Chapter 1, which mainly focused on revising the basics of Dart and Flutter. The session included understanding how Flutter uses Dart as its core programming language and how a single codebase can be used to build applications for multiple platforms like Android, iOS, Windows, macOS, and Linux. It also covered basic differences such as using Kotlin for Android and Swift for iOS in native development.",
        "learning_outcome": "Strengthened understanding of Flutter's cross-platform capabilities and how it simplifies development using a single codebase. Gained clarity on the role of Dart in Flutter and how it powers UI and logic together. Revised basic concepts which helped in refreshing the foundation for further learning.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-05", "hours": 5, "phase": "April",
        "work_summary": "Today I completed Chapter 2 and began Chapter 3 of the Flutter course. The session mainly focused on revising and understanding the structure of a Flutter project, including the lib folder, test folder, and metadata files, along with their purpose. I also explored how Flutter code works internally, how packages are imported, and what happens when dependencies are missing. Additionally, I learned some short tricks for writing efficient Flutter and Dart code, including formatting and organizing code properly. The session also covered how widgets are structured, overridden, and centered, along with demonstrations of running a Hello World app on emulators.",
        "learning_outcome": "Gained a clearer understanding of the Flutter project structure and file organization, which is essential for real-world development. Learned how package management works and how dependencies affect application execution. Improved knowledge of widget behavior, layout alignment, and code formatting practices.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-06", "hours": 5, "phase": "April",
        "work_summary": "Today I worked on the Chapter 2 assignment, which involved building a Dice Game application using Flutter. The task focused on implementing both Stateful and Stateless widgets and understanding how they interact within an application. I also worked on integrating the assets folder to load dice images and understood how images are managed within a Flutter project. The dice values were updated dynamically using the Random function, allowing the UI to change on each interaction. Additionally, I learned how to optimize code using const where applicable for better performance.",
        "learning_outcome": "Strengthened understanding of Stateful vs Stateless widgets and their role in dynamic UI updates. Gained practical experience in using the Random function to create interactive applications. Improved knowledge of asset management in Flutter, including adding and displaying images correctly. Also learned the importance of code optimization using const, which helps improve performance.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-07", "hours": 6, "phase": "April",
        "work_summary": "Today I completed Chapter 3, which focused on building a more advanced Quiz Application using Flutter. The session included setting up the app logo, implementing core logic, and designing proper data structures to manage questions and answers efficiently. I worked on creating an optimized UI, integrating Google Fonts, and handling layout issues such as overflow using proper widget structuring and wrapping techniques. Features like adding questions and answers, shuffling questions dynamically, and tracking correct and incorrect responses were implemented.",
        "learning_outcome": "Gained strong understanding of building structured applications with proper logic and data handling in Flutter. Learned how to design interactive UI with dynamic content, including managing multiple screens and user flows. Improved knowledge of handling layout challenges such as overflow and responsive design, along with using external packages like Google Fonts.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-08", "hours": 6, "phase": "April",
        "work_summary": "Today I completed Chapter 4, which focused on debugging and performance analysis in Flutter applications. I learned how to run applications in debug mode, use options like start and restart, and identify errors step-by-step using the debug console. The session also introduced Flutter DevTools, including how to use profiling options in main.dart and analyze app performance through logs and visual tools in the browser. I explored features like the command palette and DevTools interface, which provide detailed insights into application behavior, UI rendering, and performance.",
        "learning_outcome": "Gained a strong understanding of debugging techniques in Flutter, including identifying and resolving errors using the debug console. Learned how to use Flutter DevTools for performance monitoring, logging, and UI inspection. Improved ability to analyze application behavior and optimize performance, especially in apps with multiple widgets and dynamic UI.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-09", "hours": 7, "phase": "April",
        "work_summary": "Today I worked on Chapter 5 and 6 in developing a Flutter-based Expense Tracker application to manage daily expenses efficiently. The application allows users to add, view, and delete expenses with details such as title, amount, date, and category. I implemented a structured data model using Dart classes and enums to organize expense information. The UI was designed using Material Design components with support for light and dark themes. I integrated a modal bottom sheet for adding new expenses along with form validation. Additionally, I implemented a dynamic chart to visualize spending across different categories. The app also includes real-time UI updates using StatefulWidgets and a swipe-to-delete feature with an undo option using SnackBar.",
        "learning_outcome": "Gained hands-on experience in building a complete Flutter application with structured data models and interactive UI. Improved understanding of state management using StatefulWidgets and real-time UI updates. Learned how to implement form validation, modal bottom sheets, and dynamic charts for better user experience. Also enhanced skills in handling themes, responsive layouts, and debugging UI issues.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced some challenges while implementing the dynamic chart and ensuring correct data mapping for categories. Also encountered minor issues with UI responsiveness and layout constraints across different screen sizes."
    },
    {
        "date": "2026-04-10", "hours": 9, "phase": "April",
        "work_summary": "Today I worked on Chapter 7 (Todo App) and Chapters 8, 9, 10 (Meal App). In the Todo App, there was a detailed discussion on Flutter internals, including the Widget Tree, Element Tree, and Render Tree. The app included features like adding tasks via bottom sheet, marking tasks as complete, swipe-to-delete, and sorting todos, along with improved UI elements like priority indicators and empty state handling. In the Meal App, I implemented GridView for category display, InkWell for making widgets interactive, meals data, cross-screen navigation, and layout designs using Stack widgets. The app also included tab-based navigation, a side drawer for navigation, and state management using Riverpod (providers and notifier methods). Additionally, I explored explicit vs implicit animations.",
        "learning_outcome": "Gained deep understanding of Flutter internals, including how the Widget Tree, Element Tree, and Render Tree work together, and how state changes affect UI rendering. Improved knowledge of building structured applications step-by-step, including UI components like GridView, Stack, and interactive widgets using InkWell. Enhanced understanding of navigation techniques such as tab navigation, drawer navigation, and cross-screen routing. Developed strong skills in state management using Riverpod, including providers and notifier methods for managing application data.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced some difficulty in understanding Flutter internals concepts like the Element Tree and Render Tree. Also encountered minor challenges while implementing Riverpod state management and handling navigation across multiple screens."
    },
    {
        "date": "2026-04-11", "hours": 10, "phase": "April",
        "work_summary": "Today I worked on Chapter 11 & 12 (Shopping List App) and Chapter 13 (Favourite Places App). In the Shopping List App, I learned backend integration using the Firebase Realtime Database REST API with the http package. I implemented operations such as GET, POST, and DELETE for grocery items, along with proper JSON handling and response decoding. The app included features like adding items through forms with validation, loading data using FutureBuilder, swipe-to-delete using Dismissible, and optimistic UI updates. In the Favourite Places App, I worked on a more advanced project involving SQLite local database, Riverpod state management, image picker, GPS location services, Google Maps, and Geocoding APIs. I learned how to store places with title, image, coordinates, and address, and persist them locally using SQLite.",
        "learning_outcome": "Gained strong understanding of REST API integration in Flutter using Firebase Realtime Database with manual HTTP requests. Learned how to manage CRUD operations, form validation, FutureBuilder loading states, optimistic UI updates, and proper state synchronization. Improved knowledge of local persistence using SQLite and advanced state management using Riverpod with StateNotifierProvider. Also learned how to integrate device capabilities such as camera access, image storage, GPS location, Google Maps, and Geocoding services into Flutter applications.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced some difficulty while understanding REST API data flow and JSON decoding, especially how response data is mapped into models. In the Favourite Places App, integrating multiple features like SQLite, camera, GPS, and maps together required careful understanding of asynchronous operations and permissions handling."
    },
    {
        "date": "2026-04-12", "hours": 6, "phase": "April",
        "work_summary": "Today I worked on the final Chapter, building a real-time Chat Application using Flutter and Firebase. The app was designed to sync messages instantly across devices using Firestore live streams, without any manual refresh. I implemented the authentication flow using Firebase Auth with login and signup on a single screen, along with form validation. During signup, user details and an auto-generated avatar URL were stored in Firestore for profile display in chats. For messaging, I used StreamBuilder to listen to the chat collection and rebuild the UI whenever new messages are added. Messages were ordered by timestamp, grouped visually for cleaner chat flow, and the text field cleared instantly after sending for better user experience. Additionally, I integrated ui-avatars.com for avatars and explored Firebase Cloud Messaging with Cloud Functions for push notifications.",
        "learning_outcome": "Gained strong practical experience in building a real-time chat system using Flutter and Firebase. Learned how to use Firestore streams with StreamBuilder for instant UI updates and synchronization. Improved understanding of authentication workflows, including login, signup, validation, and storing user profiles in Firestore. Also learned how to improve UX through grouped messages and instant UI feedback. Enhanced knowledge of push notifications, Cloud Functions, and third-party avatar integration.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Since Firebase Storage required credit card credentials to go with proper flow, I was unable to use it properly, which resulted in slow down of push notification features in the project even though all the backend and Firebase tools handled properly, so working on alternative approach."
    },
    {
        "date": "2026-04-13", "hours": 6, "phase": "April",
        "work_summary": "Today I attended my Internship Review – Phase 1 and presented the work completed so far during the internship. I prepared a detailed PowerPoint presentation covering my learning journey, skills developed, mini projects, major applications, achievements, and future goals. During the review, I explained my progress in front of my college internship guide, coordinator, and other members. I presented applications built using Flutter, Firebase, and Supabase, along with quiz achievements and practical learning outcomes gained throughout the internship.",
        "learning_outcome": "Improved my presentation and communication skills by explaining technical projects and concepts in front of faculty members. Gained confidence in showcasing my work, achievements, and learning journey in a professional manner. The preparation process helped me revise previous topics, strengthen conceptual clarity, and reflect on my progress so far. It also improved my ability to organize technical information in a structured presentation format.",
        "skills": "Flutter, Android Studio",
        "blockers": "No Blockers."
    },
    {
        "date": "2026-04-14", "hours": 5, "phase": "April",
        "work_summary": "Today I focused on revising previously learned Flutter concepts and recapping the major topics covered during the internship. The session helped refresh my understanding of Flutter fundamentals, widgets, UI design, state management, Firebase integration, and project workflows. Along with the revision, there was a surprise interview-style assessment session based on overall learning progress. The discussion included areas such as technical knowledge, work ethics, deliverables & outcomes, and learning adaptability. I participated confidently and performed well in the session.",
        "learning_outcome": "Strengthened conceptual understanding by revisiting important Flutter and project development topics. Improved confidence in explaining technical concepts and responding to interview-style questions. Gained better awareness of how professional evaluations are conducted based on knowledge, adaptability, outcomes, and work ethics. Also improved communication and quick-thinking skills during the interactive session.",
        "skills": "Flutter, Android Studio",
        "blockers": "Faced minor pressure due to the unexpected nature of the interview-style session and the need to answer quickly. Some questions required recalling concepts instantly from previous lessons. These challenges were managed through revision, confidence, and clear communication."
    },
    {
        "date": "2026-04-15", "hours": 5, "phase": "April",
        "work_summary": "Today I learned about Play Store deployment concepts, including how Flutter applications can be prepared, published, and updated after release. I also spent time on self-learning to strengthen my understanding of Flutter, especially in areas I find challenging. Additionally, I explored Flutter open-source projects related to programs like GSoC, as I had already applied before the deadline. I reviewed project ideas and concepts to improve my practical understanding of real-world Flutter development. I also applied for GirlScript Summer of Code (GSSoC) to gain coding experience, collaborate with teams, and further improve development skills through open-source contribution opportunities.",
        "learning_outcome": "Gained awareness of the app deployment lifecycle, including release preparation, publishing, and updates on the Play Store. Improved motivation to learn Flutter deeply by focusing on challenging concepts through self-study. Developed better understanding of how open-source programs like GSoC and GSSoC help in learning teamwork, code contribution, and industry-level workflows.",
        "skills": "Flutter, Android Studio, Git",
        "blockers": "Faced some difficulty while understanding advanced Flutter concepts independently and identifying the right open-source projects to start with. Also needed time to explore contribution processes and expectations. These challenges were managed through research, self-learning, and continuous practice."
    },
]

def run():
    conn = sqlite3.connect(DB)
    for e in ENTRIES:
        conn.execute(
            '''INSERT INTO entries (date, hours, phase, work_summary, learning_outcome, skills, blockers)
               VALUES (?,?,?,?,?,?,?)''',
            (e['date'], e['hours'], e['phase'], e['work_summary'],
             e['learning_outcome'], e['skills'], e['blockers'])
        )
    conn.commit()
    conn.close()
    print(f"Seeded {len(ENTRIES)} entries.")

if __name__ == '__main__':
    from app import init_db
    init_db()
    run()
