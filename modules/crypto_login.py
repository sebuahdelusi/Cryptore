
import hashlib
import os
import base64
import hmac

def hash_password(password):
    salt_bytes = os.urandom(16)
    password_bytes = password.encode('utf-8')
    
    hashed_password_bytes = hashlib.pbkdf2_hmac(
        'sha256', 
        password_bytes, 
        salt_bytes, 
        100000
    )
    
    salt_b64 = base64.b64encode(salt_bytes).decode('utf-8')
    hash_b64 = base64.b64encode(hashed_password_bytes).decode('utf-8')
    
    return salt_b64, hash_b64

def verify_password(salt_b64, hash_b64, provided_password):
    try:
        stored_salt_bytes = base64.b64decode(salt_b64)
        stored_hash_bytes = base64.b64decode(hash_b64)
        
        password_bytes = provided_password.encode('utf-8')
        
        new_hash_bytes = hashlib.pbkdf2_hmac(
            'sha256',
            password_bytes,
            stored_salt_bytes,
            100000
        )
        
        return hmac.compare_digest(new_hash_bytes, stored_hash_bytes)
        
    except Exception as e:
        print(f"Error saat verifikasi: {e}")
        return False