import {Streamlit} from "streamlit-component-lib"
import React from "react"
import "./bootstrap.min.css"

const NavItem = (props) => {
  let menu_item = props.menuitem;
  let is_active = props.isactive;
  let menu_id = props.menu_id;
  const parent_toggle = props.menu_callback;

  const containsEmojis = (input) => {

    if (input) {
      for (var c of input) {
          var cHex = ("" + c).codePointAt(0);
          if(cHex) {
          var sHex = cHex.toString(16);
          var lHex = sHex.length;
            if (lHex > 3) {

                var prefix = sHex.substring(0, 2);

                if (lHex === 5 && prefix === "1f") {
                    return true;
                }

                if (lHex === 4) {
                    if (["20", "21", "23", "24", "25", "26", "27", "2B", "29", "30", "32"].indexOf(prefix) > -1)
                        return true;
                }
            }
        }
      }
    }

    return false;
  }

  const onSelect = (id) => {
    parent_toggle('');
    Streamlit.setComponentValue(id);
  }

  const create_item = (item,kid, is_active) => {
      let ret_id = "";
      let label = "";
      let icon ="";
  
      if(item.id) {
        ret_id = item.id;
      }else {
        ret_id = item.label;
      }
  
      if(containsEmojis(item.icon)) {
        label = item.icon + " " + item.label;
      } else {
        icon = item.icon;
        label = item.label;
      }

      if(is_active) {
        return (
          <li className="nav-item active" key={kid}>
            <a className="nav-link" href={"#" + kid} onClick={()=>onSelect(ret_id)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
          </li>
        );
      } else {
        return (
          <li className="nav-item" key={kid}>
            <a className="nav-link" href={"#" + kid} onClick={()=>onSelect(ret_id)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
          </li>
        );
      }
  }
  
  return create_item(menu_item,menu_id,is_active);

}

export default NavItem