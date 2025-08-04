# Module 02B: Flow Control & Iteration

## 🎯 Learning Objectives
- Master conditional statements (if/elif/else)
- Use for and while loops effectively
- Control loop flow with break/continue
- Understand loop patterns and best practices

## 🛡️ Why it matters for a pentester
Flow control powers everything from brute-force attempts to parsing scan results. Whether iterating through wordlists or making decisions based on response codes, mastering loops and conditionals is essential.

## 📚 Vocabulary
- **Conditional**: Code that executes based on a condition
- **Iteration**: Repeating code for each item in a sequence
- **Boolean**: True/False value used in conditions
- **Nested loop**: Loop inside another loop
- **Short-circuit evaluation**: Stopping condition checks early

## 📂 Example References
- `calc.py` - Conditional logic for operation selection

## 💡 Mini-Project: Country Code Pinger
Write a loop that:
- Generates all two-letter country codes (AA-ZZ)
- Attempts to ping each as a domain (e.g., google.aa)
- Tracks successful responses in a list
- Reports statistics at the end

## ✅ Checkpoint Questions
1. When should you use `while` instead of `for`?
2. What's the difference between `break` and `continue`?
3. How do you check if an item is "in" a list or dictionary?

## 🔗 Next Steps
Ready for more complex data? Move to Module 03: Data Structures