import React from "react";
import Navbar from "../../common/navbar";
import {strategyoptions} from "../strategyoptions";

export default function StraddleOptions(){

    return(<div>
        <Navbar menuItems={strategyoptions}/>
    </div>);
}