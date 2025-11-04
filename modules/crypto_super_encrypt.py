# Simpan sebagai: modules/crypto_super_encrypt.py

import numpy as np
import hashlib
import base64
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# =====================================================================
# [BARU] FUNGSI HILL CIPHER DIGABUNGKAN KE SINI
# =====================================================================

def _mod_inverse(a, m):
    """Internal: Mencari invers modular dari a mod m"""
    m0, x0, x1 = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += m0
    return x1

def _get_key_matrix_inverse(key_matrix):
    """Internal: Menghitung invers modular matriks (K^-1) untuk Hill Cipher 2x2."""
    det = np.linalg.det(key_matrix)
    det_int = int(np.round(det)) % 26
    det_inv = _mod_inverse(det_int, 26)
    
    adj_matrix = np.array([[key_matrix[1, 1], -key_matrix[0, 1]],
                           [-key_matrix[1, 0], key_matrix[0, 0]]])
    
    inv_key_matrix = (adj_matrix * det_inv) % 26
    return inv_key_matrix

def create_key_matrix(key):
    """
    (Publik) Mengubah string kunci (4 huruf) menjadi matriks kunci numpy 2x2.
    Fungsi ini diekspos untuk validasi di UI.
    """
    cleaned_key = "".join(filter(str.isalpha, key)).upper()
    if len(cleaned_key) < 4:
        raise ValueError("Kunci Hill Cipher (2x2) harus terdiri dari 4 huruf.")
        
    key_numbers = [ord(char) - ord('A') for char in cleaned_key[:4]]
    key_matrix = np.array(key_numbers).reshape(2, 2)
    
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    if det == 0 or _mod_inverse(det, 26) == 0:
         raise ValueError(f"Determinan matriks ({det}) tidak valid untuk dekripsi.")
        
    return key_matrix

def _hill_encrypt(plaintext, key_matrix):
    """Internal: Menenkripsi plaintext menggunakan Hill Cipher 2x2."""
    encrypted_text = ""
    cleaned_text = "".join(filter(str.isalpha, plaintext)).upper()
    
    if len(cleaned_text) % 2 != 0:
        cleaned_text += 'X' # Padding
        
    for i in range(0, len(cleaned_text), 2):
        block = cleaned_text[i : i+2]
        p_vector = np.array([ord(block[0]) - ord('A'), ord(block[1]) - ord('A')])
        c_vector = np.dot(key_matrix, p_vector) % 26
        encrypted_text += chr(c_vector[0] + ord('A')) + chr(c_vector[1] + ord('A'))
        
    return encrypted_text

def _hill_decrypt(ciphertext, key_matrix):
    """Internal: Mendekripsi ciphertext menggunakan Hill Cipher 2x2."""
    decrypted_text = ""
    inv_key_matrix = _get_key_matrix_inverse(key_matrix)
    cleaned_text = "".join(filter(str.isalpha, ciphertext)).upper()

    if len(cleaned_text) % 2 != 0:
        raise ValueError("Ciphertext tidak valid, panjangnya ganjil.")

    for i in range(0, len(cleaned_text), 2):
        block = cleaned_text[i : i+2]
        c_vector = np.array([ord(block[0]) - ord('A'), ord(block[1]) - ord('A')])
        p_vector = np.dot(inv_key_matrix, c_vector) % 26
        decrypted_text += chr(p_vector[0] + ord('A')) + chr(p_vector[1] + ord('A'))
        
    return decrypted_text

# =====================================================================
# FUNGSI BLOWFISH & SUPER ENKRIPSI
# =====================================================================

def _get_blowfish_key_bytes(key_str):
    return hashlib.sha256(key_str.encode('utf-8')).digest()

def _blowfish_encrypt(plaintext_str, key_bytes):
    plaintext_bytes = plaintext_str.encode('utf-8')
    cipher = Blowfish.new(key_bytes, Blowfish.MODE_CBC)
    iv = cipher.iv
    ciphertext_bytes = cipher.encrypt(pad(plaintext_bytes, Blowfish.block_size))
    return iv, ciphertext_bytes

def _blowfish_decrypt(ciphertext_bytes, iv, key_bytes):
    cipher = Blowfish.new(key_bytes, Blowfish.MODE_CBC, iv=iv)
    decrypted_bytes = unpad(cipher.decrypt(ciphertext_bytes), Blowfish.block_size)
    return decrypted_bytes.decode('utf-8')

# --- FUNGSI UTAMA (PUBLIK) ---

def super_encrypt(plaintext, hill_key_str, blowfish_key_str):
    """Melakukan Super Enkripsi: Hill Cipher -> Blowfish -> Base64"""
    try:
        matriks_kunci_hill = create_key_matrix(hill_key_str)
        text_after_hill = _hill_encrypt(plaintext, matriks_kunci_hill)
        
        key_bytes_blowfish = _get_blowfish_key_bytes(blowfish_key_str)
        iv, ciphertext_bytes = _blowfish_encrypt(text_after_hill, key_bytes_blowfish)
        
        iv_b64 = base64.b64encode(iv).decode('utf-8')
        cipher_b64 = base64.b64encode(ciphertext_bytes).decode('utf-8')
        
        return f"{iv_b64}:{cipher_b64}"
    except ValueError as e:
        return None

def super_decrypt(ciphertext_gabungan, hill_key_str, blowfish_key_str):
    """Melakukan Super Dekripsi: Base64 -> Blowfish -> Hill Cipher"""
    try:
        iv_b64, cipher_b64 = ciphertext_gabungan.split(':')
        iv = base64.b64decode(iv_b64)
        ciphertext_bytes = base64.b64decode(cipher_b64)

        key_bytes_blowfish = _get_blowfish_key_bytes(blowfish_key_str)
        text_after_hill = _blowfish_decrypt(ciphertext_bytes, iv, key_bytes_blowfish)

        matriks_kunci_hill = create_key_matrix(hill_key_str)
        original_text = _hill_decrypt(text_after_hill, matriks_kunci_hill)

        return original_text
    except Exception as e:
        return None