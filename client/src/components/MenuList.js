import React from 'react'
import MenuCard from './MenuCard'

function MenuList({menuItems}) {
    return (
        <div>
            {menuItems.map(menuItem => <MenuCard key={menuItem.id} menuItem={menuItem}/> )}
        </div>
    )
}

export default MenuList