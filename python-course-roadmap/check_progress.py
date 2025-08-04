#!/usr/bin/env python3
"""
Progress Checker for Python Security Tools Course
Scans for COMPLETED.md files and reports progress
"""

import os
from pathlib import Path
from datetime import datetime

def check_course_progress():
    """Check which modules have been completed"""
    
    course_dir = Path(__file__).parent
    modules = []
    
    # Define module order
    module_names = [
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
    
    print("🐍 Python Security Tools Course - Progress Report")
    print("=" * 50)
    
    completed_count = 0
    
    for module in module_names:
        module_path = course_dir / module
        completed_file = module_path / "COMPLETED.md"
        
        if completed_file.exists():
            completed_count += 1
            # Try to read completion date from file
            try:
                with open(completed_file, 'r') as f:
                    content = f.read()
                    # Look for completion date
                    for line in content.split('\n'):
                        if 'Completion Date:' in line:
                            date = line.split(':', 1)[1].strip()
                            status = f"✅ Completed on {date}"
                            break
                    else:
                        status = "✅ Completed"
            except:
                status = "✅ Completed"
        else:
            status = "⏳ In Progress" if completed_count == len(modules) else "📚 Not Started"
            
        print(f"{module:<20} {status}")
    
    print("=" * 50)
    print(f"Progress: {completed_count}/{len(module_names)} modules completed")
    print(f"Completion: {(completed_count/len(module_names)*100):.1f}%")
    
    if completed_count == len(module_names):
        print("\n🎉 Congratulations! You've completed the entire course!")
    elif completed_count > 0:
        print(f"\n💪 Keep going! You're making great progress!")
        print(f"Next module: {module_names[completed_count]}")
    else:
        print("\n🚀 Ready to start? Begin with 01_core_syntax!")
    
    # Check for mini-projects
    print("\n📂 Mini-Projects Status:")
    project_count = 0
    for module in module_names:
        module_path = course_dir / module / "mini_project"
        if module_path.exists() and any(module_path.iterdir()):
            project_count += 1
            print(f"  ✅ {module} mini-project found")
    
    if project_count > 0:
        print(f"\nTotal mini-projects completed: {project_count}")

if __name__ == "__main__":
    check_course_progress()