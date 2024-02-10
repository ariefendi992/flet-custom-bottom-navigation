from dataclasses import replace
from typing import Optional, Union, List
from flet import *


class CTextStyle(TextStyle):

    def __get_copy(self, **kwargs):
        return replace(self, **kwargs)

    def copy_with(
        self,
        *,
        size: OptionalNumber = None,
        height: OptionalNumber = None,
        weight: Optional[FontWeight] = None,
        italic: Optional[bool] = None,
        decoration: Optional[TextDecoration] = None,
        decoration_color: Optional[str] = None,
        decoration_style: Optional[TextDecorationStyle] = None,
        font_family: Optional[str] = None,
        color: Optional[str] = None,
        bgcolor: Optional[str] = None,
        shadow: Union[None, BoxShadow, List[BoxShadow]] = None,
        foreground: Optional[Paint] = None
    ):
        return self.__get_copy(
            size=size,
            height=height,
            weight=weight,
            italic=italic,
            decoration=decoration,
            decoration_color=decoration_color,
            decoration_style=(
                decoration_style
                if self.decoration_style is None
                else self.decoration_style
            ),
            font_family=font_family if self.font_family is None else self.font_family,
            color=color or self.color,
            bgcolor=bgcolor or self.bgcolor,
            shadow=shadow or self.shadow,
            foreground=foreground or self.foreground,
        )
