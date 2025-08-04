#!/usr/bin/env python3
"""
Setup script to create standard files in all module directories
"""

import os
from pathlib import Path

# Module list
modules = [
    "01_core_syntax",
    "02A_functions",
    "02B_flow_control",
    "03_data_structures",
    "04_io_exceptions",
    "05_packages_venv",
    "06A_filesystem_os",
    "06B_subprocess",
    "07_networking",
    "08_testing_debugging"
]

# Files to create in each module
standard_files = [
    "CHECKPOINT_ANSWERS.md",
    "EXERCISES.md",
    "EXAMPLES.md",
    "MINI_PROJECT.md",
    "NOTES.md"
]

def create_placeholder_content(module_name, file_type):
    """Generate placeholder content for missing files"""
    
    module_display = module_name.replace("_", " ").title()
    
    if file_type == "EXERCISES.md":
        return f"""# 🏋️ {module_display} - Exercises

## 📚 Concept 1: [CONCEPT NAME]

### 🔍 What You'll Learn:
[Brief explanation]

### 📖 Example:
```python
# Example code
```

### ✏️ Exercise 1.1: [Exercise Name]
```python
# TODO: Your exercise here
```

---

*Complete all exercises before moving to the mini-project!*
"""
    
    elif file_type == "EXAMPLES.md":
        return f"""# 🌟 {module_display}: Real-World Examples

## 🛡️ Security Tool Examples

### Example 1: [Example Name]
```python
# Real-world code example
```

---

*Study these examples to see concepts in action!*
"""
    
    elif file_type == "MINI_PROJECT.md":
        return f"""# 🚀 {module_display}: Mini-Project

## 📋 Project Overview
[Project description]

## 🎯 Project Goals
Build a tool that:
1. [Goal 1]
2. [Goal 2]

## 📝 Requirements
- [ ] [Requirement 1]
- [ ] [Requirement 2]

---

*Apply your knowledge in this practical project!*
"""
    
    elif file_type == "NOTES.md":
        return f"""# 📓 {module_display} - My Notes

## 📅 Study Log
**Started:** [DATE]  
**Time Spent:** [HOURS]

## 🧠 Key Concepts I Learned
- 
- 

## 💡 "Aha!" Moments
1. 

## 🤔 Things That Confused Me
- 

## 📝 Code Snippets to Remember
```python
# Important code
```

---

*Keep updating these notes as you learn!*
"""
    
    elif file_type == "CHECKPOINT_ANSWERS.md":
        return f"""# 📝 {module_display}: Checkpoint Answers

## Questions from README:

### 1. [Question 1]
**Your Answer:**
```
[Write your answer here]
```

### 2. [Question 2]
**Your Answer:**
```
[Write your answer here]
```

### 3. [Question 3]
**Your Answer:**
```
[Write your answer here]
```

## 🎯 Self-Assessment
Rate your confidence (1-5):
- [ ] [Skill 1]
- [ ] [Skill 2]

---

*Fill this out after studying the module!*
"""
    
    return f"# {module_display} - {file_type}\n\n[Content to be added]"

def setup_module_files():
    """Create standard files in each module directory"""
    
    base_dir = Path(__file__).parent
    created_count = 0
    
    print("🚀 Setting up module files...")
    
    for module in modules:
        module_path = base_dir / module
        
        if not module_path.exists():
            print(f"⚠️  Module directory not found: {module}")
            continue
            
        print(f"\n📁 Processing {module}:")
        
        for file_name in standard_files:
            file_path = module_path / file_name
            
            if not file_path.exists():
                # Create the file with placeholder content
                content = create_placeholder_content(module, file_name)
                
                with open(file_path, 'w') as f:
                    f.write(content)
                
                print(f"  ✅ Created {file_name}")
                created_count += 1
            else:
                print(f"  ⏭️  {file_name} already exists")
    
    print(f"\n✨ Setup complete! Created {created_count} new files.")
    print("\n📝 Next steps:")
    print("1. Review the EXERCISES.md in each module")
    print("2. Study the EXAMPLES.md for real-world usage")
    print("3. Complete the MINI_PROJECT.md")
    print("4. Fill out CHECKPOINT_ANSWERS.md")
    print("5. Keep your NOTES.md updated!")

if __name__ == "__main__":
    setup_module_files()