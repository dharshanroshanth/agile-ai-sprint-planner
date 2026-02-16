import pytest
from src.feature_engine.feature_extractor import FeatureExtractor
from src.data_model.team_member import TeamMember, Skill
from src.data_model.task import Task, Priority
from datetime import datetime, timedelta


@pytest.fixture
def sample_member():
    """Create a sample team member for testing"""
    return TeamMember(
        id="member_1",
        name="John Doe",
        email="john@example.com",
        skills=[
            Skill(name="Python", proficiency=0.9),
            Skill(name="FastAPI", proficiency=0.8),
        ],
        total_hours_available=40.0,
        current_workload=10.0,
        reliability_score=0.85,
        sprint_velocity=2.0
    )


@pytest.fixture
def sample_task():
    """Create a sample task for testing"""
    return Task(
        id="task_1",
        title="Build API",
        description="Create REST API",
        required_skills=["Python", "FastAPI"],
        complexity=0.7,
        estimated_hours=8.0,
        priority=Priority.HIGH,
        deadline=datetime.utcnow() + timedelta(days=5)
    )


class TestFeatureExtraction:
    """Test feature extraction functionality"""
    
    def test_skill_compatibility(self, sample_member, sample_task):
        """Test skill-task compatibility scoring"""
        score = FeatureExtractor.skill_task_compatibility(sample_member, sample_task)
        assert 0.0 <= score <= 1.0
        assert score > 0.7  # High compatibility expected
    
    def test_workload_utilization(self, sample_member):
        """Test workload utilization calculation"""
        util = FeatureExtractor.workload_utilization_ratio(sample_member)
        assert util == 0.25  # 10/40 = 0.25
    
    def test_performance_reliability(self, sample_member):
        """Test reliability index"""
        reliability = FeatureExtractor.performance_reliability_index(sample_member)
        assert reliability == 0.85
    
    def test_assignment_score(self, sample_member, sample_task):
        """Test composite assignment score"""
        score = FeatureExtractor.compute_assignment_score(sample_member, sample_task)
        assert 0.0 <= score <= 1.0
    
    def test_sprint_capacity(self):
        """Test sprint capacity calculation"""
        members = [
            TeamMember(
                id="m1", name="Member 1", email="m1@example.com",
                skills=[], total_hours_available=40.0,
                current_workload=0.0
            ),
            TeamMember(
                id="m2", name="Member 2", email="m2@example.com",
                skills=[], total_hours_available=40.0,
                current_workload=0.0
            )
        ]
        capacity = FeatureExtractor.sprint_capacity_score(None, members)
        assert capacity["total_capacity"] == 80.0
        assert capacity["available_capacity"] == 80.0
        assert capacity["utilization_ratio"] == 0.0
