from typing import Any, Union

def add_to_dict(key: Any, value: Any, dictionary: dict) -> Union[dict, Any]:
    ...

my_dict = {"Apple": "iPhone", "Samsung": "Galaxy"}
add_to_dict("Xiaomi", "Mi", my_dict)