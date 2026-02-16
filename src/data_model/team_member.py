from pydantic import BaseModel, Field
from typing import Dict, List
from datetime import datetime

class Skill(BaseModel):
    """Represents a skill with proficiency level"""
    name: str
    proficiency: float = Field(ge=0.0, le=1.0)  # 0.0 to 1.0
    
class TeamMember(BaseModel):
    """Represents a team member with skills and workload"""
    id: str
    name: str
    email: str
    skills: List[Skill]
    
    # Capacity and workload
    total_hours_available: float  # Hours available in sprint
    current_workload: float = 0.0  # Current assigned hours
    max_workload_percent: float = 0.85  # Max 85% utilization
    
    # Performance metrics
    average_task_completion_time: float = 0.0  # Historical average
    sprint_velocity: float = 1.0  # Tasks per sprint
    reliability_score: float = 0.8  # Based on on-time completion
    
    # Metadata
    availability: bool = True
    on_leave: bool = False
    leave_start: datetime = None
    leave_end: datetime = None
    
    def available_hours(self) -> float:
        """Calculate remaining available hours"""
        return self.total_hours_available - self.current_workload
    
    def workload_utilization(self) -> float:
        """Calculate current workload utilization ratio"""
        if self.total_hours_available == 0:
            return 0.0
        return self.current_workload / self.total_hours_available
    
    def can_take_task(self, estimated_hours: float) -> bool:
        """Check if member can take on a task"""
        new_utilization = (self.current_workload + estimated_hours) / self.total_hours_available
        return new_utilization <= self.max_workload_percent and self.availability