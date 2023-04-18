import { useState } from "react";
import LoginForm from "./LoginForm";

function Login({ onLogin }) {

    return (
        <div>
            <LoginForm onLogin={onLogin}/>
        </div>
    )
}

export default Login;