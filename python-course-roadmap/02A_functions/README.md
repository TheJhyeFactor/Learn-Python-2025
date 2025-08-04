# Module 02A: Functions

## 🎯 Learning Objectives
- Define and call functions
- Work with parameters and return values
- Understand function scope
- Create reusable code blocks

## 🛡️ Why it matters for a pentester
Functions let you wrap complex operations (like banner grabbing or port checking) into reusable tools. One function can handle all your HTTP header parsing across multiple targets.

## 📚 Vocabulary
- **Function**: Reusable block of code
- **Parameter**: Variable in function definition
- **Argument**: Value passed to function
- **Return value**: Data sent back from function
- **Scope**: Where variables can be accessed

## 📂 Example References
- `calc.py` - Multiple arithmetic functions with parameters

## 💡 Mini-Project: Security Utilities
Create a function library with:
- `is_private_ip(ip)` - Check if IP is in private range
- `validate_port(port)` - Verify port is valid (1-65535)
- `parse_url(url)` - Extract protocol, host, port from URL

## ✅ Checkpoint Questions
1. What happens if you forget the `return` statement?
2. Can a function modify a list passed as parameter?
3. What's the difference between a parameter and an argument?

## 🔗 Next Steps
Master functions? Continue to Module 02B: Flow Control