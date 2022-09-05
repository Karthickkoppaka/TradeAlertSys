import React, {useState} from "react";
import { useEffect } from "react";
import {FiAlertTriangle, FiCheckCircle} from "react-icons/fi";
import axios from "axios";

export default function FyersStatus({handleLoginState}){
    const [loginStatus, setLoginStatus] = useState(false);
    
    useEffect(() => {
        function getData(){
            axios.get('http://127.0.0.1:8000/api/Fyers/Status')
            .then(response => {
                console.log("FyersStatus Success");
                setLoginStatus(true);
                handleLoginState(true);
            })
            .catch(err => {
                console.log("FyersStatus Fail");
                setLoginStatus(false);
                handleLoginState(false);
            });
            handleLoginState(true);
        }
        getData()
    }, [])


    return (
        <div className="fyersStatus">
            <label>Fyers Login Status</label>
            {
                loginStatus ? (<div className="active">
                                <label>Acitve</label>
                                <FiCheckCircle/>
                              </div>)
                              :
                              (<div className="inactive">
                                <div>
                                    <label>In-Acitve</label>
                                    <FiAlertTriangle/>
                                </div>
                                <a className="fyersbutton" href="/api/Fyers/Login">Login</a>
                               </div>)
            }
        </div>
    );
}