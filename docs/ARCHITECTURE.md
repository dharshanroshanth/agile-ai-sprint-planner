# Architecture Guide

## System Design

### Core Components

#### 1. Data Models
- **TeamMember**: Represents team capacity, skills, and performance
- **Task**: Represents work items with requirements and urgency
- **Sprint**: Container for tasks with timeline and constraints
- **Assignment**: Links between tasks and team members with scoring

#### 2. Feature Extraction Engine
Transforms raw data into optimization-friendly features:
- Skill-task compatibility
- Workload metrics
- Performance indices
- Urgency factors

#### 3. Decision Engine
Performs multi-objective optimization:
- Scores each task-member pair
- Enforces hard constraints
- Handles soft constraints
- Produces explainable assignments

#### 4. Sprint Optimizer
Ensures sprint feasibility:
- Capacity planning
- Risk assessment
- Task selection
- Schedule validation

#### 5. Learning & Feedback Loop
Enables continuous improvement:
- Collects post-sprint data
- Updates member profiles
- Refines predictions
- Generates insights

### Data Flow

```
Input Data
    ↓
Feature Engineering
    ↓
Scoring & Optimization
    ↓
Assignment Generation
    ↓
Sprint Planning
    ↓
Feasibility Check
    ↓
Approved Sprint Plan
    ↓
Execution
    ↓
Post-Sprint Feedback
    ↓
Model Updates
```

## Algorithm Details

### Task Assignment Algorithm

1. **Sort tasks by urgency**
2. **For each task:**
   - Evaluate all team members
   - Score based on: skill, workload, reliability, urgency
   - Apply constraints (skill threshold, workload limit)
   - Select best candidate
   - Update member workload

### Scoring Function

```
Score = (0.4 × SkillScore) + (0.3 × WorkloadPenalty) + (0.2 × ReliabilityScore) + (0.1 × UrgencyBoost)
```

## Constraint Handling

### Hard Constraints (Must be satisfied)
- No member exceeds max workload
- Minimum skill threshold met
- Dependencies respected

### Soft Constraints (Preferred)
- Balanced workload distribution
- Assign to reliable performers
- Reduce spillover risk

## Architecture Layers

### 1. Data Model Layer
**Location:** `src/data_model/`

Defines core data structures:
- **TeamMember**: Represents team members with skills, capacity, and performance metrics
- **Task**: Represents work items with requirements, priority, and dependencies
- **Sprint**: Represents sprint containers with timeline and team information
- **Assignment**: Represents task-to-member assignments with scoring
- **Skill**: Represents individual skills with proficiency levels

### 2. Feature Engineering Layer
**Location:** `src/feature_engine/feature_extractor.py`

Extracts meaningful features for ML algorithms:
- Skill-task compatibility scoring
- Workload utilization ratios
- Performance reliability indices
- Task urgency factors
- Sprint capacity assessment
- Assignment composite scoring

### 3. Decision Engine Layer
**Location:** `src/decision_engine/task_assigner.py`

Implements intelligent task assignment:
- Constraint-based assignment algorithm
- Candidate evaluation and ranking
- Optimal matching using feature scores
- Assignment reasoning generation

### 4. Sprint Planning Layer
**Location:** `src/sprint_planner/sprint_optimizer.py`

Optimizes overall sprint planning:
- Sprint capacity calculation
- Task selection within capacity
- Feasibility assessment
- Risk level evaluation
- Workload balancing

### 5. Learning & Feedback Layer
**Location:** `src/learning/feedback_loop.py`

Improves system over time:
- Post-sprint feedback collection
- Prediction accuracy tracking
- Member performance updates
- Historical data accumulation

### 6. API Layer
**Location:** `src/api/`

Exposes functionality via REST API:
- Team member management
- Task creation and tracking
- Sprint planning
- Assignment tracking
- Health checks

### 7. Configuration Layer
**Location:** `config/settings.py`

Manages application configuration:
- API keys (OpenAI, Gemini)
- Environment settings
- Database configuration
- Logging levels

## Data Flow

```
1. Input: Team Members, Tasks, Sprint Parameters
   ↓
2. Feature Extraction: Extract meaningful features
   ↓
3. Decision Engine: Find optimal assignments
   ↓
4. Sprint Optimizer: Plan feasible sprint
   ↓
5. Output: Sprint plan with assignments
   ↓
6. Feedback: Collect post-sprint metrics
   ↓
7. Learning: Update models based on feedback
```

## Key Algorithms

### Task Assignment Algorithm
1. Sort tasks by urgency (deadline + priority)
2. For each task:
   - Find candidate team members
   - Filter by hard constraints (availability, skills)
   - Score candidates using feature-based algorithm
   - Select best candidate
   - Update member workload

### Sprint Feasibility Assessment
1. Calculate total sprint capacity
2. Estimate total effort required
3. Check workload balance across team
4. Assess risk factors:
   - Over-utilization (>95%)
   - Unbalanced workload (variance)
   - Missing skills
5. Assign risk level (low/medium/high)

## Technology Stack

- **Framework**: FastAPI
- **Data Validation**: Pydantic
- **ML/AI**: Scikit-learn, Feature engineering from scratch
- **API Clients**: OpenAI, Google Generative AI
- **Database**: SQLAlchemy (SQLite default)
- **Testing**: Pytest
- **Logging**: Python logging + Loki

## Deployment Considerations

- Containerized with Docker
- Environment-based configuration
- Database abstraction for easy migration
- Scalable API design
- Comprehensive logging for monitoring
