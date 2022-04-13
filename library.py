import requests

BASE_URL = 'https://raw.githubusercontent.com/ivanl-exe/library/main/catalog/'

def __format_name__(name: str) -> str:
    if name[-4:].find('.txt') == -1:
        name += '.txt'
    return name

def __format_dir__(dir: str) -> str:
    if dir.rfind('/') != len(dir) - 1:
        dir += '/'
    return dir

def borrow(filename: str) -> str:
    url = ''.join([
        __format_dir__(BASE_URL),
        __format_name__(filename)
    ])

    for i in range(2):
        response = requests.get(url)
        if response.status_code != 200: return ''
        if i == 1:
            code = response.text
            break
        url = response.text
    return code

def save(filename: str, save_directory: str = ''):
    filename = __format_name__(filename)
    save_directory = ''.join([__format_dir__(save_directory), filename])
    
    code = borrow(filename)
    file = open(save_directory, 'w')

    file.write(
        '\n'.join([l.replace('    ', '', 1) for l in code.split('\n') if l.find('class') == -1])
    )
    return code