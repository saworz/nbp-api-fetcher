import './MainPageView.css';
import React, { useState, useEffect } from 'react';
import SelectCurrencyWindow from "../SelectCurrencyWindow";
import SaveButton from "../SaveButton";
import PreviewButton from "../PreviewButton";

const MainPageView = () => {

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow />

      <div className="buttons-field">
        <div className="single-button">
          <PreviewButton />
        </div>
        <div className="single-button">
          <SaveButton />
        </div>
      </div>
    </div>
  );
};

export default MainPageView;