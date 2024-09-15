import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [cursos, setCursos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/cursos/')
      .then(response => {
        console.log(response.data);
        setCursos(response.data.results);
      })
      .catch(error => {
        console.error('Erro ao buscar os cursos:', error);
      });
  }, []);

  return (
    <div>
      <h1>Lista de Cursos</h1>
      {cursos.length > 0 ? (
        <ul>
          {cursos.map(curso => (
            <li key={curso.id}>{curso.nome} - {curso.descricao}</li>
          ))}
        </ul>
      ) : (
        <p>Nenhum curso disponível.</p>
      )}
    </div>
  );
}

export default App;
