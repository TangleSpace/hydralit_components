import {ComponentProps,Streamlit,withStreamlitConnection,} from "streamlit-component-lib"
import React, {useEffect,useState} from "react"
import NavItem from "./NavItem.jsx"
import NavSubItem from "./NavSubItem.jsx"
import "./bootstrap.min.css"
import './custom.css'


const NavBar = (props: ComponentProps) => {
  let menu_items = props.args["menu_definition"];
  const using_home = props.args['home'];
  const using_secure = props.args['login'];
  let first_select = props.args["first_select"];
  const override_theme = props.args["override_theme"];
  let sttheme = props.theme;
  let refresh_size = false;

  const [expand_state, setExpandState] = useState(false);
  const [selected_submenu, setSelectedMenuState] = useState('');
  const [expand_submenu, setSubMenuState] = useState(false);
  const [block_state, setBlockState] = useState("none");

  useEffect(() => {Streamlit.setFrameHeight();});

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
      menu_items = [{id: using_home, label: null, icon: "fa fa-home", ttip: using_home},...menu_items];
    }

    if(using_secure) {
      menu_items = [...menu_items,{id: using_secure, label: null, icon: "fa fa-user-circle", ttip: using_secure}];
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
        <NavSubItem subitem={item} menu_id={kid} submenu_callback = {toggleSubMenu} parent_id ={item.label}/>
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
      if(selected_submenu === id) {
        setSubMenuState(!expand_submenu);
      } else {
        setSubMenuState(true);
      }
    }

    setSelectedMenuState(id);  
    delayed_resize(1300);
    delayed_resize(2500);
  }

  const create_menu = (item: MenuItem,kid:number, issub:boolean) => {
    let label = "";
    let icon ="";

    if(containsEmojis(item.icon)) {
      label = item.icon + " " + item.label;
    } else {
      icon = item.icon;
      label = item.label;
    }

    if(Array.isArray(item.submenu)) {
      if(kid === first_select){
        return (
          <li className="nav-item dropdown active" key={kid*100}>
            <a className="nav-link dropdown-toggle"  href={"#_sub"+kid} key={"sub1_"+kid} onClick={()=>toggleSubMenu(item.label)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
            <ul className={(selected_submenu === item.label && expand_submenu)? "dropdown-menu show" : "dropdown-menu"} >
              {(item.submenu).map((item: MenuItem,index: number)=>create_submenu(item,index))}
            </ul>
          </li>
        );
      }else {
        return (
          <li className="nav-item dropdown" key={kid*100}>
            <a className="nav-link dropdown-toggle"  href={"#_sub"+kid} key={"sub1_"+kid} onClick={()=>toggleSubMenu(item.label)} data-toggle="tooltip" data-placement="top" data-html="true" title={item.ttip}><i className={icon}></i>{label}</a>
            <ul className={(selected_submenu === item.label && expand_submenu)? "dropdown-menu show" : "dropdown-menu"} >
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
    let merged_theme = {'menu_background': '#F0F2F6','txc_inactive': '#FFFFFF','txc_active': '#FFFFFF','option_active': '#F63366'};

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
    return (    
      <div>
      <style>
        {setTheme()}
      </style>
      <nav className="navbar navbar-expand-custom navbar-mainbg w-100">
        <button className="navbar-toggler" type="button" onClick={()=>toggleNav()} aria-expanded={expand_state}>
          <i className="fas fa-bars text-white"></i>
        </button>
        <div className="navbar-collapse" id="complexnavbarSupportedContent" style={{display: block_state}}>
            <ul className="navbar-nav">
              <div className="hori-selector">
                <div className="left"></div>
                <div className="right"></div>
              </div>
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

export default withStreamlitConnection(NavBar)