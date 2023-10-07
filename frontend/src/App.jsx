import './App.css'
import { Routes, Route, Navigate} from 'react-router-dom'
import { NavBar } from './routes/components/NavBar'
import { ListCareer } from './routes/ListCareer'
import { CreateCareer } from './routes/CreateCareer'


function App() {

  return (
    <>
      <NavBar></NavBar>
      <Routes>
        <Route path="/create-career" element={ <CreateCareer></CreateCareer> }></Route>
        <Route path="/list-career" element={ <ListCareer></ListCareer> }></Route>
        <Route path="/*" element={ <Navigate to="/"></Navigate> }></Route>
      </Routes>
    </>
  )
}

export default App
