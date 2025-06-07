# PDF Bruteforce Tool

Tool untuk melakukan brute force password pada file PDF yang terproteksi menggunakan wordlist.

## Deskripsi

Script Python ini menggunakan library `pikepdf` untuk mencoba berbagai password dari wordlist guna membuka file PDF yang dilindungi password. Tool ini berguna untuk penetration testing dan recovery password PDF yang terlupa.

## Fitur

- ✅ Brute force password PDF menggunakan wordlist
- ✅ Support encoding UTF-8 untuk wordlist
- ✅ Error handling yang baik
- ✅ Progress indicator dengan nomor percobaan
- ✅ Validasi file input
- ✅ Command line interface yang mudah digunakan

## Requirements

### Dependencies
```bash
pip install pikepdf
```

### System Requirements
- Python 3.6+
- Library pikepdf
- File PDF target
- Wordlist file

## Instalasi

1. Clone atau download script ini
2. Install dependencies:
   ```bash
   pip install pikepdf
   ```

## Penggunaan

### Syntax Dasar
```bash
python bf.py -f <path_file_pdf> -w <path_wordlist>
```

### Parameter
- `-f, --file`: Path ke file PDF yang ingin di-crack (required)
- `-w, --wordlist`: Path ke file wordlist yang berisi daftar password (required)

### Contoh Penggunaan

1. **Basic usage:**
   ```bash
   python bf.py -f document.pdf -w passwords.txt
   ```

2. **Dengan path lengkap:**
   ```bash
   python bf.py -f /path/to/encrypted.pdf -w /path/to/wordlist.txt
   ```

3. **Menggunakan wordlist umum:**
   ```bash
   python bf.py -f target.pdf -w /usr/share/wordlists/rockyou.txt
   ```

## Format Wordlist

Wordlist harus berupa file text dengan satu password per baris:
```
password
123456
admin
password123
letmein
```

## Output

### Password Ditemukan
```
[+] Mulai brute force pada file: document.pdf
[1] Mencoba: password
[2] Mencoba: 123456
[3] Mencoba: admin
[✓] Password ditemukan: 'admin'
```

### Password Tidak Ditemukan
```
[+] Mulai brute force pada file: document.pdf
[1] Mencoba: password
[2] Mencoba: 123456
[3] Mencoba: admin
...
[1000] Mencoba: lastpassword
[-] Gagal menemukan password di wordlist.
```

### Error Handling
```
[!] File PDF tidak ditemukan: /path/to/nonexistent.pdf
[!] Wordlist tidak ditemukan: /path/to/nonexistent.txt
[!] Error tidak terduga: <error_message>
```

## Tips Penggunaan

1. **Gunakan wordlist yang tepat:**
   - Untuk PDF personal: password umum, tanggal lahir, nama
   - Untuk PDF corporate: kombinasi nama perusahaan, tahun, dll
   - Wordlist besar: rockyou.txt, common-passwords.txt

2. **Optimasi performa:**
   - Mulai dengan password pendek dan umum
   - Gunakan wordlist yang sudah disortir berdasarkan popularitas
   - Monitor penggunaan CPU dan memory

3. **Keamanan:**
   - Hanya gunakan pada file PDF yang Anda miliki
   - Jangan gunakan untuk tujuan ilegal
   - Backup file PDF sebelum mencoba

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'pikepdf'
```bash
pip install pikepdf
```

### Error: Permission denied
```bash
chmod +x bf.py
```

### File tidak ditemukan
- Pastikan path file PDF dan wordlist benar
- Gunakan path absolut jika perlu
- Periksa permission file

## Ethical Usage

⚠️ **PENTING**: Tool ini hanya boleh digunakan untuk:
- File PDF milik sendiri
- Penetration testing yang authorized
- Educational purposes
- Password recovery yang legitimate

❌ **JANGAN** gunakan untuk:
- Mengakses file PDF orang lain tanpa izin
- Aktivitas ilegal
- Melanggar privacy orang lain

## Limitasi

- Kecepatan tergantung pada kompleksitas password dan ukuran wordlist
- Tidak efektif untuk password yang sangat kompleks atau panjang
- Memory usage meningkat dengan wordlist yang besar

## Lisensi

Tool ini dibuat untuk tujuan edukasi dan testing. Pengguna bertanggung jawab atas penggunaan tool ini.

## Author

Dibuat untuk IDN Bootcamp - PDF Security Testing

---

**Disclaimer**: Tool ini dibuat untuk tujuan edukasi dan security testing. Penggunaan yang tidak bertanggung jawab adalah risiko pengguna.

