import axios from "axios";

const api = axios.create({
    // baseURL: 'http://localchost:8000/',
    withCredentials: true,
})


export default api;