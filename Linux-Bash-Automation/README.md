# 🐧 Linux & Bash Automation

Welcome to my Linux & Bash scripting journey. This section of the **FunLearn Projects Hub** is where I document everything I learn about using the Linux terminal, writing Bash scripts, and applying automation to real-world projects like my Django-based platform **Volunteen**.

---

## Goals

- Build confidence working in Linux environments (Ubuntu, Debian, etc.)
- Learn to write clean and practical Bash scripts
- Automate common tasks like deployment, backups, health checks, and file management
- Apply everything I learn to real-world applications (e.g., Volunteen server automation)
- Create a growing toolkit of reusable scripts and documentation

---

## Structure

```bash
Linux-Bash-Automation/
├── README.md # This file
├── scripts/ # All Bash scripts
│ ├── day01-basic-commands.sh
│ └── ...
│ └── deploy-volunteen.sh # Real-world automation example
├── notes/  # Learning notes, summaries, and references
│ ├── day01.md
│ └── ...
├── .gitignore # Local ignore rules (exercises/, output/)
├── exercises/ (ignored) # Practice scripts and learning playground
└── output/ (ignored) # Script outputs, logs, generated files
```


---

## What’s Inside

### `scripts/`
Contains all the Bash scripts I write. Each one has comments and is organized by topic or task (e.g., backups, file watchers, deployment scripts).

### `notes/`
Markdown files documenting each learning session or concept — including explanations, commands used, helpful links, and notes on what I struggled with or learned.

---

## Real-World Use Cases

The goal isn't just to learn, but to **apply** it in real projects. Example:

### `deploy-volunteen.sh` (WIP)

A Bash script to:
- Activate virtual environment
- Pull the latest changes from GitHub
- Run Django migrations
- Collect static files
- Restart the server 
- Log output to a timestamped file

---
