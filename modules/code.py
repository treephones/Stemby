import requests

engine = "https://emkc.org/api/v2/piston/execute"

def get_data(language, version, code):
    return {
        "language": language,
        "version": version,
        "files": [
            {
                code
            }
        ]
    }

def execute(code, lang, runtimes):
    version = None
    for runtime in runtimes:
        if runtime['language'] == lang or lang in runtime['aliases']:
            version = runtime['version']
            break
    response = requests.post(url=engine, data=get_data(lang, version, code))
    return response.json()
