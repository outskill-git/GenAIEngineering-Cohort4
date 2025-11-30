# How to Download Week Folders from the Course Repository

This guide will help you download only the week folders you need from the GenAIEngineering-Cohort4 repository, saving time and disk space.

## Why This Approach?

Instead of downloading the entire repository (which can be large), you'll:
- Start with Week 1 in the first week
- Add new weeks as the course progresses
- Save disk space on your computer
- Keep your workspace clean and organized
- **Save your modified code to your own GitHub repository**

## Prerequisites

- Git installed on your computer ([Download Git](https://git-scm.com/downloads))
- Python 3.11.9 installed on your computer
  - 📘 **[Follow our Python 3.11 Installation Guide](PYTHON_INSTALLATION.md)** for detailed instructions for Windows, macOS, and Linux
- A GitHub account ([Sign up for free](https://github.com/join))
- Basic familiarity with command line/terminal

## Week-by-Week Instructions

### Week 1: Initial Setup

On the first week of the course, clone the repository with sparse checkout enabled:

```bash
# Clone the repository with sparse checkout enabled
git clone --filter=blob:none --sparse https://github.com/outskill-git/GenAIEngineering-Cohort4.git

# Navigate into the repository folder
cd GenAIEngineering-Cohort4

# Download Week1 folder
git sparse-checkout set Week1
```

**What this does:**
- Creates a local copy of the repository on your computer
- Only downloads the files for Week1
- Sets up sparse checkout for future weeks
- Saves disk space by not downloading other weeks yet

### Week 2 Onwards: Adding New Weeks

Starting from Week 2, you'll add new week folders to your existing repository:

**Week 2:**
```bash
# Navigate to your repository folder
cd GenAIEngineering-Cohort4

# Add Week2 folder (keeps Week1 too)
git sparse-checkout add Week2

# Get the latest updates
git pull
```

**Week 3:**
```bash
cd GenAIEngineering-Cohort4
git sparse-checkout add Week3
git pull
```

**Week 4:**
```bash
cd GenAIEngineering-Cohort4
git sparse-checkout add Week4
git pull
```

**...and so on for each week!**

**Important Notes:**
- Always use `git sparse-checkout add` to keep your previous weeks
- Don't use `git sparse-checkout set` after Week 1, as it will replace your existing weeks
- Always run `git pull` after adding a new week to get the latest content

### If You Need to Catch Up (Multiple Weeks at Once)

If you missed some weeks and need to download multiple weeks:

```bash
# Download Week1 through Week5 all at once
git sparse-checkout set Week1 Week2 Week3 Week4 Week5

# Get the latest updates
git pull
```

### Updating Existing Week Content

When the instructor updates materials for a week you already have:

```bash
# Make sure you're in the repository folder
cd GenAIEngineering-Cohort4

# Pull the latest updates
git pull
```

## Saving Your Modified Code to Your Own Repository

⚠️ **IMPORTANT:** The course repository is read-only. You cannot push your changes to it. Instead, you'll create your own repository to save your work.

### One-Time Setup: Create Your Personal Repository

Do this once at the beginning of the course:

**Step 1: Create a new repository on GitHub**
1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it something like `GenAI-Engineering-MyWork` or `genai-cohort4-solutions`
5. Choose "Private" if you want to keep your work private
6. **DO NOT** initialize with README, .gitignore, or license
7. Click "Create repository"

**Step 2: Set up your personal repository**
```bash
# Navigate to the course repository folder
cd GenAIEngineering-Cohort4

# Add your personal repository as a remote (replace YOUR_USERNAME with your GitHub username)
git remote add myrepo https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git

# Verify your remotes
git remote -v
```

You should see two remotes:
- `origin` - points to the course repository (read-only)
- `myrepo` - points to your personal repository (you can push here)

### Workflow: Making Changes and Saving Your Work

Here's the recommended workflow for each week:

**1. Download the week's materials (if you haven't already)**
```bash
cd GenAIEngineering-Cohort4
git sparse-checkout add Week3  # or whatever week you're on
git pull
```

**2. Work on your assignments and modify the code**
- Edit files, write code, complete exercises
- Test your solutions

**3. Save your changes locally**
```bash
# Check what files you've modified
git status

# Stage your changes (add specific files or use . for all)
git add Week3/assignment1.py Week3/assignment2.py
# OR add all changes
git add .

# Commit your changes with a descriptive message
git commit -m "Completed Week 3 assignments: RAG implementation and vector databases"
```

**4. Push your changes to your personal repository**
```bash
# Push to your personal repository
git push myrepo main

# If this is your first push, you might need to set upstream
git push -u myrepo main
```

### Complete Weekly Workflow Example

Here's a complete example for Week 3:

```bash
# Navigate to course repository
cd GenAIEngineering-Cohort4

# Download Week 3 materials
git sparse-checkout add Week3
git pull

# Work on your assignments (edit files, write code)
# ... (you do your work here) ...

# Save your work
git add Week3/
git commit -m "Week 3: Completed all exercises on LangChain and agents"

# Push to YOUR repository
git push myrepo main
```

### Handling Conflicts When Instructor Updates Files

If the instructor updates files that you've already modified:

```bash
# Pull the latest changes from the course repository
git pull origin main

# If there are conflicts, Git will notify you
# You'll need to manually resolve them in your code editor

# After resolving conflicts, stage and commit
git add .
git commit -m "Merged instructor updates with my solutions"

# Push to your repository
git push myrepo main
```

### Best Practices for Version Control

1. **Commit often**: Save your work frequently with descriptive messages
   ```bash
   git commit -m "Implemented basic chatbot functionality"
   git commit -m "Added error handling to API calls"
   git commit -m "Fixed bug in prompt template"
   ```

2. **Use descriptive commit messages**: Make them meaningful
   - ✅ Good: "Completed Week 2 RAG assignment with custom embeddings"
   - ❌ Bad: "Updated files" or "Week 2"

3. **Push regularly**: Don't wait until the end of the week
   ```bash
   # Push after completing each major milestone
   git push myrepo main
   ```

4. **Create branches for experiments** (optional, advanced):
   ```bash
   # Create a new branch for experimental features
   git checkout -b experiment-multimodal-rag
   
   # Work on your experiment
   # ...
   
   # Push the branch to your repository
   git push myrepo experiment-multimodal-rag
   
   # Switch back to main branch
   git checkout main
   ```

### Viewing Your Commit History

```bash
# See your recent commits
git log --oneline

# See detailed commit history
git log

# See what changed in the last commit
git show
```

### Backing Up Your Work

Your work is now safely stored in three places:
1. **Your local computer** - in the GenAIEngineering-Cohort4 folder
2. **Your GitHub repository** - pushed to `myrepo`
3. **GitHub's servers** - backed up automatically

To clone your work on another computer:
```bash
git clone https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git
```

## Common Commands Cheat Sheet

| Task | Command |
|------|---------|
| See which weeks you have | `git sparse-checkout list` |
| Add a new week | `git sparse-checkout add Week13` |
| Get latest updates from course | `git pull` |
| Check current status | `git status` |
| See your changes | `git diff` |
| Stage changes | `git add filename` or `git add .` |
| Commit changes | `git commit -m "Your message"` |
| Push to your repository | `git push myrepo main` |
| View commit history | `git log --oneline` |
| Check remotes | `git remote -v` |

## Complete Example Workflow

Here's exactly what you'll do throughout the course:

**Week 1 (First time setup):**
```bash
# Clone course repository
git clone --filter=blob:none --sparse https://github.com/outskill-git/GenAIEngineering-Cohort4.git
cd GenAIEngineering-Cohort4
git sparse-checkout set Week1

# Add your personal repository
git remote add myrepo https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git

# Work on Week 1 assignments
# ... (do your work) ...

# Save and push your work
git add Week1/
git commit -m "Completed Week 1: Introduction to GenAI and prompting"
git push myrepo main
```

**Week 2:**
```bash
cd GenAIEngineering-Cohort4

# Get Week 2 materials
git sparse-checkout add Week2
git pull

# Work on assignments
# ... (do your work) ...

# Save and push
git add Week2/
git commit -m "Completed Week 2: RAG and vector databases"
git push myrepo main
```

**Week 3:**
```bash
cd GenAIEngineering-Cohort4

# Get Week 3 materials
git sparse-checkout add Week3
git pull

# Work on assignments
# ... (do your work) ...

# Save and push
git add Week3/
git commit -m "Completed Week 3: Advanced RAG techniques"
git push myrepo main
```

**Week 4:**
```bash
cd GenAIEngineering-Cohort4

# Get Week 4 materials
git sparse-checkout add Week4
git pull

# Work on assignments
# ... (do your work) ...

# Save and push
git add Week4/
git commit -m "Completed Week 4: LangChain and agents"
git push myrepo main
```

**...continue this pattern for each new week!**

## Troubleshooting

### "I accidentally closed the terminal. How do I continue?"

Just navigate back to your folder and continue where you left off:
```bash
cd GenAIEngineering-Cohort4
git sparse-checkout add Week3  # or whatever week you're on
git pull
```

### "I want to start over from Week 1"

Delete the folder and clone again:
```bash
# On Mac/Linux
rm -rf GenAIEngineering-Cohort4

# On Windows
rmdir /s GenAIEngineering-Cohort4

# Then start from Week 1 setup
git clone --filter=blob:none --sparse https://github.com/outskill-git/GenAIEngineering-Cohort4.git
cd GenAIEngineering-Cohort4
git sparse-checkout set Week1
git remote add myrepo https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git
```

### "I want to see all weeks"

```bash
git sparse-checkout disable
```

This will download everything. To go back to sparse mode, use `git sparse-checkout set Week10` again.

### "The command doesn't work"

Make sure:
1. You have Git installed (check with `git --version`)
2. You're running the commands in the correct folder
3. You have internet connection

### "I get 'permission denied' when trying to push"

This means you're trying to push to the course repository (which you can't do). Make sure you're pushing to your personal repository:
```bash
# Check your remotes
git remote -v

# Should show:
# origin    https://github.com/outskill-git/GenAIEngineering-Cohort4.git (fetch)
# origin    https://github.com/outskill-git/GenAIEngineering-Cohort4.git (push)
# myrepo    https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git (fetch)
# myrepo    https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git (push)

# Always push to myrepo, not origin
git push myrepo main
```

### "I have merge conflicts after git pull"

When the instructor updates files you've modified:
```bash
# Open the conflicted files in your code editor
# Look for conflict markers: <<<<<<<, =======, >>>>>>>
# Edit the file to keep what you want
# Remove the conflict markers

# After resolving all conflicts
git add .
git commit -m "Resolved merge conflicts with instructor updates"
git push myrepo main
```

### "I forgot to commit and want to see what I changed"

```bash
# See what files you modified
git status

# See the actual changes
git diff

# See changes in a specific file
git diff Week3/assignment.py
```

### "I want to undo my last commit but keep the changes"

```bash
# Undo the last commit but keep your changes
git reset --soft HEAD~1

# Now you can modify and commit again
```

### "I want to completely discard my changes and start fresh"

⚠️ **WARNING:** This will permanently delete your local changes!

```bash
# Discard all changes and go back to last commit
git reset --hard HEAD

# Discard changes in a specific file
git checkout -- Week3/assignment.py
```

## Alternative Method (If Sparse Checkout Doesn't Work)

If you're having issues with sparse checkout, you can use SVN to download individual folders:

```bash
# Download just Week1
svn export https://github.com/outskill-git/GenAIEngineering-Cohort4/trunk/Week1

# Download just Week2
svn export https://github.com/outskill-git/GenAIEngineering-Cohort4/trunk/Week2
```

**Note:** This downloads files without Git history, so you won't be able to use `git pull` to update. You'll need to download each week separately. You'll also need to initialize your own Git repository:

```bash
# After downloading with SVN, initialize Git
git init
git remote add myrepo https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git
git add .
git commit -m "Initial commit with course materials"
git push -u myrepo main
```

## Need Help?

- Check if Git is installed: `git --version`
- Check your current location: `pwd` (Mac/Linux) or `cd` (Windows)
- List files in current folder: `ls` (Mac/Linux) or `dir` (Windows)
- View Git configuration: `git config --list`
- Get help with a command: `git help push` or `git push --help`

## Quick Reference Card

```bash
# Week 1 - First time setup
git clone --filter=blob:none --sparse https://github.com/outskill-git/GenAIEngineering-Cohort4.git
cd GenAIEngineering-Cohort4
git sparse-checkout set Week1
git remote add myrepo https://github.com/YOUR_USERNAME/GenAI-Engineering-MyWork.git

# Week 2 onwards - Get new materials
cd GenAIEngineering-Cohort4
git sparse-checkout add Week2
git pull

# After completing your work - Save to your repository
git add .
git commit -m "Completed Week 2: RAG implementation"
git push myrepo main

# Week 3
git sparse-checkout add Week3
git pull
# ... (do your work) ...
git add .
git commit -m "Completed Week 3 assignments"
git push myrepo main

# Week 4
git sparse-checkout add Week4
git pull
# ... (do your work) ...
git add .
git commit -m "Completed Week 4: LangChain and agents"
git push myrepo main

# Useful commands
git sparse-checkout list    # See which weeks you have
git status                  # Check status
git pull                    # Update from course repository
git remote -v               # See your repositories
git log --oneline           # See your commit history
git diff                    # See your changes
```

## Git Workflow Summary

```
┌─────────────────────────────────────────────────────────┐
│  Course Repository (Read-only)                          │
│  https://github.com/outskill-git/GenAIEngineering-...   │
└───────────────────┬─────────────────────────────────────┘
                    │ git pull (download updates)
                    ↓
┌─────────────────────────────────────────────────────────┐
│  Your Local Computer                                    │
│  ~/GenAIEngineering-Cohort4/                           │
│  - You edit files here                                  │
│  - You test your code here                              │
└───────────────────┬─────────────────────────────────────┘
                    │ git push myrepo main (save your work)
                    ↓
┌─────────────────────────────────────────────────────────┐
│  Your Personal Repository (You own this)                │
│  https://github.com/YOUR_USERNAME/GenAI-Engineering-... │
│  - Your modified code is saved here                     │
│  - Safe backup of all your work                         │
└─────────────────────────────────────────────────────────┘
```

---

**Happy Learning! 🚀**

**Remember:** 
- Pull from the course repository to get new materials
- Push to YOUR repository to save your work
- Commit often with descriptive messages
- Your code is valuable - keep it safe in your own repository!
