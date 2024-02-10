from flet import *
from shared.themes import *


class WalletPage(UserControl):
    def __init__(self):
        self._super = super().__init__()

    def build(self):
        return Container(
            alignment=alignment.center,
            content=Text(
                "Wallet Page",
                size=18,
                color=kBlackColor,
                weight=FontWeight.W_600,
            ),
        )
