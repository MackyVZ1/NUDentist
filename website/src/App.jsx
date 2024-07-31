import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <>
      <div>
        <h3> โรงพยาบาลทันตกรรม มหาวิทยาลัยนเรศวร</h3>
        <h4> กรุณาเลือกทำการ</h4>
        <button className='button'> ลงทะเบียนผู้ป่วยใหม่</button>
        <button className='button'> ผู้ป่วยที่มีประวัติแล้ว</button>
      </div>
      <div>
        <h4> พัฒนาโดย</h4>
        <h4> นายวีรภัทร พิชญ์วรรณขาม</h4>
        <h4> นางสาวเบญญาภา แก้วพาปราบ</h4>
      </div>
    </>
  )
}

export default App
