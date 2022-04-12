import requests

URL = 'https://raw.githubusercontent.com/ivanl-exe/library/main/src/'

def fetch(filename: str, execute_locally: bool = None) -> str:
    if execute_locally == None:
        execute_locally = False
    
    if filename.find('.py') == -1:
        filename += '.py'
    main_url = URL
    if URL.rfind('/') != len(URL) - 1:
        main_url += '/'

    response = requests.get(f'{main_url}{filename}')
    if response.status_code == 200:
        code = response.text
        if execute_locally == True:
            exec(code)
        return code