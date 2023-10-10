import React, { useEffect, useState } from 'react'
import { ConfirmationModal } from './components/ConfirmationModal'

const CreateSubjects = () => {

  const initialForm = {
    subjectName: '',
    studyDuration: 0,
		careerId: 0
  } 

  const [formState, setFormState] = useState(initialForm)
  const [status, setStatus ] = useState(500)
  const [responseValue, setResponseValue] = useState(0)
	const [careerList, setCareerList] = useState([])

  const { subjectName, studyDuration, careerId } = formState

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
    const url = `${import.meta.env.VITE_BACKEND_URL}/subject-create`
    const response = await fetch(url , {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
				name: subjectName,
				study_duration: parseInt(studyDuration),
				career_id: parseInt(careerId)
			}),
    })
    setStatus(response.status)
    const data = await response.json();
    setResponseValue(data)
  };

	const handleGetCareer = async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/select-careers/`
    const response = await fetch(url , {
      method: "GET",
      //headers: {
      //  'Content-Type': 'application/json',
      //},
      params: {},
    })
    const data = await response.json();
		setCareerList(data)
    console.log('Materia encontrada:', data);
  };

	useEffect(() => {
    handleGetCareer();
  }, []);

  return (
    <>
    <div className="modal-content rounded-4 shadow">
      <div className="modal-body p-5">
        <form onSubmit={ handleSubmit } className="container left-elemets border">
          <br></br>
          <div className="input-group mb-3">
            <span className="input-group-text">Materia</span>
            <input 
              type="text"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="subjectName"
              value={ subjectName }
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
					<div className="input-group mb-3">
						<span className="input-group-text">Carrera</span>
						<select
							className="form-select"
							id="inputGroupSelect03"
							aria-label="Example select with button addon"
							name="careerId"
							onChange={handleChange}
						>
							<option>--- Seleccione una materia ...</option>
							{careerList.map((item) => {
								return (
									<option key={ item.id } value={ item.id }>{ item.name }</option>
								)
							})}
						</select>
					</div>
          <ConfirmationModal
            onConfirm={handleConfirmSubmit}
            status={ status }
            responseValue={ responseValue }
          />
        </form>
        <button type="submit" className="btn btn-lg btn-primary mt-5 w-100" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Crear Materia</button>
      </div>
    </div>
    </>
  )
}

export { CreateSubjects }
