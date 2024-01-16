# 1. 介绍

该项目测试和验证 Python 代码保护工具, 测试工具如下:

- [sourcedefender(commercial)](https://pypi.org/project/sourcedefender/): SOURCEdefender can protect your plaintext Python source code with AES 256-bit Encryption. There is no impact on the performance of your running application as the decryption process takes place during the import of your module or when loading your script on the command-line. Encrypted code won't run any slower once loaded from a .pye file compared to loading from a .py or .pyc file
- [pyarmor(commercial)](https://pypi.org/project/pyarmor/): A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.
- [PyObfuscator](https://github.com/mauricelambert/PyObfuscator/): This module obfuscates python code.
- [pyconcrete](https://github.com/Falldog/pyconcrete): Protect your python script, encrypt it as .pye and decrypt when import it

# 2. 运行和验证

商业软件 sourcedefender 和 pyarmor 不验证了, 因为其文档详细且商业行为已经证明其可靠性, 另外不想注册账号和付费来验证, 这两个可以作为商业解决方案参考.

## 2.1 安装依赖

```bash
source .venv/bin/activate

pip install -r requirements.txt
pip install PyObfuscator
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
