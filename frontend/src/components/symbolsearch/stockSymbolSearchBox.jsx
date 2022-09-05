import React, {useState, useEffect} from "react";
import {BiSearchAlt2} from "react-icons/bi";

export default function StockSymbolSearchBox({stockSearch}){
    const [searchKey, setSearchKey] = useState("");
    const [isSearch, setIsSearch] = useState(false);

    function handleClick(searchValue){
        console.log(`Function call ${searchValue}`)
        stockSearch(searchKey, true);
    }

    return(
    <div className="searchBox">
        <label>Search Stock Symbol</label>
        <input type="text" value={searchKey} placeholder="Enter Stock Symbol" onChange={(event) => {setSearchKey(event.target.value)}}/>
        <button className="searchButton" onClick={() => handleClick(searchKey)}>
            <BiSearchAlt2 />
        </button>
    </div>
    );
}