# hackathon-manager
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
