import React from "react";
import Table from "../../common/TableContainer";
import { SelectColumnFilter } from "../../common/Filter";
import {BsXCircleFill} from "react-icons/bs";

export default function StockSymbolDataDisplay(props){

    const datacolumns = [
        {
            Header: "Symbol",
            accessor: "Symbol",
            id: "Symbol",
        },
        {
            Header: "LTP",
            accessor: "Close",
            id: "LTP",
        },  
        {
            Header: "Day High",
            accessor: "High",
            id: "High",
        },
        {
            Header: "Day Low",
            accessor: "Low",
            id: "Low",
        },  
        {
            Header: "Delete",
            accessor: "Symbol",
            id: "Delete",
            disableFilters: true,
            Cell: ({ cell: { value } }) => <div onClick={()=>{props.DeleteSymbol(value);}}><BsXCircleFill/></div>,
        },
    ];

    const UpdateList = (index) => {
        console.log('UpdateList');
        console.log(index);
        props.DeleteSymbol(index);
        console.log(props.stockData);
    };

    console.log('List Display');
    console.log(props.stockData);
    
    return(
        <div>
             <h1>
            <center>Stock Data</center>
            </h1>
            <Table columns={datacolumns} data={props.stockData} />
        </div>
    );
}

