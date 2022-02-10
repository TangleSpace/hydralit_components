import os
import pathlib
import streamlit as st
import bs4

# find the "index.html" template page
STREAMLIT_STATIC_PATH = os.path.join(pathlib.Path(st.__path__[0]),'static')
STREAMLIT_INDEX_HTML = os.path.join(STREAMLIT_STATIC_PATH,'index.html')

def hydralit_experimental(enable_features, inject_scripts=None,inject_styles=None, inject_html=None, inject_raw_script=None):
  try:
    if enable_features:
        #---------------injection----------------------------------------------------------------------------------------------------
        new_scripts = [
        {'crossorigin':"anonymous",'integrity':"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN",'src':"https://code.jquery.com/jquery-3.2.1.slim.min.js"},
        {'crossorigin':"anonymous",'integrity':"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q",'src':"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"},
        {'crossorigin':"anonymous",'integrity':"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl",'src':"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"}
        ]

        if inject_scripts is not None:
            if isinstance(inject_scripts,dict):
                new_scripts.append(inject_scripts)
            else:
                new_scripts.extend(inject_scripts)

        new_style_sheets =[
        {'crossorigin':"anonymous",'href':"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",'integrity':"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm",'rel':"stylesheet"}
        ]

        if inject_styles is not None:
            new_style_sheets.append(new_style_sheets)
        
        _add_injections(new_scripts,new_style_sheets,inject_html,inject_raw_script)
    else:
        _remove_injections()

  except Exception as e:
    print('Unable to toggle Hydralit experimental features.')
    print('Usual cause is permissions on files and folders within your Python package directory.')
    print(e)


def _remove_injections():
    # load the file
    with open(STREAMLIT_INDEX_HTML) as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt,features="lxml")

    #check it hasn't been done before      
    hidden_header = soup.find(id="hiddenheader")
    hydralit_div = soup.find(id="hydralit")

    if hydralit_div is not None:
        hydralit_div.unwrap()

        if hidden_header is not None:
            hidden_header.decompose()

        # save the file again
        with open(STREAMLIT_INDEX_HTML, "w") as outf:
            outf.write(str(soup))

        print('Hydralit experimental features disabled.')

def _add_injections(new_scripts,new_style_sheets,custom_html,inject_raw_script):
    # load the file
    with open(STREAMLIT_INDEX_HTML) as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt,features="lxml")

    #check it hasn't been done before
    hydralit_div = soup.find(id="hydralit")
    hidden_header = soup.find(id="hiddenheader")

    if hidden_header is None:
        hidden_header = soup.new_tag('div', id="hiddenheader",style="display: none;")

        # add new scripts to heaeder
        for sct in new_scripts:
            new_script = soup.new_tag('script', **sct)
            hidden_header.append(new_script)

        if inject_raw_script is not None:           
            new_script = soup.new_tag('script')
            new_script.append(inject_raw_script)
            hidden_header.append(new_script)
        
        # add new stylesheets to heaeder
        for sct in new_style_sheets:
            new_style = soup.new_tag('link', **sct)
            hidden_header.append(new_style)

        soup.head.append(hidden_header)

        #leave our mark
        stroot_div = soup.find(id="root")
        
        if hydralit_div is None:
            hydralit_div = soup.new_tag('div', id="hydralit")
            stroot_div.wrap(hydralit_div)

        if custom_html is not None:
            hydralit_div.append(custom_html)

        # save the file again
        with open(STREAMLIT_INDEX_HTML, "w") as outf:
            outf.write(str(soup))

        print('Hydralit experimental features enabled.')