import os
import streamlit.components.v1 as components
import datetime

from hydralit_components import IS_RELEASE

if IS_RELEASE:
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    build_path = os.path.join(absolute_path, "frontend/build")
    _component_func = components.declare_component("cookie_manager", path=build_path)
else:
    _component_func = components.declare_component("cookie_manager", url="http://localhost:3001")


class CookieManager:
    def __init__(self,key=None):
        self.cookie_manager = _component_func
        self.cookies = self.cookie_manager(method="getAll", key=key+"_start")
        self.use_streamlit_state = True
        self._key = key


    def get(self, cookie: str) -> any:
        try:
            return self.cookies.get(cookie)
        except:
            return None


    def set(self, cookie, val, expires_at=datetime.datetime.now() + datetime.timedelta(days=1)):
        try:
            if cookie is not None or cookie != "":
                expires_at = expires_at.isoformat()
                self.cookie_manager(method="set", cookie=cookie, value=val, expires_at=expires_at, key=self._key+"_setter")
        except:
            pass


    def delete(self, cookie):
        try:
            if cookie is not None or cookie != "":
                self.cookie_manager(method="delete", cookie=cookie, key=self._key+"_delete")
        except:
            pass


    def get_all(self) -> dict:
        try:
            return self.cookie_manager(method="getAll", key=self._key+"_getall")
        except:
            return None
