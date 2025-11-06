"""
Build script for creating Cryptore executable using PyInstaller
"""
import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# PyInstaller configuration
PyInstaller.__main__.run([
    'main.py',
    '--name=Cryptore',
    '--onefile',
    '--windowed',
    '--icon=assets/images/logo.png' if os.path.exists('assets/images/logo.png') else '',
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
])

print("\n" + "="*60)
print("Build complete! Executable is in the 'dist' folder")
print("="*60)
