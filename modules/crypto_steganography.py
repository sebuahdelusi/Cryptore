
import os
from PIL import Image

def get_message_bits(message):
    message_with_delimiter = message + "$$$END$$$"
    
    all_bits = []
    for char in message_with_delimiter:
        ascii_val = ord(char)
        binary_val = format(ascii_val, '08b')
        for bit in binary_val:
            all_bits.append(int(bit))
    return all_bits

def hide_message_in_image(image_path, message_to_hide, output_path):
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
        img.close()
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Gambar '{image_path}' tidak ditemukan.")
    except Exception as e:
        raise e


def extract_message_from_image(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        pixels = img.load()
        
        extracted_bits = []
        extracted_message = ""
        delimiter = "$$$END$$$"
        
        def check_bits():
            nonlocal extracted_message
            
            if len(extracted_bits) % 8 == 0:
                byte_bits = extracted_bits[-8:]
                byte_str = "".join(map(str, byte_bits))
                ascii_val = int(byte_str, 2)
                extracted_message += chr(ascii_val)
                
                if extracted_message.endswith(delimiter):
                    return "STOP" # Kirim sinyal untuk berhenti
            return None

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                extracted_bits.append(r & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)]
                
                extracted_bits.append(g & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)]
                
                extracted_bits.append(b & 1)
                if check_bits() == "STOP":
                    img.close()
                    return extracted_message[:-len(delimiter)]
        
        img.close()
        return "Tidak ada pesan (atau delimiter tidak ditemukan)."
        
    except FileNotFoundError:
        return f"Error: Gambar '{image_path}' tidak ditemukan."
    except Exception as e:
        return f"Error saat ekstraksi: {e}"



if __name__ == "__main__":
    

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

        assert PESAN_RAHASIA == pesan_ditemukan
        print("\nVerifikasi: SUKSES! Pesan asli sama dengan pesan yang diekstrak.")
        
        os.remove(STEGO_IMAGE)

    except FileNotFoundError:
        print(f"\nVerifikasi GAGAL: File '{COVER_IMAGE}' tidak ditemukan untuk testing.")
    except AssertionError:
        print("\nVerifikasi: GAGAL! Pesan tidak cocok.")
    except Exception as e:
        print(f"Error saat tes: {e}")