import React, { useState, useEffect } from 'react'
import axios from 'axios';
import { Pagination } from './components/Pagination';

const ListEnrollmentStudy = () => {
  const initialData = { items: [], count: 0 }
  const [data, setData] = useState(initialData)
  const [page, setPage] = useState(1)
  const itemsPerPage = 10; // Número de elementos por página

  const method = 'GET'
  const url = `${import.meta.env.VITE_BACKEND_URL}/enrollment-study/`
  const headers = {
    'Content-Type': 'application/json',
    //'Authorization': 'Bearer your-access-token',
  }
  const params = {
    skip: (page - 1) * itemsPerPage,
    limit: itemsPerPage
  }

  useEffect(() => {
    const getEnrollmentsStudy = async () => {
      const response = await axios({method, url, headers, params})
      const response_data = await response.data
      setData(response_data)
    }
    getEnrollmentsStudy()
  }, [page])


  const totalPages = Math.ceil(data.count / itemsPerPage)

  return (
    <>
    <div className="container border">
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nombre</th>
            <th scope="col">Apellido</th>
            <th scope="col">Dni</th>
            <th scope="col">Materia</th>
            <th scope="col">Carrera</th>
            <th scope="col">Fecha de Registro</th>
          </tr>
        </thead>
        <tbody>
          {data.items.map((item) => {
            return (
              <tr key={ item.id } scope="row">
                <td >{ item.id }</td>
                <td>{ item.first_name }</td>
                <td>{ item.last_name }</td>
                <td>{ item.dni }</td>
                <td>{ item.subject_name }</td>
                <td>{ item.career_name }</td>
                <td>{ item.registration_date }</td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
    <Pagination
      totalPages={ totalPages }
      page={ page }
      setPage={ setPage }
    />
    </>
  )
}

export { ListEnrollmentStudy }
