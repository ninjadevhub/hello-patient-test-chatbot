import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const fetchMessages = async (email: string) => {
  const encodedEmail = encodeURIComponent(email);
  const response = await axios.get(`${API_BASE_URL}/get-history-by-user/${encodedEmail}`);
  console.log("API Response (fetchMessages):", response);
  return response.data;
};

export const sendMessageAPI = async (messageData: {
  email: string;
  prompt: string;
}) => {
  const response = await axios.post(`${API_BASE_URL}/generate-text`, messageData);
  return response.data;
};







