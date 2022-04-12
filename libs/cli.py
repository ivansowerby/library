from os import system, name

class cli:
    def clear() -> None:
        if name == 'nt': system('cls')
        else: system('clear')
        return None