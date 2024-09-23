// import logo from "./logo.svg";
import "./App.css";
// import React, { useState } from "react";
import axios from "axios";
import React, { useState, useEffect } from "react";

// function App() {
//   const currDate = new Date();
//   return (
//     // <div className="App">
//     //   <header className="App-header">
//     //     <img src={logo} className="App-logo" alt="logo" />
//     //     <p>
//     //       Edit <code>src/App.js</code> and save to reload.
//     //     </p>
//     //     <a
//     //       className="App-link"
//     //       href="https://reactjs.org"
//     //       target="_blank"
//     //       rel="noopener noreferrer"
//     //     >
//     //       Learn React
//     //     </a>
//     //   </header>
//     // </div>
//     <div>
//       <h1>Hello World</h1>
//       <h2>The time now is {currDate.toLocaleTimeString()}.</h2>
//     </div>
//   );
// }

// const App = (props) => {
//   const [counter, setCounter] = useState(0);

//   let incrementCounter = () => {
//     setCounter(counter + 1);
//   };
//   let colorStyle = { color: props["color"], fontSize: props["size"] };
//   return (
//     <div style={colorStyle}>
//       React Component
//       <br />
//       <br />
//       <button onClick={incrementCounter}>Click me</button>
//       <br />
//       <br />
//       {counter}
//     </div>
//   );
// };
// export default App;

const App = (props) => {
  //define the state and the setter
  const [APIlist, setAPIlist] = useState();
  //On load invoke method to genrate list
  useEffect(() => {
    let url = "https://api.publicapis.org/entries?category=Animals";
    axios({
      method: "get",
      url: url,
      responseType: "json",
    })
      .then((resp) => {
        let listOfEntries = resp.data.entries;
        let listOfEntriesAsArray = Object.entries(listOfEntries);
        let i = 1;
        let entryDetails = listOfEntriesAsArray.map((entryDetail) => {
          return (
            <li key={i++}>
              <a href={entryDetail[1]["Link"]} target="_blank" rel="noreferrer">
                {entryDetail[1]["API"]}
              </a>
            </li>
          );
        });
        setAPIlist(entryDetails);
      })
      .catch((err) => {
        console.log(err.toString());
      });
  }, []);
  const colorStyle = { color: props["color"], fontSize: props["size"] };
  return (
    <div>
      <h2>APIs List</h2>
      <br />
      <div style={colorStyle}>
        <ul>{APIlist}</ul>
      </div>
    </div>
  );
};
export default App;
