import React from "react";
import StockSymbolSearch from "../symbolsearch/stocksymbolsearch";
import StockDataNavBar from "./stockoperations/stockdataNavBar";

export default function StockDataHome(){
    return(
        <div>
            <StockDataNavBar/>
            <StockSymbolSearch/>
        </div>
    );
}