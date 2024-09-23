import React, { useContext, useState } from "react";
import { AppContext } from "../context/AppContext";

const Budget = () => {
  const { budget, expenses, currency } = useContext(AppContext);
  const [newBudget, setNewBudget] = useState(budget);
  const handleBudgetChange = (event) => {
    const inputValue = event.target.value;
    if (inputValue <= 20000) {
      setNewBudget(inputValue);
    } else {
      alert("The value cannot exceed 20000");
    }

    if (inputValue < expenses) {
      alert("You cannot reduce the budget valuee lower than the spending.");
    }
  };
  return (
    <div className="alert alert-secondary">
      <span>Budget: {currency}</span>
      <input
        type="number"
        step="10"
        value={newBudget}
        onChange={handleBudgetChange}
      ></input>
    </div>
  );
};
export default Budget;
