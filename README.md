# 1. 介绍

该项目测试和验证 Python 代码保护工具, 测试工具如下:

- [sourcedefender(commercial)](https://pypi.org/project/sourcedefender/): SOURCEdefender can protect your plaintext Python source code with AES 256-bit Encryption. There is no impact on the performance of your running application as the decryption process takes place during the import of your module or when loading your script on the command-line. Encrypted code won't run any slower once loaded from a .pye file compared to loading from a .py or .pyc file
- [pyarmor(commercial)](https://pypi.org/project/pyarmor/): A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.
- [PyObfuscator](https://github.com/mauricelambert/PyObfuscator/): This module obfuscates python code.
- [pyconcrete](https://github.com/Falldog/pyconcrete): Protect your python script, encrypt it as .pye and decrypt when import it
- [pyinstaller](https://pyinstaller.org/en/stable/): PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.8 and newer, and correctly bundles many major Python packages such as numpy, matplotlib, PyQt, wxPython, and others.

# 2. 运行和验证

商业软件 sourcedefender 和 pyarmor 不验证了, 因为其文档详细且商业行为已经证明其可靠性, 另外不想注册账号和付费来验证, 这两个可以作为商业解决方案参考.

## 2.1 安装依赖

```bash
python3.11 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install PyObfuscator pyinstaller
PYCONCRETE_PASSPHRASE=sourcedefender CFLAGS="-Wno-implicit-function-declaration" pip install pyconcrete # https://github.com/Falldog/pyconcrete/issues/94
```

## 2.2 pyconcrete 验证

```bash
# compile, find more info by run: pyconcrete-admin.py --help
pyconcrete-admin.py compile -s main.py --pye
pyconcrete-admin.py compile -s main.py --pyc

# run
pyconcrete main.pye
python main.pyc
```

## 2.3 PyObfuscator 验证

```bash
PyObfuscator main.py --output main-obfuscated.py

python main-obfuscated.py
```

## 2.4 pyc 验证

```bash
python -m py_compile main.py

python -m compileall main.py
```

## 2.5 pyinstaller 验证

```bash
# compile
pyinstaller --onefile main.py

# run
./dist/main
```

## 2.5 反编译验证

```bash
# install
git clone https://github.com/zrax/pycdc
cd pycdc
cmake .
make
make check
cp pycdc ~/.local/bin

# compile
python -m py_compile main.py
# decompile
pycdc __pycache__/main.cpython-311.pyc
```

反编译结果:

```python
# Source Generated with Decompyle++
# File: main.cpython-311.pyc (Python 3.11)

import requests

def get_github_status():
Unsupported opcode: PUSH_EXC_INFO
    api_url = 'https://www.githubstatus.com/api/v2/status.json'
    response = requests.get(api_url)
    if response.status_code == 200:
        status_data = response.json()
        status = status_data.get('status')
        description = status_data.get('body', { }).get('markdown')
        print(f'''GitHub Status: {status}''')
        print(f'''Status Description: {description}''')
        return None
    None(f'''Failed to retrieve GitHub status. Status code: {response.status_code}''')
    return None
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    get_github_status()
    return None
```
