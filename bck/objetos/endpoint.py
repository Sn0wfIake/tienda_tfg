import requests

from Objetos import *
from conector import *

db = database()
st = crudusuarios()
listausu = st.listausuarios()

api_url = "http://localhost:63342/muestracatalogo"
response = requests.post(api_url, json=listausu)
response.json()
response.status_code