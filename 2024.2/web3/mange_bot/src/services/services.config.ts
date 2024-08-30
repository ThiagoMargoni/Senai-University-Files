import axios, { type AxiosResponse } from "axios";
export const BASE_URL = import.meta.env.VITE_BACKEND_URL;

export const getAxios = () => {
    const createAxios = axios.create({
        baseURL: '/proxy-api/api',
        timeout: 40000,
        headers: {
            'Content-Type': 'application/json',
            credentials: 'include',
            Authorization: 'Bearer ${token}' 
        }
    });

    // createAxios.interceptors.request.use(verificarTokenValido)
    createAxios.interceptors.response.use(getAxiosResponse);

    return createAxios;
};

const getAxiosResponse = (response: AxiosResponse) => {
    return response.data;
};