# Simpan sebagai: modules/crypto_debug.py

import json
import os
from datetime import datetime
import hashlib

class CryptoDebugger:
    """Class untuk mencatat dan menelusuri operasi kriptografi."""
    
    def __init__(self, log_file="data/crypto_debug.json"):
        """
        Inisialisasi debugger.
        
        Args:
            log_file (str): Path ke file log JSON
        """
        self.log_file = log_file
        self.ensure_log_file()
    
    def ensure_log_file(self):
        """Memastikan file log dan direktorinya ada."""
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump({"operations": []}, f, indent=2)
    
    def log_operation(self, operation_type, **params):
        """
        Mencatat operasi kriptografi.
        
        Args:
            operation_type (str): Jenis operasi (encrypt/decrypt/sign/verify/etc)
            **params: Parameter yang digunakan dalam operasi
        """
        # Baca log yang ada
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        except json.JSONDecodeError:
            log_data = {"operations": []}
        
        # Buat entri log baru
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Hash sensitive data jika ada
        if "plaintext" in params:
            params["plaintext_hash"] = hashlib.sha256(
                str(params["plaintext"]).encode()
            ).hexdigest()
            params["plaintext_preview"] = str(params["plaintext"])[:50] + "..."
            del params["plaintext"]
            
        if "key" in params:
            params["key_hash"] = hashlib.sha256(
                str(params["key"]).encode()
            ).hexdigest()
            del params["key"]
        
        log_entry = {
            "timestamp": timestamp,
            "operation": operation_type,
            "parameters": params
        }
        
        # Tambahkan ke log
        log_data["operations"].append(log_entry)
        
        # Tulis kembali ke file
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)
    
    def search_logs(self, **filters):
        """
        Mencari log berdasarkan filter.
        
        Args:
            **filters: Filter pencarian (operation, timestamp, dll)
            
        Returns:
            list: Daftar operasi yang cocok dengan filter
        """
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        filtered_ops = log_data["operations"]
        
        # Filter berdasarkan operasi
        if "operation" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["operation"] == filters["operation"]
            ]
        
        # Filter berdasarkan tanggal
        if "date" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["timestamp"].startswith(filters["date"])
            ]
        
        # Filter berdasarkan hash plaintext
        if "plaintext_hash" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["parameters"].get("plaintext_hash") == filters["plaintext_hash"]
            ]
        
        # Filter berdasarkan hash key
        if "key_hash" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["parameters"].get("key_hash") == filters["key_hash"]
            ]
            
        return filtered_ops
    
    def get_latest_operations(self, count=10):
        """
        Mengambil operasi terbaru.
        
        Args:
            count (int): Jumlah operasi yang akan diambil
            
        Returns:
            list: Daftar operasi terbaru
        """
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        return log_data["operations"][-count:]
    
    def find_by_file(self, filename):
        """
        Mencari operasi yang berkaitan dengan file tertentu.
        
        Args:
            filename (str): Nama file yang dicari
            
        Returns:
            list: Daftar operasi yang berkaitan dengan file
        """
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        return [
            op for op in log_data["operations"]
            if any(
                filename in str(value) 
                for value in op["parameters"].values()
                if isinstance(value, str)
            )
        ]

# Contoh penggunaan:
if __name__ == "__main__":
    debugger = CryptoDebugger()
    
    # Contoh mencatat operasi enkripsi
    debugger.log_operation(
        "encrypt",
        algorithm="AES",
        mode="CBC",
        file="test.txt",
        plaintext="This is a test message",
        key="mysecretkey123"
    )
    
    # Contoh mencatat operasi steganografi
    debugger.log_operation(
        "steganography_hide",
        image_file="image.png",
        output_file="stego.png",
        plaintext="Hidden message",
        key="stego_password"
    )
    
    # Ambil operasi terbaru
    latest = debugger.get_latest_operations(2)
    print("\nOperasi Terbaru:")
    print(json.dumps(latest, indent=2))
    
    # Cari operasi berdasarkan file
    file_ops = debugger.find_by_file("test.txt")
    print("\nOperasi untuk file test.txt:")
    print(json.dumps(file_ops, indent=2))