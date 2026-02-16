# Data Schema

## Core Entities

### TeamMember

```json
{
  "id": "uuid",
  "name": "string",
  "email": "string",
  "skills": [
    {
      "name": "Python",
      "proficiency": 0.9
    }
  ],
  "total_hours_available": 40.0,
  "current_workload": 20.5,
  "max_workload_percent": 0.85,
  "average_task_completion_time": 5.2,
  "sprint_velocity": 1.0,
  "reliability_score": 0.85,
  "availability": true,
  "on_leave": false
}
```

### Task

```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "required_skills": ["Python", "FastAPI"],
  "complexity": 0.7,
  "estimated_hours": 8.0,
  "priority": "high",
  "deadline": "2026-03-01T17:00:00Z",
  "depends_on": [],
  "assigned_to": "member-uuid",
  "status": "pending"
}
```

### Sprint

```json
{
  "id": "uuid",
  "name": "Sprint 1",
  "start_date": "2026-02-16T00:00:00Z",
  "end_date": "2026-03-02T00:00:00Z",
  "duration_days": 14,
  "team_members": ["member-id-1", "member-id-2"],
  "task_ids": ["task-id-1", "task-id-2"],
  "planned_tasks": 5,
  "completed_tasks": 0,
  "is_feasible": true,
  "risk_level": "medium"
}
```

### Assignment

```json
{
  "id": "uuid",
  "task_id": "uuid",
  "member_id": "uuid",
  "estimated_hours": 8.0,
  "skill_compatibility_score": 0.95,
  "final_score": 0.82,
  "reasoning": {
    "skill_match": 0.95,
    "workload": 0.5,
    "reliability": 0.85,
    "urgency": 0.9
  }
}
```

## Sprint

```json
{
  "id": "string (UUID)",
  "name": "string",
  "start_date": "datetime",
  "end_date": "datetime",
  "duration_days": "integer",
  "team_members": ["string (TeamMember IDs)"],
  "total_sprint_capacity": "float",
  "task_ids": ["string (Task IDs)"],
  "planned_tasks": "integer",
  "completed_tasks": "integer",
  "failed_tasks": "integer",
  "risk_level": "enum (low|medium|high)",
  "is_feasible": "boolean",
  "created_at": "datetime",
  "status": "enum (planning|in_progress|completed)"
}
```

## Assignment

```json
{
  "id": "string (UUID)",
  "task_id": "string",
  "member_id": "string",
  "estimated_hours": "float",
  "skill_compatibility_score": "float (0.0-1.0)",
  "workload_penalty": "float (0.0-1.0)",
  "urgency_boost": "float (0.0-1.0)",
  "final_score": "float (0.0-1.0)",
  "assigned_at": "datetime",
  "started_at": "datetime or null",
  "completed_at": "datetime or null",
  "actual_hours": "float or null",
  "reasoning": {
    "skill_match": "float",
    "workload": "float",
    "reliability": "float",
    "urgency": "float"
  }
}
```
