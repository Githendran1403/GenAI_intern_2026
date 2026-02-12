# Task 2: Pass / Fail Analyzer
# Real-World Application: Academic evaluation systems

def analyze_results(marks):
    """
    Analyze student results and count pass/fail students
    
    Args:
        marks: List of student marks
    
    Returns:
        None (prints analysis)
    """
    pass_count = 0
    fail_count = 0
    passing_marks = 50
    
    # Count pass and fail students
    for mark in marks:
        if mark >= passing_marks:
            pass_count += 1
        else:
            fail_count += 1
    
    # Print results
    print("=" * 40)
    print("STUDENT RESULT ANALYSIS")
    print("=" * 40)
    print(f"Total Students: {len(marks)}")
    print(f"Pass Students: {pass_count}")
    print(f"Fail Students: {fail_count}")
    print(f"Pass Percentage: {(pass_count/len(marks))*100:.2f}%")
    print("=" * 40)

# Test the function
marks = [45, 78, 90, 33, 60]
analyze_results(marks)
