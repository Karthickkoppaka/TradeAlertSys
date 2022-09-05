import React, {useState, useEffect} from "react";
import axios from "axios";

export const StockLtpGetData = (stockList, setStockData) => {
    function getLtp(inputStock){
        console.log('ltp called');
        let maxItems = 100;
        const today = new Date();
        const pastDate = new Date(today);
        pastDate.setDate(pastDate.getDate() - 5);
        let fromDate=new Date(pastDate.toLocaleString("en-Us", {timeZone: 'Asia/Kolkata'})).toLocaleDateString("en-CA"), toDate=new Date(new Date().toLocaleString("en-Us", {timeZone: 'Asia/Kolkata'})).toLocaleDateString("en-CA");
        let url = `http://127.0.0.1:8000/api/Fyers/StockData/List/Ltp?StockSymbolList=${inputStock}&FromDate=${fromDate}&ToDate=${toDate}`;
        axios.get(url)
        .then(response => {
            console.log(`LTP stockData ${response["data"]["data"]}`);
            console.log(response["data"]["data"]);
            setStockData(response["data"]["data"]);
        })
        .catch(err => {
            console.log(`FyersStatus err ${err}`);
        });
    }
    if(stockList!=null){
        console.log(`ltp get data inside ${stockList}`);
        getLtp(stockList);
    }
};
