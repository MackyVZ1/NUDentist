import { useState } from 'react' // import library
import reactLogo from './assets/react.svg' // import file
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)
  
  const getClick = () => {
    const res = axios.get('http://localhost:8000')
    console.log(res);
  }
  return (
    <>
      <button onClick={getClick}>
        Click
      </button>
    </>
  )
}

export default App
