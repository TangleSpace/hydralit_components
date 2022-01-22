import {Streamlit} from "streamlit-component-lib"
import React, {useState} from "react"
import { useStreamlit } from "streamlit-component-lib-react-hooks"
import NavItem from "./NavItem.jsx"
import NavSubItem from "./NavSubItem.jsx"
import "./bootstrap.min.css"
import './custom.css'


const NavBar:React.VFC = () => {
  const renderData = useStreamlit();

  const [expand_state, setExpandState] = useState(false);
  const [selected_submenu, setSelectedMenuState] = useState('');
  const [expand_submenu, setSubMenuState] = useState(false);
  const [block_state, setBlockState] = useState("none");

  if (renderData == null) {
    return null
  }

  let menu_items = renderData.args["menu_definition"];
  const using_home = renderData.args['home'];
  const use_animation = renderData.args['use_animation'];
  const using_secure = renderData.args['login'];
  let first_select = renderData.args["first_select"];
  const override_theme = renderData.args["override_theme"];
  const comp_key = renderData.args["key"];
  let force_value = renderData.args["fvalue"];
  let sttheme = renderData.theme;

  const check_forced = () => {
    if(force_value){
      Streamlit.setComponentValue(force_value);
    }

    return (null);
  }

  const delayed_resize = (wait_time: number) => setTimeout(() => {
    Streamlit.setFrameHeight();
  }, wait_time);


  interface MenuItem {
    icon: string
    id: string
    label: string
    ttip: string
    submenu: []
  }

  const addHomeLogin = () => {
    if(using_home) {
      let label = "";
      let icon ="";
      let hlabel ="";
      

      if(using_home.label){
          hlabel = using_home.label;
      }

      if(containsEmojis(using_home.icon)) {

        label = using_home.icon + " " + hlabel;
      } else {
        icon = using_home.icon;
        label = " " + hlabel;
      }

      menu_items = [{id: using_home.id, label: label, icon: icon, ttip: using_home.ttip},...menu_items];
    }

    if(using_secure) {
      let label = "";
      let icon ="";
      let slabel = "";

      if(using_secure.label){
        slabel = using_secure.label;
      }

      if(containsEmojis(using_secure.icon)) {
        label = using_secure.icon + " " + slabel;
      } else {
        icon = using_secure.icon;
        label = " " + slabel;
      }

      menu_items = [...menu_items,{id: using_secure.id, label: label, icon: icon, ttip: using_secure.ttip}];
    }
  }

  const containsEmojis = (input: string) => {

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

  const create_submenu = (item: MenuItem,kid:number) => {
      return (
        <NavSubItem subitem={item} menu_id={kid} submenu_callback = {toggleSubMenu} parent_id ={item.label} key={kid}/>
      );
  }

  const toggleNav = () => {
    if(expand_state) {
      setExpandState(false);
      setBlockState("none");
    }else {
      setExpandState(true);
      setBlockState("block");
    }
  }

  const toggleSubMenu = (id: any) => {
    if(id === '') {
      setSubMenuState(false);
    }else {
        setSubMenuState(!expand_submenu);
    }

    setSelectedMenuState(id);  
    Streamlit.setFrameHeight();
    delayed_resize(250);
  }

  const create_menu = (item: MenuItem,kid:number, issub:boolean) => {
    let label = "";
    let icon ="";

    if(containsEmojis(item.icon)) {
      label = item.icon + " " + item.label;
    } else {
      icon = item.icon;
      label = " " + item.label;
    }

    if(Array.isArray(item.submenu)) {
      if(kid === first_select){
        return (
          <li className="nav-item py-0 dropdown active" key={kid*100}>
            <a className="nav-link dropdown-toggle"  href={"#_sub"+kid} key={"sub1_"+kid} onClick={()=>toggleSubMenu(item.label)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
            <ul className={(selected_submenu === item.label && expand_submenu)? "dropdown-menu show" : "dropdown-menu"} key={kid*103}>
              {(item.submenu).map((item: MenuItem,index: number)=>create_submenu(item,index))}
            </ul>
          </li>
        );
      }else {
        return (
          <li className="nav-item py-0 dropdown" key={kid*100}>
            <a className="nav-link dropdown-toggle"  href={"#_sub"+kid} key={"sub1_"+kid} onClick={()=>toggleSubMenu(item.label)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
            <ul className={(selected_submenu === item.label && expand_submenu)? "dropdown-menu show" : "dropdown-menu"} key={kid*103}>
              {(item.submenu).map((item: MenuItem,index: number)=>create_submenu(item,index))}
            </ul>
          </li>
        );
      }
    }else {
      return (
        <NavItem menuitem={item} menu_id={kid} isactive={kid === first_select} menu_callback = {toggleSubMenu}/>
      );
    }
  }

  const setTheme = () => {
    let merged_theme = {'menu_background': '#F0F2F6','txc_inactive': '#FFFFFF','txc_active': '#FFFFFF','option_active': '#F63366', 'padding-top': '0rem'};

    if(sttheme) {
      merged_theme.menu_background = sttheme.primaryColor;
      merged_theme.txc_inactive = sttheme.secondaryBackgroundColor;
      merged_theme.txc_active = sttheme.textColor;
      merged_theme.option_active = sttheme.backgroundColor;
    }
    
    if(override_theme){
      merged_theme.menu_background = override_theme.menu_background ?? merged_theme.menu_background;
      merged_theme.txc_inactive = override_theme.txc_inactive ?? merged_theme.txc_inactive;
      merged_theme.txc_active = override_theme.txc_active ?? merged_theme.txc_active;
      merged_theme.option_active = override_theme.option_active ?? merged_theme.option_active;
    }

    return ":root {--menu_background: " + merged_theme.menu_background + ";--txc_inactive: " +merged_theme.txc_inactive + ";--txc_active:" + merged_theme.txc_active + ";--option_active:" + merged_theme.option_active + ";}";

  }

  const complex_nav = () => {
    let menu_look = "complexnavbarSupportedContent";
    let selector = ( <div className="hori-selector">
                      <div className="left"></div>
                      <div className="right"></div>
                    </div>);

    if(use_animation){
      menu_look = "complexnavbarSupportedContent";
      selector = ( <div className="hori-selector">
                        <div className="left"></div>
                        <div className="right"></div>
                      </div>);
    }else{
      menu_look = "navbarSupportedContent";
      selector =(<></>);
    }
    return (    
      <div key={comp_key}>
      <style>
        {setTheme()}
      </style>
      <nav className="navbar navbar-expand-custom navbar-mainbg w-100 py-0 py-md-0">
        <button className="navbar-toggler" type="button" onClick={()=>toggleNav()} aria-expanded={expand_state}>
          <i className="fas fa-bars text-white"></i>
        </button>
        <div className="navbar-collapse" id={menu_look} style={{display: block_state}}>
            <ul className="navbar-nav py-0">
              {selector}
              {addHomeLogin()}
              {menu_items.map((item: MenuItem,index: number)=>create_menu(item,index,false))}
            </ul>
          </div>
          </nav>
    </div>
    );
    
  }

  return complex_nav();

}

export default NavBar