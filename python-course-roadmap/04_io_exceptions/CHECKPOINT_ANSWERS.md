# 📝 Module 04: Checkpoint Answers

## Questions from README:

### 1. What's the difference between catching `Exception` vs specific exceptions?

**Your Answer:**
```
[Write your answer here]
```

**Compare these approaches:**
```python
# Approach 1:
try:
    # some code
except Exception as e:
    print(f"Error: {e}")

# Approach 2:
try:
    # some code
except ValueError:
    # handle value errors
except FileNotFoundError:
    # handle file errors
```

---

### 2. When should you use `finally`?

**Your Answer:**
```
[Write your answer here]
```

**Example scenario:**
```python
# When is finally useful here?
file = None
try:
    file = open('data.txt')
    # process file
except IOError:
    print("Error reading file")
finally:
    # What goes here?
```

---

### 3. Why use `with open()` instead of just `open()`?

**Your Answer:**
```
[Write your answer here]
```

**Compare:**
```python
# Method 1:
file = open('data.txt')
# do something
file.close()

# Method 2:
with open('data.txt') as file:
    # do something

# What's the advantage?
```

---

## 🎯 Self-Assessment

Rate your confidence (1-5):
- [ ] I can validate user input
- [ ] I handle errors gracefully
- [ ] I work with files safely
- [ ] I write defensive code

## 💡 Key Concepts to Remember

1. 
2. 
3. 

## 🤔 Questions for Further Study

- 
- 

---

*Fill this out after studying the module and attempting the checkpoint questions!*