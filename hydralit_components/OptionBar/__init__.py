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


def option_bar(option_definition,title=None,horizontal_orientation=True, first_select=0, key=None,override_theme=None, font_styling = None):
    """
    Creates an options bar using a list of dictionaries defining the icons and labels that should be displayed.
    Fully suports Font Awesome and Bootstrap icons on or off line.

    Parameters
    -------------
    option_definition : List[Dict]
        A list of dictionaries specifying the option data, for example
        [{'icon': "far fa-copy", 'label':"Left End"},
        {'icon':"🐙",'label':"Copy"}]
    title: str
        The title to use for the option bar.
    horizontal_orientation: bool (default True)
        To render the option bar horizontally or not, if False, will be rendered vertically.
    first_select: int (default 0)
        The first selected entry when the option bar is created.
    key:
        A unique key or name for this component
    override_theme: dict
        Override the Streamlit theme applied to the option bar
        {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}

    font_styling: dict
        Override the styling of the title text of the option bar, for example.
        {'font-class':'h2','font-size':'150%'}

    Returns
    ---------
    label of selected entry
    """
    
    # max_len = 0
    # for mitem in option_definition:
    #     label_len = len(mitem.get('label',''))
    #     if label_len > max_len:
    #         max_len = label_len

    # for i, mitem in enumerate(option_definition):
    #     option_definition[i]['label'] = f"{mitem.get('label',''):^{max_len+10}}"
    

    if font_styling is None:
        font_class = 'h3'
        font_styling = {'font-size':'150%;','color':None, 'text-align':'left;'}
    else:
        font_class = font_styling.pop('font-class')

    font_format_str = ';'.join([f"{str(k)}:{str(v)}" for k,v in font_styling.items()])

    if title is not None:
        st.markdown(f"<{font_class} style='padding: 0px 0px;{font_format_str};'>{title}</{font_class}>",unsafe_allow_html=True)

    component_value = _component_func(menu_definition=option_definition, first_select=first_select,key=key,override_theme=override_theme,horizontal_orientation=horizontal_orientation)


    if component_value is None:
        menu_item = option_definition[first_select]

        if 'id' in menu_item:
            return menu_item.get('id')
        else:
            return menu_item.get('label')
    else:
        return component_value

