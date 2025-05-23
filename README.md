# Djangomat by Mateusz Hyla

## About
This project is about creating Django app that automates boring work stuff like working with Excel files, images, sending
bulk and automate emails, reminders and stuff.

## List of Functionalities
- Export Data - user can export data from choosed model to a CSV file which is send to his email after task is done. Export is done asynchronicaly with Celery worker and Redis as backend so exporting large amount of data is possible. 
- Import Data - user can import data from CSV file to choosed model by uploading CSV file to web app through template form. Import is done asynchronicaly with Celery worker and Redis as backend so importing large amount of data is possible. User is notified by email when task is done.
- Bulk Emails - user can send emails in bulk mode to specified group of interesants from web app data model. This task is done asynchronicaly by Celery worker and Redis as a backend.
- Email Tracking - user can see list of send bulk emails and see how many of them were opened and from how many of them recipiend clicked on link in email content. These values are represented by percentages.
- Compress Images - user can upload image to web app through form and choose how much compression he want to make. In output he receive compressed image downloaded to his computer automaticaly after task is done.
- Stock Market Analysis - user can choose a company from searchable list and view its stock market data web scraped from Yahoo Finance website.
- Cheap Book - user can see details of daily cheap ebook that details are web scraped from ebookpoint.pl website. Everyday they give one, random cheap ebook for 9.90zł to buy.

## Author
My Name is Mateusz Hyla and I am aspiring Full Stack Developer focusing on Python and 
Django stack to learn how to develop Web Apps. I am also very interested in learning 
Game Development in PyGame, Unity and Unreal Engines. You can connect with me through
[Linkedin.com](https://pl.linkedin.com/in/eccololo).