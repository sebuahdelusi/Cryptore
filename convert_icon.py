from PIL import Image
import os

icon_jpg = os.path.join("assets", "images", "icon.jpg")
icon_ico = os.path.join("assets", "images", "icon.ico")

if os.path.exists(icon_jpg):
    img = Image.open(icon_jpg)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(icon_ico, format='ICO', sizes=icon_sizes)
    
    print(f"✅ Icon converted successfully!")
    print(f"   Input:  {icon_jpg}")
    print(f"   Output: {icon_ico}")
else:
    print(f"❌ Error: {icon_jpg} not found!")
