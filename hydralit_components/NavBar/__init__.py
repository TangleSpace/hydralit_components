import os
import streamlit as st
import math
import streamlit.components.v1 as components
from hydralit_components import IS_RELEASE

PINNED_NAV_STYLE = """
                    <style>
                    .reportview-container .sidebar-content {
                        padding-top: 0rem;
                    }
                    .reportview-container .main .block-container {
                        padding-top: 0rem;
                        padding-right: 4rem;
                        padding-left: 4rem;
                        padding-bottom: 4rem;
                    }

                    </style>
                """

STICKY_NAV_STYLE = """
                    <style>
                    div[data-stale="false"] > iframe[title="hydralit_components.NavBar.nav_bar"] {
                        position: fixed;
                        width: 100%;
                        z-index: 99;
                        box-sizing: border-box;
                        top: 0;
                    }
                """

HIDE_ST_STYLE = """
                    <style>
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


def nav_bar(menu_definition, first_select=0, key=None,home_name=None,login_name=None,override_theme=None, sticky_nav=True,force_value=None,use_animation=True,hide_streamlit_markers=True,sticky_mode='pinned'):

    first_select = math.floor(first_select/10)
    component_value = _component_func(menu_definition=menu_definition, first_select=first_select,key=key,home=home_name,fvalue=force_value,login=login_name,override_theme=override_theme,use_animation=use_animation)

    if sticky_nav:
        if sticky_mode == 'pinned':
            st.markdown(PINNED_NAV_STYLE,unsafe_allow_html=True)
        else:
            st.markdown(STICKY_NAV_STYLE,unsafe_allow_html=True)

    if hide_streamlit_markers:
        st.markdown(HIDE_ST_STYLE,unsafe_allow_html=True)


    if component_value is None:
        if first_select > len(menu_definition):
            if login_name is not None:
                return login_name
            else:
                menu_item = menu_definition[-1]

        elif home_name is None:
            menu_item = menu_definition[first_select]

        else:
            if first_select == 0:
                return home_name
            else:
                menu_item = menu_definition[(first_select-1)]

        if 'id' in menu_item:
            return menu_item['id']
        else:
            return menu_item['label']
    else:
        return component_value

