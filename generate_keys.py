# Simpan sebagai: generate_keys.py (di folder PROYEK/)

from Crypto.PublicKey import RSA
import os

# Tentukan path
KEY_DIR = os.path.join("assets", "keys")
os.makedirs(KEY_DIR, exist_ok=True)

# Buat kunci baru
key = RSA.generate(2048)

# Simpan Kunci Privat
private_key_path = os.path.join(KEY_DIR, "private_key.pem")
with open(private_key_path, "wb") as f:
    f.write(key.export_key())

# Simpan Kunci Publik
public_key_path = os.path.join(KEY_DIR, "public_key.pem")
with open(public_key_path, "wb") as f:
    f.write(key.publickey().export_key())

print(f"Kunci berhasil dibuat di dalam folder {KEY_DIR}")