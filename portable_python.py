import os
import sys

path_name = "reyette_py"

main_exe_url = "https://raw.githubusercontent.com/Zeev-x/portable-python-windows/refs/heads/main/pyr.exe"

url_64bit_312 = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-amd64.zip"
url_32bit_312 = "https://www.python.org/ftp/python/3.12.10/python-3.12.10-embed-win32.zip"


url_64bit_314 = "https://www.python.org/ftp/python/3.14.7/python-3.14.7-embed-amd64.zip"
url_32bit_314 = "https://www.python.org/ftp/python/3.14.7/python-3.14.7-embed-win32.zip"

url_64bit_315 = "https://www.python.org/ftp/python/3.15.0/python-3.15.0a1-embed-amd64.zip"
url_32bit_315 = "https://www.python.org/ftp/python/3.15.0/python-3.15.0a1-embed-win32.zip"


python_12_pth = """python312.zip
.
Lib\\site-packages
..

# Uncomment to run site.main() automatically
#import site
"""

python_14_pth = """python314.zip
.
Lib\\site-packages
..

# Uncomment to run site.main() automatically
#import site
"""

python_15_pth = """python315.zip
.
Lib\\site-packages
..

# Uncomment to run site.main() automatically
#import site
"""

def get_python_version():
    global py_version
    if len(sys.argv) >= 3:
        py_version = int(sys.argv[2])
        if py_version not in [12, 14, 15]:
            print("Invalid version specified. Please use '12', '14', or '15'.")
            sys.exit(1)
        return
    while True:
        vers = input("Select your version (12/14/15): ")
        if vers in ["12", "14", "15"]:
            py_version = int(vers)
            return
        else:
            print("Invalid input. Please enter '12', '14' or '15'.")

def get_python_embed_url():
    if len(sys.argv) >= 4:
        arch = sys.argv[3]
        if arch not in ["32", "64"]:
            print("Invalid architecture specified. Please use '32' or '64'.")
            sys.exit(1)
        if arch == "32":
            if py_version == 12:
                return url_32bit_312
            elif py_version == 14:
                return url_32bit_314
            elif py_version == 15:
                return url_32bit_315
        elif arch == "64":
            if py_version == 12:
                return url_64bit_312
            elif py_version == 14:
                return url_64bit_314
            elif py_version == 15:
                return url_64bit_315
    while True:
        arch = input("Enter the architecture (32 or 64): ")
        if arch == "32":
            if py_version == 12:
                return url_32bit_312
            elif py_version == 14:
                return url_32bit_314
            elif py_version == 15:
                return url_32bit_315
        elif arch == "64":
            if py_version == 12:
                return url_64bit_312
            elif py_version == 14:
                return url_64bit_314
            elif py_version == 15:
                return url_64bit_315
        else:
            print("Invalid input. Please enter '32' or '64'.")

def installer():
    get_python_version()
    os.makedirs(path_name, exist_ok=True)
    cmds = [
        f"curl -L --output pyr.exe {main_exe_url}",
        f"curl -L -o reyette.zip {get_python_embed_url()}",
        f"powershell -command \"Expand-Archive -Path reyette.zip -DestinationPath {path_name}\"",
        f"curl -L -o {path_name}\\get-pip.py https://bootstrap.pypa.io/get-pip.py",
        f"{path_name}\\python.exe {path_name}\\get-pip.py",
    ]
    try:
        for cmd in cmds:
            print(f"Executing: {cmd}")
            os.system(cmd)

        def get_pth_version():
            if py_version == 12:
                return "python312._pth", python_12_pth
            elif py_version == 14:
                return "python314._pth", python_14_pth
            elif py_version == 15:
                return "python315._pth", python_15_pth

        pth1, pth2 = get_pth_version()
        
        with open(f"{path_name}\\{pth1}", "w") as f:
            f.write(pth2)

        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def worker():
    if installer():
        os.remove("reyette.zip")
        os.remove(f"{path_name}\\get-pip.py")
        print("Installation completed successfully.")

if __name__ == "__main__":
    worker()
