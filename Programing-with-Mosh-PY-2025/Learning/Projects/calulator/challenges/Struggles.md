# 🧠 Calculator Project – Struggles & Lessons Learned

## ✅ What I Built
A basic calculator using:
- Functions to define arithmetic operations
- A dictionary to map operation names to functions
- User input and conditionals for dynamic operation selection

## 😕 What I Struggled With

### 1. **Incorrect Condition Check**
I originally wrote:

```python
if op == opration.keys():
```

But this did **not work**, because `.keys()` returns a **view object**, not a string or list that can be directly compared using `==`.

#### ✅ Fix:
I realized I needed to check if the user input is **in** the list of available operations:

```python
if op in opration.keys():
```

This made the check dynamic and worked perfectly.

## 💡 What Helped Me Solve It
- Saying the logic out loud
- Thinking through the problem like:  
  > "I'm not checking if it equals all the keys — I'm checking if it exists **within** them."

## 📌 Note for Future Me
- Use `in` when checking membership in lists, dicts, sets, etc.
