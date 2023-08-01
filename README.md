# hackathon-manager

Django application that performs CRUD (Create, Read, Update, Delete) operations on a postgress database using a REST API.

Python version used : `3.10.6`

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a `.env` file inside `hackathon_manager` folder and add the following variables
```bash
DB_URL=`url of database`
DB_USER=`username of database`
DB_PASSWORD=`password of database`
```

To install the required packages
```bash
pip  install -r requirements.txt
```
To Run the app
```bash
python manage.py runserver
```

The app will be availiable on http://localhost:8000

## API Endpoints
1. GET `/api/hackathons/` - Get all hackathons
2. GET `/api/hackathons/<hackathon_id>` - Get a specific hackathon
3. POST `/api/hackathons/` - Create a hackathon
4. PUT `/api/hackathons/<hackathon_id>` - Update a hackathon
5. DELETE `/api/hackathons/<hackathon_id>` - Delete a hackathon
6. GET `/api/hackathons/participate/<int:pk>/` - Get all hackathons current user is participating in
7. POST `/api/hackathons/participate/<int:pk>/` - Update participation status of current user in a hackathon
8. GET `/api/hackathons/user/submissions/<int:pk>/` - Get all submissions of current user in a hackathon
9. POST `/api/hackathons/user/submissions/<int:pk>/` - Create a submission for current user in a hackathon
10. GET `/api/hackathons/user/participating/` - Get all hackathons current user is participating in
11. POST `/auth/register/` - Register a new user
12. POST `/auth/login/` - Login a user
13. POST `/auth/login/refresh` - Refresh a user's access token
14. GET `hackathons/user/atleastone/` -  Get all the users(participants) who have enrolled in atleast one hackathon
15. GET `hackathons/user/notone/` -  Get all the users(participants) who have not enrolled in a single hackathon