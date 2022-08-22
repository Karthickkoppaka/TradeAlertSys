import React from "react";
import {BsFillCaretRightSquareFill, BsFillInboxFill, BsFillHouseDoorFill} from "react-icons/bs";    
import Links from "./links";

export default function SideBar(){
    const links = [
        {
            text: "Dashboard",
            icon: BsFillHouseDoorFill,
            to: "/",
            active: true
        },
        {
            text: "StockData",
            icon: BsFillCaretRightSquareFill,
            to: "/StockData",
        },
        {
            text: "Strategies",
            icon: BsFillInboxFill,
            to: "/Strategies",
        },
        {
            text: "Orders",
            icon: BsFillCaretRightSquareFill,
            to : "/Orders"
        },
    ];
    return (<div className="sidebar">
        <h2>Trade Alert System</h2>
        <div className="links">
            <Links links={links}/>
        </div>
    </div>);
}