import React from "react";
import Navbar from "../../common/navbar";
import { stockdataoptions } from "./stockdataoptions";

export default function StockDataNavBar(){
    return(
        <div>
            <Navbar menuItems={stockdataoptions}/>
        </div>
    );
}