import pikepdf
import time
import argparse
from pathlib import Path

def brute_force_pdf(pdf_path, wordlist_path):
    pdf_path = Path(pdf_path)
    wordlist_path = Path(wordlist_path)

    if not pdf_path.exists():
        print(f"[!] File PDF tidak ditemukan: {pdf_path}")
        return
    if not wordlist_path.exists():
        print(f"[!] Wordlist tidak ditemukan: {wordlist_path}")
        return

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
        print(f"[+] Mulai brute force pada file: {pdf_path}")
        for idx, password in enumerate(wordlist, 1):
            password = password.strip()
            try:
                with pikepdf.open(pdf_path, password=password):
                    print(f"[✓] Password ditemukan: '{password}'")
                    return
            except pikepdf.PasswordError:
                print(f"[{idx}] Mencoba: {password}")
            except Exception as e:
                print(f"[!] Error tidak terduga: {e}")
                return
        print("[-] Gagal menemukan password di wordlist.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Password Brute Forcer")
    parser.add_argument("-f", "--file", required=True, help="Path file PDF")
    parser.add_argument("-w", "--wordlist", required=True, help="Path file wordlist")

    args = parser.parse_args()
    brute_force_pdf(args.file, args.wordlist)
