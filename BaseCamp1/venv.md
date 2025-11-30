# Python Virtual Environment Guide

Learn how to create, activate, manage, and deactivate Python virtual environments using a **dedicated venvs folder** for better organization.

## Table of Contents

- [What is a Virtual Environment?](#what-is-a-virtual-environment)
- [Why Use Virtual Environments?](#why-use-virtual-environments)
- [Recommended Folder Structure](#recommended-folder-structure)
- [Windows Setup](#windows-setup)
- [Linux Setup](#linux-setup)
- [macOS Setup](#macos-setup)
- [Managing Multiple Environments](#managing-multiple-environments)
- [Troubleshooting](#troubleshooting)

---

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install packages specific to a project without affecting your system-wide Python installation or other projects.

## Why Use Virtual Environments?

✅ **Isolation**: Each project has its own dependencies
✅ **Version Control**: Different projects can use different package versions
✅ **Clean System**: Keeps your system Python clean
✅ **Reproducibility**: Easy to share exact package versions with teammates
✅ **No Conflicts**: Avoid package version conflicts between projects

---

## Recommended Folder Structure

We'll use a **dedicated `venvs` folder** to store all virtual environments in one place:

```
📁 Your Documents or Home folder
├── 📁 venvs/                        # All virtual environments here
│   ├── 📁 old_numpy_env/            # Environment with NumPy 1.26.4
│   ├── 📁 new_numpy_env/            # Environment with NumPy 2.2.0
│   ├── 📁 week1_env/
│   └── 📁 week2_env/
│
├── 📁 Projects/                     # Your actual project code
│   ├── 📁 OldProjects/              # Uses old_numpy_env
│   ├── 📁 NewProjects/              # Uses new_numpy_env
│   ├── 📁 Week1/
│   └── 📁 Week2/
```

**Benefits of this approach:**

- All environments in one location - easy to find and manage
- Project folders stay clean (no `venv` folder cluttering each project)
- Easy to delete old environments
- Clear separation between code and environments
- Can have different NumPy versions for different projects

---

## Windows Setup

### Step 1: Create the venvs Folder

Open **Command Prompt** and create a dedicated folder for virtual environments:

```bash
# Create venvs folder in your user directory
cd %USERPROFILE%
mkdir venvs
```

Or place it in your Documents folder:

```bash
cd %USERPROFILE%\Documents
mkdir venvs
```

### Step 2: Create a Virtual Environment

**Using `python` command:**

```bash
# Navigate to venvs folder
cd %USERPROFILE%\venvs

# Create a virtual environment named "old_numpy_env"
python -m venv old_numpy_env
```

**Using `py` launcher (recommended for multiple Python versions):**

```bash
# Navigate to venvs folder
cd %USERPROFILE%\venvs

# Create a virtual environment with Python 3.11
py -3.11 -m venv old_numpy_env
```

### Step 3: Activate the Virtual Environment

**Using Command Prompt (CMD):**

```bash
# Activate old_numpy_env
%USERPROFILE%\venvs\old_numpy_env\Scripts\activate
```

**Using PowerShell:**

```bash
# Activate old_numpy_env
& "$env:USERPROFILE\venvs\old_numpy_env\Scripts\Activate.ps1"
```

**If you get a PowerShell error, run this first:**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**After activation**, you'll see `(old_numpy_env)` at the start of your prompt:

```
(old_numpy_env) C:\Users\YourName>
```

### Step 4: Install Packages

```bash
# Install NumPy and Pandas with specific versions
pip install numpy==1.26.4 pandas==2.2.0

# Or install latest versions
pip install numpy pandas

# Verify installation
pip list
```

### Step 5: Work on Your Project

```bash
# Navigate to your project folder (keep environment activated)
cd %USERPROFILE%\Documents\Projects\Week1

# Run your Python scripts
python your_script.py
```

### Step 6: Deactivate When Done

```bash
deactivate
```

### Complete Windows Example

**Command Prompt - Creating Environment with Old NumPy (1.26.4):**

```bash
# Create venvs folder (one-time setup)
cd %USERPROFILE%
mkdir venvs

# Create virtual environment for old NumPy projects
cd venvs
python -m venv old_numpy_env

# Activate environment
old_numpy_env\Scripts\activate

# Install old NumPy and Pandas
pip install numpy==1.26.4 pandas==2.2.0

# Verify installation
pip list

# Navigate to your project and work
cd %USERPROFILE%\Documents\Projects\Week1
python analysis.py

# Deactivate when done
deactivate
```

**PowerShell - Creating Environment with New NumPy (2.2.0):**

```bash
# Navigate to venvs folder
cd $env:USERPROFILE\venvs

# Create virtual environment for new NumPy projects
py -3.11 -m venv new_numpy_env

# Activate environment
& ".\new_numpy_env\Scripts\Activate.ps1"

# Install new NumPy and Pandas
pip install numpy==2.2.0 pandas==2.2.0

# Verify installation
pip list

# Navigate to your project and work
cd $env:USERPROFILE\Documents\Projects\Week2
python analysis.py

# Deactivate when done
deactivate
```

**Switching Between Environments:**

```bash
# Work with old NumPy
cd %USERPROFILE%\venvs
old_numpy_env\Scripts\activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 1.26.4
deactivate

# Work with new NumPy
cd %USERPROFILE%\venvs
new_numpy_env\Scripts\activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 2.2.0
deactivate
```

---

## Linux Setup

### Step 1: Create the venvs Folder

Open **Terminal** and create a dedicated folder for virtual environments:

```bash
# Create venvs folder in your home directory
cd ~
mkdir venvs
```

### Step 2: Create a Virtual Environment

```bash
# Navigate to venvs folder
cd ~/venvs

# Create a virtual environment named "old_numpy_env"
python3.11 -m venv old_numpy_env
```

### Step 3: Activate the Virtual Environment

```bash
# Activate old_numpy_env
source ~/venvs/old_numpy_env/bin/activate
```

**After activation**, you'll see `(old_numpy_env)` at the start of your prompt:

```
(old_numpy_env) user@hostname:~$
```

### Step 4: Install Packages

```bash
# Install NumPy and Pandas with specific versions
pip install numpy==1.26.4 pandas==2.2.0

# Or install latest versions
pip install numpy pandas

# Verify installation
pip list
```

### Step 5: Work on Your Project

```bash
# Navigate to your project folder (keep environment activated)
cd ~/Projects/Week1

# Run your Python scripts
python your_script.py
```

### Step 6: Deactivate When Done

```bash
deactivate
```

### Complete Linux Example

**Creating Environment with Old NumPy (1.26.4):**

```bash
# Create venvs folder (one-time setup)
mkdir ~/venvs

# Create virtual environment for old NumPy projects
cd ~/venvs
python3.11 -m venv old_numpy_env

# Activate environment
source ~/venvs/old_numpy_env/bin/activate

# Install old NumPy and Pandas
pip install numpy==1.26.4 pandas==2.2.0

# Verify installation
pip list

# Navigate to your project and work
cd ~/Projects/Week1
python analysis.py

# Deactivate when done
deactivate
```

**Creating Environment with New NumPy (2.2.0):**

```bash
# Create virtual environment for new NumPy projects
cd ~/venvs
python3.11 -m venv new_numpy_env

# Activate environment
source ~/venvs/new_numpy_env/bin/activate

# Install new NumPy and Pandas
pip install numpy==2.2.0 pandas==2.2.0

# Verify installation
pip list

# Navigate to your project and work
cd ~/Projects/Week2
python analysis.py

# Deactivate when done
deactivate
```

**Switching Between Environments:**

```bash
# Work with old NumPy
source ~/venvs/old_numpy_env/bin/activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 1.26.4
deactivate

# Work with new NumPy
source ~/venvs/new_numpy_env/bin/activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 2.2.0
deactivate
```

### Creating Aliases for Easy Activation (Optional)

Add this to your `~/.bashrc` or `~/.zshrc` file:

```bash
# Add aliases for activating environments
alias activate-old-numpy="source ~/venvs/old_numpy_env/bin/activate"
alias activate-new-numpy="source ~/venvs/new_numpy_env/bin/activate"
```

Then reload your shell:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

Now you can activate with simple commands:

```bash
activate-old-numpy
# or
activate-new-numpy
```

---

## macOS Setup

### Step 1: Create the venvs Folder

Open **Terminal** and create a dedicated folder for virtual environments:

```bash
# Create venvs folder in your home directory
cd ~
mkdir venvs
```

### Step 2: Create a Virtual Environment

```bash
# Navigate to venvs folder
cd ~/venvs

# Create a virtual environment named "old_numpy_env"
python3.11 -m venv old_numpy_env
```

### Step 3: Activate the Virtual Environment

```bash
# Activate old_numpy_env
source ~/venvs/old_numpy_env/bin/activate
```

**After activation**, you'll see `(old_numpy_env)` at the start of your prompt:

```
(old_numpy_env) username@MacBook ~ %
```

### Step 4: Install Packages

```bash
# Install NumPy and Pandas with specific versions
pip install numpy==1.26.4 pandas==2.2.0

# Or install latest versions
pip install numpy pandas

# Verify installation
pip list
```

### Step 5: Work on Your Project

```bash
# Navigate to your project folder (keep environment activated)
cd ~/Projects/Week1

# Run your Python scripts
python your_script.py
```

### Step 6: Deactivate When Done

```bash
deactivate
```

### Complete macOS Example

**Creating Environment with Old NumPy (1.26.4):**

```bash
# Create venvs folder (one-time setup)
mkdir ~/venvs

# Create virtual environment for old NumPy projects
cd ~/venvs
python3.11 -m venv old_numpy_env

# Activate environment
source ~/venvs/old_numpy_env/bin/activate

# Install old NumPy and Pandas
pip install numpy==1.26.4 pandas==2.2.0

# Verify installation
pip list

# Navigate to your project and work
cd ~/Projects/Week1
python analysis.py

# Deactivate when done
deactivate
```

**Creating Environment with New NumPy (2.2.0):**

```bash
# Create virtual environment for new NumPy projects
cd ~/venvs
python3.11 -m venv new_numpy_env

# Activate environment
source ~/venvs/new_numpy_env/bin/activate

# Install new NumPy and Pandas
pip install numpy pandas

# Verify installation
pip list

# Navigate to your project and work
cd ~/Projects/Week2
python analysis.py

# Deactivate when done
deactivate
```

**Switching Between Environments:**

```bash
# Work with old NumPy
source ~/venvs/old_numpy_env/bin/activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 1.26.4
deactivate

# Work with new NumPy
source ~/venvs/new_numpy_env/bin/activate
python -c "import numpy; print('NumPy version:', numpy.__version__)"
# Output: NumPy version: 2.2.0
deactivate
```

### Creating Aliases for Easy Activation (Optional)

Add this to your `~/.zshrc` file (macOS uses zsh by default):

```bash
# Add aliases for activating environments
alias activate-old-numpy="source ~/venvs/old_numpy_env/bin/activate"
alias activate-new-numpy="source ~/venvs/new_numpy_env/bin/activate"
```

Then reload your shell:

```bash
source ~/.zshrc
```

Now you can activate with simple commands:

```bash
activate-old-numpy
# or
activate-new-numpy
```

---

## Managing Multiple Environments

With a dedicated `venvs` folder, managing multiple environments is simple and organized.

### Creating Environments for Different NumPy Versions

**Windows:**

```bash
# Navigate to venvs folder
cd %USERPROFILE%\venvs

# Create environment for old NumPy (1.26.4)
python -m venv old_numpy_env
old_numpy_env\Scripts\activate
pip install numpy==1.26.4 pandas==2.2.0
deactivate

# Create environment for new NumPy (2.2.0)
python -m venv new_numpy_env
new_numpy_env\Scripts\activate
pip install numpy==2.2.0 pandas==2.2.0
deactivate

# Create environment for Week 1
python -m venv week1_env
week1_env\Scripts\activate
pip install numpy==1.26.4 pandas==2.2.0 matplotlib
deactivate

# Create environment for Week 2
python -m venv week2_env
week2_env\Scripts\activate
pip install numpy==2.2.0 pandas matplotlib seaborn
deactivate
```

**Linux/macOS:**

```bash
# Navigate to venvs folder
cd ~/venvs

# Create environment for old NumPy (1.26.4)
python3.11 -m venv old_numpy_env
source old_numpy_env/bin/activate
pip install numpy==1.26.4 pandas==2.2.0
deactivate

# Create environment for new NumPy (2.2.0)
python3.11 -m venv new_numpy_env
source new_numpy_env/bin/activate
pip install numpy==2.2.0 pandas==2.2.0
deactivate

# Create environment for Week 1
python3.11 -m venv week1_env
source week1_env/bin/activate
pip install numpy==1.26.4 pandas==2.2.0 matplotlib
deactivate

# Create environment for Week 2
python3.11 -m venv week2_env
source week2_env/bin/activate
pip install numpy==2.2.0 pandas matplotlib seaborn
deactivate
```

### Switching Between Environments

**Windows:**

```bash
# Work with old NumPy
%USERPROFILE%\venvs\old_numpy_env\Scripts\activate
cd %USERPROFILE%\Documents\Projects\OldProject
python script.py
deactivate

# Switch to new NumPy
%USERPROFILE%\venvs\new_numpy_env\Scripts\activate
cd %USERPROFILE%\Documents\Projects\NewProject
python script.py
deactivate
```

**Linux/macOS:**

```bash
# Work with old NumPy
source ~/venvs/old_numpy_env/bin/activate
cd ~/Projects/OldProject
python script.py
deactivate

# Switch to new NumPy
source ~/venvs/new_numpy_env/bin/activate
cd ~/Projects/NewProject
python script.py
deactivate
```

### Verifying Which NumPy Version You're Using

```bash
# Activate environment
# (Windows) %USERPROFILE%\venvs\old_numpy_env\Scripts\activate
# (Linux/macOS) source ~/venvs/old_numpy_env/bin/activate

# Check NumPy version
python -c "import numpy; print('NumPy version:', numpy.__version__)"

# Or use pip
pip show numpy

# Deactivate
deactivate
```

### Listing All Your Environments

**Windows (Command Prompt):**

```bash
dir %USERPROFILE%\venvs
```

**Windows (PowerShell):**

```bash
ls $env:USERPROFILE\venvs
```

**Linux/macOS:**

```bash
ls ~/venvs
```

### Deleting an Environment

**Windows:**

```bash
# Delete old_numpy_env
rmdir /s %USERPROFILE%\venvs\old_numpy_env

# Delete new_numpy_env
rmdir /s %USERPROFILE%\venvs\new_numpy_env
```

**Linux/macOS:**

```bash
# Delete old_numpy_env
rm -rf ~/venvs/old_numpy_env

# Delete new_numpy_env
rm -rf ~/venvs/new_numpy_env
```

### Using requirements.txt

Save your exact package versions to share with teammates or recreate environments:

**Creating requirements.txt:**

```bash
# Activate your environment
# (Windows) %USERPROFILE%\venvs\old_numpy_env\Scripts\activate
# (Linux/macOS) source ~/venvs/old_numpy_env/bin/activate

# Save all installed packages to a file
pip freeze > requirements.txt

# Deactivate
deactivate
```

**Installing from requirements.txt:**

```bash
# Create new environment
# (Windows) cd %USERPROFILE%\venvs && python -m venv new_project_env
# (Linux/macOS) cd ~/venvs && python3.11 -m venv new_project_env

# Activate new environment
# (Windows) new_project_env\Scripts\activate
# (Linux/macOS) source new_project_env/bin/activate

# Install all packages from requirements.txt
pip install -r requirements.txt

# Deactivate
deactivate
```

**Example requirements.txt for old_numpy_env:**

```
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.0
```

**Example requirements.txt for new_numpy_env:**

```
numpy==2.2.0
pandas==2.2.0
matplotlib==3.9.0
seaborn==0.13.0
```

---

## Troubleshooting

### Windows: PowerShell Execution Policy Error

**Problem:** `cannot be loaded because running scripts is disabled`

**Solution:**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### Windows: "python is not recognized"

**Problem:** Python command not found

**Solution:** Use the `py` launcher instead:

```bash
# Create environment with py launcher
cd %USERPROFILE%\venvs
py -3.11 -m venv week1_env

# Activate still works the same way
week1_env\Scripts\activate
```

### Linux/macOS: "command not found: python3.11"

**Problem:** Python 3.11 not installed correctly

**Solution:** Verify Python installation:

```bash
# Check if Python 3.11 is installed
which python3.11

# If not found, install it (see PYTHON_INSTALLATION.md)
```

### Environment Not Activating

**Problem:** Activation command doesn't work

**Solution:** Make sure you're using the correct path:

**Windows:**

```bash
# Full path activation
%USERPROFILE%\venvs\old_numpy_env\Scripts\activate

# Or navigate to venvs first
cd %USERPROFILE%\venvs
old_numpy_env\Scripts\activate
```

**Linux/macOS:**

```bash
# Full path activation
source ~/venvs/old_numpy_env/bin/activate

# Or navigate to venvs first
cd ~/venvs
source old_numpy_env/bin/activate
```

### Packages Not Found After Installation

**Problem:** Installed packages but Python can't find them

**Solution:**

1. Check if environment is activated (look for `(env_name)` in prompt)
2. Verify you're in the correct environment:
   ```bash
   which python  # Linux/macOS
   where python  # Windows
   ```

### Wrong Python Version in Environment

**Problem:** Environment uses wrong Python version

**Solution:** Delete and recreate with specific version:

**Windows:**

```bash
# Delete old environment
rmdir /s %USERPROFILE%\venvs\old_numpy_env

# Create new one with specific Python version
cd %USERPROFILE%\venvs
py -3.11 -m venv old_numpy_env
```

**Linux/macOS:**

```bash
# Delete old environment
rm -rf ~/venvs/old_numpy_env

# Create new one with specific Python version
cd ~/venvs
python3.11 -m venv old_numpy_env
```

---

## Quick Reference

### Command Summary by Platform

#### Windows Commands

| Action                 | Command Prompt                                           | PowerShell                                                      |
| ---------------------- | -------------------------------------------------------- | --------------------------------------------------------------- |
| Create venvs folder    | `cd %USERPROFILE% && mkdir venvs`                        | `cd $env:USERPROFILE; mkdir venvs`                              |
| Create old_numpy_env   | `cd %USERPROFILE%\venvs && python -m venv old_numpy_env` | `cd $env:USERPROFILE\venvs; py -3.11 -m venv old_numpy_env`     |
| Create new_numpy_env   | `cd %USERPROFILE%\venvs && python -m venv new_numpy_env` | `cd $env:USERPROFILE\venvs; py -3.11 -m venv new_numpy_env`     |
| Activate old_numpy_env | `%USERPROFILE%\venvs\old_numpy_env\Scripts\activate`     | `& "$env:USERPROFILE\venvs\old_numpy_env\Scripts\Activate.ps1"` |
| Activate new_numpy_env | `%USERPROFILE%\venvs\new_numpy_env\Scripts\activate`     | `& "$env:USERPROFILE\venvs\new_numpy_env\Scripts\Activate.ps1"` |
| Install old NumPy      | `pip install numpy==1.26.4 pandas==2.2.0`                | `pip install numpy==1.26.4 pandas==2.2.0`                       |
| Install new NumPy      | `pip install numpy==2.2.0 pandas==2.2.0`                 | `pip install numpy==2.2.0 pandas==2.2.0`                        |
| Check NumPy version    | `python -c "import numpy; print(numpy.__version__)"`     | `python -c "import numpy; print(numpy.__version__)"`            |
| List packages          | `pip list`                                               | `pip list`                                                      |
| Deactivate             | `deactivate`                                             | `deactivate`                                                    |
| List environments      | `dir %USERPROFILE%\venvs`                                | `ls $env:USERPROFILE\venvs`                                     |
| Delete environment     | `rmdir /s %USERPROFILE%\venvs\old_numpy_env`             | `rm -r $env:USERPROFILE\venvs\old_numpy_env`                    |

#### Linux Commands

| Action                 | Command                                              |
| ---------------------- | ---------------------------------------------------- |
| Create venvs folder    | `mkdir ~/venvs`                                      |
| Create old_numpy_env   | `cd ~/venvs && python3.11 -m venv old_numpy_env`     |
| Create new_numpy_env   | `cd ~/venvs && python3.11 -m venv new_numpy_env`     |
| Activate old_numpy_env | `source ~/venvs/old_numpy_env/bin/activate`          |
| Activate new_numpy_env | `source ~/venvs/new_numpy_env/bin/activate`          |
| Install old NumPy      | `pip install numpy==1.26.4 pandas==2.2.0`            |
| Install new NumPy      | `pip install numpy==2.2.0 pandas==2.2.0`             |
| Check NumPy version    | `python -c "import numpy; print(numpy.__version__)"` |
| List packages          | `pip list`                                           |
| Deactivate             | `deactivate`                                         |
| List environments      | `ls ~/venvs`                                         |
| Delete environment     | `rm -rf ~/venvs/old_numpy_env`                       |

#### macOS Commands

| Action                 | Command                                              |
| ---------------------- | ---------------------------------------------------- |
| Create venvs folder    | `mkdir ~/venvs`                                      |
| Create old_numpy_env   | `cd ~/venvs && python3.11 -m venv old_numpy_env`     |
| Create new_numpy_env   | `cd ~/venvs && python3.11 -m venv new_numpy_env`     |
| Activate old_numpy_env | `source ~/venvs/old_numpy_env/bin/activate`          |
| Activate new_numpy_env | `source ~/venvs/new_numpy_env/bin/activate`          |
| Install old NumPy      | `pip install numpy==1.26.4 pandas==2.2.0`            |
| Install new NumPy      | `pip install numpy==2.2.0 pandas==2.2.0`             |
| Check NumPy version    | `python -c "import numpy; print(numpy.__version__)"` |
| List packages          | `pip list`                                           |
| Deactivate             | `deactivate`                                         |
| List environments      | `ls ~/venvs`                                         |
| Delete environment     | `rm -rf ~/venvs/old_numpy_env`                       |

---

## Week-by-Week Course Example

### Week 1

**Windows:**

```bash
# One-time setup: Create venvs folder
cd %USERPROFILE%
mkdir venvs

# Create Week 1 environment
cd venvs
python -m venv week1_env

# Activate
week1_env\Scripts\activate

# Install required packages
pip install numpy==1.26.4 pandas==2.2.0

# Work on assignments in your project folder
cd %USERPROFILE%\Documents\GenAIEngineering-Cohort4\Week1
python assignment.py

# Deactivate when done
deactivate
```

**Linux/macOS:**

```bash
# One-time setup: Create venvs folder
mkdir ~/venvs

# Create Week 1 environment
cd ~/venvs
python3.11 -m venv week1_env

# Activate
source week1_env/bin/activate

# Install required packages
pip install numpy==1.26.4 pandas==2.2.0

# Work on assignments in your project folder
cd ~/GenAIEngineering-Cohort4/Week1
python assignment.py

# Deactivate when done
deactivate
```

### Week 2

**Windows:**

```bash
# Create Week 2 environment (different requirements)
cd %USERPROFILE%\venvs
python -m venv week2_env

# Activate
week2_env\Scripts\activate

# Install Week 2 packages
pip install numpy==2.2.0 pandas matplotlib

# Work on Week 2
cd %USERPROFILE%\Documents\GenAIEngineering-Cohort4\Week2
python assignment.py

# Deactivate
deactivate
```

**Linux/macOS:**

```bash
# Create Week 2 environment (different requirements)
cd ~/venvs
python3.11 -m venv week2_env

# Activate
source week2_env/bin/activate

# Install Week 2 packages
pip install numpy==2.2.0 pandas matplotlib

# Work on Week 2
cd ~/GenAIEngineering-Cohort4/Week2
python assignment.py

# Deactivate
deactivate
```

---

## Best Practices

✅ **Use a dedicated venvs folder** - Keep all environments in `~/venvs` (Linux/macOS) or `%USERPROFILE%\venvs` (Windows)
✅ **Name environments descriptively** - Use clear names like `old_numpy_env`, `new_numpy_env`, `week1_env`, `ml_project_env`
✅ **One environment per project/requirement** - Don't try to share environments between projects with different dependencies
✅ **Always activate before working** - Check for `(env_name)` in your prompt
✅ **Deactivate when switching projects** - Clean separation between environments
✅ **Use requirements.txt** to track and share dependencies
✅ **Delete old environments** - Clean up environments you no longer need to save disk space
✅ **Document which environment is for which project** - Keep a simple text file listing your environments and their purpose

---

**Happy Coding! 🐍**

### Creating Different Environments for Different Projects

**Project 1 - Data Analysis (NumPy 1.26.4, Pandas 2.2.0):**

```bash
mkdir project1_data_analysis
cd project1_data_analysis
python -m venv venv                    # Windows: python or py -3.11
# source venv/bin/activate              # macOS/Linux
venv\Scripts\activate                  # Windows
pip install numpy==1.26.4 pandas==2.2.0
deactivate
```

**Project 2 - Machine Learning (NumPy 2.2.0, Pandas latest):**

```bash
mkdir project2_ml
cd project2_ml
python -m venv venv                    # Windows: python or py -3.11
# source venv/bin/activate              # macOS/Linux
venv\Scripts\activate                  # Windows
pip install numpy==2.2.0 pandas
deactivate
```

Each project has its own isolated environment with different package versions!

### Using requirements.txt

Save your exact package versions to share with teammates:

```bash
# Activate your environment
venv\Scripts\activate                  # Windows
# source venv/bin/activate              # macOS/Linux

# Save all installed packages to a file
pip freeze > requirements.txt

# Share requirements.txt with teammates
# They can install the same versions using:
pip install -r requirements.txt
```

**Example requirements.txt:**

```
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.0
```

---

## Troubleshooting

### Virtual Environment Not Activating (Windows PowerShell)

**Problem:** `cannot be loaded because running scripts is disabled`

**Solution:**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:

```bash
venv\Scripts\Activate.ps1
```

### Wrong Python Version in Virtual Environment

**Problem:** Virtual environment uses wrong Python version

**Solution:** Delete and recreate with specific Python version

**Windows:**

```bash
# Delete old environment
rmdir /s venv

# Create new one with specific Python version
py -3.11 -m venv venv
```

**macOS/Linux:**

```bash
# Delete old environment
rm -rf venv

# Create new one with specific Python version
python3.11 -m venv venv
```

### Packages Not Found After Installation

**Problem:** Installed packages but Python can't find them

**Solution:** Make sure virtual environment is activated

- Check for `(venv)` prefix in your command prompt
- If not there, activate the environment again

### Cannot Create Virtual Environment

**Problem:** `No module named venv`

**Solution (Ubuntu/Debian Linux):**

```bash
sudo apt install python3.11-venv
```

**Solution (Windows):** Reinstall Python and ensure all components are selected

### Accidentally Installed Packages in System Python

**Problem:** Installed packages without activating venv

**Solution:**

1. Activate the virtual environment
2. Reinstall the packages
3. Optionally, uninstall from system Python:

   ```bash
   # Deactivate venv first
   deactivate

   # Uninstall from system Python
   python -m pip uninstall numpy pandas  # Windows
   python3.11 -m pip uninstall numpy pandas  # macOS/Linux
   ```

---

## Best Practices

✅ **Always use virtual environments** for your projects
✅ **Create one venv per project** in the project's root directory
✅ **Activate before working** on your project
✅ **Deactivate when done** to avoid confusion
✅ **Use requirements.txt** to track dependencies
✅ **Don't commit venv folder** to git (add `venv/` to `.gitignore`)
✅ **Name consistently**: Use `venv`, `env`, or `.venv` for all projects

---

## Quick Reference

### Commands Summary

| Action                   | Windows (python)                  | Windows (py)                      | macOS/Linux                       |
| ------------------------ | --------------------------------- | --------------------------------- | --------------------------------- |
| Create venv              | `python -m venv venv`             | `py -3.11 -m venv venv`           | `python3.11 -m venv venv`         |
| Activate (CMD)           | `venv\Scripts\activate`           | `venv\Scripts\activate`           | `source venv/bin/activate`        |
| Activate (PowerShell)    | `venv\Scripts\Activate.ps1`       | `venv\Scripts\Activate.ps1`       | N/A                               |
| Install package          | `pip install package`             | `pip install package`             | `pip install package`             |
| Install specific version | `pip install package==1.0.0`      | `pip install package==1.0.0`      | `pip install package==1.0.0`      |
| List packages            | `pip list`                        | `pip list`                        | `pip list`                        |
| Save dependencies        | `pip freeze > requirements.txt`   | `pip freeze > requirements.txt`   | `pip freeze > requirements.txt`   |
| Install from file        | `pip install -r requirements.txt` | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate               | `deactivate`                      | `deactivate`                      | `deactivate`                      |

---

## Real-World Example: Week-by-Week Course Setup

### Week 1 Setup

```bash
# Create Week1 folder and environment
mkdir Week1
cd Week1
python -m venv venv                    # Windows (or py -3.11 -m venv venv)
# python3.11 -m venv venv              # macOS/Linux

# Activate
venv\Scripts\activate                  # Windows CMD
# venv\Scripts\Activate.ps1            # Windows PowerShell
# source venv/bin/activate             # macOS/Linux

# Install required packages
pip install numpy==1.26.4 pandas==2.2.0

# Work on Week 1 assignments...

# Deactivate when done
deactivate
```

### Week 2 Setup (New Requirements)

```bash
# Create Week2 folder and environment
mkdir Week2
cd Week2
python -m venv venv                    # Windows (or py -3.11 -m venv venv)
# python3.11 -m venv venv              # macOS/Linux

# Activate
venv\Scripts\activate                  # Windows CMD
# source venv/bin/activate             # macOS/Linux

# Install different versions if needed
pip install numpy==2.2.0 pandas matplotlib

# Work on Week 2 assignments...

# Deactivate when done
deactivate
```

---

**Happy Coding! 🐍**
