from dataclasses import dataclass

from utils.urls import PHONE_COVER_DETAIL_PAGE_URL


@dataclass
class PhoneCover:
    id: str
    url: str = PHONE_COVER_DETAIL_PAGE_URL
    quantity: str = '1'
    price: str = None
    color: str = None
    manufacturer: str = None
    title: str = 'Phone Cover'
