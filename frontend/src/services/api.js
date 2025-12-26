import axios from 'axios';

// Use relative URL for Docker/production, or environment variable for development
const API_BASE_URL = process.env.REACT_APP_API_URL || '/api';

export const getTasks = async () => {
  const response = await axios.get(`${API_BASE_URL}/tasks`);
  return response.data;
};

export const createTask = async (taskData) => {
  const response = await axios.post(`${API_BASE_URL}/tasks`, taskData);
  return response.data;
};

export const deleteTask = async (taskId) => {
  const response = await axios.delete(`${API_BASE_URL}/tasks/${taskId}`);
  return response.data;
};

export const updateTask = async (taskId, updateData) => {
  const response = await axios.put(`${API_BASE_URL}/tasks/${taskId}`, updateData);
  return response.data;
};

export const transcribeAudio = async (audioBlob) => {
  const formData = new FormData();
  formData.append('audio', audioBlob, 'recording.webm');

  const response = await axios.post(`${API_BASE_URL}/transcribe`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};
