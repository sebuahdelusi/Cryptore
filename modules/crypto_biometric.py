# Simpan sebagai: modules/crypto_biometric.py

import sys
import subprocess
import asyncio
from winrt.windows.security.credentials.ui import (
    UserConsentVerifier,
    UserConsentVerifierAvailability,
    UserConsentVerificationResult
)

# --- Bagian yang akan dijalankan oleh Helper Process ---

async def _check_availability_async():
    """Pemeriksaan ketersediaan Windows Hello (Async)."""
    try:
        availability = await UserConsentVerifier.check_availability_async()
        if availability == UserConsentVerifierAvailability.AVAILABLE:
            return "AVAILABLE"
        elif availability == UserConsentVerifierAvailability.NOT_CONFIGURED_FOR_USER:
            return "NOT_CONFIGURED"
        else:
            return "NOT_AVAILABLE"
    except Exception as e:
        return "ERROR"

async def _request_verification_async(message):
    """Meminta verifikasi Windows Hello (Async)."""
    try:
        consent_result = await UserConsentVerifier.request_verification_async(message)
        if consent_result == UserConsentVerificationResult.VERIFIED:
            return "VERIFIED"
        elif consent_result == UserConsentVerificationResult.CANCELED:
            return "CANCELED"
        else:
            return "NOT_VERIFIED"
    except Exception as e:
        return "ERROR"

def _hello_helper_main(flag, message=None):
    """
    Fungsi utama yang dijalankan oleh helper process.
    Hanya menjalankan satu tugas async dan keluar.
    """
    if flag == "--hello-available":
        result = asyncio.run(_check_availability_async())
        if result == "AVAILABLE":
            sys.exit(0) # Sukses
        elif result == "NOT_CONFIGURED":
            sys.exit(1) # Gagal (Tidak dikonfigurasi)
        else:
            sys.exit(2) # Gagal (Lainnya)
            
    elif flag == "--hello-verify":
        static_message = "Konfirmasi identitas Anda untuk Cryptore"
        result = asyncio.run(_request_verification_async(static_message))
        
        if result == "VERIFIED":
            sys.exit(0) # Sukses
        elif result == "CANCELED":
            sys.exit(1) # Dibatalkan
        else:
            sys.exit(2) # Gagal
    
    sys.exit(99) # Flag tidak dikenal

# --- Bagian yang akan dijalankan oleh Aplikasi Utama (Main.py) ---

def _run_helper_process(flag, message=None):
    """
    Menjalankan helper process (script ini sendiri) dengan flag tertentu.
    """
    command = [sys.executable, __file__, flag]
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode
    except Exception as e:
        return -1

def check_biometric_availability():
    """
    (Publik) Memeriksa ketersediaan Windows Hello dari aplikasi utama.
    Mengembalikan tuple (is_available, status_message)
    """
    return_code = _run_helper_process("--hello-available")
    
    if return_code == 0:
        return (True, "Windows Hello tersedia dan siap digunakan")
    elif return_code == 1:
        return (False, "Windows Hello tersedia, tapi belum Anda siapkan (set up).")
    elif return_code == 2:
        return (False, "Perangkat biometrik tidak ditemukan atau tidak tersedia.")
    else:
        return (False, f"Error saat memeriksa biometrik (code: {return_code}).")

def verify_biometric_with_prompt():
    """
    (Publik) Menampilkan prompt Windows Hello dan menunggu hasil.
    Mengembalikan True jika berhasil, False jika gagal atau dibatalkan.
    """
    return_code = _run_helper_process("--hello-verify")
    return return_code == 0

# --- Entry Point untuk Helper Process ---
if __name__ == "__main__":
    # Jika script ini dijalankan langsung dengan flag, masuk ke mode helper
    if len(sys.argv) > 1 and sys.argv[1] in ["--hello-available", "--hello-verify"]:
        _hello_helper_main(sys.argv[1])