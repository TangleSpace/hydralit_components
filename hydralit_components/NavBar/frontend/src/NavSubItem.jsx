import {Streamlit} from "streamlit-component-lib"
import React from "react"
import "./bootstrap.min.css"

const NavSubItem = (props) => {
  let menu_subitem = props.subitem;
  let menu_id = props.menuid;
  let parent_id = props.parent_id;
  const parent_toggle = props.submenu_callback;

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

  const onSelect = (id, parent_id) => {
    parent_toggle(parent_id);
    Streamlit.setComponentValue(id);
  }

  const create_submenuitem = (item, kid,parent_id) => {
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

      return (
        <li key={parent_id+kid*97}>
        <a className="dropdown-item" href={"#" + kid*97} onClick={()=>onSelect(ret_id,parent_id)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
        </li>
      );
  }
  
  return create_submenuitem(menu_subitem,menu_id,parent_id);

}

export default NavSubItem