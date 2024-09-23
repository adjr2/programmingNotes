// import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
function ref() {
  root.render(<App color="green" size="20ps" />);
}
// root.render(
//   // <React.StrictMode>
//   <App />
//   // </React.StrictMode>
// );
setInterval(ref, 1000);

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
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
