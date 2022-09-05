import React from "react";

const Dropdown = ({ label, value, options, onChange }) => {
    return (
      <label className="commonDropdown">
        {label}
        <select value={value} onChange={onChange}>
        <option value="" key="" disabled selected>Select your option</option>
          {options.map((option) => (
            <option key={option.value} value={option.value}>{option.label}</option>
          ))}
        </select>
      </label>
    );
  };

  export default Dropdown;