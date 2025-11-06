import PyInstaller.__main__
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = 'assets/images/icon.ico'

args = [
    'main.py',
    '--name=Cryptore',
    '--onefile',
    '--windowed',
    f'--icon={icon_path}',
    '--add-data=assets;assets',
    '--add-data=data;data',
    '--add-data=modules;modules',
    '--add-data=ui;ui',
    '--hidden-import=PIL._tkinter_finder',
    '--hidden-import=winrt',
    '--hidden-import=keyring',
    '--hidden-import=cryptography',
    '--hidden-import=numpy',
    '--collect-all=winrt',
    '--collect-all=keyring',
    '--noconsole',
    '--clean',
]

PyInstaller.__main__.run(args)

print("\n" + "="*60)
print("Build complete! Executable is in the 'dist' folder")
print("="*60)
