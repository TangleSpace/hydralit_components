import os
import streamlit as st
import uuid
import streamlit.components.v1 as components
from hydralit_components import IS_RELEASE


if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("info_card", path=build_path)
else:
    _component_func = components.declare_component("info_card", url="http://localhost:3000")


def info_card(title=None, content=None,sentiment=None,bar_value=None,theme_override=None,key=None):

    if theme_override is None:
        if sentiment == 'good':
            theme_override = {'bgcolor': '#EFF8F7','title_color': '#2A4657','content_color': 'green','progress_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}
        elif sentiment == 'bad':
            theme_override = {'bgcolor': '#FFF0F0','title_color': '#2A4657','content_color': 'red','progress_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
        elif sentiment == 'neutral':
            theme_override = {'bgcolor': '#fcf8e5','title_color': '#2A4657','content_color': 'orange','progress_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
        else:
            theme_override = None #{'bgcolor': None,'title_color': None,'content_color': None,'icon_color': None, 'icon': None}

    component_value = _component_func(title=title, content=content,bar_value=bar_value, key=key,theme_override=theme_override)

    return component_value