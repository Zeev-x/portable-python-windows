import os
import sys
import subprocess

def main():
    script_dir = os.getcwd()
    python_path = os.path.join(script_dir, "reyette_py", "python.exe")
    #print("Python portable di:", python_path)

    if os.path.exists(python_path):
        cmd = [python_path] + sys.argv[1:]
        subprocess.run(cmd, cwd=os.getcwd())
    else:
        print(f'Python portable tidak ditemukan di "{python_path}"')

if __name__ == "__main__":
    main()
