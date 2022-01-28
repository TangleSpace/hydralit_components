import {Streamlit} from "streamlit-component-lib"
import React, {useState} from "react"
import { useStreamlit } from "streamlit-component-lib-react-hooks"
import "./bootstrap.min.css"
import './custom.css'

const InfoCard:React.VFC = () => {
  const renderData = useStreamlit();

  if (renderData == null) {
    return null
  }

  let title = renderData.args["title"];
  let contents = renderData.args['content'];
  let bar_value = renderData.args['bar_value'];
  const comp_key = renderData.args["key"];
  let sttheme = renderData.theme;
  const override_theme = renderData.args['theme_override'];
  let icon = "fa fa-info-circle";
  
  const setTheme = () => {
    let merged_theme = {'border_color':'#F0F2F6','bgcolor': '#F0F2F6','content_color': '#FFFFFF','progress_color': '#F63366','title_color':'#FFFFFF','icon_color':'#F63366'};

    if(sttheme) {
      merged_theme.bgcolor = sttheme.secondaryBackgroundColor;
      merged_theme.border_color = sttheme.secondaryBackgroundColor;
      merged_theme.content_color = sttheme.textColor;
      merged_theme.progress_color = sttheme.primaryColor;
      merged_theme.title_color = sttheme.textColor;
      merged_theme.icon_color = sttheme.primaryColor;
    }
    
    if(override_theme){
      merged_theme.bgcolor = override_theme.bgcolor ?? merged_theme.bgcolor;
      merged_theme.border_color = override_theme.border_color ?? merged_theme.border_color;
      merged_theme.content_color = override_theme.content_color ?? merged_theme.content_color;
      merged_theme.progress_color = override_theme.progress_color ?? merged_theme.progress_color;
      merged_theme.title_color = override_theme.title_color ?? merged_theme.title_color;
      merged_theme.icon_color = override_theme.icon_color ?? merged_theme.icon_color;
      icon = override_theme.icon;
    }

    // if (override_theme) {
    //   icon = override_theme.icon;
    // }
    
    return ":root {--bgcolor: " + merged_theme.bgcolor + 
    ";--content-color: " + merged_theme.content_color + 
    ";--border-color: " + merged_theme.border_color + 
    ";--progress-color: " + merged_theme.progress_color + 
    ";--progress-value: " + bar_value + "%" + 
    ";--title-color:" + merged_theme.title_color
    + ";--icon-color:" + merged_theme.icon_color + ";}";
  }

  const ProgressBar = () => {
    if (bar_value) {
      return (        
        <div className="w3-light-grey">
            <div className="progressbar"></div>
        </div>);
    }
  }

  const info_card= () => {
    return (
      <div key={comp_key} className="card">
      <style>
        {setTheme()}
      </style>
      <table className="table-format">
        <thead>
          <tr>
            <th style={{width: "80%"}} className="header-row card-title">
              <p className="title-style">{title}</p>
            </th>
            <th style={{width: "20%"}} className="header-row info-icon">    
              <i className={icon}></i>
            </th>
          </tr>
        </thead>
      </table>
      <p className='content-row card-content'>{contents}</p>
      {ProgressBar()}
    </div>
    );
  }

  return info_card();

}

export default InfoCard