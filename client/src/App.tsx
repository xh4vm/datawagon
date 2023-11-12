import React, { useState } from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Login from "./pages/LoginPage/Login";
import Main from "./pages/MainPage/Main";

const App: React.FC = () => {
    const [isAuthent, setIsAuthent] = useState(true)
    console.log(isAuthent)

    const handleLogin = () => {
        setIsAuthent(!isAuthent);
        console.log(isAuthent)
    };

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={isAuthent ? <Main isAuthent={isAuthent} handleLogin={handleLogin}/> : <Login onLogin={handleLogin}/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
