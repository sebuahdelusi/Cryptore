# Simpan sebagai: steganografi.py

import os
from PIL import Image

def get_message_bits(message):
    """Mengubah string pesan (termasuk delimiter) menjadi daftar bit."""
    message_with_delimiter = message + "$$$END$$$"
    
    all_bits = []
    for char in message_with_delimiter:
        ascii_val = ord(char)
        binary_val = format(ascii_val, '08b')
        for bit in binary_val:
            all_bits.append(int(bit))
    return all_bits

def hide_message_in_image(image_path, message_to_hide, output_path):
    """
    Menyembunyikan pesan teks ke dalam gambar menggunakan LSB.
    """
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        pixels = img.load()
        message_bits = get_message_bits(message_to_hide)
        
        total_pixels = width * height
        if len(message_bits) > (total_pixels * 3):
            raise ValueError("Gambar terlalu kecil untuk pesan ini.")

        bit_index = 0
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                if bit_index < len(message_bits):
                    r = (r & 0b11111110) | message_bits[bit_index]
                    bit_index += 1
                
                if bit_index < len(message_bits):
                    g = (g & 0b11111110) | message_bits[bit_index]
                    bit_index += 1

                if bit_index < len(message_bits):
                    b = (b & 0b11111110) | message_bits[bit_index]
                    bit_index += 1
                
                pixels[x, y] = (r, g, b)
                
                if bit_index >= len(message_bits):
                    break
            if bit_index >= len(message_bits):
                break
        
        img.save(output_path)
        # Hapus print ini agar tidak muncul di app.py
        # print(f"Pesan berhasil disembunyikan di '{output_path}'")
        img.close()
        
    except FileNotFoundError:
        print(f"Error: Gambar '{image_path}' tidak ditemukan.")
        # Re-raise error agar GUI bisa menangkapnya
        raise FileNotFoundError(f"Error: Gambar '{image_path}' tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menyembunyikan: {e}")
        raise e


# --- [FUNGSI YANG DIPERBAIKI] ---
def extract_message_from_image(image_path):
    """
    Mengekstrak pesan tersembunyi dari gambar LSB. (VERSI PERBAIKAN)
    """
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        pixels = img.load()
        
        extracted_bits = []
        extracted_message = ""
        delimiter = "$$$END$$$"
        
        # Kita buat helper function internal untuk mengecek per-bit
        def check_bits():
            nonlocal extracted_message # Kita perlu izin untuk mengubah variabel di luar fungsi ini
            
            # Cek apakah kita punya 8 bit baru
            if len(extracted_bits) % 8 == 0:
                # Ambil 8 bit terakhir
                byte_bits = extracted_bits[-8:]
                # Gabungkan: [0, 1, 0, 0, 0, 0, 0, 1] -> '01000001'
                byte_str = "".join(map(str, byte_bits))
                # Ubah biner ke angka: '01000001' -> 65
                ascii_val = int(byte_str, 2)
                # Ubah angka ke karakter: 65 -> 'A'
                extracted_message += chr(ascii_val)
                
                # Cek apakah kita menemukan delimiter
                if extracted_message.endswith(delimiter):
                    return "STOP" # Kirim sinyal untuk berhenti
            return None # Lanjutkan

        # Iterasi melalui piksel
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                # Ekstrak LSB dari RED dan langsung cek
                extracted_bits.append(r & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)] # Kembalikan pesan bersih
                
                # Ekstrak LSB dari GREEN dan langsung cek
                extracted_bits.append(g & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)]
                
                # Ekstrak LSB dari BLUE dan langsung cek
                extracted_bits.append(b & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)]
        
        img.close()
        # Jika loop selesai tapi delimiter tidak ketemu
        return "Tidak ada pesan (atau delimiter tidak ditemukan)."
        
    except FileNotFoundError:
        return f"Error: Gambar '{image_path}' tidak ditemukan."
    except Exception as e:
        return f"Error saat ekstraksi: {e}"


# =====================================================================
# --- CONTOH PENGGUNAAN STEGANOGRAFI ---
# (Dibungkus if __name__ == "__main__" agar tidak jalan saat di-import)
# =====================================================================

if __name__ == "__main__":
    
    # PENTING:
    # 1. Buat sebuah gambar dan simpan di folder yang sama dengan file .py ini
    # 2. Beri nama gambar itu 'cover.png' (atau ganti nama filenya di bawah)

    PESAN_RAHASIA = "Ini adalah pesan rahasia yang disembunyikan di dalam gambar produk toko online."
    COVER_IMAGE = "cover.png" 
    STEGO_IMAGE = "gambar_rahasIA.png" 

    print("--- Proses Steganografi (Menyembunyikan) ---")
    try:
        hide_message_in_image(COVER_IMAGE, PESAN_RAHASIA, STEGO_IMAGE)
        print(f"Pesan berhasil disembunyikan di '{STEGO_IMAGE}'")

        print("\n--- Proses Steganografi (Mengekstrak) ---")
        pesan_ditemukan = extract_message_from_image(STEGO_IMAGE)
        print(f"Pesan yang ditemukan: {pesan_ditemukan}")

        # Verifikasi
        assert PESAN_RAHASIA == pesan_ditemukan
        print("\nVerifikasi: SUKSES! Pesan asli sama dengan pesan yang diekstrak.")
        
        # Hapus file tes
        os.remove(STEGO_IMAGE)

    except FileNotFoundError:
        print(f"\nVerifikasi GAGAL: File '{COVER_IMAGE}' tidak ditemukan untuk testing.")
    except AssertionError:
        print("\nVerifikasi: GAGAL! Pesan tidak cocok.")
    except Exception as e:
        print(f"Error saat tes: {e}")