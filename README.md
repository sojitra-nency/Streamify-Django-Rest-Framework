# Streamify-Django-Rest-Framework
Streamify is a web application built using Django Rest Framework for streaming and sharing videos. 

It provides functionalities such as user authentication, CRUD operations for videos, scheduled video posting, commenting on videos, and search filtering based on video title and description.

## Features
### User Authentication: 
Allows users to sign up, sign in, change password, and send password reset emails using JWT authentication.
### CRUD Operations for Videos: 
Users can create, read, update, and delete videos.
### Scheduled Video Post: 
Users can schedule videos to be posted at a later date and time.
### Comments: 
Users can view and post comments on specific videos.
### Search Filter: 
Enables users to search for videos based on title and description.
### User Profile: 
Users have profiles containing their information and uploaded videos.

## Installation
### Clone the repository:
  git clone https://github.com/your_username/streamify.git
### Navigate into the project directory:
  cd streamify
### Install dependencies:
  pip install -r requirements.txt
### Set up database migrations:
  python manage.py makemigrations

  python manage.py migrate
### Create a superuser:
  python manage.py createsuperuser
### Start the development server:
  python manage.py runserver
### Access the application:
  http://localhost:8000
  
## API Endpoints
### Authentication:
POST /stream/register/: Sign up a new user.

POST /stream/login/: Sign in an existing user.

POST /stream/change-password/: Change user password.

POST /stream/send-password-reset-mail/: Send password reset mail.

POST /stream/password-reset/<uid>/<token>/: Reset password.

### User:

GET /stream/profile/: List all User Profile.

### Videos:

POST /stream/create-videos/: Create a new video.

PUT /stream/video-detail/<pk>/: Update a specific video.

GET /stream/video-detail/<pk>/: Retrieve a specific video.

DELETE /stream/video-detail/<pk>/: Delete a specific video.

GET /stream/list/: Retrieve all videos.

GET /stream/list/?page=<page_number>/: Pagination applied to list of all videos

### Comments:

GET /stream/comments/<int:video_id>/: Retrieve comments for a specific video.

POST /stream/comments/<int:video_id>/: Post a comment on a specific video.

### Search:

GET /stream/search/?query={search_query}: Search videos based on title and description.

## Contributing
We welcome contributions to improve Streamify. Feel free to fork the repository, make changes, and submit a pull request.
