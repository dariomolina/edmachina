import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ListLead = () => {
  const [data, setData] = useState([]);

  const method = 'GET'
  const url = `${import.meta.env.VITE_BACKEND_URL}/leads/`
  const headers = {
    'Content-Type': 'application/json',
    //'Authorization': 'Bearer your-access-token',
  }
  const params = {}

  useEffect(() => {
    const getLeads = async () => {
      const response = await axios({method, url, headers, params})
      const response_data = await response.data
      setData(response_data)
      console.log(response_data)
    }
    getLeads();
  }, []);

  return (
    <>
    <div className="container border">
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nombre</th>
            <th scope="col">Apellido</th>
            <th scope="col">Email</th>
            <th scope="col">Dni</th>
            <th scope="col">Dirección</th>
            <th scope="col">Telefono</th>
            <th scope="col">Fecha de Registro</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => {
            return (
              <tr key={ item.id } scope="row">
                <td >{ item.id }</td>
                <td>{ item.first_name }</td>
                <td>{ item.last_name }</td>
                <td>{ item.email }</td>
                <td>{ item.dni }</td>
                <td>{ item.address }</td>
                <td>{ item.phone }</td>
                <td>{ item.registration_date }</td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
    </>
  )
}

export { ListLead }
