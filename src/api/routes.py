from fastapi import APIRouter, HTTPException
from typing import List
from src.api.models import (
    CreateTeamMemberRequest,
    CreateTaskRequest,
    CreateSprintRequest,
    SprintPlanResponse
)
from src.data_model.team_member import TeamMember
from src.data_model.task import Task
from src.data_model.sprint import Sprint
from src.sprint_planner.sprint_optimizer import SprintOptimizer
from datetime import datetime, timedelta
import uuid

router = APIRouter()
sprint_optimizer = SprintOptimizer()

# In-memory storage (replace with database in production)
team_members: List[TeamMember] = []
tasks: List[Task] = []
sprints: List[Sprint] = []

@router.post("/team-members")
def create_team_member(request: CreateTeamMemberRequest):
    """Create a new team member"""
    member = TeamMember(
        id=str(uuid.uuid4()),
        name=request.name,
        email=request.email,
        skills=request.skills,
        total_hours_available=request.total_hours_available
    )
    team_members.append(member)
    return member

@router.post("/tasks")
def create_task(request: CreateTaskRequest):
    """Create a new task"""
    task = Task(
        id=str(uuid.uuid4()),
        title=request.title,
        description=request.description,
        required_skills=request.required_skills,
        complexity=request.complexity,
        estimated_hours=request.estimated_hours,
        priority=request.priority,
        deadline=datetime.fromisoformat(request.deadline)
    )
    tasks.append(task)
    return task

@router.post("/sprints/plan")
def plan_sprint(request: CreateSprintRequest):
    """Plan a new sprint"""
    try:
        # Get team members
        sprint_team = [m for m in team_members if m.id in request.team_member_ids]
        if not sprint_team:
            raise HTTPException(status_code=400, detail="No valid team members provided")
        
        # Create sprint
        sprint = Sprint(
            id=str(uuid.uuid4()),
            name=request.name,
            start_date=datetime.utcnow(),
            end_date=datetime.utcnow() + timedelta(days=request.duration_days),
            duration_days=request.duration_days,
            team_members=request.team_member_ids
        )
        
        # Plan sprint
        planned_sprint, selected_tasks = sprint_optimizer.plan_sprint(
            sprint,
            [t for t in tasks if not t.assigned_to],
            sprint_team
        )
        
        sprints.append(planned_sprint)
        
        return {
            "sprint": planned_sprint.dict(),
            "tasks": [t.dict() for t in selected_tasks]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error planning sprint: {str(e)}")

@router.get("/sprints/{sprint_id}")
def get_sprint(sprint_id: str):
    """Get sprint details"""
    sprint = next((s for s in sprints if s.id == sprint_id), None)
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    return sprint

@router.get("/team-members")
def list_team_members():
    """List all team members"""
    return team_members

@router.get("/tasks")
def list_tasks():
    """List all tasks"""
    return tasks