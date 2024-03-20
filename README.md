# Streamify-Django-Rest-Framework
Streamify is a web application built using Django Rest Framework for streaming and sharing videos. 

It provides functionalities such as user authentication, CRUD operations for videos, scheduled video posting, commenting on videos, and search filtering based on video title and description.

## Features
#### User Authentication: 
Allows users to sign up, sign in, change password, and send password reset emails using JWT authentication.
#### CRUD Operations for Videos: 
Users can create, read, update, and delete videos.
#### Scheduled Video Post: 
Users can schedule videos to be posted at a later date and time.
#### Comments: 
Users can view and post comments on specific videos.
#### Search Filter: 
Enables users to search for videos based on title and description.
#### User Profile: 
Users have profiles containing their information and uploaded videos.

## Installation
#### Clone the repository:
git clone https://github.com/your_username/streamify.git
#### Navigate into the project directory:
cd streamify
#### Install dependencies:
pip install -r requirements.txt
#### Set up database migrations:
python manage.py makemigrations

python manage.py migrate
#### Create a superuser:
python manage.py createsuperuser
#### Start the development server:
python manage.py runserver
#### Access the application:
http://localhost:8000.


