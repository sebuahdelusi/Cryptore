# Simpan sebagai: crypto_login.py

import hashlib
import os
import base64
import hmac

def hash_password(password):
    """
    Membuat hash dari password menggunakan salt yang unik.
    Mengembalikan salt dan hash-nya (keduanya sebagai string base64).
    """
    salt_bytes = os.urandom(16)
    password_bytes = password.encode('utf-8')
    
    hashed_password_bytes = hashlib.pbkdf2_hmac(
        'sha256', 
        password_bytes, 
        salt_bytes, 
        100000
    )
    
    # Ubah bytes ke string Base64 agar bisa disimpan di JSON
    salt_b64 = base64.b64encode(salt_bytes).decode('utf-8')
    hash_b64 = base64.b64encode(hashed_password_bytes).decode('utf-8')
    
    return salt_b64, hash_b64

def verify_password(salt_b64, hash_b64, provided_password):
    """
    Memverifikasi apakah password yang diberikan cocok dengan hash yang disimpan.
    Semua input adalah string.
    """
    try:
        # Ubah string Base64 kembali ke bytes
        stored_salt_bytes = base64.b64decode(salt_b64)
        stored_hash_bytes = base64.b64decode(hash_b64)
        
        # Hash password yang diberikan
        password_bytes = provided_password.encode('utf-8')
        
        new_hash_bytes = hashlib.pbkdf2_hmac(
            'sha256',
            password_bytes,
            stored_salt_bytes,
            100000
        )
        
        # Bandingkan hash-nya
        return hmac.compare_digest(new_hash_bytes, stored_hash_bytes)
        
    except Exception as e:
        print(f"Error saat verifikasi: {e}")
        return False