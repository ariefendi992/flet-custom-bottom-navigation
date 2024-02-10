from typing import Any, Dict


class PageState:
    __attrs: Dict[str, Any] = {}

    def __init__(self, state: int | None = None):
        self.state = state

    def set_attr(self, key: str, value: Any):
        key = key.lower()
        origin_val = self.__attrs.get(key)

        if origin_val is None and value is None:
            return

        self.__attrs.clear()
        self.__attrs[key] = value

    def get_attr(self, key: str, def_value=None):
        key = key.lower()
        if key not in self.__attrs:
            return def_value

        s_val = self.__attrs[key]
        return s_val

    @property
    def set_page(self):
        return self.get_attr("newPage", def_value=0)

    @set_page.setter
    def set_page(self, value):
        self.set_attr("newPage", value)
