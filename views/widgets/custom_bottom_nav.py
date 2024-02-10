import threading
from time import sleep
from flet import *
from shared.themes import *
from state.page_state import PageState


class CustomBottomNavigation(UserControl):
    def __init__(
        self,
        *,
        imgUrl: str,
        isActive: bool,
        key: str | None = None,
        on_click: any = None,
    ):
        super().__init__()
        self._img_url = imgUrl
        self._key = key
        self._is_active = isActive
        self._on_click = on_click

    @property
    def set_active(self):
        return self._is_active

    @set_active.setter
    def set_active(self, value):
        self._is_active = value

    def set_color(self):
        if self._is_active:
            return kPrimaryColor
        else:
            return kGreyColor

    def build(self):
        self.image = Image(
            self._img_url,
            width=24,
            height=24,
            color=self.set_color(),
        )

        self.line = Container(
            width=30,
            height=2,
            border_radius=border_radius.all(18),
            bgcolor=self.set_color(),
        )
        return Container(
            content=Column(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[Container(), self.image, self.line],
                spacing=0,
            ),
            on_click=self._on_click,
            key=self._key,
        )
