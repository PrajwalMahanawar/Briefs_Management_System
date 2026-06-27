# Briefs Management System

A full-stack enterprise workflow platform developed during my internship at SkillzCollab. The system was designed to manage competition briefs, collaborative workflows, analytics, and recommendation features using Django REST Framework, PostgreSQL, and React (Next.js).

The platform supports secure authentication, RESTful APIs, workflow management, graph-based analytics, and recommendation-driven brief discovery.

---

## Features

* Full-stack enterprise workflow platform
* Secure JWT-based authentication
* Competition brief management
* CRUD operations for briefs and workflows
* RESTful API architecture
* PostgreSQL database integration
* React (Next.js) frontend integration
* Graph-based analytics and recommendation features
* Agile/Scrum development workflow
* Postman API testing

---

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework (DRF)
* PostgreSQL

### Frontend

* React
* Next.js

### Tools & Platforms

* Postman
* Git & GitHub
* JIRA
* Shell Scripting

---

## Project Architecture

```bash id="g4c88y"
Frontend (React / Next.js)
        ↓
REST APIs (Django REST Framework)
        ↓
Business Logic & Analytics Layer
        ↓
PostgreSQL Database
```

---

## Core Functionalities

### Authentication & Security

* JWT-based authentication
* User registration and login
* Protected API endpoints

### Brief Management

* Create competition briefs
* Update and manage workflows
* Store structured brief information
* Collaborative management workflows

### Analytics & Recommendations

* Graph-inspired relationship analysis
* Recommendation workflows for related briefs
* Influence and relationship insights
* Cascade-inspired analytics concepts

### Backend Automation

* Shell scripting for backend startup automation
* PostgreSQL database checks
* Migration execution automation
* Local development workflow setup

---

## API Features

### Authentication APIs

```http id="u6z7z4"
POST /api/auth/register
POST /api/auth/login
```

### Brief APIs

```http id="x0xkh2"
GET /api/briefs
POST /api/briefs
PUT /api/briefs/{id}
DELETE /api/briefs/{id}
```

### Analytics APIs

```http id="jlwmw2"
GET /api/analytics
GET /api/recommendations
```

---

## Database

The project uses PostgreSQL for:

* User management
* Brief storage
* Workflow tracking
* Analytics data
* Relationship mapping

---

## Run Backend

### Activate Environment

```bash id="8j1cwl"
pipenv shell
```

### Run Migrations

```bash id="kh0fbq"
python manage.py migrate
```

### Start Server

```bash id="9xt0mk"
python manage.py runserver
```

---

## Run Frontend

```bash id="l1b8ml"
npm install
npm run dev
```
## Sample Outputs

### Authentication API Response

#### Login Successful

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

### Create Brief API Response

```json
{
  "id": 1,
  "title": "AI Marketing Campaign",
  "description": "Create a social media campaign for AI product launch.",
  "category": "Marketing",
  "status": "ACTIVE"
}
```

---

### Get All Briefs Response

```json
[
  {
    "id": 1,
    "title": "AI Marketing Campaign",
    "category": "Marketing",
    "status": "ACTIVE"
  },
  {
    "id": 2,
    "title": "UI/UX Redesign Challenge",
    "category": "Design",
    "status": "ACTIVE"
  }
]
```

---

### Analytics Output Example

```json
{
  "total_briefs": 25,
  "active_briefs": 18,
  "most_influential_brief": "AI Marketing Campaign",
  "cascade_depth": 4,
  "branching_factor": 2.3,
  "structural_virality": 3.7
}
```

---

### Recommendation Output Example

```json
{
  "recommended_briefs": [
    {
      "brief_id": 12,
      "title": "AI Product Branding",
      "score": 0.91
    },
    {
      "brief_id": 18,
      "title": "Digital Growth Strategy",
      "score": 0.87
    }
  ]
}
```

---

### Backend Startup Automation

#### Shell Script Execution

```bash
./start_backend.sh
```

#### Example Output

```text
Checking PostgreSQL connection...
Database found.
Running migrations...
Starting Django development server...
Server running at http://127.0.0.1:8000/
```

---

## Future Improvements

* Advanced recommendation engine
* Real-time collaboration
* Notification system
* AI-assisted brief recommendations
* Dashboard analytics
* Docker deployment
* CI/CD deployment pipelines
* Role-based access control

---

## Learning Outcomes

This project strengthened understanding of:

* Full-stack software engineering
* REST API development
* Django REST Framework
* PostgreSQL database management
* React frontend integration
* JWT authentication
* Enterprise workflow systems
* Agile/Scrum development
* Backend automation using shell scripting

---

## Author

### Prajwal Mahanawar

* GitHub: https://github.com/PrajwalMahanawar
* LinkedIn: https://www.linkedin.com/in/prajwal-mahanawar-710325222/
