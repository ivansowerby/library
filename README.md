<h1>Library</h1>

<p style="text-align:right">Revision for 0.2.1</p>

### List of contents:
1. Brief Introduction
2. Instructions
3. Legal (MIT license)

<b><h2 style="text-align:center">Brief Introduction</h3></b>

---

A <i>library</i> of useful python scripts imported through HTTP requests to the catalog, a dictionary of raw URLs to scripts; maintained and contributed to by the open-source community.
* Due to be updated (without notice) regularly as more scripts are introduced, <b>however the community should aim to keep existing files in their respective directories</b>.

<b><h2 style="text-align:center">Instructions</h3></b>

---

<i>Library</i> can either be utilised by downloading the relevant <i>libs</i> locally or rather (as suggested below) by sending a HTTP request to the raw <i>catalog</i> URL (which itself redirects to the relevant python script/s), to then execute that locally with the <i>exec()</i> function.

Shown below is the code contained within [library.py](https://raw.githubusercontent.com/ivanl-exe/library/main/library.py), which should be downloaded and placed in the same directory as it is wished to be used.

``` python
import requests

BASE_URL = 'https://raw.githubusercontent.com/ivanl-exe/library/main/catalog/'

def __format_name__(name: str) -> str:
    if name[-4:].find('.py') == -1:
        name += '.py'
    return name

def __format_dir__(dir: str) -> str:
    if dir.rfind('/') != len(dir) - 1:
        dir += '/'
    return dir

def borrow(filename: str) -> str:
    url = ''.join([
        __format_dir__(BASE_URL),
        filename
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
    save_directory = ''.join([__format_dir__(save_directory), __format_name__(filename)])
    
    code = borrow(filename)
    file = open(save_directory, 'w')

    file.write(
        '\n'.join([l.replace('    ', '', 1) for l in code.split('\n') if l.find('class') == -1])
    )
    return code
```

---

At the start of the python application import the <i>library</i>.py file to utilise the functions. Specify the file location if not in the current working directory (<i>pwd</i>)

~~~ python
import library
~~~

---

<b><h3>library.borrow()</h3></b>


``` python
exec(library.borrow(__FILE_NAME__))
```

* <b>Example</b>

``` python
from time import sleep
import library
for lib in ('ascii', 'cli'):
    exec(library.borrow(lib))

s = 'Hello, World!'
while True:
    cli.clear()
    s = ascii.rotate(s, 1)
    print(s, end = '')
    sleep(0.1)
```

---

<b><h3>library.save()</h3></b>

``` python
exec(library.save(__FILE_NAME__[, __DIRECTORY__]))
```

* <b>Example</b>

``` python
import library

for lib in ('ascii', 'cli'):
    library.save(lib)
    print(f'{lib} successfully saved to the pwd')
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