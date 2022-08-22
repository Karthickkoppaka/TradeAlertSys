import React from "react";
import {Link} from "react-router-dom";

export default function Links({links}){
    return (
        <ul>
            {
                links.map(
                    (link) => {
                        return (
                            <li className={link.active ? "active" : ""}>
                                <Link to={link.to}> 
                                    <link.icon/>
                                    {link.text}
                                </Link>
                            </li>
                        )
                })
            }
        </ul>
    );
}