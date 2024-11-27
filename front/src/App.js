import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [profesores, setProfesores] = useState([]);

    useEffect(() => {
        fetchProfesores();
    }, []);

    const fetchProfesores = async () => {
        try {
            const response = await axios.get("http://localhost:5000/profesores");
            setProfesores(response.data);
        } catch (error) {
            console.error("Error al cargar los profesores:", error);
        }
    };

    return (
        <div>
            <h1>Lista de Profesores</h1>
            <ul>
                {profesores.map((profesor, index) => (
                    <li key={index}>{profesor.nombre} {profesor.apellido}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
const fetchProfesores = async () => {
    try {
        const response = await axios.get("http://localhost:5000/profesores"); // Cambia el puerto si es necesario
        setProfesores(response.data);
    } catch (error) {
        console.error("Error al cargar los profesores:", error);
    }
};
