import { useState } from "react";
import {React} from "react";
import FyersStatus from "./fyersstatus";
import RefreshStockSymbols from "./refreshstocksymbols";

export default function Dashboard(){
    const [stockState, setStockState] = useState(false);

    const handleLoginState = stockStateInput => {
        if(stockStateInput && !stockState){
            // axios.get('http://127.0.0.1:8000/api/Fyers/Stock/StockListRefresh')
            // .catch(err => {
            //     console.log(err);
            //     setStockState(false);
            // });
            // setStockState(true);
            // console.log("Stock method called");
        }
    }

    return (<div>
        <h1>Dashboard</h1>
        <FyersStatus handleLoginState={handleLoginState}/>
        <RefreshStockSymbols stockState={stockState}/>
    </div>);
}