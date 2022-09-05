import React from "react";

export default function StockListDropDown(props){
    
    return(
    <div className="searchResults">
        {props.stockList!=null ?
            <ul>
            {
                props.stockList.map(
                    (stock) => {
                        return(
                            <li key={stock.index}>
                                <label onClick={() => props.selectedStockHandler(stock.SymbolTicker)}>{stock.SymbolDetails}</label>
                            </li>
                        )
                    }
                )
            }   
            </ul> 
            : <div/>           
        }
    </div>);
}