# APPLICATION PROGRAMMING INTERFACE
import requests

x = requests.get(
    'https://api.dictionaryapi.dev/api/v2/entries/en/hello'
    )

print(
    (eval(x.text)[0])
    .get("meanings", None)[0]
    .get("definitions", None)[0]
    .get("definition", None)
)