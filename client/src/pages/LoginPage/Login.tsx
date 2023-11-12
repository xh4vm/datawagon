import React, { useState } from 'react';
import styles from './Login.module.scss';

interface LoginProps {
    onLogin: () => void,
}

const Login: React.FC<LoginProps> = ({ onLogin }: LoginProps) => {
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = () => {
        if (!login || !password) {
            setError('Введите логин и пароль.');
        } else if (login === "admin" || password === "admin") {
            onLogin();
            setError('');
        } else {
            setError('Неверный логин или пароль.');
        }
    };

    return (
        <div className={styles.pageContainer}>
            <div className={styles.loginContainer}>
            <h2>Login</h2>
            <form>
                <label>
                    <span className={styles.labelText}>Login:</span>
                    <input
                        type="text"
                        value={login}
                        onChange={(e) => setLogin(e.target.value)}
                        className={login ? '' : styles.errorInput}
                    />
                </label>
                <label>
                    <span className={styles.labelText}>Password:</span>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className={password ? '' : styles.errorInput}
                    />
                </label>
                {error && <p className={styles.errorMessage}>{error}</p>}
                <button type="button" onClick={handleLogin}>
                    Login
                </button>
            </form>
        </div>
        </div>
    );
};

export default Login;