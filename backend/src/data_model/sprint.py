from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime, timedelta

class Sprint(BaseModel):
    """Represents an agile sprint"""
    id: str
    name: str
    
    # Sprint timeline
    start_date: datetime
    end_date: datetime
    duration_days: int = 14  # Default 2 weeks
    
    # Team and capacity
    team_members: List[str]  # List of member IDs
    total_sprint_capacity: float = 0.0  # Total available hours
    
    # Tasks
    task_ids: List[str] = []
    
    # Planning metrics
    planned_tasks: int = 0
    completed_tasks: int = 0
    failed_tasks: int = 0
    
    # Risk and feasibility
    risk_level: str = "medium"  # low, medium, high
    is_feasible: bool = True
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "planning"  # planning, in_progress, completed
    
    def days_remaining(self) -> int:
        """Calculate days remaining in sprint"""
        return (self.end_date - datetime.utcnow()).days
    
    def sprint_progress(self) -> float:
        """Calculate sprint progress (0.0 to 1.0)"""
        total = self.planned_tasks
        if total == 0:
            return 0.0
        return self.completed_tasks / total
    
    def success_rate(self) -> float:
        """Calculate sprint success rate"""
        total = self.planned_tasks
        if total == 0:
            return 0.0
        return self.completed_tasks / total
        return self.completed_tasks / total