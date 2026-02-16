# Agile AI Sprint Planner

An intelligent, AI-powered system for optimal Agile sprint planning and task assignment.

## 🎯 Problem Statement

Traditional Agile sprint planning relies on manual, intuition-based task assignment, leading to:
- Unbalanced workloads
- Missed deadlines
- Sprint failures
- Team burnout

## ✨ Solution

This system uses AI to:
- **Intelligently assign** tasks based on skills, workload, and history
- **Optimize capacity** to prevent overcommitment
- **Predict risks** before sprints fail
- **Learn continuously** from past sprints

## 🏗️ Architecture

The system uses a multi-layer architecture:

```
┌─────────────────────────────────────────────────┐
│ FastAPI Web Application                         │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌──────────────┐         ┌──────────────┐    │
│  │ Task Assigner│         │Sprint Planner│    │
│  │ (Decision    │         │ (Optimizer)  │    │
│  │ Engine)      │         │              │    │
│  └──────────────┘         └──────────────┘    │
│        ▲                          ▲            │
│        └──────────┬───────────────┘            │
│                   │                            │
│  ┌────────────────────────────────────────┐   │
│  │  Feature Extraction Engine             │   │
│  │  - Skill-Task Compatibility            │   │
│  │  - Workload Utilization                │   │
│  │  - Performance Reliability             │   │
│  │  - Task Urgency                        │   │
│  └────────────────────────────────────────┘   │
│        ▲                                       │
│  ┌─────────────────────────────────────────┐  │
│  │  Data Models                            │  │
│  │  - Team Members                         │  │
│  │  - Tasks                                │  │
│  │  - Sprints                              │  │
│  │  - Assignments                          │  │
│  └─────────────────────────────────────────┘  │
│        ▲                                       │
│  ┌─────────────────────────────────────────┐  │
│  │  Learning & Feedback Loop               │  │
│  │  - Post-Sprint Analysis                 │  │
│  │  - Model Updates                        │  │
│  │  - Continuous Improvement               │  │
│  └─────────────────────────────────────────┘  │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 🛠️ API Endpoints

### 1. Create Team Member

```bash
POST /team-members
Content-Type: application/json

{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "skills": [
    {"name": "Python", "proficiency": 0.9},
    {"name": "FastAPI", "proficiency": 0.8}
  ],
  "total_hours_available": 40
}
```

### 2. Create Task

```bash
POST /tasks
Content-Type: application/json

{
  "title": "Build Authentication System",
  "description": "Implement JWT-based authentication",
  "required_skills": ["Python", "FastAPI"],
  "complexity": 0.7,
  "estimated_hours": 8,
  "priority": "high",
  "deadline": "2026-03-01T17:00:00"
}
```

### 3. Plan Sprint

```bash
POST /sprints/plan
Content-Type: application/json

{
  "name": "Sprint 1",
  "duration_days": 14,
  "team_member_ids": ["member-id-1", "member-id-2"]
}
```

## 📦 Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dharshanroshanth/agile-ai-sprint-planner.git
   cd agile-ai-sprint-planner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   python src/main.py
   ```

   The API will be available at `http://localhost:8000`
   
   Interactive API documentation: `http://localhost:8000/docs`

## 📊 Key Features

### 1. Intelligent Task Assignment
- Matches tasks to team members based on skills
- Considers workload and availability
- Respects deadline urgency
- Validates hard constraints (capacity, skills)

### 2. Capacity Planning
- Calculates realistic sprint capacity
- Prevents overcommitment
- Balances workload across team
- Targets 85% utilization for optimal throughput

### 3. Risk Assessment
- Evaluates sprint feasibility
- Identifies high-risk scenarios
- Classifies risk levels: low, medium, high, critical
- Recommends adjustments based on variance

### 4. Learning & Improvement
- Tracks post-sprint performance
- Updates member profiles
- Improves predictions over time
- Continuously refines algorithms

## 📈 Metrics

The system tracks:

- **Sprint Success Rate**: % of tasks completed on time
- **Workload Balance**: Variance in team member utilization
- **Prediction Accuracy**: Error between estimated and actual time
- **Spillover Rate**: Tasks moved to next sprint

## 🔧 Configuration

Edit `src/config/settings.py` to customize:

- API keys (from `.env`)
- Models (ChatGPT, Gemini)
- Weights for optimization algorithm
- Constraints and thresholds

## 📚 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) - System design and algorithms
- [Data Schema](docs/DATA_SCHEMA.md) - Complete data model documentation
- [API Documentation](docs/API_DOCUMENTATION.md) - Endpoint reference with examples

## 🧪 Testing

Run tests with pytest:

```bash
pytest tests/ -v
```

Run specific test suite:

```bash
pytest tests/test_feature_engine.py -v
pytest tests/test_decision_engine.py -v
pytest tests/test_sprint_planner.py -v
```

## 🎓 How It Works

### Step 1: Data Representation
Team members, tasks, and sprints are converted into structured data with features like:
- Skills and proficiency levels
- Workload and availability
- Task complexity and priority
- Historical performance

### Step 2: Feature Engineering
Raw data is transformed into meaningful signals:
- Skill-task compatibility score
- Workload utilization ratio
- Performance reliability index
- Task urgency factor

### Step 3: Decision Engine
Tasks are assigned using multi-objective optimization:
- Maximize skill-task fit
- Minimize workload imbalance
- Respect sprint capacity
- Prioritize urgent tasks

### Step 4: Sprint Planning
Individual assignments are combined into a feasible sprint plan that respects constraints and minimizes risk.

### Step 5: Learning Loop
After each sprint, actual performance is compared to predictions, and models are updated for continuous improvement.

## 🤝 Contributing

Contributions welcome! Areas for enhancement:

- Reinforcement learning for strategy optimization
- Burnout prediction models
- Integration with Jira/Azure DevOps
- Advanced dependency handling
- Cross-team optimization

## 📄 License

MIT License - see LICENSE file

## 👨‍💻 Author

Built by Dharshan Roshanth

## 🙏 Acknowledgments

Inspired by:

- Agile software development best practices
- AI optimization and machine learning
- Real-world sprint planning challenges
   ```