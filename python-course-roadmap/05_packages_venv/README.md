# Module 05: Packages, venv & Imports

## 🎯 Learning Objectives
- Understand Python's import system
- Create and activate virtual environments
- Install packages with pip
- Structure code into modules
- Manage dependencies properly

## 🛡️ Why it matters for a pentester
Professional security tools require external libraries (requests, scapy, paramiko). Virtual environments prevent version conflicts between projects and ensure your tools run reliably on any system.

## 📚 Vocabulary
- **Module**: Single Python file
- **Package**: Directory of modules
- **Virtual environment**: Isolated Python installation
- **pip**: Python package installer
- **requirements.txt**: Dependency specification file
- **Namespace**: Container for names/variables

## 📂 Example References
- Existing import statements in your code files

## 💡 Mini-Project: Tool Packaging
Structure a multi-file security tool:
- Main script imports from utility modules
- Create requirements.txt
- Set up virtual environment
- Document installation steps

## ✅ Checkpoint Questions
1. What's the difference between `import module` and `from module import function`?
2. Why use virtual environments for each project?
3. How do you share project dependencies with others?

## 🔗 Next Steps
Packages organized? Learn system interaction in Module 06A: Filesystem & OS