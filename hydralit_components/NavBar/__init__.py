import os
import streamlit as st
import math
import streamlit.components.v1 as components
from hydralit_components import IS_RELEASE

STICKY_NAV_STYLE = """
                    <style>
                    div[data-stale="false"] > iframe[title="hydralit_components.NavBar.nav_bar"] {
                        position: fixed;
                        width: 100%;
                        z-index: 99;
                        box-sizing: border-box;
                        top: 0;
                    }

                    div[data-testid="stToolbar"] {
                    display: none;
                    position: none;
                    }

                    div[data-testid="stDecoration"] {
                    display: none;
                    position: none;
                    }

                    div[data-testid="stStatusWidget"] {
                    display: none;
                    position: none;
                    }

                    #MainMenu {
                    display: none;
                    }
                    header {
                    display: none;
                    }
                    </style>
                """

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("nav_bar", path=build_path)
else:
    _component_func = components.declare_component("nav_bar", url="http://localhost:3000")


def nav_bar(menu_definition, first_select=0, key=None,home_name=None,login_name=None,override_theme=None, sticky_nav=True,force_value=None,use_animation=True):
    if sticky_nav:
        st.markdown(STICKY_NAV_STYLE,unsafe_allow_html=True)

    first_select = math.floor(first_select/10)
    component_value = _component_func(menu_definition=menu_definition, first_select=first_select,key=key,home=home_name,fvalue=force_value,login=login_name,override_theme=override_theme,use_animation=use_animation)


    if component_value is None:
        if first_select > len(menu_definition):
            if login_name is not None:
                return login_name
            else:
                return menu_definition[-1]['label']

        if home_name is None:
            return menu_definition[first_select]['label']
        else:
            if first_select == 0:
                return home_name
            else:
                return menu_definition[(first_select-1)]['label']
    else:
        return component_value

