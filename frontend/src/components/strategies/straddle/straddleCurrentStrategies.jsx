import React from "react";
import axios from "axios";

export function GetCurrentStraddle(setStrategyList){
    function getCurrentStraddles(){
        let url = `http://127.0.0.1:8000/api/Fyers/Strategy/Active`;
        axios.get(url)
        .then(response => {
            console.log(`LTP stockData ${response["data"]["data"]}`);
            console.log(response["data"]["data"]);
            setStrategyList(response["data"]["data"]);
        })
        .catch(err => {
            console.log(`FyersStatus err ${err}`);
        });
    }
    getCurrentStraddles();
}