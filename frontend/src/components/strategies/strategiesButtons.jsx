import React, {useState} from "react";
import Dropdown from "../common/dropdown";
import StraddleHome from "./straddle/straddlehome";
import {useNavigate} from "react-router-dom";

export default function StrategiesButtons(){
    const [strategy, setStrategy] = useState("");
    const navigate = useNavigate();

    const strategiesButtonList = [
        {
            label: "Straddle",
            value: "Straddle",
            href : "",
        },
        {
            label: "Strangle",
            value: "Strangle",
            href : "",
        },
        {
            label: "BreakOut",
            value: "BreakOut",
            href : "",
        },
        {
            label: "Reversal-15Min",
            value: "15MinReversal",
            href : "",
        },
    ];

    const handleChange = (event) => {
        let val = event.target.value;
        setStrategy(val);
        navigate(`./${val}`, { replace: true })
    };

    return(
        <div className="strategiesbuttons">
            <Dropdown
                label="Select Strategies"
                options={strategiesButtonList}
                value={strategy}
                onChange={handleChange}
            />  
        </div>
    );
}
