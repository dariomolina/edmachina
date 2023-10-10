import React, { useEffect, useState } from 'react'
import { ConfirmationModal } from './components/ConfirmationModal'

const CreateLead = () => {

  const InitialForm = {
    firstName: '',
    lastName: '',
    email: '',
		dni: 0,
    address: '',
    phone: ''
  }

  const [formState, setFormState] = useState(InitialForm)
  const [status, setStatus ] = useState(500)
  const [responseValue, setResponseValue] = useState(0)

  const { firstName, lastName, email, dni, address, phone } = formState

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
    const url = `${import.meta.env.VITE_BACKEND_URL}/leads/`
    const response = await fetch(url , {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
				first_name: firstName,
				last_name: lastName,
				email: email,
				dni: dni,
				address: address,
				phone: phone
			}),
    })
    setStatus(response.status)
    const data = await response.json();
    setResponseValue(data)
    setFormState(InitialForm)
  };

  return (
    <>
    <div className="modal-content rounded-4 shadow">
      <div className="modal-body p-5">
        <form onSubmit={ handleSubmit } className="container left-elemets border">
          <br></br>
          <div className="input-group mb-3">
            <span className="input-group-text">Nombre</span>
            <input 
              type="text"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="firstName"
              value={ firstName }
              onChange={ handleChange }
            />
          </div>
          <div className="input-group mb-3">
            <span className="input-group-text">Apellido</span>
            <input
              type="text"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="lastName"
              value={ lastName }
              onChange={ handleChange }
            />
          </div>
					<div className="input-group mb-3">
            <span className="input-group-text">Dni</span>
            <input
              type="number"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="dni"
              value={ dni }
              onChange={ handleChange }
            />
          </div>
					<div className="input-group mb-3">
            <span className="input-group-text">Email</span>
            <input
              type="email"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="email"
              value={ email }
              onChange={ handleChange }
            />
          </div>
					<div className="input-group mb-3">
            <span className="input-group-text">Address</span>
            <input
              type="text"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="address"
              value={ address }
              onChange={ handleChange }
            />
          </div>
					<div className="input-group mb-3">
            <span className="input-group-text">Phone</span>
            <input
              type="number"
              className="form-control"
              aria-label="Amount (to the nearest dollar)"
              name="phone"
              value={ phone }
              onChange={ handleChange }
            />
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

export { CreateLead }
