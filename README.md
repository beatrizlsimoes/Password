# Python Brute Force Password Simulation

## Overview

This project is an **educational Python script** that demonstrates how a brute‑force attack works.  
The program systematically tests **all possible character combinations** until it finds a predefined secret password.

> ⚠️ This project is for **learning purposes only**.  
> Do NOT use it to access real accounts or systems.

---

## Features

- Uses **lowercase letters, uppercase letters, numbers, and symbols**
- Counts the **number of attempts**
- Measures **execution time**
- Shows **progress during long runs**
- Demonstrates the **exponential difficulty** of cracking strong passwords

---

## Requirements

- Python **3.x**
- No external libraries needed (only built‑in Python modules)

Check Python version:

```bash
python --version
```

---

## Installation

Clone this repository:

```bash
git clone https://github.com/beatrizlsimoes/python-password-password.git
cd python-password-password
```

---

## Usage

1. Open the file `password.py`
2. Define the secret password inside the script:

```python
secret_password = "abc"
```

3. Run the program in the terminal:

```bash
python password.py
```

4. The script will try every possible combination until the password is found.

> 💡 Tip:  
> Reduce `max_length` if the program takes too long to run.

---

## Example Output

```
Attempts so far: 100000
Attempts so far: 200000
Password found: abc 
Attempts: 345678
Time: 12.3456 seconds
```

---

## What This Project Teaches

- Why **short passwords are insecure**
- How **character variety increases security**
- Why **long passwords (12+ characters)** are extremely hard to brute force
- Basic concepts of **cybersecurity and password protection**

---

## Project Structure

```
python-password-password/
│
├── password.py
└── README.md
```

---

## Disclaimer

This code is intended **only for educational and ethical cybersecurity learning**.  
The author is **not responsible for misuse** of this project.

---

## License

Open‑source and free to use for **educational purposes**.




