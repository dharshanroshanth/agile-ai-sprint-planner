# Backend - Agile AI Sprint Planner

REST API backend for the Agile AI Sprint Planner system.

## 📋 Architecture

**Framework:** FastAPI 0.104.1  
**Language:** Python 3.12  
**Database:** SQLite (dev), PostgreSQL (production)

### Directory Structure

```
backend/
├── src/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/                    # API routes and models
│   ├── data_model/             # Pydantic data models
│   ├── feature_engine/         # ML feature extraction
│   ├── decision_engine/        # Task assignment algorithm
│   ├── sprint_planner/         # Sprint optimization
│   ├── learning/               # Feedback loop
│   └── utils/                  # Logging and utilities
├── config/
│   └── settings.py             # Configuration management
├── tests/
│   ├── test_feature_engine.py
│   ├── test_decision_engine.py
│   └── test_sprint_planner.py
├── logs/                       # Application logs
├── migrations/                 # Database migrations (Alembic)
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
└── Dockerfile                 # Docker configuration
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip

### Installation

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env

# Run the server
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at: `http://localhost:8000`

**Interactive API Documentation:** `http://localhost:8000/docs`

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test suite
pytest tests/test_feature_engine.py -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

## 📚 API Endpoints

### Team Members
- `POST /team-members` - Create team member
- `GET /team-members` - List all team members
- `GET /team-members/{id}` - Get team member details

### Tasks
- `POST /tasks` - Create task
- `GET /tasks` - List all tasks
- `GET /tasks/{id}` - Get task details

### Sprints
- `POST /sprints/plan` - Plan a new sprint
- `GET /sprints/{id}` - Get sprint details
- `GET /sprints` - List all sprints

### Health
- `GET /health` - Health check
- `GET /` - Welcome message

See [API_DOCUMENTATION.md](../docs/API_DOCUMENTATION.md) for detailed endpoint documentation.

## 🏗️ Core Components

### 1. Data Models (`src/data_model/`)
- **TeamMember**: Represents team capacity, skills, and performance
- **Task**: Represents work items with requirements and urgency
- **Sprint**: Container for tasks with timeline and constraints
- **Assignment**: Links tasks to team members with scoring

### 2. Feature Extraction (`src/feature_engine/`)
Transforms raw data into optimization-friendly features:
- Skill-task compatibility scoring
- Workload utilization metrics
- Performance reliability indices
- Task urgency factors
- Sprint capacity assessment

### 3. Decision Engine (`src/decision_engine/`)
Implements intelligent task assignment:
- Constraint-based assignment algorithm
- Candidate evaluation and ranking
- Optimal matching using feature scores
- Assignment reasoning generation

### 4. Sprint Optimizer (`src/sprint_planner/`)
Optimizes sprint planning:
- Sprint capacity calculation
- Task selection within capacity
- Feasibility assessment
- Risk level evaluation
- Workload balancing

### 5. Learning Feedback Loop (`src/learning/`)
Enables continuous improvement:
- Post-sprint performance tracking
- Member profile updates
- Prediction refinement
- Performance insights

## 🔧 Configuration

Edit `config/settings.py` or `.env` file:

```env
# Server
DEBUG=True
HOST=127.0.0.1
PORT=8000

# Database
DATABASE_URL=sqlite:///./agile_planner.db

# LLM APIs
OPENAI_API_KEY=your-key
GEMINI_API_KEY=your-key

# Application
LOG_LEVEL=INFO
```

## 🐳 Docker

Build and run with Docker:

```bash
# Build image
docker build -t agile-ai-backend .

# Run container
docker run -p 8000:8000 agile-ai-backend

# Or use docker-compose from root directory
cd ..
docker-compose up backend
```

## 📊 Database

### SQLite (Development)
Default for local development. Database file: `agile_planner.db`

### PostgreSQL (Production)
To use PostgreSQL, update `DATABASE_URL`:
```
postgresql://user:password@localhost:5432/agile_planner
```

### Migrations
Database migrations using Alembic:
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

## 🔐 Security

- API uses CORS middleware (configurable origins)
- Input validation with Pydantic
- Environment variables for sensitive data
- No secrets in version control

## 📈 Performance

- FastAPI with async/await support
- In-memory caching for frequently accessed data
- Optimized SQL queries
- Connection pooling for database

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Find and kill process on port 8000
lsof -i :8000
kill -9 <PID>
```

### Module Import Errors
```bash
# Set Python path
export PYTHONPATH=$(pwd)
```

### Database Issues
```bash
# Reset database
rm agile_planner.db

# Reinitialize
python -c "from src.db import init_db; init_db()"
```

## 📝 Related Documentation

- [Architecture Guide](../docs/ARCHITECTURE.md)
- [Data Schema](../docs/DATA_SCHEMA.md)
- [API Documentation](../docs/API_DOCUMENTATION.md)
- [Testing Guide](../TESTING.md)
- [Contributing](../CONTRIBUTING.md)

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines.

## 📄 License

MIT License - see LICENSE file at root

---

**Version:** 1.0.0  
**Last Updated:** February 16, 2026
