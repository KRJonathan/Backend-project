from fastapi import FastAPI, Query, Body
import uvicorn


app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name": "Sochi_hotel"},
    {"id": 2, "title": "Dubai", "name": "Dubai_hotel"},
    {"id": 3, "title": "Moscow", "name": "Moscow_hotel"},
]

'''---------- ПОЛУЧЕНИЕ ЭЛЕМЕНТА ----------'''
@app.get("/hotels")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Расположение отеля"),
        name: str | None = Query(None, description="Название отеля")
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        if name and hotel["name"] != name:
            continue
        hotels_.append(hotel)
    return hotels_
    return [hotel for hotel in hotels if hotel["title"] == title and hotel["id"] == id and hotel["name"] == name]



'''---------- ДОБАВЛЕНИЕ ЭЛЕМЕНТА ----------'''
@app.post("/hotels")
def create_hotel(
        title: str = Body(embed=True),
        name: str = Body(embed=True),
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": title,
        "name": name
    })
    return {"status": "OK"}



'''---------- ИЗМЕНЕНИЕ ЭЛЕМЕНТА ----------'''
def update_hotel(
        hotels: list,
        hotel_id: int,
        title: str | None,
        name: str | None
):
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title is not None:
                hotel["title"] = title
            if name is not None:
                hotel["name"] = name
            return {"status": "ok"}
    return {"error": "hotel not found"}

@app.put("/hotels/{hotel_id}")
def update_hotel_put(
    hotel_id: int,
    title: str = Query(..., description="Расположение отеля"),
    name: str = Query(..., description="Название отеля"),
):
    return update_hotel(hotels, hotel_id, title, name)

@app.patch("/hotels/{hotel_id}")
def update_hotel_patch(
    hotel_id: int,
    title: str | None = Query(None, description="Расположение отеля"),
    name: str | None = Query(None, description="Название отеля"),
):
    return update_hotel(hotels, hotel_id, title, name)


'''---------- УДАЛЕНИЕ ЭЛЕМЕНТА ----------'''
@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
