import pandas as pd
import matplotlib.pyplot as plt

try:
    # 1. IT LOADS THE DATA
    students = pd.read_csv("../data/students.csv")
    print("=" * 40)
    print("   STUDENT PERFORMANCE ANALYZER LOADED   ")
    print("=" * 40 + "\n")
    
    # 2. IT CLEANS & PROCESSES THE DATA
    # Calculate Total and Average scores for each student
    students['Total'] = students['Math'] + students['English'] + students['Science']
    students['Average'] = (students['Total'] / 3).round(1)
    
    # 3. IT GENERATES A TEXT REPORT 
    print("---  CLASS PERFORMANCE REPORT ---")
    
    # A. THE AVERAGES OF THE SUBJECTS
    subjects = ['Math', 'English', 'Science']
    print("\n🔹 Subject Averages:")
    print(students[subjects].mean().round(1))
    print("-" * 30)
    
    # B. THE TOP PERFORMING STUDENT(SO PROUD)
    top_student_idx = students['Average'].idxmax()
    top_student = students.loc[top_student_idx]
    print(f" Top Performing Student: {top_student['Name']} (Avg: {top_student['Average']})")
    print("-" * 30)
    
    # C. STUDENTS THAT NEED SUPPORT
    failing_students = students[students['Average'] < 60]
    print(" Students Needing Support (Average < 60):")
    if failing_students.empty:
        print("   Great news! No students are currently failing.")
    else:
        print(failing_students[['Name', 'Average']].to_string(index=False))
    print("\n" + "=" * 40 + "\n")

    # 4. IT GENERATES A VISUAL CHARTS THAT SAVES TO THE IMAGE OLDDER
    print("---  GENERATING VISUALIZATIONS ---")

    # Chart 1: IT SHOWS THE STUDENT'S AVERAGES
    plt.figure(figsize=(10, 5))
    plt.bar(students['Name'], students['Average'], color='skyblue', edgecolor='black')
    plt.title('Average Scores by Student', fontsize=14, fontweight='bold')
    plt.xlabel('Students', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.axhline(y=60, color='red', linestyle='--', label='Passing Mark (60)')
    plt.legend()
    plt.savefig('../images/student_averages.png', bbox_inches='tight')
    plt.close()
    print("✓ Saved: images/student_averages.png")

    # Chart 2: IT COMPARES THE SUBJECT PERFORMANCE
    plt.figure(figsize=(7, 5))
    subject_means = students[subjects].mean()
    plt.bar(subject_means.index, subject_means.values, color=['#FFA07A', '#98FB98', '#DDA0DD'], edgecolor='black')
    plt.title('Class Average by Subject', fontsize=14, fontweight='bold')
    plt.xlabel('Subjects', fontsize=12)
    plt.ylabel('Mean Score', fontsize=12)
    plt.savefig('../images/subject_averages.png', bbox_inches='tight')
    plt.close()
    print("✓ Saved: images/subject_averages.png")
    
    print("\n Success! All analysis and visualizations are complete.")

except FileNotFoundError:
    print("❌ Error: Could not find 'students.csv'. Please check your data directory layout.")
    #I TRY SHA