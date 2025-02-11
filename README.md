# Http-api
Тестовое задание для CDN-video

# Руководство пользователя:
Данное руководство содержит сценарий использования, покрывающий все функции разработанного API.

### 0. Убедиться, что установлены библиотеки:
pip install fastapi uvicorn sqlalchemy requests

### 1. Для запуска сервера: 
Открываем папку c проектом в VS Code, запустим новый терминал, введём команду:

uvicorn main:app --reload

### 2. Для добавления города: 
В командной строке Windows:

curl -X POST "http://localhost:8000/cities/" -H "Content-Type: application/json" -d "{\"name\": \"ИмяНашегоГорода\"}"

P.S. Мы берем информацию по первому городу, которое нам выдает в списке API, так что следует в будущем уточнить по какому городу мы хотим работать. 

Варианты:

* Передавать в тело запроса сразу город + регион + страну
* Работать не с названием города, а его Id

### 3. Для удаления города: 
В командной строке Windows:

curl -X DELETE "http://localhost:8000/cities/НазваниеГородаИзБазеДанных"

### 4. Вывести список городов: 
В командной строке Windows:

curl "http://localhost:8000/cities/"

### 5. Вывести ближайшие города: 
В командной строке Windows:

curl "http://localhost:8000/cities/nearby?lat=Широта&lon=Долгота"