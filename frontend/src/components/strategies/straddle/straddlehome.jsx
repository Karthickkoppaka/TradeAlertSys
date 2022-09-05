import React, {useState, useEffect} from "react";
import StraddleOptions from "./straddleoptions";
import StraddleDisplayTable from "./straddleDisplayTable";
import { GetCurrentStraddle } from "./straddleCurrentStrategies";

export default function StraddleHome(){
    const [strategyList, setStrategyList] = useState([]);

    useEffect(
        () => {
            GetCurrentStraddle(setStrategyList);
        }
    ,[]);

    return(
        <div>
            <h1>Straddle</h1>
            <StraddleOptions/>
            {/* Get Current Strategies */}
            {strategyList !=null && strategyList.length > 0 ? <StraddleDisplayTable strategyList={strategyList}/> : <div/>}
        </div>
    );
}