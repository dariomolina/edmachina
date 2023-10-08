import './App.css'
import { Routes, Route, Navigate} from 'react-router-dom'
import { NavBar } from './routes/components/NavBar'
import { ListCareer } from './routes/ListCareer'
import { CreateCareer } from './routes/CreateCareer'
import { ListSubjects } from './routes/ListSubjects'
import { CreateSubjects } from './routes/CreateSubjects'
import { CreateLead } from './routes/CreateLead'
import { ListLead } from './routes/ListLead'
import { CreateEnrollmentStudy } from './routes/CreateEnrollment'
import { ListEnrollmentStudy } from './routes/ListEnrollment'


function App() {

  return (
    <>
      <NavBar></NavBar>
      <Routes>
        <Route path="/create-career" element={ <CreateCareer></CreateCareer> }></Route>
        <Route path="/list-career" element={ <ListCareer></ListCareer> }></Route>
        <Route path="/create-subjects" element={ <CreateSubjects></CreateSubjects> }></Route>
        <Route path="/list-subjects" element={ <ListSubjects></ListSubjects> }></Route>
        <Route path="/create-lead" element={ <CreateLead></CreateLead> }></Route>
        <Route path="/list-lead" element={ <ListLead></ListLead> }></Route>
        <Route path="/create-enrollment" element={ <CreateEnrollmentStudy></CreateEnrollmentStudy> }></Route>
        <Route path="/list-enrollment" element={ <ListEnrollmentStudy></ListEnrollmentStudy> }></Route>
        <Route path="/*" element={ <Navigate to="/"></Navigate> }></Route>
      </Routes>
    </>
  )
}

export default App
