from typing import List, Dict, Tuple, Optional
from src.data_model.team_member import TeamMember
from src.data_model.task import Task
from src.data_model.assignment import Assignment
from src.feature_engine.feature_extractor import FeatureExtractor
from datetime import datetime
import uuid

class TaskAssigner:
    """Decision engine for intelligent task assignment"""
    
    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.assignments: List[Assignment] = []
    
    def assign_tasks(
        self,
        tasks: List[Task],
        team_members: List[TeamMember],
        constraints: Dict = None
    ) -> List[Assignment]:
        """
        Main assignment algorithm
        Assigns tasks to optimal team members respecting constraints
        """
        if constraints is None:
            constraints = {}
        
        # Sort tasks by urgency (high-priority tasks first)
        sorted_tasks = sorted(
            tasks,
            key=lambda t: self.feature_extractor.task_urgency_factor(t),
            reverse=True
        )
        
        assignments = []
        
        for task in sorted_tasks:
            if task.is_assigned():
                continue
            
            # Find best candidate for this task
            best_assignment = self._find_best_candidate(
                task,
                team_members,
                constraints
            )
            
            if best_assignment:
                assignments.append(best_assignment)
                # Update member workload
                member = next(m for m in team_members if m.id == best_assignment.member_id)
                member.current_workload += task.estimated_hours
                task.assigned_to = best_assignment.member_id
        
        self.assignments.extend(assignments)
        return assignments
    
    def _find_best_candidate(
        self,
        task: Task,
        team_members: List[TeamMember],
        constraints: Dict
    ) -> Optional[Assignment]:
        """
        Finds the best team member for a task
        """
        candidates = []
        
        for member in team_members:
            # Hard constraints
            if not member.availability or member.on_leave:
                continue
            
            # Check workload capacity
            new_utilization = (member.current_workload + task.estimated_hours) / member.total_hours_available
            if new_utilization > member.max_workload_percent:
                continue
            
            # Check skill requirements
            skill_score = self.feature_extractor.skill_task_compatibility(member, task)
            if skill_score < 0.3:  # Minimum skill threshold
                continue
            
            # Calculate composite score
            score = self.feature_extractor.compute_assignment_score(member, task)
            
            candidates.append({
                "member": member,
                "score": score,
                "skill_score": skill_score
            })
        
        if not candidates:
            return None
        
        # Select best candidate
        best = max(candidates, key=lambda x: x["score"])
        
        # Create assignment object
        assignment = Assignment(
            id=str(uuid.uuid4()),
            task_id=task.id,
            member_id=best["member"].id,
            estimated_hours=task.estimated_hours,
            skill_compatibility_score=best["skill_score"],
            workload_penalty=1.0 - self.feature_extractor.workload_utilization_ratio(best["member"]),
            urgency_boost=self.feature_extractor.task_urgency_factor(task),
            final_score=best["score"],
            reasoning={
                "skill_match": best["skill_score"],
                "workload": best["member"].workload_utilization(),
                "reliability": best["member"].reliability_score,
                "urgency": self.feature_extractor.task_urgency_factor(task)
            }
        )
        
        return assignment
    
    def get_assignment_reasoning(self, assignment: Assignment) -> str:
        """Generate human-readable reasoning for an assignment"""
        return f"""
        Task Assigned: {assignment.task_id}
        Assigned To: {assignment.member_id}
        
        Scores:
        - Skill Compatibility: {assignment.skill_compatibility_score:.2%}
        - Workload Penalty: {assignment.workload_penalty:.2%}
        - Urgency Boost: {assignment.urgency_boost:.2%}
        - Final Score: {assignment.final_score:.2%}
        
        Reasoning: {assignment.reasoning}
        """