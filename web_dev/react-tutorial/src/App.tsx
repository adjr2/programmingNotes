import useDragger from "./hooks/userDragger";
import "./App.css";

function App() {
  useDragger("rose-box");
  return (
    <main>
      <div className="container">
        <div id="rose-box" className="box"></div>
      </div>
    </main>
  );
}

export default App;
