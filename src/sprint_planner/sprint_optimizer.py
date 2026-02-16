from typing import List, Dict, Tuple
from src.data_model.sprint import Sprint
from src.data_model.team_member import TeamMember
from src.data_model.task import Task
from src.decision_engine.task_assigner import TaskAssigner
from src.feature_engine.feature_extractor import FeatureExtractor

class SprintOptimizer:
    """Optimizes sprint planning and feasibility"""
    
    def __init__(self):
        self.task_assigner = TaskAssigner()
        self.feature_extractor = FeatureExtractor()
    
    def plan_sprint(
        self,
        sprint: Sprint,
        available_tasks: List[Task],
        team_members: List[TeamMember]
    ) -> Tuple[Sprint, List[Task]]:
        """
        Plans a sprint by:
        1. Selecting tasks within capacity
        2. Assigning tasks to team members
        3. Evaluating feasibility
        """
        
        # Calculate sprint capacity
        capacity = self._calculate_sprint_capacity(team_members)
        
        # Select tasks that fit within capacity
        selected_tasks = self._select_tasks_for_sprint(
            available_tasks,
            capacity
        )
        
        # Assign selected tasks
        assignments = self.task_assigner.assign_tasks(
            selected_tasks,
            team_members
        )
        
        # Evaluate sprint feasibility
        sprint.is_feasible, sprint.risk_level = self._assess_sprint_feasibility(
            sprint,
            selected_tasks,
            team_members,
            assignments
        )
        
        sprint.planned_tasks = len(selected_tasks)
        
        return sprint, selected_tasks
    
    def _calculate_sprint_capacity(self, team_members: List[TeamMember]) -> float:
        """Calculate total sprint capacity in hours"""
        return sum(member.total_hours_available for member in team_members)
    
    def _select_tasks_for_sprint(
        self,
        available_tasks: List[Task],
        sprint_capacity: float
    ) -> List[Task]:
        """
        Select tasks that fit within sprint capacity
        Uses greedy algorithm: prioritize by urgency
        """
        selected = []
        total_effort = 0.0
        
        # Sort by urgency
        sorted_tasks = sorted(
            available_tasks,
            key=lambda t: self.feature_extractor.task_urgency_factor(t),
            reverse=True
        )
        
        for task in sorted_tasks:
            if total_effort + task.estimated_hours <= sprint_capacity * 0.85:  # 85% utilization target
                selected.append(task)
                total_effort += task.estimated_hours
        
        return selected
    
    def _assess_sprint_feasibility(
        self,
        sprint: Sprint,
        tasks: List[Task],
        team_members: List[TeamMember],
        assignments: List
    ) -> Tuple[bool, str]:
        """
        Assess if sprint plan is feasible
        Returns: (is_feasible, risk_level)
        """
        
        if not assignments:
            return False, "critical"  # No tasks assigned
        
        # Check workload balance
        workloads = [member.workload_utilization() for member in team_members]
        workload_variance = self._calculate_variance(workloads)
        
        # Check utilization
        total_effort = sum(task.estimated_hours for task in tasks)
        total_capacity = sum(member.total_hours_available for member in team_members)
        utilization = total_effort / total_capacity if total_capacity > 0 else 0.0
        
        # Determine risk level
        if utilization > 0.95:
            risk = "high"
            feasible = False
        elif utilization > 0.85:
            risk = "medium"
            feasible = True
        elif workload_variance > 0.3:
            risk = "medium"
            feasible = True
        else:
            risk = "low"
            feasible = True
        
        return feasible, risk
    
    @staticmethod
    def _calculate_variance(values: List[float]) -> float:
        """Calculate variance of values"""
        if not values:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance ** 0.5  # Standard deviation