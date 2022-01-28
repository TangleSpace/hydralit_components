import {Streamlit} from "streamlit-component-lib"
import React, {useState} from "react"
import { useStreamlit } from "streamlit-component-lib-react-hooks"
import "./bootstrap.min.css"
import './custom.css'


const ProgressBar:React.VFC = () => {
  const renderData = useStreamlit();

  if (renderData == null) {
    return null
  }

  let value = renderData.args["value"];
  const content_text = renderData.args['content_text'];
  const override_theme = renderData.args["override_theme"];
  const comp_key = renderData.args["key"];
  let sttheme = renderData.theme;


  const setTheme = () => {
    let merged_theme = {'border_color':'#E0E6EB','bgcolor': '#f1f1f1','content_color': '#FFFFFF','progress_color': '#F63366'};

    if(sttheme) {
      merged_theme.bgcolor = sttheme.secondaryBackgroundColor;
      merged_theme.border_color = sttheme.secondaryBackgroundColor;
      merged_theme.content_color = sttheme.textColor;
      merged_theme.progress_color = sttheme.primaryColor;
    }
    
    if(override_theme){
      merged_theme.bgcolor = override_theme.bgcolor ?? merged_theme.bgcolor;
      merged_theme.border_color = override_theme.border_color ?? merged_theme.border_color;
      merged_theme.content_color = override_theme.content_color ?? merged_theme.content_color;
      merged_theme.progress_color = override_theme.progress_color ?? merged_theme.progress_color;
    }
    
    return ":root {--bgcolor: " + merged_theme.bgcolor + 
    ";--content-color: " + merged_theme.content_color + 
    ";--border-color: " + merged_theme.border_color + 
    ";--progress-color: " + merged_theme.progress_color + 
    ";--progress-value: " + value + "%"  + ";}";
  }

  const progressbar = () => {
      return (      
        <div key={comp_key} className='parent'>
          <style>
            {setTheme()}
          </style>
          <div className="w3-light-grey">
              <div className="progressbar">
                <div className="content">
                {content_text}
                </div>
              </div>
          </div>
        </div>
      );
  }

  return progressbar();

}

export default ProgressBar