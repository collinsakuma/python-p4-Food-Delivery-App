import React from 'react';
import { NavLink } from "react-router-dom";

function Navbar({ handleLogout }) {
    return (
        <div className='navbar'>
            <NavLink exact to='/' className='navbar btn'>Home</NavLink>
            <NavLink to='/neworder' className='navbar btn'>New Order</NavLink>
            <NavLink to='/menu' className='navbar btn'>Menu</NavLink>
            <NavLink to='/profile' className='navbar btn'>Profile</NavLink>
            <button onClick={handleLogout}>Logout</button>
        </div>
    )
}

export default Navbar;
