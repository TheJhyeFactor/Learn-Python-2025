# 🚀 Module 01: Mini-Project - Security Tool Banner Generator

## 📋 Project Overview

Create a professional banner generator for security tools that produces clean, formatted output with tool information, disclaimers, and visual separators.

## 🎯 Project Goals

Build a script that:
1. Displays a professional ASCII banner
2. Shows tool information (name, version, author)
3. Includes a legal disclaimer
4. Adds timestamp and system info
5. Uses proper formatting and separators

## 📝 Requirements

Your banner generator should:
- [ ] Use variables for all dynamic content
- [ ] Apply string formatting techniques
- [ ] Include string repetition for borders
- [ ] Display multiple lines cleanly
- [ ] Use proper string concatenation

## 🏗️ Project Structure

```python
# banner_generator.py

# Tool Information Variables
tool_name = "CyberScanner"
version = "1.0.0"
author = "Your Name"
description = "Network Security Assessment Tool"

# System Information
# Add current date/time (you can hardcode for now)
scan_date = "2024-01-15"
scan_time = "14:30:00"

# TODO: Create the banner
# Your code starts here...
```

## 📊 Expected Output Example

```
========================================
=====    CyberScanner v1.0.0      =====
========================================
Network Security Assessment Tool

Author: Your Name
Date: 2024-01-15
Time: 14:30:00

[!] LEGAL DISCLAIMER [!]
This tool is for authorized testing only.
Use only on networks you own or have 
explicit permission to test.

Ready to start scanning...
========================================
```

## 🔨 Implementation Steps

1. **Create the top banner**
   - Use string repetition for the border
   - Center the tool name and version

2. **Add tool description**
   - Display the description clearly

3. **Show metadata**
   - Format author, date, and time

4. **Include disclaimer**
   - Create a noticeable warning section

5. **Add finishing touches**
   - Bottom border
   - Ready message

## 🎨 Bonus Challenges

1. **Add ASCII Art**: Include a small ASCII logo
2. **Color Support**: Add ANSI color codes
3. **Configuration**: Read tool info from variables at the top
4. **Width Control**: Make banner adapt to different widths
5. **Multiple Styles**: Create different banner styles (box, simple, fancy)

## 📁 Starter Code

```python
# banner_generator.py

# Configuration
BANNER_WIDTH = 50
tool_name = "CyberScanner"
version = "1.0.0"
author = "Your Name"

# Banner components
border_char = "="
side_char = "="

# Create top border
top_border = # TODO: Use string repetition

# Create title line
# TODO: Center the tool name and version

# Create disclaimer
disclaimer_text = """This tool is for authorized testing only.
Use only on networks you own or have 
explicit permission to test."""

# Build the complete banner
# TODO: Combine all components

# Print the banner
# TODO: Display everything
```

## ✅ Success Criteria

Your project is complete when:
1. Banner displays all required information
2. Formatting is clean and professional
3. Code uses concepts from Module 01
4. Output is properly aligned
5. All text is readable and well-spaced

## 💡 Hints

- Use `str.center(width)` to center text
- Remember `"=" * 50` creates 50 equals signs
- Use triple quotes for multi-line strings
- F-strings make formatting easier
- Test with different tool names/versions

## 📤 Submission

Save your completed project as:
- `01_core_syntax/mini_project/banner_generator.py`

## 🤔 Reflection Questions

After completing the project:
1. What string method was most useful?
2. How would you make the banner width dynamic?
3. What other information might be useful in a security tool banner?

---

*This mini-project reinforces all Module 01 concepts in a practical security context!*