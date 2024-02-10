from flet import *
from shared.themes import *
from state.page_state import PageState


class HomePage(UserControl):
    def __init__(self):
        self._super = super().__init__()

    def did_mount(self):
        self._page = PageState()

    def on_click(self, e):
        self.page.go("/detail")

    def build(self):
        return Container(
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Home Page",
                        style=blackTextStyle.copy_with(
                            size=18,
                            weight=semiBold,
                        ),
                    ),
                    ElevatedButton(
                        "Go Detail",
                        bgcolor=kPrimaryColor,
                        color=kWhiteColor,
                        height=44,
                        width=220,
                        style=ButtonStyle(),
                        on_click=self.on_click,
                    ),
                ],
            ),
        )
