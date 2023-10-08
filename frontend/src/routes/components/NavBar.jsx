import React from 'react'
import { Link, NavLink} from 'react-router-dom'

export const NavBar = () => {
  return (
		<>
    <nav className="navbar navbar-expand-lg bg-body-tertiary border">
			<div className="container-fluid">
				<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarNavDropdown">
					<ul className="navbar-nav">
						<li className="nav-item dropdown">
							<Link className="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
								Carreras
							</Link>
							<ul className="dropdown-menu">
								<li><NavLink className="nav-link" to="/create-career">Crear</NavLink></li>
								<li><NavLink className="nav-link" to="/list-career">Listar</NavLink></li>
							</ul>
						</li>
						<li className="nav-item dropdown">
							<Link className="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
								Materias
							</Link>
							<ul className="dropdown-menu">
								<li><NavLink className="nav-link" to="/create-subjects">Crear</NavLink></li>
								<li><NavLink className="nav-link" to="/list-subjects">Listar</NavLink></li>
							</ul>
						</li>
						<li className="nav-item dropdown">
							<Link className="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
								Leads
							</Link>
							<ul className="dropdown-menu">
								<li><NavLink className="nav-link" to="/create-lead">Crear</NavLink></li>
								<li><NavLink className="nav-link" to="/list-lead">Listar</NavLink></li>
							</ul>
						</li>
						<li className="nav-item dropdown">
							<Link className="nav-link dropdown-toggle active" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
								Inscripción
							</Link>
							<ul className="dropdown-menu">
								<li><NavLink className="nav-link" to="/create-enrollment">Crear</NavLink></li>
								<li><NavLink className="nav-link" to="/list-enrollment">Listar</NavLink></li>
							</ul>
						</li>
					</ul>
				</div>
			</div>
		</nav>
		</>
	)
}
