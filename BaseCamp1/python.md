# Python 3.11 Installation Guide

This course requires **Python 3.11.9**. Follow the instructions for your operating system below.

## Table of Contents
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Troubleshooting](#troubleshooting-python-installation)
- [Quick Validation](#quick-validation-checklist)

---

## Windows Installation

### Step 1: Download Python 3.11.9

1. Visit: https://www.python.org/downloads/release/python-3119/
2. Scroll down to the "Files" section
3. Download: **Windows installer (64-bit)** - `python-3.11.9-amd64.exe`
   - For 32-bit systems: Download **Windows installer (32-bit)** - `python-3.11.9.exe`

### Step 2: Install Python

1. Run the downloaded `.exe` file
2. ⚠️ **IMPORTANT:** Check the box **"Add Python 3.11 to PATH"** at the bottom of the installer
3. Click **"Install Now"**
4. Wait for installation to complete
5. Click **"Close"** when finished

### Step 3: Verify Installation

1. Open **Command Prompt** (search for "cmd" in Start menu)
2. Run these commands:

```bash
python --version
```
**Expected output:** `Python 3.11.9`

```bash
pip --version
```
**Expected output:** `pip 24.0 from ... (python 3.11)`

```bash
python -c "print('Hello, Python!')"
```
**Expected output:** `Hello, Python!`

✅ If all three commands work, your installation is successful!

#### Alternative: Using the Python Launcher (py)

If the `python` command doesn't work, Windows also provides a `py` launcher. Try these commands:

```bash
py --version
# or
py -3.11 --version
```
**Expected output:** `Python 3.11.9`

```bash
py -m pip --version
# or
py -3.11 -m pip --version
```
**Expected output:** `pip 24.0 from ... (python 3.11)`

**Note:** The `py` launcher is helpful when you have multiple Python versions installed. Use `py -3.11` to specifically run Python 3.11.

#### Which command should I use?

Windows users can use either:
- `python` and `pip` (if Python was added to PATH during installation)
- `py` and `py -m pip` (using the Python launcher)
- `py -3.11` and `py -3.11 -m pip` (to specifically target Python 3.11)

All three methods work - use whichever works on your system!

---

## macOS Installation

### Step 1: Download Python 3.11.9

1. Visit: https://www.python.org/downloads/release/python-3119/
2. Scroll down to the "Files" section
3. Download: **macOS 64-bit universal2 installer** - `python-3.11.9-macos11.pkg`

### Step 2: Install Python

1. Open the downloaded `.pkg` file
2. Follow the installation wizard:
   - Click **"Continue"**
   - Click **"Agree"** to the license
   - Click **"Install"**
3. Enter your password if prompted
4. Click **"Close"** when finished

### Step 3: Verify Installation

1. Open **Terminal** (search for "Terminal" in Spotlight or go to Applications → Utilities → Terminal)
2. Run these commands:

```bash
python3.11 --version
```
**Expected output:** `Python 3.11.9`

```bash
pip3.11 --version
```
**Expected output:** `pip 24.0 from ... (python 3.11)`

```bash
python3.11 -c "print('Hello, Python!')"
```
**Expected output:** `Hello, Python!`

**Important Note:** On macOS, you must use `python3.11` and `pip3.11` (not just `python` or `pip`), as macOS comes with an older system Python.

✅ If all three commands work, your installation is successful!

---

## Linux Installation

### Ubuntu/Debian

#### Step 1: Install Python 3.11

Open Terminal and run these commands:

```bash
# Update package list
sudo apt update

# Install required packages
sudo apt install software-properties-common

# Add deadsnakes PPA (provides Python 3.11)
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package list again
sudo apt update

# Install Python 3.11 and related packages
sudo apt install python3.11 python3.11-venv python3.11-dev
```

#### Step 2: Install pip for Python 3.11

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

#### Step 3: Verify Installation

```bash
python3.11 --version
```
**Expected output:** `Python 3.11.9` or `Python 3.11.x`

```bash
python3.11 -m pip --version
```
**Expected output:** `pip 24.0 from ... (python 3.11)`

```bash
python3.11 -c "print('Hello, Python!')"
```
**Expected output:** `Hello, Python!`

✅ If all three commands work, your installation is successful!

---

### Fedora/RHEL/CentOS

#### Step 1: Install Python 3.11

```bash
sudo dnf install python3.11 python3.11-pip python3.11-devel
```

#### Step 2: Verify Installation

```bash
python3.11 --version
python3.11 -m pip --version
python3.11 -c "print('Hello, Python!')"
```

---

### Arch Linux

#### Step 1: Install Python 3.11

```bash
sudo pacman -S python311
```

#### Step 2: Verify Installation

```bash
python3.11 --version
python3.11 -m pip --version
python3.11 -c "print('Hello, Python!')"
```

---

## Troubleshooting Python Installation

### Windows Issues

#### Problem: "python is not recognized as an internal or external command"

**Cause:** Python wasn't added to PATH during installation.

**Solution 1 (Quick Fix):** Use the `py` launcher instead
```bash
py --version           # Instead of: python --version
py -3.11 --version     # To specifically use Python 3.11
py -m pip --version    # Instead of: pip --version
```

The `py` launcher is installed automatically with Python and doesn't require PATH configuration.

**Solution 2 (Recommended):** Reinstall Python with PATH
1. Uninstall Python from Settings → Apps
2. Download the installer again
3. Run it and **make sure to check "Add Python 3.11 to PATH"**

**Solution 3:** Manually add Python to PATH
1. Press `Windows + R`, type `sysdm.cpl`, and press Enter
2. Click **"Advanced"** tab → **"Environment Variables"**
3. Under "System variables", find **"Path"** and click **"Edit"**
4. Click **"New"** and add these two paths (replace `YourUsername` with your actual username):
   - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311`
   - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts`
5. Click **OK** on all windows
6. Close and reopen Command Prompt

#### Problem: Wrong Python version showing

**Solution:** If you have multiple Python versions, use the `py` launcher with version flag:
```bash
py -3.11 --version     # Run Python 3.11 specifically
py -3.10 --version     # Run Python 3.10 specifically
py -0                  # List all installed Python versions
```

#### Problem: "pip is not recognized"

**Solution:** Use pip through the `py` launcher:
```bash
py -m pip --version
py -3.11 -m pip install package_name
```

---

### macOS Issues

#### Problem: "command not found: python3.11"

**Cause:** Python 3.11 wasn't installed correctly or not in PATH.

**Solution:** 
1. Reinstall Python using the `.pkg` installer
2. After installation, try the verification commands again
3. If still not working, try:
   ```bash
   /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 --version
   ```

#### Problem: "python --version" shows old version

**Solution:** macOS has a system Python. Always use `python3.11` for this course:
```bash
python3.11 --version  # ✅ Correct
python --version      # ❌ This shows system Python
```

---

### Linux Issues

#### Problem: "command not found: python3.11"

**Cause:** Python 3.11 wasn't installed correctly.

**Solution:** Follow the installation steps again for your distribution.

#### Problem: "E: Unable to locate package python3.11" (Ubuntu/Debian)

**Cause:** The deadsnakes PPA wasn't added correctly.

**Solution:**
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
```

---

### Common Issues (All Platforms)

#### Problem: pip not working

**Windows (Option 1 - using python):**
```bash
python -m pip --version
```

**Windows (Option 2 - using py launcher):**
```bash
py -m pip --version
# or specifically for Python 3.11:
py -3.11 -m pip --version
```

**macOS/Linux:**
```bash
python3.11 -m pip --version
```

If pip is missing, reinstall Python or install pip separately.

#### Problem: Multiple Python versions installed

**Windows:** Use the `py` launcher to select versions:
```bash
py -0                   # List all installed Python versions
py -3.11                # Run Python 3.11
py -3.10                # Run Python 3.10
py -3.11 -m pip         # Use pip for Python 3.11
py -3.11 -m pip install package  # Install package with Python 3.11
```

**macOS/Linux:** Use version-specific commands:
```bash
python3.11      # Run Python 3.11
python3.10      # Run Python 3.10
python3.9       # Run Python 3.9
```

#### Problem: Not sure which Python versions are installed

**Windows:**
```bash
py -0           # Lists all installed Python versions
```

**macOS/Linux:**
```bash
ls /usr/bin/python*      # Ubuntu/Debian
ls /usr/local/bin/python*  # macOS
```

---

## Quick Validation Checklist

Use this checklist to confirm your Python 3.11.9 installation is working correctly.

### Windows

Open Command Prompt and run:

**Option 1: Using `python` command** (if Python is in PATH):
```bash
# Check Python version
python --version
# Expected: Python 3.11.9

# Check pip version
pip --version
# Expected: pip X.X from ... (python 3.11)

# Test Python execution
python -c "print('Hello, Python!')"
# Expected: Hello, Python!

# Test pip installation (optional)
pip install requests
# Should install without errors
```

**Option 2: Using `py` launcher** (works even without PATH):
```bash
# Check Python version
py --version
# or to be specific:
py -3.11 --version
# Expected: Python 3.11.9

# Check pip version
py -m pip --version
# or:
py -3.11 -m pip --version
# Expected: pip X.X from ... (python 3.11)

# Test Python execution
py -c "print('Hello, Python!')"
# or:
py -3.11 -c "print('Hello, Python!')"
# Expected: Hello, Python!

# Test pip installation (optional)
py -m pip install requests
# or:
py -3.11 -m pip install requests
# Should install without errors
```

**Note:** Use whichever option works on your system. Both are correct!

### macOS

Open Terminal and run:

```bash
# Check Python version
python3.11 --version
# Expected: Python 3.11.9

# Check pip version
pip3.11 --version
# Expected: pip X.X from ... (python 3.11)

# Test Python execution
python3.11 -c "print('Hello, Python!')"
# Expected: Hello, Python!

# Test pip installation (optional)
pip3.11 install requests
# Should install without errors
```

### Linux

Open Terminal and run:

```bash
# Check Python version
python3.11 --version
# Expected: Python 3.11.9 or Python 3.11.x

# Check pip version
python3.11 -m pip --version
# Expected: pip X.X from ... (python 3.11)

# Test Python execution
python3.11 -c "print('Hello, Python!')"
# Expected: Hello, Python!

# Test pip installation (optional)
python3.11 -m pip install requests
# Should install without errors
```

---

## Summary of Commands by Platform

| Task | Windows (Option 1) | Windows (Option 2) | macOS | Linux |
|------|-------------------|-------------------|-------|-------|
| Run Python | `python` | `py` or `py -3.11` | `python3.11` | `python3.11` |
| Run pip | `pip` | `py -m pip` | `pip3.11` | `python3.11 -m pip` |
| Check version | `python --version` | `py --version` or `py -3.11 --version` | `python3.11 --version` | `python3.11 --version` |
| Install package | `pip install package` | `py -m pip install package` | `pip3.11 install package` | `python3.11 -m pip install package` |
| List Python versions | N/A | `py -0` | N/A | N/A |

**Windows Notes:**
- **Option 1** requires Python to be in PATH (check "Add Python to PATH" during installation)
- **Option 2** uses the Python Launcher (`py`) which works even without PATH configuration
- Use `py -3.11` to specifically target Python 3.11 when you have multiple versions installed

---

## Need More Help?

If you're still having issues:

1. Check that you downloaded the correct installer for your system (64-bit vs 32-bit)
2. Make sure you have administrator/sudo privileges
3. Try restarting your computer after installation
4. Check the [official Python documentation](https://docs.python.org/3.11/)
5. Ask for help in the course discussion forum

---

**Happy Coding! 🐍**
