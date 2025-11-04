import sys
import ctypes
from ctypes import wintypes
import win32security
import pywintypes
import win32com.client

# Windows API constants
BIOMETRIC_PROVIDER = "Windows Hello"
CREDUI_FLAGS_ALWAYS_SHOW_UI = 0x00080
CREDUI_FLAGS_GENERIC_CREDENTIALS = 0x40000000
CREDUI_FLAGS_DO_NOT_PERSIST = 0x00002
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX = 0x00040
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS = 0x00004000

def check_biometric_status():
    """
    Check detailed biometric status of the system.
    Returns a tuple of (is_available, status_message)
    """
    if not sys.platform.startswith('win'):
        return False, "Sistem operasi bukan Windows"
    
    try:
        # Check if we're on Windows 10 or later
        win_ver = sys.getwindowsversion()
        if win_ver.major < 10:
            return False, "Windows Hello membutuhkan Windows 10 atau lebih baru"

        # Check if the required DLL is available
        try:
            credui = ctypes.windll.credui
        except AttributeError:
            return False, "Windows Credential UI tidak tersedia"

        # Check for biometric hardware
        try:
            wbem = win32com.client.GetObject("winmgmts:\\\\.\\root\\cimv2")
            biometric_devices = wbem.ExecQuery("Select * from Win32_PnPEntity WHERE (PNPClass = 'Biometric' OR Description LIKE '%Fingerprint%' OR Description LIKE '%Face%')")
            
            if len(list(biometric_devices)) == 0:
                return False, "Tidak ditemukan perangkat biometrik (fingerprint/face recognition)"
        except Exception:
            return False, "Gagal memeriksa perangkat biometrik"

        # Try to access Windows Hello
        try:
            provider = win32security.LookupAccountName(None, BIOMETRIC_PROVIDER)
            return True, "Windows Hello tersedia dan siap digunakan"
        except pywintypes.error:
            return False, "Windows Hello tidak dikonfigurasi pada sistem"

    except Exception as e:
        return False, f"Error saat memeriksa biometrik: {str(e)}"

def is_windows_hello_setup():
    """Check if Windows Hello is set up on this device."""
    is_available, _ = check_biometric_status()
    return is_available

def verify_biometric(message="Konfirmasi identitas untuk login ke Toko Keren"):
    """Verify user using Windows credential UI."""
    try:
        if not sys.platform.startswith('win'):
            return False

        # Load Windows Credential UI DLL
        credui = ctypes.windll.credui

        flags = (CREDUI_FLAGS_GENERIC_CREDENTIALS | 
                CREDUI_FLAGS_ALWAYS_SHOW_UI | 
                CREDUI_FLAGS_DO_NOT_PERSIST |
                CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS)

        auth_buffer = ctypes.c_void_p()
        auth_package = ctypes.c_ulong()
        
        # Show Windows security prompt
        result = credui.CredUIPromptForWindowsCredentialsW(
            None,  # Parent window handle
            0,     # Message ID
            message,
            None,  # Reserved
            0,     # Reserved
            ctypes.byref(auth_buffer),
            ctypes.byref(auth_package),
            None,  # Save checkbox
            flags
        )

        # Clean up
        if auth_buffer:
            credui.CredFree(auth_buffer)

        # Return True if user authenticated successfully
        return result == 0

    except Exception as e:
        print(f"Error during biometric verification: {e}")
        return False

def is_biometric_available():
    """Check if biometric authentication is available."""
    if not sys.platform.startswith('win'):
        return False
    return is_windows_hello_setup()

# For compatibility with previous code
def verify_biometric_sync():
    """Synchronous biometric verification."""
    return verify_biometric()