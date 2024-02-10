from flet import *
from shared.themes import *
from state.page_state import PageState


class DetailPage(UserControl):

    def __init__(self):
        super().__init__()

    def did_mount(self):
        self._page = PageState()

    def on_click(self, e):
        self._page.set_page = 1
        self.page.go("/")

    def build(self):
        return Container(
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Detail Page",
                        size=18,
                        color=kBlackColor,
                        weight=FontWeight.W_600,
                    ),
                    ElevatedButton(
                        "Go Transaction",
                        bgcolor=kPrimaryColor,
                        color=kWhiteColor,
                        height=44,
                        on_click=self.on_click,
                    ),
                ],
            ),
            height=defaultHeight,
        )
