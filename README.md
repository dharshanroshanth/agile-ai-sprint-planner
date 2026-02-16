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

## 🏗️ Project Structure

```
agile-ai-sprint-planner/
├── backend/                    # FastAPI REST API
│   ├── src/
│   │   ├── main.py
│   │   ├── api/               # REST endpoints
│   │   ├── data_model/        # Pydantic models
│   │   ├── feature_engine/    # ML features
│   │   ├── decision_engine/   # Task assignment
│   │   ├── sprint_planner/    # Sprint optimization
│   │   ├── learning/          # Feedback loop
│   │   └── utils/             # Logging
│   ├── config/                # Settings
│   ├── tests/                 # Unit tests
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile             # Docker config
│   └── README.md
│
├── frontend/                   # React Application
│   ├── public/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── hooks/             # Custom hooks
│   │   ├── utils/             # Utilities
│   │   └── styles/            # Styling
│   ├── package.json           # NPM dependencies
│   ├── Dockerfile             # Docker config
│   └── README.md
│
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md         # System design
│   ├── DATA_SCHEMA.md          # Data models
│   └── API_DOCUMENTATION.md    # API reference
│
├── docker-compose.yml          # Multi-container setup
├── README.md                   # Main documentation
├── TESTING.md                  # Testing guide
├── CONTRIBUTING.md             # Contribution guidelines
└── .gitignore

## Architecture Layers

### Backend Layers
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

### Frontend
- React 18 with modern hooks
- Responsive UI components
- Real-time API integration
- Data visualization dashboard
```

## 🛠️ API Endpoin & Setup

### Prerequisites
- Python 3.12+
- Node.js 16+
- Docker & Docker Compose (optional)

### Option 1: Local Development

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Run backend
uvicorn src.main:app --reload
```

Backend API: `http://localhost:8000`  
API Docs: `http://localhost:8000/docs`

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env

# Run frontend
npm start
```

Frontend App: `http://localhost:3000`

### Option 2: Docker Compose (All-in-One)

```bash
# From root directory
docker-compose up

# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 3: Individual Docker Containers

```bash
# Backend
cd backend
docker build -t agile-ai-backend .
docker run -p 8000:8000 agile-ai-backend

# Frontend
cd frontend
docker build -t agile-ai-frontend .
docker run -p 3000:3000 agile-ai-frontend
```

### Configuration

**Backend** (`backend/.env`):
```env
DEBUG=True
DATABASE_URL=sqlite:///./agile_planner.db
OPENAI_API_KEY=your-key
GEMINI_API_KEY=your-key
```
### Backend Documentation
- [Backend README](backend/README.md) - Backend setup and configuration
- [Architecture Guide](docs/ARCHITECTURE.md) - System design and algorithms
- [Data Schema](docs/DATA_SCHEMA.md) - Complete data model documentation
- [API Documentation](docs/API_DOCUMENTATION.md) - Endpoint reference with examples

### Frontend Documentation
- [Frontend README](frontend/README.md) - Frontend setup and components

### Development & Testing
- [Testing Guide](TESTING.md) - Complete testing instructions with API examples
- [Contributing Guide](CONTRIBUTING.md) - Development guidelines and PR process

### Related Resources
- [GitHub Repository](https://github.com/dharshanroshanth/agile-ai-sprint-planner)
- [Issues & Roadmap](https://github.com/dharshanroshanth/agile-ai-sprint-planner/issues)
REACT_APP_API_URL=http://localhost:8000
``
}
### Backend Tests
```bash
cd backend

# Run all tests
pytest tests/ -v

# Run specific test suite
pytest tests/test_feature_engine.py -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Frontend Tests (Coming Soon)
```bash
cd frontend

# Run React tests
npm test

# Run with coverage
npm test -- --coverage
```

### Full Test Suite Results
✅ 18/18 Backend Tests Passing
- Feature Extraction: 5 tests
- Decision Engine: 5 tests  
- Sprint Planning: 8 tests

See [TESTING.md](TESTING.md) for detailed test documentation and API testing examples.
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