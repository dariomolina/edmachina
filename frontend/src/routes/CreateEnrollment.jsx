import React, { useEffect, useState } from 'react'
import { ConfirmationModal } from './components/ConfirmationModal'

const CreateEnrollmentStudy = () => {

  const initialForm = {
    leadId: 0,
    careerId: 0,
		subjectId: 0
  }

  const [formState, setFormState] = useState(initialForm)
  const [status, setStatus ] = useState(500)
  const [responseValue, setResponseValue] = useState(0)
	const [careerList, setCareerList] = useState([])
	const [leadList, setLeadList] = useState([])
	const [subjectsList, setSubjectsList] = useState([])

  const { leadId, careerId, subjectId } = formState

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormState({
      ...formState,
      [name]: value
    })
  }

	const handleChangeCareer = (event) => {
		const { name, value } = event.target
    setFormState({
      ...formState,
      [name]: value
    })
		handleGetSubjects(value)
	}

  const handleSubmit = async (event) => {
    event.preventDefault()
  }

  const handleConfirmSubmit = async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/enrollment-study/`
    const response = await fetch(url , {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
				lead_id: parseInt(leadId),
				career_id: parseInt(careerId),
				subject_id: parseInt(subjectId)
			}),
    })
    setStatus(response.status)
    const data = await response.json();
    setResponseValue(data)
  };

	const handleGetLead = async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/select-leads/`
    const response = await fetch(url , {
      method: "GET",
      headers: {
       'Content-Type': 'application/json',
      },
      params: {},
    })
    const data = await response.json();
		setLeadList(data)
    console.log('Materia encontrada:', data);
  };

	const handleGetCareer = async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/select-careers/`
    const response = await fetch(url , {
      method: "GET",
      headers: {
       'Content-Type': 'application/json',
      },
      params: {},
    })
    const data = await response.json();
		setCareerList(data)
    console.log('Materia encontrada:', data);
  };

	const handleGetSubjects = async (career_id) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}/select-subjects/${career_id}`
    const response = await fetch(url , {
      method: "GET",
      headers: {
       'Content-Type': 'application/json',
      },
      params: {},
    })
    const data = await response.json();
		setSubjectsList(data)
    console.log('Materia encontrada:', data);
  };

	useEffect(() => {
		handleGetLead()
    handleGetCareer()
  }, []);

  return (
    <>
    <div className="modal-content rounded-4 shadow">
      <div className="modal-body p-5">
        <form onSubmit={ handleSubmit } className="container left-elemets border">
          <br></br>
					<div className="input-group mb-3">
						<span className="input-group-text">Lead</span>
						<select
							className="form-select"
							id="inputGroupSelect03"
							aria-label="Example select with button addon"
							name="leadId"
							onChange={handleChange}
						>
							<option>--- Seleccione un Lead ...</option>
							{leadList.map((item) => {
								return (
									<option key={ item.id } value={ item.id }>{ item.first_name } {item.last_name}</option>
								)
							})}
						</select>
					</div>
					<div className="input-group mb-3">
						<span className="input-group-text">Carrera</span>
						<select
							className="form-select"
							id="inputGroupSelect03"
							aria-label="Example select with button addon"
							name="careerId"
							onChange={ handleChangeCareer }
						>
							<option>--- Seleccione una carrera ...</option>
							{careerList.map((item) => {
								return (
									<option key={ item.id } value={ item.id }>{ item.name }</option>
								)
							})}
						</select>
					</div>
					<div className="input-group mb-3">
						<span className="input-group-text">Materia</span>
						<select
							className="form-select"
							id="inputGroupSelect03"
							aria-label="Example select with button addon"
							name="subjectId"
							onChange={handleChange}
						>
							<option>--- Seleccione una materia ...</option>
							{subjectsList.map((item) => {
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
        <button type="submit" className="btn btn-lg btn-primary mt-5 w-100" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Great, thanks!</button>
      </div>
    </div>
    </>
  )
}

export { CreateEnrollmentStudy }
