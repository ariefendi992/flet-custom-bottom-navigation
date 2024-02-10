from flet import *
from shared.themes import *
from state.page_state import PageState
from views.pages.home_page import HomePage
from views.pages.setting_page import SettingPage
from views.pages.transaction_page import TransactionPage
from views.pages.wallet_page import WalletPage
from views.widgets.custom_bottom_nav import CustomBottomNavigation


class MainPage(UserControl):
    def __init__(self):
        super().__init__()
        self._current_page = PageState().set_page

    def build_content(self, current_index: int):
        match current_index:
            case 0:
                return HomePage()
            case 1:
                return TransactionPage()
            case 2:
                return WalletPage()
            case 3:
                return SettingPage()
            case default:
                return HomePage()

    def widgetBottomNav(self):
        def on_click(e: ControlEvent):
            key = e.control.key
            for index in range(len(self.bottomNav.content.controls)):
                self.bottomNav.content.controls[index] = CustomBottomNavigation(
                    imgUrl=imgUrlBottomNav[index],
                    key=index,
                    isActive=True if index == key else False,
                    on_click=on_click,
                )
            self.stackWidget.controls[0] = self.build_content(key)
            self.update()

        self.bottomNav = Container(
            height=60,
            bgcolor=kWhiteColor,
            margin=margin.only(left=24, right=24, bottom=30),
            padding=padding.only(bottom=0.8),
            border_radius=border_radius.all(18),
            bottom=0,
            left=0,
            right=0,
            shadow=BoxShadow(
                spread_radius=0.2,
                blur_radius=18,
                color=colors.with_opacity(0.5, kGreyColor),
                blur_style=ShadowBlurStyle.OUTER,
                offset=Offset(0.0, 4.0),
            ),
            content=Row(
                alignment=MainAxisAlignment.SPACE_AROUND,
                controls=[
                    CustomBottomNavigation(
                        imgUrl="/icon_home.png",
                        key=0,
                        isActive=True if self._current_page == 0 else False,
                        on_click=on_click,
                    ),
                    CustomBottomNavigation(
                        imgUrl="/icon_booking.png",
                        isActive=True if self._current_page == 1 else False,
                        key=1,
                        on_click=on_click,
                    ),
                    CustomBottomNavigation(
                        imgUrl="/icon_card.png",
                        key=2,
                        isActive=True if self._current_page == 2 else False,
                        on_click=on_click,
                    ),
                    CustomBottomNavigation(
                        imgUrl="/icon_settings.png",
                        key=3,
                        isActive=True if self._current_page == 3 else False,
                        on_click=on_click,
                    ),
                ],
                spacing=0,
            ),
        )

        return self.bottomNav

    def build(self):
        self.stackWidget = Stack(
            controls=[
                self.build_content(self._current_page),
                self.widgetBottomNav(),
            ],
            height=defaultHeight,
            width=defaultWidth,
        )
        return Container(content=self.stackWidget)
