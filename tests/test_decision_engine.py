import pytest
from src.decision_engine.task_assigner import TaskAssigner
from src.data_model.team_member import TeamMember, Skill
from src.data_model.task import Task, Priority
from datetime import datetime, timedelta


@pytest.fixture
def task_assigner():
    """Create a task assigner instance"""
    return TaskAssigner()


@pytest.fixture
def team_members():
    """Create sample team members"""
    return [
        TeamMember(
            id="member_1",
            name="Alice",
            email="alice@example.com",
            skills=[
                Skill(name="Python", proficiency=0.9),
                Skill(name="FastAPI", proficiency=0.8),
            ],
            total_hours_available=40.0,
            current_workload=0.0,
            reliability_score=0.9
        ),
        TeamMember(
            id="member_2",
            name="Bob",
            email="bob@example.com",
            skills=[
                Skill(name="JavaScript", proficiency=0.85),
                Skill(name="React", proficiency=0.8),
            ],
            total_hours_available=40.0,
            current_workload=0.0,
            reliability_score=0.8
        ),
    ]


@pytest.fixture
def tasks():
    """Create sample tasks"""
    return [
        Task(
            id="task_1",
            title="Build Backend API",
            description="Create REST API endpoints",
            required_skills=["Python", "FastAPI"],
            complexity=0.7,
            estimated_hours=16.0,
            priority=Priority.HIGH,
            deadline=datetime.utcnow() + timedelta(days=5)
        ),
        Task(
            id="task_2",
            title="Build Frontend",
            description="Create React components",
            required_skills=["JavaScript", "React"],
            complexity=0.6,
            estimated_hours=12.0,
            priority=Priority.MEDIUM,
            deadline=datetime.utcnow() + timedelta(days=7)
        ),
    ]


class TestTaskAssignment:
    """Test task assignment functionality"""
    
    def test_assign_tasks(self, task_assigner, team_members, tasks):
        """Test basic task assignment"""
        assignments = task_assigner.assign_tasks(tasks, team_members)
        assert len(assignments) > 0
    
    def test_assignment_respects_skills(self, task_assigner, team_members, tasks):
        """Test that assignments respect skill requirements"""
        assignments = task_assigner.assign_tasks(tasks, team_members)
        
        for assignment in assignments:
            task = next(t for t in tasks if t.id == assignment.task_id)
            member = next(m for m in team_members if m.id == assignment.member_id)
            
            # Check that member has required skills
            member_skills = {s.name for s in member.skills}
            required_skills = set(task.required_skills)
            assert required_skills.issubset(member_skills) or len(required_skills) == 0
    
    def test_assignment_respects_capacity(self, task_assigner, team_members, tasks):
        """Test that assignments respect workload capacity"""
        assignments = task_assigner.assign_tasks(tasks, team_members)
        
        for member in team_members:
            # Get all assignments for this member
            member_assignments = [a for a in assignments if a.member_id == member.id]
            total_hours = sum(a.estimated_hours for a in member_assignments)
            
            # Check against capacity
            assert total_hours <= member.total_hours_available
    
    def test_assignment_scoring(self, task_assigner, team_members, tasks):
        """Test assignment scoring is within valid range"""
        assignments = task_assigner.assign_tasks(tasks, team_members)
        
        for assignment in assignments:
            assert 0.0 <= assignment.final_score <= 1.0
            assert 0.0 <= assignment.skill_compatibility_score <= 1.0
    
    def test_assignment_reasoning(self, task_assigner, team_members, tasks):
        """Test assignment has reasoning"""
        assignments = task_assigner.assign_tasks(tasks, team_members)
        
        for assignment in assignments:
            reasoning_str = task_assigner.get_assignment_reasoning(assignment)
            assert assignment.task_id in reasoning_str
            assert assignment.member_id in reasoning_str
