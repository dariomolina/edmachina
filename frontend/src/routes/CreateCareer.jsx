import React, { useEffect, useState } from 'react'
import { ConfirmationModal } from './components/ConfirmationModal'

const CreateCareer = () => {

  const initialForm = {
    careerName: '',
    studyDuration: 0
  }

  const [formState, setFormState] = useState(initialForm)
  const [status, setStatus ] = useState(500)
  const [responseValue, setResponseValue] = useState(0)

  const { careerName, studyDuration } = formState

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormState({
      ...formState,
      [name]: value
    })
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
  }

  const handleConfirmSubmit = async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/career`
    const response = await fetch(url , {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: careerName, study_duration: parseInt(studyDuration) }),
    })
    setStatus(response.status)
    const data = await response.json();
    setResponseValue(data)
    setFormState(initialForm)
  };

  return (
    <>
    <div className="modal-content rounded-4 shadow">
      <div className="modal-body p-5">
        <form onSubmit={ handleSubmit } className="container left-elemets border">
          <br></br>
          <div className="input-group mb-3">
            <span className="input-group-text">Carrera</span>
            <input 
              type="text"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="careerName"
              value={ careerName }
              onChange={ handleChange }
            />
          </div>
          <div className="input-group mb-3">
            <span className="input-group-text">Duracion</span>
            <input
              type="number"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="studyDuration"
              value={ studyDuration }
              onChange={ handleChange }
            />
          </div>
          <ConfirmationModal
            onConfirm={handleConfirmSubmit}
            status={ status }
            responseValue={ responseValue }
          />
        </form>
        <button type="submit" className="btn btn-lg btn-primary mt-5 w-100" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Crear Carrera</button>
      </div>
    </div>

    </>
  )
}

export { CreateCareer }
