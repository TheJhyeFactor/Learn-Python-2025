# Module 03: Data Structures

## 🎯 Learning Objectives
- Master lists, dictionaries, and sets
- Use slicing and indexing effectively
- Write list and dictionary comprehensions
- Choose the right data structure for the task

## 🛡️ Why it matters for a pentester
Data structures organize your reconnaissance data. Store discovered hosts in sets (no duplicates), map ports to services with dictionaries, and process IP ranges with list comprehensions.

## 📚 Vocabulary
- **List**: Ordered, mutable collection
- **Dictionary**: Key-value mapping
- **Set**: Unordered collection of unique items
- **Tuple**: Immutable ordered collection
- **Comprehension**: Concise way to create collections
- **Slice**: Extract portion of a sequence

## 📂 Example References
- `calc.py` - Dictionary mapping operation names to functions

## 💡 Mini-Project: Log Parser
Transform raw comma-separated log lines into structured data:
- Read log file with IP, timestamp, status code
- Parse into list of dictionaries
- Filter by IP address or status code
- Generate summary statistics

## ✅ Checkpoint Questions
1. When would you use a set instead of a list?
2. Can dictionary keys be lists? Why or why not?
3. How do you safely get a dictionary value that might not exist?

## 🔗 Next Steps
Data organized? Learn error handling in Module 04: Robust I/O & Exceptions