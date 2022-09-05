import React, {useState, useEffect} from "react";
import StockSymbolSearch from "../../symbolsearch/stocksymbolsearch";
import StockSymbolDataDisplay from "./stockltpListDisplay";
import {StockLtpGetData} from "./stockltpGetData";

export default function StockLtp(props){
    const [stockName, setStockName] = useState(props.stockName);
    const [stockList, setStockList] = useState([]);
    const [stockData, setStockData] = useState([]);
    const [showSearch, setShowSearch] = useState(false);

    const GetSymbol = (stockKey) => {
        if(stockKey != null){
        console.log(`StockLtp ${stockKey}`);
        setStockName(stockKey);
        setStockList([...stockList, stockKey]);
        setShowSearch(false);
        }
    }

    const DeleteSymbol = (stockKey) => {
        if(stockKey != null){
            const index = stockList.indexOf(stockKey);
            if (index > -1) { 
                stockList.splice(index, 1); 
            }
            setStockList(stockList);
        }
    }

    useEffect(()=> {
        if(stockList!=null && stockList.length > 0){
            StockLtpGetData(stockList, setStockData);
        }
        else
        {
            setStockData([]);
        }
        const intervalId = setInterval(() => {
            if(stockList!=null){
             StockLtpGetData(stockList, setStockData);
            }
          }, 10000);
        return () => {
            clearInterval(intervalId);
        };
    },[stockList]);

    useEffect(
        ()=>{console.log('stockData main list');console.log(stockData);}
    ,[stockData]);

    return(<div>
            <div className="StockLtpOptions">
                <button onClick={()=> {setShowSearch(true)}}>Add</button>
                <button onClick={()=> {setShowSearch(true)}}>Delete</button>
                <button onClick={()=> {setShowSearch(true)}}>Modify</button>
            </div>
            {showSearch ? <StockSymbolSearch GetSymbol={GetSymbol}/> : <div/>}
            {stockName != null ? <h3>{stockName}</h3> : <div/>}
            {stockData !=null && stockData.length > 0 ? <StockSymbolDataDisplay stockData={stockData} DeleteSymbol={DeleteSymbol}/> : <div/>}
    </div>);
}

