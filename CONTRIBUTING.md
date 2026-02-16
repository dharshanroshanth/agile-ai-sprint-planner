# Contributing Guide

Thank you for your interest in contributing to the Agile AI Sprint Planner! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/dharshanroshanth/agile-ai-sprint-planner.git
cd agile-ai-sprint-planner
```

### 2. Set Up Development Environment
```bash
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/bug-description
```

## 📝 Code Style

- **Python Style:** PEP 8 compliant
- **Algorithm:** Use type hints throughout
- **Docstrings:** Include docstrings for all functions/classes
- **Comments:** Explain complex logic, not obvious code

### Example:
```python
def calculate_skill_score(member: TeamMember, task: Task) -> float:
    """
    Calculate skill-task compatibility score.
    
    Args:
        member: Team member with skills
        task: Task with required skills
        
    Returns:
        float: Score between 0.0 and 1.0, where 1.0 is perfect match
    """
    if not task.required_skills:
        return 1.0
    
    # Calculate average proficiency for required skills
    matching_skills = [
        skill.proficiency for skill in member.skills
        if skill.name in task.required_skills
    ]
    
    return sum(matching_skills) / len(task.required_skills) if matching_skills else 0.0
```

## 🧪 Testing Requirements

- **Unit Tests:** All new features must have corresponding tests
- **Test Coverage:** Maintain >90% coverage
- **Run Tests:** `pytest tests/ -v`
- **Test Naming:** Use descriptive names: `test_<function>_<scenario>`

### Test Template:
```python
def test_feature_works_correctly():
    """Test that feature X works with scenario Y"""
    # Arrange
    input_data = {...}
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result.value == expected_value
    assert result.status == "success"
```

## 📚 Documentation

Document all changes:
- Update `README.md` if changing user-facing features
- Update `docs/ARCHITECTURE.md` if changing system design
- Update `docs/API_DOCUMENTATION.md` if adding/modifying API endpoints
- Include docstrings in code

## 🔄 Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/feature-name
   ```

2. **Make Changes** with frequent commits
   ```bash
   git add src/module.py
   git commit -m "feat: implement feature X"
   ```

3. **Run Tests Locally**
   ```bash
   pytest tests/ -v --cov=src
   ```

4. **Push to Your Fork**
   ```bash
   git push origin feature/feature-name
   ```

5. **Create Pull Request**
   - Use descriptive title: `feat: Add X functionality`
   - Reference issues: `Closes #123`
   - Include test results and screenshots if applicable

### PR Description Template:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #123

## Testing
- [x] Added unit tests
- [x] Existing tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
...
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Database persistence (SQLAlchemy → PostgreSQL)
- [ ] Advanced ML models (scikit-learn integration)
- [ ] LLM-powered assignment reasoning
- [ ] Burnout prediction models

### Medium Priority
- [ ] GitHub/Jira integration
- [ ] REST API pagination
- [ ] Advanced dependency handling
- [ ] Cross-team optimization

### Low Priority
- [ ] UI Dashboard
- [ ] Mobile app support
- [ ] Advanced reporting
- [ ] Performance optimizations

See [GitHub Issues](https://github.com/dharshanroshanth/agile-ai-sprint-planner/issues) for current tasks.

## 📋 Commit Message Format

Follow conventional commits:
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style
- `refactor`: Code refactoring
- `test`: Test addition/modification
- `chore`: Build, dependency, tooling

### Example:
```
feat(decision-engine): improve task assignment scoring

Add workload variance calculation to better balance team assignments.
Increase skill threshold from 0.2 to 0.3.

Closes #42
```

## 🔐 Security

- Never commit secrets or API keys
- Use `.env.example` for template environment variables
- Report security issues privately: [See SECURITY.md if exists]

## 📞 Questions?

- Open an issue for bug reports
- Start a discussion for feature requests
- Email maintainers for security concerns

## 👥 Code of Conduct

Be respectful and inclusive. We welcome contributions from everyone.

---

**Thank you for contributing!** 🙏
