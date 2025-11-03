# Simpan sebagai: modules/crypto_rsa_file.py

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os

# [MODIFIKASI] Path ke folder kunci
BASE_PATH = os.path.dirname(__file__) # Ini adalah folder 'modules'
ASSETS_PATH = os.path.join(BASE_PATH, "..", "assets") # Naik satu level, lalu ke 'assets'
KEY_PATH = os.path.join(ASSETS_PATH, "keys")
PUBLIC_KEY_PATH = os.path.join(KEY_PATH, "public_key.pem")
PRIVATE_KEY_PATH = os.path.join(KEY_PATH, "private_key.pem")


def rsa_encrypt_file(file_path):
    """Menenkripsi file menggunakan Kunci Publik."""
    try:
        output_path = file_path + ".enc"
        with open(file_path, "rb") as f_in:
            data = f_in.read()
            
        session_key = get_random_bytes(16)
        cipher_aes = AES.new(session_key, AES.MODE_GCM)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        
        # Gunakan path global
        recipient_key = RSA.import_key(open(PUBLIC_KEY_PATH).read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        
        with open(output_path, "wb") as f_out:
            f_out.write(enc_session_key) 
            f_out.write(cipher_aes.nonce)
            f_out.write(tag)
            f_out.write(ciphertext)
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' atau Kunci RSA di '{KEY_PATH}' tidak ditemukan.")
    except Exception as e:
        raise e

def rsa_decrypt_file(encrypted_file_path):
    """Mendekripsi file menggunakan Kunci Privat."""
    try:
        output_path, _ = os.path.splitext(encrypted_file_path)
        
        # Gunakan path global
        private_key = RSA.import_key(open(PRIVATE_KEY_PATH).read())

        with open(encrypted_file_path, "rb") as f_in:
            enc_session_key = f_in.read(private_key.size_in_bytes())
            nonce = f_in.read(16)
            tag = f_in.read(16)
            ciphertext = f_in.read()
            
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        
        cipher_aes = AES.new(session_key, AES.MODE_GCM, nonce=nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        
        with open(output_path, "wb") as f_out:
            f_out.write(data)
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{encrypted_file_path}' atau Kunci RSA di '{KEY_PATH}' tidak ditemukan.")
    except (ValueError, TypeError):
        raise ValueError("Dekripsi gagal! Kunci privat salah atau file korup.")
    except Exception as e:
        raise e