
import json
import os
from datetime import datetime
import hashlib

class CryptoDebugger:
    
    def __init__(self, log_file="data/crypto_debug.json"):
        self.log_file = log_file
        self.ensure_log_file()
    
    def ensure_log_file(self):
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump({"operations": []}, f, indent=2)
    
    def log_operation(self, operation_type, **params):
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        except json.JSONDecodeError:
            log_data = {"operations": []}
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
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
        
        log_data["operations"].append(log_entry)
        
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)
    
    def search_logs(self, **filters):
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        filtered_ops = log_data["operations"]
        
        if "operation" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["operation"] == filters["operation"]
            ]
        
        if "date" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["timestamp"].startswith(filters["date"])
            ]
        
        if "plaintext_hash" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["parameters"].get("plaintext_hash") == filters["plaintext_hash"]
            ]
        
        if "key_hash" in filters:
            filtered_ops = [
                op for op in filtered_ops 
                if op["parameters"].get("key_hash") == filters["key_hash"]
            ]
            
        return filtered_ops
    
    def get_latest_operations(self, count=10):
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        return log_data["operations"][-count:]
    
    def find_by_file(self, filename):
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

if __name__ == "__main__":
    debugger = CryptoDebugger()
    
    debugger.log_operation(
        "encrypt",
        algorithm="AES",
        mode="CBC",
        file="test.txt",
        plaintext="This is a test message",
        key="mysecretkey123"
    )
    
    debugger.log_operation(
        "steganography_hide",
        image_file="image.png",
        output_file="stego.png",
        plaintext="Hidden message",
        key="stego_password"
    )
    
    latest = debugger.get_latest_operations(2)
    print("\nOperasi Terbaru:")
    print(json.dumps(latest, indent=2))
    
    file_ops = debugger.find_by_file("test.txt")
    print("\nOperasi untuk file test.txt:")
    print(json.dumps(file_ops, indent=2))