from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class Assignment(BaseModel):
    """Represents a task assignment"""
    id: str
    task_id: str
    member_id: str
    
    # Assignment details
    assigned_at: datetime = datetime.utcnow()
    estimated_hours: float
    
    # Scoring
    skill_compatibility_score: float  # 0.0 to 1.0
    workload_penalty: float  # Penalty for overload
    urgency_boost: float  # Boost for urgent tasks
    final_score: float  # Composite score
    
    # Tracking
    started_at: datetime = None
    completed_at: datetime = None
    actual_hours: float = None
    
    # Reasoning
    reasoning: Dict[str, Any] = {}  # Why this assignment was made
    
    def assignment_quality(self) -> float:
        """Calculate assignment quality"""
        return self.final_score