import os
import streamlit as st
import math
import streamlit.components.v1 as components
from hydralit_components import IS_RELEASE


if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("option_bar", path=build_path)
else:
    _component_func = components.declare_component("option_bar", url="http://localhost:3000")


def option_bar(menu_definition,title=None,horizontal_orientation=True, first_select=0, key=None,override_theme=None, font_styling = None):

    
    max_len = 0
    for mitem in menu_definition:
        label_len = len(mitem.get('label',''))
        if label_len > max_len:
            max_len = label_len

    for i, mitem in enumerate(menu_definition):
        menu_definition[i]['label'] = f"{mitem.get('label',''):^{max_len+10}}"
    

    if font_styling is None:
        font_class = 'h3'
        font_styling = {'font-size':'150%;','color':None, 'text-align':'left;'}
    else:
        font_class = font_styling.pop('font-class')

    font_format_str = ';'.join([f"{str(k)}:{str(v)}" for k,v in font_styling.items()])

    if title is not None:
        st.markdown(f"<{font_class} style='padding: 0px 0px;{font_format_str};'>{title}</{font_class}>",unsafe_allow_html=True)

    component_value = _component_func(menu_definition=menu_definition, first_select=first_select,key=key,override_theme=override_theme,horizontal_orientation=horizontal_orientation)


    if component_value is None:
        menu_item = menu_definition[first_select]

        if 'id' in menu_item:
            return menu_item.get('id')
        else:
            return menu_item.get('label')
    else:
        return component_value

