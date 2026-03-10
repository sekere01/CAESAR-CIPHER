<div align="center">

# 🔐 Caesar Cipher Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A Python desktop application to encrypt and decrypt text using the Caesar Cipher algorithm — featuring a clean GUI, clipboard support, and full input validation.

</div>

---

## 📸 Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. This tool brings it to life with a user-friendly GUI built in Python's `tkinter`, allowing you to encrypt and decrypt messages instantly with any shift value.

---

## ✨ Features

### 🖥️ User-Friendly GUI
- Clean, modern interface with themed `ttk` widgets
- Responsive layout that works on different screen sizes
- Clear labeling and intuitive organisation

### 🔑 Caesar Cipher Functionality
- Encrypt messages with any integer shift value
- Decrypt messages using the same shift value
- Handles both **uppercase** and **lowercase** letters
- Preserves non-alphabetic characters (spaces, punctuation, numbers, etc.)

### ⚙️ Additional Features
- 📋 Copy result to clipboard with one click
- ✅ Input validation to prevent errors
- 🔢 Default shift value of `3` (the traditional Caesar cipher)
- 📝 Large text areas for comfortable message entry

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- `tkinter` (included with standard Python installations)

### Installation

```bash
# Clone the repository
git clone https://github.com/sekere01/caesar-cipher.git

# Navigate into the directory
cd caesar-cipher

# Run the application
python caesarcipher.py
```

---

## 🛠️ How It Works

The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet.

**Example with shift = 3:**

| Input | Output |
|---|---|
| `HELLO` | `KHOOR` |
| `WORLD` | `ZRUOG` |
| `hello world` | `khoor zruog` |

**Encryption formula:**
```
encrypted = (char_position + shift) % 26
```

**Decryption** simply applies a negative shift:
```
decrypted = (char_position - shift) % 26
```

---

## 📖 Usage

1. **Enter your message** in the top text area
2. **Set the shift value** (default is `3`)
3. **Select operation** — Encrypt or Decrypt
4. Click **Process**
5. View the result and optionally click **Copy Result** to copy to clipboard

---

## 📁 Project Structure

```
caesar-cipher/
│
├── caesarcipher.py   # Main application file
└── README.md          # Project documentation
```

---

## 🧠 Algorithm

```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Preserve spaces, punctuation, etc.
    return result
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 Disclaimer

This tool is intended for **educational purposes only**. The Caesar Cipher is not suitable for securing sensitive or real-world data.
