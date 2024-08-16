import React from 'react';

const Header: React.FC = () => {
    return (
        <header className="header">
            <h1>Be Kind</h1>
            <nav>
                <ul>
                    <li><a href="#gratitude">Gratitude</a></li>
                    <li><a href="#kindness">Acts of Kindness</a></li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;