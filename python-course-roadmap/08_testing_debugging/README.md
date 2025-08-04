# Module 08: Testing & Debugging

## 🎯 Learning Objectives
- Write unit tests with pytest
- Debug code with pdb
- Add logging to applications
- Profile code performance
- Create reliable, maintainable tools

## 🛡️ Why it matters for a pentester
Security tools must be reliable. A bug in your scanner might miss vulnerabilities or cause false positives. Testing ensures your tools work correctly under all conditions.

## 📚 Vocabulary
- **Unit test**: Test for individual function
- **Test fixture**: Setup/teardown for tests
- **Assertion**: Statement that must be true
- **Breakpoint**: Pause execution for debugging
- **Log level**: Severity of log messages
- **Code coverage**: Percentage of code tested

## 📂 Example References
- Create tests for your existing code

## 💡 Mini-Project: Test Your Scanner
Add pytest tests that verify:
- Port validation rejects invalid inputs
- Timeout handling works correctly
- Banner parsing handles edge cases
- Network errors are caught properly

## ✅ Checkpoint Questions
1. What makes a good unit test?
2. When should you use logging vs print statements?
3. How do you test code that requires network connections?

## 🔗 Prerequisites
- All previous modules (you need code to test!)

## 🎉 Congratulations!
You've completed the Python Security Tools learning path. You now have the skills to build professional penetration testing tools. Keep practicing, keep learning, and always test responsibly!