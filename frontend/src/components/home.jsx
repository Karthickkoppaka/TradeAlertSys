import React from "react";
import {BrowserRouter as Router,
    Routes,
    Route} from "react-router-dom";
import Dashboard from "./dashboard";
import Orders from "./orders";
import StockData from "./stockdata";
import Strategies from "./strategies";
import SideBar from "./sidebar";
import PostLogin from "./postlogin";

export default function Home(){
    return(
        <Router>
            <SideBar/>
            <div className="home">
            <Routes>
                {/* <Route exact path="/:status?" element={<Dashboard />}/> */}
                <Route path="/" element={<Dashboard />}/>
                <Route path="/postlogin" element={<PostLogin />}/>
                <Route path="/orders" element={<Orders />}/>
                <Route path="/stockdata" element={<StockData />}/>
                <Route path="/strategies" element={<Strategies />}/>
            </Routes>
            </div>
        </Router>
    );
}