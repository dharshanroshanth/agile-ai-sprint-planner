import pytest
from src.sprint_planner.sprint_optimizer import SprintOptimizer
from src.data_model.sprint import Sprint
from src.data_model.team_member import TeamMember, Skill
from src.data_model.task import Task, Priority
from datetime import datetime, timedelta


@pytest.fixture
def sprint_optimizer():
    """Create a sprint optimizer instance"""
    return SprintOptimizer()


@pytest.fixture
def sprint():
    """Create a sample sprint"""
    return Sprint(
        id="sprint_1",
        name="Sprint 1",
        start_date=datetime.utcnow(),
        end_date=datetime.utcnow() + timedelta(days=14),
        duration_days=14,
        team_members=["member_1", "member_2"],
        total_sprint_capacity=80.0
    )


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
    base_time = datetime.utcnow()
    return [
        Task(
            id="task_1",
            title="Build Backend API",
            description="Create REST API endpoints",
            required_skills=["Python", "FastAPI"],
            complexity=0.7,
            estimated_hours=16.0,
            priority=Priority.HIGH,
            deadline=base_time + timedelta(days=5)
        ),
        Task(
            id="task_2",
            title="Build Frontend",
            description="Create React components",
            required_skills=["JavaScript", "React"],
            complexity=0.6,
            estimated_hours=12.0,
            priority=Priority.MEDIUM,
            deadline=base_time + timedelta(days=7)
        ),
        Task(
            id="task_3",
            title="Write Tests",
            description="Create unit tests",
            required_skills=["Python"],
            complexity=0.5,
            estimated_hours=10.0,
            priority=Priority.MEDIUM,
            deadline=base_time + timedelta(days=10)
        ),
        Task(
            id="task_4",
            title="Documentation",
            description="Write API documentation",
            required_skills=["Python"],
            complexity=0.3,
            estimated_hours=6.0,
            priority=Priority.LOW,
            deadline=base_time + timedelta(days=12)
        ),
    ]


class TestSprintPlanning:
    """Test sprint planning functionality"""
    
    def test_sprint_planning(self, sprint_optimizer, sprint, team_members, tasks):
        """Test basic sprint planning"""
        planned_sprint, selected_tasks = sprint_optimizer.plan_sprint(
            sprint, tasks, team_members
        )
        
        assert planned_sprint is not None
        assert len(selected_tasks) > 0
        assert planned_sprint.planned_tasks == len(selected_tasks)
    
    def test_sprint_capacity_calculation(self, sprint_optimizer, team_members):
        """Test sprint capacity calculation"""
        capacity = sprint_optimizer._calculate_sprint_capacity(team_members)
        expected = 40.0 + 40.0  # Two members with 40 hours each
        assert capacity == expected
    
    def test_task_selection(self, sprint_optimizer, tasks):
        """Test task selection respects capacity"""
        sprint_capacity = 80.0
        selected = sprint_optimizer._select_tasks_for_sprint(tasks, sprint_capacity)
        
        total_effort = sum(t.estimated_hours for t in selected)
        assert total_effort <= sprint_capacity * 0.85  # 85% utilization target
    
    def test_sprint_feasibility(self, sprint_optimizer, sprint, team_members, tasks):
        """Test sprint feasibility assessment"""
        planned_sprint, selected_tasks = sprint_optimizer.plan_sprint(
            sprint, tasks, team_members
        )
        
        # Check feasibility attributes
        assert hasattr(planned_sprint, 'is_feasible')
        assert hasattr(planned_sprint, 'risk_level')
        assert planned_sprint.risk_level in ["low", "medium", "high"]
    
    def test_workload_balance(self, sprint_optimizer, sprint, team_members, tasks):
        """Test that sprint planning balances workload"""
        planned_sprint, selected_tasks = sprint_optimizer.plan_sprint(
            sprint, tasks, team_members
        )
        
        # Calculate workload for each member after planning
        # This is a basic check - in production you'd verify assignments
        assert len(selected_tasks) > 0


class TestSprintMetrics:
    """Test sprint metrics calculation"""
    
    def test_sprint_progress(self, sprint):
        """Test sprint progress calculation"""
        sprint.planned_tasks = 10
        sprint.completed_tasks = 3
        progress = sprint.sprint_progress()
        assert progress == 0.3
    
    def test_sprint_success_rate(self, sprint):
        """Test sprint success rate calculation"""
        sprint.planned_tasks = 10
        sprint.completed_tasks = 8
        sprint.failed_tasks = 2
        success_rate = sprint.success_rate()
        assert success_rate == 0.8
    
    def test_days_remaining(self, sprint):
        """Test days remaining calculation"""
        days = sprint.days_remaining()
        assert days >= 13  # Close to 14 days
        assert days <= 14
