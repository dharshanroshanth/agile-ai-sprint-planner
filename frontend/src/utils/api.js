import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
const API_TIMEOUT = process.env.REACT_APP_API_TIMEOUT || 30000;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token if available
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle errors globally
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// API Methods - Team Members
export const teamMembersAPI = {
  getAll: () => apiClient.get('/team-members'),
  getById: (id) => apiClient.get(`/team-members/${id}`),
  create: (data) => apiClient.post('/team-members', data),
  update: (id, data) => apiClient.put(`/team-members/${id}`, data),
  delete: (id) => apiClient.delete(`/team-members/${id}`),
};

// API Methods - Tasks
export const tasksAPI = {
  getAll: (params) => apiClient.get('/tasks', { params }),
  getById: (id) => apiClient.get(`/tasks/${id}`),
  create: (data) => apiClient.post('/tasks', data),
  update: (id, data) => apiClient.put(`/tasks/${id}`, data),
  delete: (id) => apiClient.delete(`/tasks/${id}`),
};

// API Methods - Sprints
export const sprintsAPI = {
  getAll: (params) => apiClient.get('/sprints', { params }),
  getById: (id) => apiClient.get(`/sprints/${id}`),
  create: (data) => apiClient.post('/sprints', data),
  update: (id, data) => apiClient.put(`/sprints/${id}`, data),
  delete: (id) => apiClient.delete(`/sprints/${id}`),
  plan: (id, data) => apiClient.post(`/sprints/${id}/plan`, data),
};

// API Methods - Health & Status
export const healthAPI = {
  check: () => apiClient.get('/health'),
  status: () => apiClient.get('/'),
};

export default apiClient;
