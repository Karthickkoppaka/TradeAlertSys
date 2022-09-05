import {React, useState, useEffect} from "react";
import axios from "axios";
import {BsArrowClockwise} from "react-icons/bs";
import { FiCheckCircle} from "react-icons/fi";

export default function RefreshStockSymbols({stockState}) {
    const [refreshState, setRefreshState] = useState(false);
    const [lastUpdate, setLastUpdate] = useState();

    console.log("RefreshStockSymbols");
    console.log(stockState);

    return(
        <div className="refreshstocksymbol">
            <label>Stock Symbol Refresh</label>
            <label>{lastUpdate!=undefined?lastUpdate:""}</label>
            {!stockState?<BsArrowClockwise className="inactive"/>:<FiCheckCircle/>}
        </div>
    );
}