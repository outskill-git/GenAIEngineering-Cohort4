# Git Installation Guide

This guide will help you download, install, and verify Git on your computer. Git is essential for downloading course materials and managing your code throughout the GenAI Engineering course.

## Table of Contents
- [What is Git?](#what-is-git)
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Verify Installation](#verify-installation)
- [Initial Configuration](#initial-configuration)
- [Troubleshooting](#troubleshooting)

## What is Git?

Git is a version control system that helps you:
- Download course materials from GitHub
- Track changes in your code
- Save your work to your own repository
- Collaborate with others

You'll use Git throughout this course to access weekly materials and save your assignments.

---

## Windows Installation

### Method 1: Using Git for Windows (Recommended)

**Step 1: Download Git**

1. Go to the official Git website: [https://git-scm.com/download/windows](https://git-scm.com/download/windows)
2. The download should start automatically
3. If not, click on "Click here to download manually"
4. Download the latest version (64-bit Git for Windows Setup)

**Step 2: Run the Installer**

1. Locate the downloaded file (usually in your Downloads folder)
2. Double-click `Git-2.xx.x-64-bit.exe` to run the installer
3. Click "Yes" if Windows asks for permission

**Step 3: Installation Wizard**

Follow these settings in the installation wizard:

1. **License Agreement**: Click "Next"

2. **Select Destination Location**: 
   - Use the default location: `C:\Program Files\Git`
   - Click "Next"

3. **Select Components**: 
   - Keep all default selections checked
   - Optionally check "On the Desktop" for a Git Bash shortcut
   - Click "Next"

4. **Select Start Menu Folder**:
   - Keep default: "Git"
   - Click "Next"

5. **Choosing the default editor used by Git**:
   - Select "Use Visual Studio Code as Git's default editor" (if you have VS Code)
   - OR select "Use Vim" (default)
   - Click "Next"

6. **Adjusting the name of the initial branch**:
   - Select "Let Git decide" or "Override the default branch name for new repositories" and enter "main"
   - Click "Next"

7. **Adjusting your PATH environment**:
   - ⭐ **Important**: Select "Git from the command line and also from 3rd-party software"
   - This allows you to use Git from Command Prompt, PowerShell, and other tools
   - Click "Next"

8. **Choosing the SSH executable**:
   - Select "Use bundled OpenSSH"
   - Click "Next"

9. **Choosing HTTPS transport backend**:
   - Select "Use the OpenSSL library"
   - Click "Next"

10. **Configuring the line ending conversions**:
    - Select "Checkout Windows-style, commit Unix-style line endings"
    - Click "Next"

11. **Configuring the terminal emulator**:
    - Select "Use MinTTY (the default terminal of MSYS2)"
    - Click "Next"

12. **Choose the default behavior of 'git pull'**:
    - Select "Default (fast-forward or merge)"
    - Click "Next"

13. **Choose a credential helper**:
    - Select "Git Credential Manager"
    - Click "Next"

14. **Configuring extra options**:
    - Keep defaults (Enable file system caching checked)
    - Click "Next"

15. **Configuring experimental options**:
    - Leave unchecked
    - Click "Install"

**Step 4: Complete Installation**

1. Wait for the installation to complete
2. Uncheck "View Release Notes" (optional)
3. Click "Finish"

**Step 5: Verify Installation**

Open Command Prompt or PowerShell:
```cmd
git --version
```

You should see something like:
```
git version 2.43.0.windows.1
```

### Method 2: Using Winget (Windows Package Manager)

If you have Windows 11 or Windows 10 with Winget installed:

```powershell
# Open PowerShell as Administrator
winget install --id Git.Git -e --source winget
```

### Method 3: Using Chocolatey

If you have Chocolatey package manager installed:

```powershell
# Open PowerShell as Administrator
choco install git
```

---

## macOS Installation

### Method 1: Using Homebrew (Recommended)

**Step 1: Install Homebrew** (if you don't have it)

Open Terminal and run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2: Install Git**

```bash
brew install git
```

**Step 3: Verify Installation**

```bash
git --version
```

You should see something like:
```
git version 2.43.0
```

### Method 2: Using Xcode Command Line Tools

**Step 1: Install Command Line Tools**

Open Terminal and run:
```bash
xcode-select --install
```

A popup will appear asking you to install the tools.

**Step 2: Click "Install"**

Follow the prompts to complete installation.

**Step 3: Verify Installation**

```bash
git --version
```

### Method 3: Download from Git Website

**Step 1: Download**

1. Go to [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
2. Download the latest macOS installer

**Step 2: Install**

1. Open the downloaded `.dmg` file
2. Double-click the `.pkg` file
3. Follow the installation wizard
4. Enter your password when prompted

**Step 3: Verify**

Open Terminal:
```bash
git --version
```

---

## Linux Installation

### Ubuntu/Debian

**Step 1: Update Package Index**

Open Terminal and run:
```bash
sudo apt update
```

**Step 2: Install Git**

```bash
sudo apt install git -y
```

**Step 3: Verify Installation**

```bash
git --version
```

You should see something like:
```
git version 2.34.1
```

### Fedora

**Step 1: Install Git**

```bash
sudo dnf install git -y
```

**Step 2: Verify Installation**

```bash
git --version
```

### CentOS/RHEL

**For CentOS/RHEL 8 and later:**

```bash
sudo dnf install git -y
```

**For CentOS/RHEL 7 and earlier:**

```bash
sudo yum install git -y
```

**Verify:**

```bash
git --version
```

### Arch Linux

**Step 1: Install Git**

```bash
sudo pacman -S git
```

**Step 2: Verify Installation**

```bash
git --version
```

### openSUSE

**Step 1: Install Git**

```bash
sudo zypper install git
```

**Step 2: Verify Installation**

```bash
git --version
```

---

## Verify Installation

After installing Git on any platform, verify it's working correctly:

### Check Git Version

Open your terminal (Command Prompt, PowerShell, Terminal, or Git Bash) and run:

```bash
git --version
```

**Expected Output:**
```
git version 2.43.0
```

The exact version number may vary, but you should see "git version" followed by numbers.

### Check Git Help

```bash
git --help
```

This should display Git's help information with available commands.

### Test Git Commands

```bash
# Check if git is in your PATH
which git          # On macOS/Linux
where git          # On Windows

# Test a simple git command
git status
```

If you're not in a Git repository, you'll see:
```
fatal: not a git repository (or any of the parent directories): .git
```

This is normal and means Git is working correctly!

---

## Initial Configuration

After installing Git, you need to configure your identity. This information will be attached to your commits.

### Set Your Name and Email

Open your terminal and run these commands (replace with your actual name and email):

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your.email@example.com"
```

**Example:**
```bash
git config --global user.name "Jane Doe"
git config --global user.email "jane.doe@gmail.com"
```

### Set Default Branch Name to 'main'

```bash
git config --global init.defaultBranch main
```

### Configure Line Endings

**On Windows:**
```bash
git config --global core.autocrlf true
```

**On macOS/Linux:**
```bash
git config --global core.autocrlf input
```

### Verify Your Configuration

```bash
# View all settings
git config --list

# View specific settings
git config user.name
git config user.email
```

**Expected Output:**
```
user.name=Your Name
user.email=your.email@example.com
init.defaultbranch=main
core.autocrlf=true
```

### Optional: Configure Default Editor

If you want to use a specific editor for Git commit messages:

**Visual Studio Code:**
```bash
git config --global core.editor "code --wait"
```

**Sublime Text:**
```bash
git config --global core.editor "subl -n -w"
```

**Nano (simple terminal editor):**
```bash
git config --global core.editor nano
```

**Vim (default on many systems):**
```bash
git config --global core.editor vim
```

---

## Troubleshooting

### Windows Issues

**Issue: "git: command not found" or "'git' is not recognized"**

**Solution 1: Restart your terminal**
- Close Command Prompt/PowerShell completely
- Open a new terminal window
- Try `git --version` again

**Solution 2: Check PATH environment variable**
1. Open System Properties → Environment Variables
2. Look for `Path` in System Variables
3. Check if `C:\Program Files\Git\cmd` is listed
4. If not, click "Edit" and add it
5. Click OK and restart your terminal

**Solution 3: Reinstall Git**
- Uninstall Git from Control Panel
- Download and reinstall from [git-scm.com](https://git-scm.com/)
- Make sure to select "Git from the command line and also from 3rd-party software" during installation

**Issue: Permission denied errors**

**Solution:**
- Run Command Prompt or PowerShell as Administrator
- Right-click the application and select "Run as administrator"

### macOS Issues

**Issue: "git: command not found"**

**Solution 1: Install Xcode Command Line Tools**
```bash
xcode-select --install
```

**Solution 2: Check if Git is installed via Homebrew**
```bash
brew list | grep git
```

If not listed, install it:
```bash
brew install git
```

**Solution 3: Update PATH**

Add to your `~/.zshrc` or `~/.bash_profile`:
```bash
export PATH="/usr/local/bin:$PATH"
```

Then reload:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

**Issue: "xcrun: error: invalid active developer path"**

**Solution:**
```bash
xcode-select --install
```

### Linux Issues

**Issue: "git: command not found"**

**Solution: Install Git**

Ubuntu/Debian:
```bash
sudo apt update
sudo apt install git -y
```

Fedora:
```bash
sudo dnf install git -y
```

**Issue: "E: Unable to locate package git"**

**Solution: Update package repositories**
```bash
sudo apt update
sudo apt upgrade
```

Then try installing again:
```bash
sudo apt install git -y
```

**Issue: Permission errors**

**Solution: Use sudo**
```bash
sudo apt install git -y
```

### General Issues

**Issue: Old version of Git**

**Solution: Update Git**

Windows (with Git Bash):
```bash
git update-git-for-windows
```

macOS (with Homebrew):
```bash
brew upgrade git
```

Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt upgrade git
```

**Issue: Configuration not saving**

**Solution: Check Git config file location**
```bash
# View where config is stored
git config --list --show-origin

# Edit global config directly
git config --global --edit
```

**Issue: "SSL certificate problem"**

**Solution (temporary, not recommended for production):**
```bash
git config --global http.sslVerify false
```

**Better solution: Update certificates**

Windows:
```bash
git config --global http.sslBackend schannel
```

macOS/Linux:
```bash
# Update CA certificates
sudo apt install ca-certificates  # Ubuntu/Debian
brew install ca-certificates       # macOS
```

---

## Quick Installation Commands Summary

### Windows
```powershell
# Download from: https://git-scm.com/download/windows
# Or use Winget:
winget install --id Git.Git -e --source winget
```

### macOS
```bash
# Using Homebrew (recommended):
brew install git

# Or install Xcode Command Line Tools:
xcode-select --install
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git -y
```

### Linux (Fedora)
```bash
sudo dnf install git -y
```

### Verify Installation (All Platforms)
```bash
git --version
```

### Initial Configuration (All Platforms)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

---

## Next Steps

After successfully installing and configuring Git:

1. ✅ Verify Git is installed: `git --version`
2. ✅ Configure your name and email
3. ✅ Create a GitHub account if you don't have one: [github.com/join](https://github.com/join)
4. 📚 Move on to the course README to download course materials
5. 🚀 Set up your personal repository for saving your work

---

## Additional Resources

- **Official Git Documentation**: [https://git-scm.com/doc](https://git-scm.com/doc)
- **Git Tutorial**: [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
- **GitHub Git Handbook**: [https://guides.github.com/introduction/git-handbook/](https://guides.github.com/introduction/git-handbook/)
- **Interactive Git Tutorial**: [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
- **Git Cheat Sheet**: [https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---

**You're all set! 🎉**

Git is now installed and configured on your system. You're ready to start working with the course repository and managing your code!
