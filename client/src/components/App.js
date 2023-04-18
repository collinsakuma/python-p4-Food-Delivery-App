import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Login from "./Login";
import Navbar from "./Navbar";
import Header from "./Header"

function App() {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetch("/check_session")
      .then((r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        }
      });
  }, []);
  
  if (!user) return <Login onLogin={setUser} />;
  
  return (
    <div classname = 'app container'>
    <div className="App">
      <Header />
      <Navbar />
      <h1>This is the start of our App</h1>
      <div>
        <Switch>
          
        </Switch>
      </div>
    </div>
    </div>
  );
}

export default App;
