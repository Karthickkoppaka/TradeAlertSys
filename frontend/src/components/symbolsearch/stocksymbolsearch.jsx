import React, {useState} from "react";
import axios from "axios";
import StockListDropDown from "./stockListDropDown";
import StockSymbolSearchBox from "./stockSymbolSearchBox";

export default function StockSymbolSearch(props){
    const [stockKey, setStockKey] = useState('');
    const [isSearch, setIsSearch] = useState(false);
    const [stockList, setStockList] = useState([]);

    const stockSearch = (stockSearchKey, inputSearch) => { 
        console.log(`funcation invoked ${stockSearchKey}`);
        if(stockSearchKey!=="" && inputSearch){
            stockDropDownList(stockSearchKey);
        }
        else
        {
            setStockKey("");
        }
    }
    
    const selectedStockHandler = (stockName) => {
        console.log(`selectedStockHandler invoked ${stockName}`);
        setStockKey(stockName);
        props.GetSymbol(stockName);
        setStockList([]);
    }

    function stockDropDownList(inputStock){
        let maxItems = 100;
        axios.get(`http://127.0.0.1:8000/api/Fyers/Stock/StockList?StockKey=${inputStock}`)
        .then(response => {
            console.log(`FyersStatus Success ${response["data"]}`);
            console.log(response);
            console.log(response["data"]["data"]);
            setStockList(response["data"]["data"].slice(0, maxItems));
            setStockKey("");
        })
        .catch(err => {
            console.log(`FyersStatus err ${err}`);
        });
    }

    return(
        <div>
        <div className="stocksymbolsearch">
            <StockSymbolSearchBox stockSearch={stockSearch}/>
            <StockListDropDown stockList={stockList} selectedStockHandler={selectedStockHandler}/>
            {
                stockKey!=null ? <label>{stockKey}</label> : <div></div>
            }
        </div>
        </div>
    );
}