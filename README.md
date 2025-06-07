# PDF Bruteforce Tool

Tool to brute force passwords on protected PDF files using wordlist.

## Deskription

This Python script uses the `pikepdf` library to try different passwords from a wordlist to open a password-protected PDF file. This tool is useful for penetration testing and recovering forgotten PDF passwords.

## Feature

- ✅ Brute force PDF password using wordlist
- ✅ Support UTF-8 encoding for wordlist
- ✅ Good error handling
- ✅ Progress indicator with attempt number
- ✅ Input file validation
- ✅ Easy to use command line interface

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

## Installation

1. Clone or download this script
2. Install dependencies: 
```bash 
pip install pikepdf 
```

## Use

### Syntax Dasar
```bash
python bf.py -f <path_file_pdf> -w <path_wordlist>
```

### Parameter
- `-f, --file`: Path ke file PDF yang ingin di-crack (required)
- `-w, --wordlist`: Path ke file wordlist yang berisi daftar password (required)

### Usage examples

1. **Basic usage:**
   ```bash
   python bf.py -f document.pdf -w passwords.txt
   ```

2. **With full path:**
   ```bash
   python bf.py -f /path/to/encrypted.pdf -w /path/to/wordlist.txt
   ```

3. **Using a common wordlist:**
   ```bash
   python bf.py -f target.pdf -w /usr/share/wordlists/rockyou.txt
   ```

## Wordlist Format

Wordlist must be a text file with one password per line:
```
password
123456
admin
password123
letmein
```

## Output

### Password Found
```
[+] Mulai brute force pada file: document.pdf
[1] Mencoba: password
[2] Mencoba: 123456
[3] Mencoba: admin
[✓] Password ditemukan: 'admin'
```

### Password Not Found
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

## Usage Tips

1. **Use the right wordlist:**
   - For personal PDFs: common passwords, birth dates, names
   - For corporate PDFs: a combination of company name, year, etc.
   - Large wordlists: rockyou.txt, common-passwords.txt

2. **Performance optimization:**
   - Start with short and common passwords
   - Use wordlists sorted by popularity
   - Monitor CPU and memory usage

3. **Security:**
   - Only use on PDF files you own
   - Do not use for illegal purposes
   - Backup PDF files before trying

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'pikepdf'
```bash
pip install pikepdf
```

### Error: Permission denied
```bash
chmod +x bf.py
```

### File not found
- Make sure the PDF file path and wordlist are correct
- Use absolute path if necessary
- Check file permissions

## Ethical Usage

⚠️ **IMPORTANT**: This tool should only be used for:
- Own PDF files
- Authorized penetration testing
- Educational purposes
- Legitimate password recovery

❌ **DO NOT** use for:
- Accessing other people's PDF files without permission
- Illegal activities
- Violating other people's privacy

## Limitations

- Speed ​​depends on password complexity and wordlist size
- Not effective for very complex or long passwords
- Memory usage increases with large wordlists

## License

This tool is made for educational and testing purposes. Users are responsible for the use of this tool.

## Author

Created for IDN Cyber ​​Security Bootcamp

---

**Disclaimer**: This tool is made for educational and security testing purposes. Irresponsible use is at the user's own risk.

