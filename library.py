import requests

URL = 'https://raw.githubusercontent.com/ivanl-exe/library/main/libs/'

def __format_name__(name: str) -> str:
    if name.find('.py') == -1:
        name += '.py'
    return name

def __format_dir__(dir: str) -> str:
    if dir.rfind('/') != len(dir) - 1:
        dir += '/'
    return dir

def borrow(filename: str) -> str:
    filename = __format_name__(filename)
    main_url = __format_dir__(URL)

    response = requests.get(f'{main_url}{filename}')
    if response.status_code == 200:
        code = response.text
        return code

def save(filename: str, save_directory: str = ''):
    filename = __format_name__(filename)
    save_directory = f'{__format_dir__(save_directory)}{filename}'
    
    code = borrow(filename)
    file = open(save_directory, 'w')

    file.write(
        '\n'.join([l.replace('    ', '', 1) for l in code.split('\n') if l.find('class') == -1])
    )
    return code