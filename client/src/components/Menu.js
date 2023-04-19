import React from 'react'
import MenuList from './MenuList'

function Menu({menuItems}) {

    return (
        <div>
            <h1>Menu</h1>
            <MenuList menuItems={menuItems}/>
        </div>
    );
}

export default Menu;