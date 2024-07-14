import React, { useState } from 'react';
import axios from 'axios';
import './App.css';


const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setError(null); 
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setError('Необходимо выбрать файл');
      setResult(null); 
      return;
    }
    const formData = new FormData();
    formData.append('file', file);
    try {
      const response = await axios.post('http://localhost:8000/uploadfile', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult({
        predictedData: response.data.predicted_data,
        ld: response.data.ld,
        group: response.data.group,
      });
      setError(null); 
      setFile(null); 
    } catch (error) {
      if (error.response && error.response.data.detail) {
        setError('Необходимо загрузить файл формата Exel');
      } else {
        setError('Ошибка при отправке файла');
      }
      setResult(null);
    }
  };

  return (
    <div className="upload-container">
      <h2>Выберите файл</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Получить</button>
      </form>
      {error && (
        <div className="error">
          {error}
        </div>
      )}
      {result && (
        <div className="result">
        <table>
   <tr>
    <td>Студент: {result.ld}</td>
    <td>Группа: {result.group}</td>
    <td>Доля двоек: {result.predictedData}%</td>
   </tr>
  </table>
             
        </div>
      )}
    </div>
  );
};

export default FileUpload;

