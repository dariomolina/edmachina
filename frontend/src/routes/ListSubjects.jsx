import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListSubjects = () => {
  const [data, setData] = useState([]);

  const method = 'GET'
  const url = `${import.meta.env.VITE_BACKEND_URL}/subjects_with_careers/`
  const headers = {
    'Content-Type': 'application/json',
    //'Authorization': 'Bearer your-access-token',
  }
  const params = {}

  useEffect(() => {
    const getSubjects = async () => {
      const response = await axios({method, url, headers, params})
      const response_data = await response.data
      setData(response_data)
    }
    getSubjects();
  }, []);

  return (
    <>
    <div className="container border">
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Materia</th>
            <th scope="col">Carrera</th>
            <th scope="col">Duracion (meses)</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => {
            return (
              <tr key={ item.id } scope="row">
                <td >{ item.id }</td>
                <td>{ item.name }</td>
                <td>{ item.career_name }</td>
                <td>{ item.study_duration }</td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
    </>
  )
}

export { ListSubjects }
