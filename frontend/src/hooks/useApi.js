import { useState, useEffect, useCallback } from 'react';
import { teamMembersAPI, tasksAPI, sprintsAPI } from '../utils/api';

// Generic hook for API calls
export const useApi = (apiFunction, dependencies = []) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await apiFunction();
      setData(response.data);
    } catch (err) {
      setError(err.message || 'An error occurred');
    } finally {
      setLoading(false);
    }
  }, [apiFunction]);

  useEffect(() => {
    fetchData();
  }, dependencies);

  const refetch = useCallback(fetchData, [fetchData]);

  return { data, loading, error, refetch };
};

// Hook for team members
export const useTeamMembers = () => {
  const { data, loading, error, refetch } = useApi(
    () => teamMembersAPI.getAll()
  );

  const addTeamMember = useCallback(
    async (memberData) => {
      try {
        const response = await teamMembersAPI.create(memberData);
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to create team member');
      }
    },
    [refetch]
  );

  const updateTeamMember = useCallback(
    async (id, memberData) => {
      try {
        const response = await teamMembersAPI.update(id, memberData);
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to update team member');
      }
    },
    [refetch]
  );

  const deleteTeamMember = useCallback(
    async (id) => {
      try {
        await teamMembersAPI.delete(id);
        refetch();
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to delete team member');
      }
    },
    [refetch]
  );

  return {
    teamMembers: data || [],
    loading,
    error,
    addTeamMember,
    updateTeamMember,
    deleteTeamMember,
    refetch,
  };
};

// Hook for tasks
export const useTasks = () => {
  const { data, loading, error, refetch } = useApi(
    () => tasksAPI.getAll()
  );

  const addTask = useCallback(
    async (taskData) => {
      try {
        const response = await tasksAPI.create(taskData);
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to create task');
      }
    },
    [refetch]
  );

  const updateTask = useCallback(
    async (id, taskData) => {
      try {
        const response = await tasksAPI.update(id, taskData);
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to update task');
      }
    },
    [refetch]
  );

  const deleteTask = useCallback(
    async (id) => {
      try {
        await tasksAPI.delete(id);
        refetch();
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to delete task');
      }
    },
    [refetch]
  );

  return {
    tasks: data || [],
    loading,
    error,
    addTask,
    updateTask,
    deleteTask,
    refetch,
  };
};

// Hook for sprints
export const useSprints = () => {
  const { data, loading, error, refetch } = useApi(
    () => sprintsAPI.getAll()
  );

  const addSprint = useCallback(
    async (sprintData) => {
      try {
        const response = await sprintsAPI.create(sprintData);
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to create sprint');
      }
    },
    [refetch]
  );

  const planSprint = useCallback(
    async (sprintId, tasks) => {
      try {
        const response = await sprintsAPI.plan(sprintId, {
          available_task_ids: tasks.map(t => t.id),
        });
        refetch();
        return response.data;
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to plan sprint');
      }
    },
    [refetch]
  );

  const deleteSprint = useCallback(
    async (id) => {
      try {
        await sprintsAPI.delete(id);
        refetch();
      } catch (err) {
        throw new Error(err.response?.data?.detail || 'Failed to delete sprint');
      }
    },
    [refetch]
  );

  return {
    sprints: data || [],
    loading,
    error,
    addSprint,
    planSprint,
    deleteSprint,
    refetch,
  };
};

// Hook for notifications
export const useNotification = () => {
  const [notification, setNotification] = useState(null);

  const showNotification = useCallback((message, type = 'info', duration = 3000) => {
    setNotification({ message, type });
    if (duration) {
      setTimeout(() => setNotification(null), duration);
    }
  }, []);

  const clearNotification = useCallback(() => {
    setNotification(null);
  }, []);

  return { notification, showNotification, clearNotification };
};
