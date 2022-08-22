import {React, useState} from "react";
import Dashboard from "./dashboard";

export default function PostLogin(){
    let [isActive, setIsActive] = useState(true);
    console.log('postlogin');
    console.log(isActive);
    return(
        <div>
            <Dashboard loginState={isActive}/>
        </div>
    );
}