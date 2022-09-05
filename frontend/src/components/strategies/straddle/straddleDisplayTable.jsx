import React from "react";
import Table from "../../common/TableContainer";

export default function StraddleDisplayTable(props){
    const datacolumns = [
        {
            Header: "Strategy",
            accessor: "Strategy",
            id: "Strategy",
        },
        {
            Header: "TargetSymbol",
            accessor: "TargetSymbol",
            id: "TargetSymbol",
        },
        {
            Header: "TriggerPrice",
            accessor: "TriggerPrice",
            id: "TriggerPrice",
        },
        {
            Header: "CurrentPrice",
            accessor: "CurrentPrice",
            id: "CurrentPrice",
        },
        {
            Header: "QueueStatus",
            accessor: "QueueStatus",
            id: "QueueStatus",
        },
        {
            Header: "TargetOptionCE",
            accessor: "TargetOptionCE",
            id: "TargetOptionCE",
        },
        {
            Header: "TargetOptionPE",
            accessor: "TargetOptionPE",
            id: "TargetOptionPE",
        },
    ]

    return(
        <div>
            <h1>
            <center>Current Straddles</center>
            </h1>
            <Table columns={datacolumns} data={props.strategyList} />
        </div>
    );
}