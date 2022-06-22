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


def info_card(title=None, content=None,sentiment=None,bar_value=None,icon_size="2.4rem",title_text_size="2.4rem",content_text_size="1.2rem",theme_override=None,key=None):
    """
    Creates an info card with a title, content text, display icon and an optional progress like bar, all with custom color and formatting.
    Fully suports Font Awesome and Bootstrap icons on or off line.

    Parameters
    -------------
    title: str
        The title to use for the info card.
    content: str
        The text content to use on the info card.
    sentiment: str (default None)
        An automatic way to color the info card as using a sentiment,for example there are 3 options ('good', 'bad, 'neutral'), you can also specify these details using the theme_override parameter.

        'good'
        {'bgcolor': '#EFF8F7','title_color': '#2A4657','content_color': 'green','progress_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}
        'bad'
        {'bgcolor': '#FFF0F0','title_color': '#2A4657','content_color': 'red','progress_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
        'neutral'
        {'bgcolor': '#fcf8e5','title_color': '#2A4657','content_color': 'orange','progress_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}

    bar_value: int (default None)
        If a value between 0-100, if specifed, a horizontal progress like bar will appear at the bottom of the info card.
    key:
        A unique key or name for this component
    theme_override: dict
        Override the Streamlit theme applied to the card
        {'bgcolor': '#EFF8F7','title_color': '#2A4657','content_color': 'green','progress_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

    Returns
    ---------
    None

    """

    if theme_override is None:
        if sentiment == 'good':
            theme_override = {'bgcolor': '#EFF8F7','title_color': '#2A4657','content_color': 'green','progress_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}
        elif sentiment == 'bad':
            theme_override = {'bgcolor': '#FFF0F0','title_color': '#2A4657','content_color': 'red','progress_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
        elif sentiment == 'neutral':
            theme_override = {'bgcolor': '#fcf8e5','title_color': '#2A4657','content_color': 'orange','progress_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
        else:
            theme_override = None #{'bgcolor': None,'title_color': None,'content_color': None,'icon_color': None, 'icon': None}

    component_value = _component_func(title=title, content=content,bar_value=bar_value,icon_size=icon_size,title_text_size=title_text_size,content_text_size=content_text_size, key=key,theme_override=theme_override)

    return component_value