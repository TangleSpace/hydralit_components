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
    """
    Creates a progress bar with bar and content text, and the ability to completely control the colour, unlike the default Streamlit progress bar.

    Parameters
    -------------
    bar_value: int (default 0)
        A value between 0-100 representing how much of the progress bar is filled
    content: str
        The text content to use on the progress bar.
    sentiment: str (default None)
        An automatic way to color the progress bar using a sentiment,for example there are 3 options ('good', 'bad, 'neutral'), you can also specify these details using the theme_override parameter.

        'good'
        {'bgcolor': '#f1f1f1','progress_color': 'green'}
        'bad'
        {'bgcolor': '#f1f1f1','progress_color': 'red'}
        'neutral'
        {'bgcolor': '#f1f1f1','progress_color': 'orange'}

    key:
        A unique key or name for this component
    theme_override: dict
        Override the Streamlit theme applied to the progress bar
        {'bgcolor': 'green','content_color': 'white','progress_color': 'red'}

    Returns
    ---------
    None

    """

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

