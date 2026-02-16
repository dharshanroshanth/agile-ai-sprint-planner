# API Documentation

## Base URL
```
http://localhost:8000
```

## Endpoints

### Root

**GET** `/`

Returns welcome message and available endpoints.

**Response:**
```json
{
  "message": "Welcome to Agile AI Sprint Planner",
  "docs": "/docs",
  "health": "/health"
}
```

### Health Check

**GET** `/health`

Checks API health status.

**Response:**
```json
{
  "status": "healthy"
}
```

### Team Members

#### Create Team Member

**POST** `/team-members`

Creates a new team member.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": [
    {"name": "Python", "proficiency": 0.9},
    {"name": "JavaScript", "proficiency": 0.7}
  ],
  "total_hours_available": 40
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "name": "John Doe",
  "email": "john@example.com",
  "skills": [...],
  "total_hours_available": 40,
  "current_workload": 0.0,
  "availability": true,
  ...
}
```

#### List Team Members

**GET** `/team-members`

Returns all team members.

**Response:** `200 OK`
```json
[
  {...},
  {...}
]
```

### Tasks

#### Create Task

**POST** `/tasks`

Creates a new task.

**Request Body:**
```json
{
  "title": "Build API Endpoint",
  "description": "Create RESTful API endpoint for user management",
  "required_skills": ["Python", "FastAPI"],
  "complexity": 0.6,
  "estimated_hours": 8,
  "priority": "high",
  "deadline": "2026-02-20T23:59:59"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "title": "Build API Endpoint",
  "description": "...",
  "required_skills": [...],
  "complexity": 0.6,
  "estimated_hours": 8,
  "priority": "high",
  "deadline": "2026-02-20T23:59:59",
  "status": "pending",
  "assigned_to": null,
  ...
}
```

#### List Tasks

**GET** `/tasks`

Returns all tasks.

**Response:** `200 OK`
```json
[
  {...},
  {...}
]
```

### Sprints

#### Plan Sprint

**POST** `/sprints/plan`

Plans a new sprint with tasks assigned to team members.

**Request Body:**
```json
{
  "name": "Sprint 1",
  "duration_days": 14,
  "team_member_ids": ["member_id_1", "member_id_2"]
}
```

**Response:** `200 OK`
```json
{
  "sprint": {
    "id": "uuid",
    "name": "Sprint 1",
    "start_date": "2026-02-16T00:00:00",
    "end_date": "2026-03-02T00:00:00",
    "duration_days": 14,
    "team_members": [...],
    "is_feasible": true,
    "risk_level": "low",
    "planned_tasks": 5,
    "status": "planning"
  },
  "tasks": [
    {
      "id": "uuid",
      "title": "...",
      "assigned_to": "member_id_1",
      "status": "assigned",
      ...
    }
  ]
}
```

#### Get Sprint

**GET** `/sprints/{sprint_id}`

Retrieves sprint details.

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "name": "Sprint 1",
  ...
}
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Interactive API Documentation

Access interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
