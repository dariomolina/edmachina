import React from 'react';


export const Alert = ({ message, typeAlert }) => {
	return (
		<>
		<div className={ `alert alert-${typeAlert}` } role="alert">
			{ message }
		</div>
		</> 
	)
}



const ConfirmationModal = ({ onConfirm, status, responseValue }) => {

	return (
  	<>
	<div className="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabIndex="-1">
		<div className="modal-dialog modal-dialog-centered">
			<div className="modal-content">
				<div className="modal-header">
					<h1 className="modal-title fs-5" id="exampleModalToggleLabel">Confirmación</h1>
					<button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div className="modal-body">
					Seleccione Confirmar para crear un nuevo registro
				</div>
				<div className="modal-footer">
					<button onClick={ onConfirm } className="btn btn-success" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal">Confirmar</button>
				</div>
			</div>
		</div>
	</div>
	<div className="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabIndex="-1">
		<div className="modal-dialog modal-dialog-centered">
			<div className="modal-content">
				<div className="modal-header">
					<h1 className="modal-title fs-5" id="exampleModalToggleLabel2">Información</h1>
					<button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div className="modal-body">
					{ status === 200 ?
						<Alert message={ `Registro exitoso con id: ${responseValue}` } typeAlert="success" />
					  : <Alert message={ `Hubo un error en la solicitud: ${responseValue.detail}` } typeAlert="danger" /> 
					}
				</div>
				<div className="modal-footer">
					<button type="button" className="btn btn-primary" data-bs-dismiss="modal">Close</button>
				</div>
			</div>
		</div>
	</div>
	</>
  );
};

export { ConfirmationModal }
