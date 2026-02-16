import math
from typing import List, Dict, Tuple
from src.data_model.team_member import TeamMember
from src.data_model.task import Task

class FeatureExtractor:
    """Extracts meaningful features from raw Agile data"""
    
    @staticmethod
    def skill_task_compatibility(member: TeamMember, task: Task) -> float:
        """
        Calculate skill-task compatibility score (0.0 to 1.0)
        Higher = better match
        """
        if not task.required_skills:
            return 1.0
        
        member_skill_map = {skill.name: skill.proficiency for skill in member.skills}
        
        compatibility_scores = []
        for required_skill in task.required_skills:
            if required_skill in member_skill_map:
                compatibility_scores.append(member_skill_map[required_skill])
            else:
                compatibility_scores.append(0.0)
        
        if not compatibility_scores:
            return 0.0
        
        # Average compatibility across all required skills
        return sum(compatibility_scores) / len(compatibility_scores)
    
    @staticmethod
    def workload_utilization_ratio(member: TeamMember) -> float:
        """
        Calculate workload utilization ratio (0.0 to 1.0)
        Returns current workload / total available
        """
        if member.total_hours_available == 0:
            return 0.0
        return min(member.current_workload / member.total_hours_available, 1.0)
    
    @staticmethod
    def performance_reliability_index(member: TeamMember) -> float:
        """
        Calculate performance reliability (0.0 to 1.0)
        Based on historical on-time completion rate
        """
        return member.reliability_score
    
    @staticmethod
    def task_urgency_factor(task: Task) -> float:
        """
        Calculate task urgency (0.0 to 1.0)
        Combines deadline proximity and priority
        """
        deadline_urgency = task.urgency_score()
        priority_weight = task.priority_weight()
        
        # Weighted average: 60% deadline, 40% priority
        return 0.6 * deadline_urgency + 0.4 * priority_weight
    
    @staticmethod
    def sprint_capacity_score(sprint, team_members: List[TeamMember]) -> Dict[str, float]:
        """
        Calculate sprint capacity metrics
        Returns feasibility assessment
        """
        total_capacity = sum(member.total_hours_available for member in team_members)
        
        return {
            "total_capacity": total_capacity,
            "available_capacity": total_capacity - sum(member.current_workload for member in team_members),
            "utilization_ratio": sum(member.current_workload for member in team_members) / total_capacity if total_capacity > 0 else 0.0
        }
    
    @staticmethod
    def compute_assignment_score(
        member: TeamMember,
        task: Task,
        weight_skill: float = 0.4,
        weight_workload: float = 0.3,
        weight_reliability: float = 0.2,
        weight_urgency: float = 0.1
    ) -> float:
        """
        Compute composite assignment score using weighted features
        
        Args:
            member: Team member candidate
            task: Task to assign
            weight_*: Feature weights (must sum to 1.0)
        
        Returns:
            Composite score (0.0 to 1.0)
        """
        # Extract features
        skill_score = FeatureExtractor.skill_task_compatibility(member, task)
        workload_ratio = FeatureExtractor.workload_utilization_ratio(member)
        reliability = FeatureExtractor.performance_reliability_index(member)
        urgency = FeatureExtractor.task_urgency_factor(task)
        
        # Workload penalty (lower utilization is better)
        workload_penalty = 1.0 - min(workload_ratio, 1.0)
        
        # Composite score
        composite_score = (
            weight_skill * skill_score +
            weight_workload * workload_penalty +
            weight_reliability * reliability +
            weight_urgency * urgency
        )
        
        return max(0.0, min(composite_score, 1.0))