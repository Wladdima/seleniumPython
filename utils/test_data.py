from utils.urls import CELLPHONE_PRODUCT_LIST_URL
from utils.product_data import (PHONE_COVER_PRODUCT_ID, PHONE_COVER_PRODUCT_MANUFACTURER,
                                PHONE_COVER_PRODUCT_COLOR)
from models.products import PhoneCover


class ProductListPageTestData:
    CASES = [
        dict(
            prod_list_url=CELLPHONE_PRODUCT_LIST_URL,
            product=PhoneCover(id=PHONE_COVER_PRODUCT_ID)
        )
    ]

class ProductDetailPageTestData:
    CASES = [
        dict(
            product=PhoneCover(id=PHONE_COVER_PRODUCT_ID, color=PHONE_COVER_PRODUCT_COLOR,
                               manufacturer=PHONE_COVER_PRODUCT_MANUFACTURER, price="10.00"),
        )
    ]

class CartPageTestData:
    CASES = [
        dict(
            product=PhoneCover(id=PHONE_COVER_PRODUCT_ID, color=PHONE_COVER_PRODUCT_COLOR,
                               manufacturer=PHONE_COVER_PRODUCT_MANUFACTURER, price="10.00"),
        )
    ]