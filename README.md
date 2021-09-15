# **Hydralit Components** <img src="https://github.com/TangleSpace/hydralit/raw/main/docs/images/hydra.png" alt="hydra" width="50"/>
A package of Streamlit components that can be used directly or with the [Hydralit](https://github.com/TangleSpace/hydralit) library.

## **Current Components**
### **Hydralit Navbar** <img src="https://github.com/TangleSpace/hydralit_components/raw/main/resources/hydra_nav.png" alt="burger" width="30"/>
The Hydralit Navbar is a Streamlit component to make a good looking responsive menu for your Streamlit applications that may or may not be using [Hydralit](https://github.com/TangleSpace/hydralit).

<br>
<p align="center">
	<a href="https://pepy.tech/project/hydralit_components/" alt="PyPI downloads">
	<img src="https://pepy.tech/badge/hydralit_components" />
	</a>
    <a href="https://www.python.org/" alt="Python version">
        <img src="https://img.shields.io/pypi/pyversions/hydralit_components" /></a>
    <a href="https://pypi.org/project/hydralit_components/" alt="PyPI version">
        <img src="https://img.shields.io/pypi/v/hydralit_components" /></a>
    <a href="https://hydralit_components.aur-license.org/" alt="License">
        <img src="http://img.shields.io/:license-Apache-blue.svg?style=flat-square"></a>
    <a href="https://streamlit.io/" alt="Streamlit">
        <img src="http://img.shields.io/:streamlit->=0.67.0-blue.svg?style=flat-square"></a>
</p>

## Installing Hydralit Components
Hydralit can be installed from PyPI:

```bash
pip install hydralit_components
```
# New in version 1.0.3
 - Enable sticky menu mode (pin to top of the window)
 - Animated dropdown menu entries to support complex navigation
 - Offline support
 - Added support for fontawesome icons
 - Full collapse in mobile view (the burger is back!)

# Features
 - Full theme color support
 - Full container support (can put on sidebar too)
 - Responsive layout
 - Use Bootstrap icons or emojis or nothing
 - Configure Response values when clicked
 - Assign tooltips
<p align="center">
<img src="https://raw.githubusercontent.com/tanglespace/hydralit_components/master/resources/hydralit_navbar.gif" title="Quick Example" alt="Quick Example", width="100%" height="100%">

### Example
A very quick example of how to modify the menu items and to show we can put it on the main page, sidebar or within a container, up to you.
```python
import streamlit as st
import hydralit_components as hc

if __name__ =="__main__":

    st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

    # specify the menu definition we'll stick in the sidebar
    side_menu_data = [
        {'icon': "far fa-copy", 'label':"Left End",'ttip':"I'm the Left End tooltip!"}, #can specify an icon from the bootstrap icon library
        {'icon': "far fa-copy", 'label':"Copy"},
        {'label':"Chart"}, # the minimum we can specify for a menu item
        {'id':'special return value here','icon': "far fa-address-book", 'label':"Book"}, #can provide a special id to return when clicked
        {'icon': "far fa-calendar-alt", 'label':"Calendar"}, #or can let the label be the return value when clicked
        {'icon':"🐙",'label':"Component",'ttip':"I'm the Component tooltip!"}, # can als use an emoji as the icon
        {'icon': "fas fa-tachometer-alt", 'label':"Dashboard"},
        {'label':"Da55shboard"}, # or no icon
        {'icon':'🤵','label':"Right End"},
    ]

    # specify the primary menu definition
    menu_data = [
        {'icon': "far fa-copy", 'label':"Left End"},
        {'id':'Copy','icon':"🐙",'label':"Copy"},
        {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
        {'icon': "far fa-address-book", 'label':"Book"},
        {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
        {'icon': "far fa-clone", 'label':"Component"},
        {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "far fa-copy", 'label':"Right End"},
    ]

    # we can override any part of the primary colors of the menu
    #over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
    over_theme = {'txc_inactive': '#FFFFFF'}
    menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

    with st.sidebar:
        side_menu_id = hc.nav_bar(menu_definition=side_menu_data,key='sidetbar',login_name='Login',override_theme=over_theme,first_select=6)
    
    #get the id of the menu item clicked
    st.info(f"{menu_id=}")
    st.info(f"{side_menu_id=}")
```

New features such as sitcky navbar and complex nav (dropdown menu items) are easy to use.
<p align="center">
<img src="https://raw.githubusercontent.com/tanglespace/hydralit_components/master/resources/hydralit_navbar_new.gif" title="New Features" alt="Quick Example", width="100%" height="100%">

```python

menu_data = [
    {'icon': "far fa-copy", 'label':"Left End"},
    {'id':'Copy','icon':"🐙",'label':"Copy"},

    # dropdown menu items are specified with a 'submenu' key and an array of menu entries
    {'icon': "fa-solid fa-radar",'label':"Dropdown1", 
        'submenu':[
                {'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1",'ttip':"I'm a sub-menu tooltip!"},
                {'id':'subid12','icon': "💀", 'label':"Sub-item 2"},
                {'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}
            ]
    },
    {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
    {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Right End"},

    # dropdown menu items support all the existing configuration items such as i return value, label, icon, tool tips
    {'icon': "fa-solid fa-radar",'label':"Dropdown2", 
        'submenu':[
                {'label':"Sub-item 1", 'icon': "fa fa-meh"},
                {'label':"Sub-item 2"},
                {'icon':'🙉','label':"Sub-item 3",}
            ]
    },
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(menu_definition=menu_data,override_theme=over_theme,home_name='Home',login_name='Logout',sticky_nav=True)

```

