<h1>Library</h1>

<p style="text-align:right">Revision for 0.0.1</p>

### List of contents:
1. Brief Introduction
2. How to Use
3. Legal (MIT license)

<b><h2 style="text-align:center">Brief Introduction</h3></b>

---

A <i>library</i> of useful python scripts, to be executed by a HTTPS request to the raw URL of the python file. Due to be updated (without notice) regularly as more scripts are introduced, however preceding files will be kept in their respective directories.

<b><h2 style="text-align:center">How to Use</h3></b>

<i>Library</i> can either be utilised by downloading the relevant code locally or rather as suggested below by sending a HTTPS request to the raw URL, to then execute that locally with the <i>exec()</i> function.

Shown below is the code contained within [library.py](https://raw.githubusercontent.com/ivanl-exe/library/main/how_to_use/library.py), which should be downloaded and placed in the same directory as it is wished to be used.

``` python
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
```

- Or alternatively the code can be pasted into the main python file with the argument <i>execute_locally</i> = True, and no need for importing.

Then in the main file of the application apply:

~~~ python
import library
~~~


Then when the library is required:

``` python
exec(library.fetch(__FILE_NAME__))
```

<b><h3>EXAMPLE</h3><b>
``` python
import library
for lib in ('ascii.py', 'cli.py'):
    exec(library.fetch(lib))

s = 'Hello, World!'
while True:
    s = ascii.rotate(s, 1)
    cli.clear()
```

<b><h2 style="text-align:center">License (MIT)</h3></b>

---
<br>

|Permissions|Conditions|Limitations|
|---|---|---|
|Commercial use|License and copyright notice|Liability|
|Distribution||Warranty|
|Modification|||
|Private use|||

```
MIT License

Copyright (c) 2022 Ivan (GitHub: ivanl-exe, E-Mail: ivan.exe@pm.me)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```