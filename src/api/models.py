from pydantic import BaseModel
from typing import List, Optional
from src.data_model.team_member import TeamMember, Skill
from src.data_model.task import Task, Priority
from src.data_model.sprint import Sprint

# Request/Response models for API

class CreateTeamMemberRequest(BaseModel):
    name: str
    email: str
    skills: List[Skill]
    total_hours_available: float

class CreateTaskRequest(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    complexity: float
    estimated_hours: float
    priority: Priority
    deadline: str  # ISO format

class CreateSprintRequest(BaseModel):
    name: str
    duration_days: int
    team_member_ids: List[str]

class AssignmentResponse(BaseModel):
    task_id: str
    member_id: str
    skill_compatibility_score: float
    final_score: float
    reasoning: dict

class SprintPlanResponse(BaseModel):
    sprint_id: str
    is_feasible: bool
    risk_level: str
    planned_tasks: int
    assignments: List[AssignmentResponse]