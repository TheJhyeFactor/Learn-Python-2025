# Module 06A: Filesystem & OS Operations

## 🎯 Learning Objectives
- Navigate directories with os and pathlib
- Read, write, and manipulate files
- Work with environment variables
- Handle cross-platform path differences

## 🛡️ Why it matters for a pentester
Security tools need to save scan results, read wordlists, parse config files, and navigate filesystem structures. Understanding OS operations enables tool automation and result management.

## 📚 Vocabulary
- **Path**: File or directory location
- **Absolute path**: Complete path from root
- **Relative path**: Path from current location
- **Environment variable**: System-wide configuration value
- **File permissions**: Read/write/execute access controls

## 📂 Example References
- File operations will be demonstrated in mini-projects

## 💡 Mini-Project: Security File Manager
Build a tool that:
- Organizes scan outputs by date/target
- Searches for specific file patterns
- Archives old results automatically
- Creates report directories with proper structure

## ✅ Checkpoint Questions
1. What's the advantage of pathlib over os.path?
2. How do you check if a file exists before reading?
3. Why use os.path.join() instead of string concatenation?

## 🔗 Next Steps
Filesystem mastered? Execute commands in Module 06B: Subprocess