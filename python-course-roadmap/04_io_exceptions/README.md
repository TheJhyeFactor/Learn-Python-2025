# Module 04: Robust I/O & Exceptions

## 🎯 Learning Objectives
- Validate and sanitize user input
- Handle errors with try/except blocks
- Work with files safely
- Create defensive, production-ready code

## 🛡️ Why it matters for a pentester
Network tools encounter constant errors: refused connections, timeouts, invalid input. Proper exception handling separates amateur scripts from professional tools that gracefully handle edge cases.

## 📚 Vocabulary
- **Exception**: Error that occurs during execution
- **Try/Except**: Blocks for handling exceptions
- **Finally**: Code that always runs
- **Raise**: Manually trigger an exception
- **Context manager**: Automatic resource cleanup (with statement)

## 📂 Example References
- `calc.py` - Input validation and error messages
- `challenges/Struggles.md` - Real debugging experience

## 💡 Mini-Project: Bulletproof Scanner Input
Create an input validator that:
- Accepts IP addresses, ranges, or hostnames
- Validates format before processing
- Handles file reading errors gracefully
- Provides helpful error messages

## ✅ Checkpoint Questions
1. What's the difference between catching `Exception` vs specific exceptions?
2. When should you use `finally`?
3. Why use `with open()` instead of just `open()`?

## 🔗 Next Steps
Ready to organize code? Continue to Module 05: Packages, venv & Imports