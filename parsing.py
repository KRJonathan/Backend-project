from fastapi import Query, Body, APIRouter
from schemas.hotels import Hotel, HotelPatch
from typing import List

router = APIRouter(prefix="/hotels", tags=["Отели"])  # Объявляем переменную роутер


"""Создание массива данных"""


hotels = [
    {"id": 1, "title": "Sochi", "name": "Sochi_hotel"},
    {"id": 2, "title": "Dubai", "name": "Dubai_hotel"},
    {"id": 3, "title": "Moscow", "name": "Moscow_hotel"},
    {"id": 4, "title": "Мальдивы", "name": "maldivi_hotel"},
    {"id": 5, "title": "Геленджик", "name": "gelendzhik_hotel"},
    {"id": 6, "title": "Казань", "name": "kazan_hotel"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb_hotel"},
]


'''---------- ПОЛУЧЕНИЕ ЭЛЕМЕНТА ----------'''


@router.get("/", response_model=List[dict], summary="Метод get()", description="<h2>Просмотр элемента</h2>")  # Адрес. Т.к. префикс в роутере равен /hotels, тут этот адрес можно убрать, да и везде где есть роутер.
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),  # Это все query параметр, параметры запроса. id, title and name.
        title: str | None = Query(None, description="Расположение отеля"),
        name: str | None = Query(None, description="Название отеля"),
        page: int = Query(1, ge=1),
        per_page: int = Query(3, ge=1),
):

    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:  # Если hotel["id"] не равен этому id, тогда пропусти этот отель
            continue
        if title and hotel["title"] != title:  # Если title текущего отеля не равен hotel["title"], пропустить
            continue
        if name and hotel["name"] != name:  # Аналогично
            continue
        hotels_.append(hotel)  # Иначе добавь этот отель

        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        items = hotels[start_index:end_index]

        return items
    return hotels_  # И верни все эти отели
