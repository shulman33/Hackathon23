import React from "react";
import { Link } from "react-router-dom";

export default function WelcomePage() {
 return (
   <div className="WelcomePage">
     <h1> Welcome to FinConnects! FinConnects is an accessible financial service for all people. </h1>
     <Link to="SignUp">
       <h2>Sign Up</h2>
     </Link>
     <Link to="SignIn">
       <h2>Log In</h2>
     </Link>
     <h2> Based on your location, it seems you live in Washington Heights. Here is a list of providers near you. </h2>
     <p> GAQ Consulting </p>
     <p> Making Money Movers </p>
     <p> OG Tax and Accounting Group </p>
     <p> TD Bank </p>
 </div>
 );
}
