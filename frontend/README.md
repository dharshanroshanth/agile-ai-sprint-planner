# Frontend - Agile AI Sprint Planner

React-based frontend for the Agile AI Sprint Planner system.

## 📋 Architecture

**Framework:** React 18.2  
**Build Tool:** react-scripts/Vite  
**Styling:** Tailwind CSS  
**Routing:** React Router v6  

### Directory Structure

```
frontend/
├── public/
│   └── index.html              # HTML entry point
├── src/
│   ├── App.js                  # Main application component
│   ├── App.css                 # Application styles
│   ├── index.js                # React entry point
│   ├── index.css               # Global styles
│   ├── components/             # Reusable React components
│   │   ├── Header.js
│   │   ├── TeamMemberForm.js
│   │   ├── TaskForm.js
│   │   ├── SprintPlanner.js
│   │   └── ...
│   ├── pages/                  # Page components
│   │   ├── Dashboard.js
│   │   ├── TeamMembers.js
│   │   ├── Tasks.js
│   │   ├── Sprints.js
│   │   └── ...
│   ├── hooks/                  # Custom React hooks
│   │   ├── useApi.js
│   │   ├── useForm.js
│   │   └── ...
│   ├── utils/                  # Utility functions
│   │   ├── api.js              # API client
│   │   ├── formatting.js
│   │   └── ...
│   └── styles/                 # Global and component styles
├── package.json                # Dependencies and scripts
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Docker configuration
└── tailwind.config.js         # Tailwind CSS config (optional)
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+
- npm or yarn

### Installation

```bash
cd frontend

# Install dependencies
npm install

# Setup environment
cp .env.example .env

# Start development server
npm start
```

The app will be available at: `http://localhost:3000`

## 🏗️ Project Structure

### Component Hierarchy

```
App
├── Header
├── Navigation
├── Dashboard
│   ├── Team Members Panel
│   ├── Tasks Panel
│   └── Sprints Panel
├── Pages
│   ├── TeamMembersPage
│   │   ├── TeamMemberList
│   │   └── TeamMemberForm
│   ├── TasksPage
│   │   ├── TaskList
│   │   └── TaskForm
│   └── SprintsPage
│       ├── SprintList
│       └── SprintForm
└── Footer
```

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm test -- --coverage

# Run specific test file
npm test -- TeamMemberForm
```

## 🎨 Styling

### Tailwind CSS
Tailwind CSS is configured for utility-first styling:

```bash
# Install Tailwind (if not already installed)
npm install -D tailwindcss

# Generate Tailwind config (if needed)
npx tailwindcss init -p
```

### Custom Styles
Component-specific styles go in `src/styles/` or alongside components.

## 🔄 API Integration

### API Client (`src/utils/api.js`)

```javascript
import api from './utils/api';

// Create team member
const response = await api.post('/team-members', {
  name: 'Alice',
  email: 'alice@example.com',
  skills: [...],
  total_hours_available: 40
});

// Get all team members
const members = await api.get('/team-members');

// Plan sprint
const sprint = await api.post('/sprints/plan', {
  name: 'Sprint 1',
  duration_days: 14,
  team_member_ids: [...]
});
```

### Environment Variables

Create `.env` file:
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=30000
REACT_APP_ENV=development
```

## 📊 Key Features to Implement

### Phase 1: MVP Dashboard
- [ ] Team Members Management UI
- [ ] Tasks Management UI
- [ ] Sprint Planning Interface
- [ ] Real-time status updates

### Phase 2: Advanced Features
- [ ] Sprint Metrics Dashboard (success rate, velocity, etc.)
- [ ] Team Member Performance Analytics
- [ ] Task Dependency Visualization
- [ ] Risk Assessment Visualization

### Phase 3: User Experience
- [ ] Drag-and-drop task assignment
- [ ] Real-time collaboration
- [ ] Dark mode support
- [ ] Mobile responsive design

## 🐳 Docker

Build and run with Docker:

```bash
# Build image
docker build -t agile-ai-frontend .

# Run container
docker run -p 3000:3000 agile-ai-frontend

# Or use docker-compose from root directory
cd ..
docker-compose up frontend
```

## 🌐 Development Server

### Hot Reload
React Scripts includes hot module reloading. Changes to files will automatically refresh the browser.

### Build for Production

```bash
# Create optimized production build
npm run build

# Build outputs to `build/` directory
# Ready to deploy to any static hosting service
```

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 3000
lsof -i :3000
kill -9 <PID>

# Or run on different port
PORT=3001 npm start
```

### API Connection Issues
```javascript
// Check API URL in .env
REACT_APP_API_URL=http://localhost:8000

// Verify backend is running
curl http://localhost:8000/health
```

### Build Errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
npm start
```

## 📚 Component Examples

### Basic Component
```jsx
import React, { useState } from 'react';

export function TeamMemberForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <form>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
      />
    </form>
  );
}
```

## 🔐 Security

- Input validation on forms
- CORS configured on backend
- API key management via environment variables
- XSS protection through React
- CSRF token integration (when needed)

## 📈 Performance Optimization

- Code splitting with React.lazy()
- Image optimization
- Bundle size analysis: `npm run build -- --analyze`
- Memoization of expensive components

## 📝 Related Documentation

- [Architecture Guide](../docs/ARCHITECTURE.md)
- [API Documentation](../docs/API_DOCUMENTATION.md)
- [Testing Guide](../TESTING.md)
- [Contributing](../CONTRIBUTING.md)
- [Backend README](../backend/README.md)

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines.

## 📄 License

MIT License - see LICENSE file at root

---

**Version:** 1.0.0  
**Status:** In Development  
**Last Updated:** February 16, 2026
