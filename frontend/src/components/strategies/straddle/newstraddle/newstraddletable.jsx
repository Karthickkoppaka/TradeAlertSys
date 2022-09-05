import React, {useState} from "react";
import StockSymbolSearch from "../../../symbolsearch/stocksymbolsearch";
import Table from "../../../common/TableContainer";
import {BiSearchAlt2} from "react-icons/bi";

export default function NewStraddleTable(){
    const [targetStockName, setTargetStockName] = useState();
    const [showTargetSymbolSearch, setTargetSymbolSearch] = useState(false);
    const [ceStockName, setCEStockName] = useState();
    const [showCESymbolSearch, setCESymbolSearch] = useState(false);
    const [peStockName, setPEStockName] = useState();
    const [showPESymbolSearch, setPESymbolSearch] = useState(false);
    const [targetSymbolPrice, setTargetSymbolPrice] = useState();
    const [showTargetSymbolPrice, setShowTargetSymbolPrice] = useState(false);


    const GetTargetSymbol = (stockKey) => {
        if(stockKey != null){
        console.log(`StockLtp ${stockKey}`);
        setTargetStockName(stockKey);
        setTargetSymbolSearch(false);
        }
    }

    const GetCETargetSymbol = (stockKey) => {
        if(stockKey != null){
        console.log(`StockLtp ${stockKey}`);
        setCEStockName(stockKey);
        setCESymbolSearch(false);
        }
    }

    const GetPETargetSymbol = (stockKey) => {
        if(stockKey != null){
        console.log(`StockLtp ${stockKey}`);
        setPEStockName(stockKey);
        setPESymbolSearch(false);
        }
    }

    const datacolumns = [
        {
            Header: "Strategy",
            accessor: "Strategy",
            id: "Strategy",
            disableFilters: true,
        },
        {
            Header: "TargetSymbol",
            accessor: "TargetSymbol",
            id: "TargetSymbol",
            disableFilters: true,
            Cell: ({ cell: { value } }) => !value  ?
                (showTargetSymbolSearch?<StockSymbolSearch GetSymbol={GetTargetSymbol}/>:
                    <div onClick={()=>setTargetSymbolSearch(true)}><BiSearchAlt2/></div>) : 
                value,
        },
        {
            Header: "TriggerPrice",
            accessor: "TriggerPrice",
            id: "TriggerPrice",
            disableFilters: true,
            Cell: ({ cell: { value } }) => <input type="textbox" value={targetSymbolPrice} onChange={(event)=>setTargetSymbolPrice(event.target.value)}></input>,
        },
        {
            Header: "TargetOptionCE",
            accessor: "TargetOptionCE",
            id: "TargetOptionCE",
            disableFilters: true,
            Cell: ({ cell: { value } }) => !value  ?
                (showCESymbolSearch?<StockSymbolSearch GetSymbol={GetCETargetSymbol}/>:
                    <div onClick={()=>setCESymbolSearch(true)}><BiSearchAlt2/></div>) : 
                value,
        },
        {
            Header: "TargetOptionPE",
            accessor: "TargetOptionPE",
            id: "TargetOptionPE",
            disableFilters: true,
            Cell: ({ cell: { value } }) => !value  ?
                (showPESymbolSearch?<StockSymbolSearch GetSymbol={GetPETargetSymbol}/>:
                    <div onClick={()=>setPESymbolSearch(true)}><BiSearchAlt2/></div>) : 
                value,
        },
        {
            Header: "Add",
            id: "Add",
            disableFilters: true,
            Cell: ({ cell: { value } }) => <button onClick={()=> onAddClick()}>Add</button>,
        },
    ]

    let coldata = [
        {
            "index": 0,
            "Id": 0,
            "Strategy": "Straddle",
            "TargetSymbol": targetStockName,
            "EnquieTimeStamp": 1662321624668,
            "TriggerPrice": 15000,
            "CurrentPrice": 536.7,
            "QueueStatus": "Pending",
            "TargetOptionCE": ceStockName,
            "TargetOptionPE": peStockName
        }
    ]

    const onClickHandler = () =>{
        console.log('onClickHandler called');
        var table = document.getElementById("tableID");
        if (table) {
        for (var i = 0; i < table.rows.length; i++) {
            table.rows[i].onclick = function() {
            tableText(this);
            };
        }
        }

        function tableText(tableRow) {
            console.log('tableText called');
        var name = tableRow.childNodes[1].innerHTML;
        var age = tableRow.childNodes[3].innerHTML;
        var obj = {'name': name, 'age': age};
        console.log(obj);
        }
    }

    const onAddClick = () => {
        console.log('targetStockName');
        console.log(targetStockName);
        console.log(targetSymbolPrice);
        console.log(ceStockName);
        console.log(peStockName);
    }

    return(
        <div>
            <Table columns={datacolumns} data={coldata} />
        </div>
    );
}