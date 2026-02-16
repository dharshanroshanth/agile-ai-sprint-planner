from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TaskStatus(str, Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    DELAYED = "delayed"

class Task(BaseModel):
    """Represents a task in the sprint"""
    id: str
    title: str
    description: str
    
    # Skills and complexity
    required_skills: List[str]  # List of skill names
    complexity: float = Field(ge=0.0, le=1.0)  # 0.0 (simple) to 1.0 (complex)
    estimated_hours: float = Field(gt=0)
    
    # Priority and urgency
    priority: Priority = Priority.MEDIUM
    deadline: datetime
    
    # Dependencies and relationships
    depends_on: List[str] = []  # Task IDs this depends on
    blocks: List[str] = []  # Task IDs this blocks
    
    # Assignment and tracking
    assigned_to: Optional[str] = None  # Team member ID
    status: TaskStatus = TaskStatus.PENDING
    actual_hours: Optional[float] = None
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.utcnow)
    sprint_id: Optional[str] = None
    
    def urgency_score(self) -> float:
        """Calculate task urgency (0.0 to 1.0)"""
        from datetime import datetime, timedelta
        # Make sure we're comparing compatible datetimes
        now = datetime.utcnow()
        deadline = self.deadline
        
        # If deadline has timezone info, remove it for comparison
        if deadline.tzinfo is not None:
            deadline = deadline.replace(tzinfo=None)
        
        days_until_deadline = (deadline - now).days
        
        if days_until_deadline <= 0:
            return 1.0
        elif days_until_deadline <= 3:
            return 0.9
        elif days_until_deadline <= 7:
            return 0.7
        else:
            return 0.3
    
    def is_assigned(self) -> bool:
        """Check if task is assigned"""
        return self.assigned_to is not None
    
    def priority_weight(self) -> float:
        """Return numeric weight for priority"""
        weights = {
            Priority.LOW: 0.3,
            Priority.MEDIUM: 0.6,
            Priority.HIGH: 0.85,
            Priority.CRITICAL: 1.0
        }
        return weights[self.priority]