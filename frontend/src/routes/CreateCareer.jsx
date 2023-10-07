import React, { useEffect, useState } from 'react'

const CreateCareer = () => {

  const [formState, setFormState] = useState({
    careerName: '',
    studyDuration: 0
  })

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
    const url = `${import.meta.env.VITE_BACKEND_URL}/career`
    const response = await fetch(url , {
      method: "POST",
      //headers: {
      //  'Content-Type': 'application/json',
      //},
      body: JSON.stringify({ name: careerName, study_duration: parseInt(studyDuration) }),
    })
    const data = await response.json();
    console.log('Carrera creada:', data);
  }

  return (
    <>
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
      <button type="submit" className="btn btn-primary">Guardar</button>
    </form>
    </>
  )
}

export { CreateCareer }
