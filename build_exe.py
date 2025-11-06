import PyInstaller.__main__
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

args = [
    'main.py',
    '--name=Cryptore',
    '--onefile',
    '--windowed',
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

if os.path.exists('assets/images/logo.png'):
    args.insert(4, '--icon=assets/images/logo.png')

PyInstaller.__main__.run(args)

print("\n" + "="*60)
print("Build complete! Executable is in the 'dist' folder")
print("="*60)
