# Cryptore - Secure E-commerce Application

Cryptore is a secure e-commerce application that implements various cryptographic features for secure messaging, file encryption, and steganography. Built with Python and Tkinter, it provides a user-friendly interface while maintaining robust security features.

## 🚀 Features

### 1. Secure Authentication
- Traditional username/password login
- Windows Hello biometric authentication support (PIN, Fingerprint, Face Recognition)
- Per-user Windows Hello configuration
- Secure password hashing with salt

### 2. UI/UX Enhancements
- **Light/Dark Mode Support** - Toggle between light and dark themes
- Theme preference persistence across sessions
- Fully themed interface with adaptive colors
- Improved chat scrolling with mousewheel support
- Enhanced button styling for better visibility
- Responsive design with proper alignment

### 3. Encrypted Chat System
- End-to-end encrypted messaging
- Super encryption using Hill Cipher and Blowfish
- WhatsApp-style chat interface with color-coded message bubbles
- Independent message decryption
- Secure chat history
- Product seller chat integration

### 4. File Security
- RSA file encryption/decryption
- Support for any file type
- Secure key management

### 5. Steganography
- Hide messages in images
- Support for PNG, JPG, JPEG, and BMP formats
- Secure metadata extraction
- Fixed text input handling

## 📋 Requirements

- Python 3.8 or higher
- Windows 10/11 (for Windows Hello support)
- Required Python packages:
  - tkinter
  - PIL (Python Imaging Library)
  - cryptography
  - numpy
  - keyring
  - winrt (Windows Runtime for Windows Hello)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/sebuahdelusi/Cryptore.git
cd Cryptore
```

2. Install required packages:
```bash
pip install pillow cryptography numpy keyring winrt
```

3. Generate RSA keys (if not already present):
```bash
python generate_keys.py
```

4. Run the application:
```bash
python main.py
```

## 🎨 Theme Customization

Cryptore now supports both light and dark modes:

1. After logging in, click on your profile name in the top right
2. Select "☀️ Light Mode" or "🌙 Dark Mode" from the dropdown
3. Your preference is saved automatically and will persist across sessions

**Dark Mode Features:**
- Dark backgrounds for reduced eye strain
- Optimized contrast for readability
- Themed buttons, input fields, and chat bubbles
- Seamless color transitions

## 📱 Usage Guide

### Initial Setup
1. Launch the application
2. Register a new account or log in with existing credentials
3. Optional: Set up Windows Hello for biometric login
   - After logging in, click your profile name
   - Select "🔐 Aktifkan Windows Hello"
   - Follow the Windows Hello authentication prompt
   - Once enabled, use the "🔐 Windows Hello" button on login page

### Windows Hello Login
1. On the login page, select your username from the dropdown
2. Click "🔐 Windows Hello" button
3. A notification will appear - look for the Windows Hello prompt
4. Authenticate using PIN, fingerprint, or face recognition
5. You'll be logged in automatically upon successful verification

### Secure Chat
1. Navigate to the chat section
2. Select a user to chat with
3. For encrypted messages:
   - Enter your message
   - Provide verification code and password when prompted
   - Messages will be encrypted before sending
4. To decrypt received messages:
   - Click on the encrypted message
   - Enter the correct verification code and password
   - Message will be decrypted and displayed

### File Encryption
1. Go to the file encryption section
2. To encrypt:
   - Select any file using "Choose File"
   - Click "Encrypt File"
   - File will be encrypted with .enc extension
3. To decrypt:
   - Select a .enc file
   - Click "Decrypt File"
   - Original file will be restored

### Steganography
1. Access the steganography section
2. To hide a message:
   - Select a cover image
   - Enter your message
   - Choose save location for the output image
3. To extract a message:
   - Select an image containing hidden message
   - Click "Extract" to reveal the hidden content

### Product Reviews
1. Navigate to the reviews section
2. To submit an encrypted review:
   - Write your review
   - Enter verification code and password
   - Submit the review
3. To view reviews:
   - Enter the correct verification code and password
   - Click "View Reviews"
   - Reviews will be decrypted and displayed

## 🔐 Security Features

### Authentication
- Passwords are hashed using secure algorithms
- Salt is added to prevent rainbow table attacks
- Optional biometric authentication

### Encryption
- Hill Cipher implementation for first-level encryption
- Blowfish algorithm for second-level encryption
- RSA encryption for file security
- Secure key management system

### Chat Security
- End-to-end encryption for messages
- Independent message decryption
- No persistence of decrypted content
- Secure chat history storage

## 📁 Project Structure
```
Cryptore/
├── main.py              # Main application file
├── generate_keys.py     # RSA key generation
├── assets/
│   ├── images/         # Application images
│   └── keys/           # RSA key storage
├── data/
│   ├── chats.json     # Encrypted chat history
│   ├── users.json     # User credentials
│   ├── reviews.json   # Encrypted reviews
│   └── theme.json     # User theme preferences
├── modules/
│   ├── crypto_biometric.py     # Biometric authentication
│   ├── crypto_chat.py          # Chat encryption
│   ├── crypto_debug.py         # Debugging utilities
│   ├── crypto_login.py         # Login security
│   ├── crypto_rsa_file.py      # File encryption
│   ├── crypto_steganography.py # Image steganography
│   └── crypto_super_encrypt.py # Message encryption
└── ui/
    ├── ui_auth_pages.py    # Authentication UI
    ├── ui_chat_page.py     # Chat interface
    ├── ui_components.py    # Reusable components
    ├── ui_crypto_pages.py  # Cryptography features
    └── ui_main_pages.py    # Main application UI
```

## ⚠️ Important Notes

1. Keep your verification codes and passwords secure
2. Don't share encryption keys with untrusted parties
3. Regularly backup your encrypted files
4. Remember that forgotten passwords cannot be recovered

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Initial work - [sebuahdelusi]

## 🙏 Acknowledgments

- Thanks to all contributors and testers
- Special thanks to the cryptography community