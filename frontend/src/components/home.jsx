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
import StraddleHome from "./strategies/straddle/straddlehome";
import NewStraddleHome from "./strategies/straddle/newstraddle/newstraddlehome";
import StockLtp from "./stockdata/priceinfo/stockltp";

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
                {/* strategies */}
                <Route path="/strategies" element={<Strategies />}/>
                <Route path="/strategies/Straddle" element={<StraddleHome />}/>
                <Route path="/strategies/Straddle/new" element={<NewStraddleHome />}/>
                {/* stockdata */}
                <Route path="/stockdata" element={<StockData />}/>
                <Route path="/stockdata/ltp" element={<StockLtp />}/>
            </Routes>
            </div>
        </Router>
    );
}