import json
import os
from datetime import datetime
from .crypto_super_encrypt import super_encrypt, super_decrypt

class SecureChat:
    def __init__(self, chat_file):
        self.chat_file = chat_file
        self.load_chats()
    
    def load_chats(self):
        try:
            if os.path.exists(self.chat_file):
                with open(self.chat_file, 'r') as f:
                    self.chats = json.load(f)
            else:
                self.chats = {}
                self.save_chats()
        except json.JSONDecodeError:
            self.chats = {}
            self.save_chats()
    
    def save_chats(self):
        os.makedirs(os.path.dirname(self.chat_file), exist_ok=True)
        
        chats_to_save = {}
        for chat_key, messages in self.chats.items():
            chats_to_save[chat_key] = []
            for msg in messages:
                msg_copy = msg.copy()
                if "decrypted_content" in msg_copy:
                    del msg_copy["decrypted_content"]
                if "is_decrypted" in msg_copy:
                    del msg_copy["is_decrypted"]
                chats_to_save[chat_key].append(msg_copy)
        
        with open(self.chat_file, 'w') as f:
            json.dump(chats_to_save, f, indent=4)

    def get_chat_key(self, sender, receiver):
        return '_'.join(sorted([sender, receiver]))
        
    def send_message(self, sender, receiver, message, hill_key=None, blowfish_key=None):
        chat_key = self.get_chat_key(sender, receiver)
        
        self.load_chats()
        
        if chat_key not in self.chats:
            self.chats[chat_key] = []
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        msg_obj = {
            "sender": sender,
            "timestamp": timestamp,
            "encrypted": bool(hill_key and blowfish_key)
        }
        
        if hill_key and blowfish_key:
            try:
                encrypted_msg = super_encrypt(message, hill_key, blowfish_key)
                if not encrypted_msg:
                    raise ValueError("Encryption failed")
                msg_obj["content"] = encrypted_msg
            except Exception as e:
                raise Exception(f"Failed to encrypt message: {str(e)}")
        else:
            msg_obj["content"] = message
        
        self.chats[chat_key].append(msg_obj)
        self.save_chats()
    
    def get_messages(self, user1, user2, hill_key=None, blowfish_key=None):
        chat_key = self.get_chat_key(user1, user2)
        
        self.load_chats()
        
        if chat_key not in self.chats:
            self.chats[chat_key] = []
            self.save_chats()
            return []
            
        for msg in self.chats[chat_key]:
            if "decrypted_content" in msg:
                del msg["decrypted_content"]
            if "is_decrypted" in msg:
                del msg["is_decrypted"]
        
        messages = []
        for msg in self.chats[chat_key]:
            msg_copy = msg.copy()
            
            if msg["encrypted"] and "decrypted_content" in msg:
                msg_copy["content"] = msg["decrypted_content"]
            elif msg["encrypted"] and hill_key and blowfish_key:
                try:
                    decrypted = super_decrypt(msg["content"], hill_key, blowfish_key)
                    if decrypted:
                        msg["decrypted_content"] = decrypted
                        msg_copy["content"] = decrypted
                        self.save_chats()
                    else:
                        msg_copy["content"] = "[Pesan Terenkripsi - Kunci Tidak Sesuai]"
                except Exception as e:
                    msg_copy["content"] = "[Pesan Terenkripsi - Error Dekripsi]"
            
            messages.append(msg_copy)
        
        return messages