from typing import List, Dict
from datetime import datetime
from src.data_model.assignment import Assignment
from src.data_model.team_member import TeamMember
from src.data_model.task import Task

class FeedbackLoop:
    """Collects post-sprint feedback and updates models"""
    
    def __init__(self):
        self.historical_data: List[Dict] = []
    
    def collect_sprint_feedback(
        self,
        assignments: List[Assignment],
        team_members: List[TeamMember],
        tasks: List[Task]
    ) -> Dict:
        """
        Collects performance data after sprint completion
        """
        feedback = {
            "timestamp": datetime.utcnow(),
            "assignments_completed": len([a for a in assignments if a.completed_at]),
            "total_assignments": len(assignments),
            "accuracy_metrics": self._calculate_accuracy(assignments),
            "member_feedback": self._collect_member_metrics(team_members),
            "task_feedback": self._collect_task_metrics(tasks)
        }
        
        self.historical_data.append(feedback)
        return feedback
    
    def _calculate_accuracy(self, assignments: List[Assignment]) -> Dict:
        """Calculate prediction vs reality metrics"""
        metrics = {
            "estimated_vs_actual": [],
            "prediction_error": 0.0
        }
        
        for assignment in assignments:
            if assignment.actual_hours is not None:
                error = abs(assignment.estimated_hours - assignment.actual_hours)
                metrics["estimated_vs_actual"].append({
                    "estimated": assignment.estimated_hours,
                    "actual": assignment.actual_hours,
                    "error": error,
                    "error_percent": (error / assignment.estimated_hours) * 100 if assignment.estimated_hours > 0 else 0
                })
        
        if metrics["estimated_vs_actual"]:
            avg_error = sum(m["error"] for m in metrics["estimated_vs_actual"]) / len(metrics["estimated_vs_actual"])
            metrics["prediction_error"] = avg_error
        
        return metrics
    
    def _collect_member_metrics(self, team_members: List[TeamMember]) -> Dict:
        """Collect performance metrics for team members"""
        metrics = {}
        for member in team_members:
            metrics[member.id] = {
                "final_workload": member.workload_utilization(),
                "reliability": member.reliability_score
            }
        return metrics
    
    def _collect_task_metrics(self, tasks: List[Task]) -> Dict:
        """Collect task outcome metrics"""
        total = len(tasks)
        completed = len([t for t in tasks if t.status.value == "completed"])
        delayed = len([t for t in tasks if t.status.value == "delayed"])
        
        return {
            "total_tasks": total,
            "completed": completed,
            "delayed": delayed,
            "completion_rate": (completed / total) * 100 if total > 0 else 0,
            "delay_rate": (delayed / total) * 100 if total > 0 else 0
        }
    
    def update_member_profile(
        self,
        member: TeamMember,
        actual_completion_hours: float,
        was_on_time: bool
    ):
        """Update member profile based on actual performance"""
        # Update average completion time
        if member.average_task_completion_time == 0:
            member.average_task_completion_time = actual_completion_hours
        else:
            # Exponential moving average
            alpha = 0.3
            member.average_task_completion_time = (
                alpha * actual_completion_hours +
                (1 - alpha) * member.average_task_completion_time
            )
        
        # Update reliability score
        if was_on_time:
            member.reliability_score = min(member.reliability_score + 0.05, 1.0)
        else:
            member.reliability_score = max(member.reliability_score - 0.1, 0.0)
    
    def get_learning_insights(self) -> Dict:
        """Extract insights from historical feedback"""
        if not self.historical_data:
            return {}
        
        insights = {
            "sprints_completed": len(self.historical_data),
            "average_completion_rate": sum(
                d["task_feedback"]["completion_rate"] for d in self.historical_data
            ) / len(self.historical_data),
            "average_prediction_error": sum(
                d["accuracy_metrics"].get("prediction_error", 0) for d in self.historical_data
            ) / len(self.historical_data)
        }
        
        return insights