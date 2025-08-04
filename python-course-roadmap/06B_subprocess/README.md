# Module 06B: Subprocess & System Commands

## 🎯 Learning Objectives
- Execute system commands from Python
- Capture and parse command output
- Handle command errors and timeouts
- Build wrappers for CLI tools

## 🛡️ Why it matters for a pentester
Subprocess lets you wrap powerful tools like nmap, dig, or whois in Python automation. Parse their output, chain commands, and build intelligence-gathering pipelines.

## 📚 Vocabulary
- **Process**: Running instance of a program
- **STDOUT**: Standard output stream
- **STDERR**: Standard error stream
- **Return code**: Exit status (0 = success)
- **Shell injection**: Security vulnerability to avoid
- **Pipe**: Connect output to input

## 📂 Example References
- `socket_testing.py` - Using subprocess for ping and ip commands

## 💡 Mini-Project: System Command Wrapper
Create a Python wrapper that:
- Executes arp command safely
- Parses output into Python dictionary
- Handles different OS formats
- Returns structured network neighbor data

## ✅ Checkpoint Questions
1. Why use `subprocess.run()` with lists instead of strings?
2. How do you capture both stdout and stderr?
3. What security risks exist with shell=True?

## 🔗 Next Steps
Ready for networking? Dive into Module 07: Network Programming