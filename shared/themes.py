from flet import *
from shared.custom import CTextStyle

kPrimaryColor = "#5C40CC"
kWhiteColor = "#FFFFFF"
kBackgroundColor = "#FAFAFA"
kBlackColor = "#1F1449"
kGreyColor = "#9698A9"

blackTextStyle = CTextStyle(color=kBlackColor)
greyTextStyle = CTextStyle(color=kGreyColor)
whiteTextStyle = CTextStyle(color=kWhiteColor)

light = FontWeight.W_300
regular = FontWeight.W_400
medium = FontWeight.W_500
semiBold = FontWeight.W_600
bold = FontWeight.W_700


defaultHeight = 812.0
defaultWidth = 375

imgUrlBottomNav = [
    "/icon_home.png",
    "/icon_booking.png",
    "/icon_card.png",
    "/icon_settings.png",
]
