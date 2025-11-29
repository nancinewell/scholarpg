# Overview
I'm expanding my Python learning to web apps. To this point, I've used Python with Tkinter and Arcade to run frontends, and honestly didn't know that using Python on a web app was an option until recently and wanted to explore it.

This app is one that has been on my project list for a while. It is a hub used for school gamification, where the students' character with experience, gold, level, skills, and skill points are housed. From here, the teacher can select a student and increase their experience and/or gold for good behaviors, and track what skills are available to students and when they use them. 

As this has a backend and is not currently hosted, you can start a python test server to run the app by using the command prompt: py manage.py runserver. This will run it to your local host. Just pull up a browser and go to 127.0.0.1:8000 to access the app. 

As always, I try to use my learning to forward my homeschool. My children and I have been doing something like this for a few years now, but we just manage it on spreadsheets. I'm excited to put this together so that our characters can be more automated and require less maintenance from me. 



{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/jStxUn6iK6A)

# Web Pages
This app contains 5 database tables: Students, Behaviors, Skills, RandomEvents, and Miracles. 
Each table has a page to view all, add, update, and delete, and Student has a view one page. There's also a confirmation page. 

Each one is called by a URL that is accepted by the urls.py file and redirected to the views file with a function call that will accept the request, usually will do something with it, and will render the appropriate page. 

On any view, update, or delete page will get student (or other applicable) infomration and send object(s) with the information to dynamically populate the information on the page when it is rendered. EG: On the view_student page, the student is retrieved and sent as an object to the page. Then where the page requires the student name, it is retrieved with the command {{student.name}}. 

# Development Environment
I wrote this program in the IDE Visual Studio Code version 1.105.1 with 4 extensions to make it more friendly to Python: Pylance, Python, Python Debugger, and Python Environments.

I wrote this program using Python and Django as the web framework, and utilized built in sqlite3.

# Useful Websites
* [Django Tutorial for Beginners – Build Powerful Backends (video)](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
* [Python Django Introduction and Beginners Tutorial (video)](https://www.youtube.com/watch?v=qcJZN1pvG6A)
* [Tutorialspoint](https://www.tutorialspoint.com/django/index.htm)
* [W3Schools](https://www.w3schools.com/django)
* [Django Project](https://docs.djangoproject.com/)

# Future Work
* I want to add a shop for the kids to spend their gold on.
* I want to add a pet shop. Each pet has powers (something we're currently manageing with the spreadsheet)
* I want to incorporate the boss battles and character quiz that I completed in separate projects (not all were written in Python) so that we have one app for everything!