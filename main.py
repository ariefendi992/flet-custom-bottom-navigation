from flet import *
from shared.themes import *
from views.pages.detail_page import DetailPage
from views.pages.main_page import MainPage


def main(page: Page):
    page.title = "Custom Bottom Navigation"
    page.window_width = defaultWidth
    # page.window_center()
    page.window_height = 851
    page.window_always_on_top = True
    page._set_attr("width", defaultWidth)
    page._set_attr("height", defaultHeight)
    page.bgcolor = kBackgroundColor
    page.padding = 0

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                View(
                    "/",
                    [
                        MainPage(),
                    ],
                    padding=0,
                    bgcolor=kBackgroundColor,
                )
            )
        if page.route == "/detail":
            page.views.append(
                View(
                    "/",
                    [
                        DetailPage(),
                    ],
                    padding=0,
                    bgcolor=kBackgroundColor,
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page._set_attr
    page.update()


if __name__ == "__main__":
    app(main)
