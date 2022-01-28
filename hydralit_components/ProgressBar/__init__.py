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


def progress_bar(value=0,content_text=None, sentiment=None, key=None,override_theme=None,):

    if override_theme is None:
        if sentiment == 'good':
            override_theme = {'bgcolor': '#f1f1f1','progress_color': 'green'}
        elif sentiment == 'bad':
            override_theme = {'bgcolor': '#f1f1f1','progress_color': 'red'}
        elif sentiment == 'neutral':
            override_theme = {'bgcolor': '#f1f1f1','progress_color': 'orange'}
        else:
            override_theme = None

    component_value = _component_func(value=value, content_text=content_text,key=key,override_theme=override_theme)

    return component_value

