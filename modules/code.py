import requests
from utils.mathutils import get_units

engine = "https://emkc.org/api/v2/piston/execute"

def get_data(language, version, code):
    data = {
        "language": language,
        "version": version,
        "files": [
            {
                code
            }
        ]
    }
    return data

def execute(language, code):
    vers_data = get_units(language)
    version = "3.9" if len(vers_data) == 1 else vers_data[1]
    data = get_data(language, version, code)
    response = requests.post(url=engine, data=data)
    return response.json()