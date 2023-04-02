import json

def get_localized_strings(language: str) -> dict:
    directory = f"db/locals/{language}/localized.json"   
    with open(directory, 'r') as file:
        localized_strings = json.load(file)
        return localized_strings
    


# src
#     |
#     |__db
#     |   |
#     |   |_local
#               |__en 
#                  |_file1.json
#               |__fr 
#                  |_file1.json
#     |__app
#     |   |
#     |   |_provider
#               |__locals.py

# voici ma structure comment ouvreir file1 dans provider en fonction de language (en or fr)