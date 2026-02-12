# Task 5: Error Message Detector
# Real-World Application: Monitoring and log analysis systems

def detect_errors(logs):
    """
    Detect and count error messages from system logs
    
    Args:
        logs: List of log entries
    
    Returns:
        None (prints error count)
    """
    error_count = 0
    
    # Count ERROR entries
    for log in logs:
        if log == "ERROR":
            error_count += 1
    
    # Print results
    print("=" * 40)
    print("LOG ANALYSIS REPORT")
    print("=" * 40)
    print(f"Total Log Entries: {len(logs)}")
    print(f"Total ERROR Count: {error_count}")
    print("=" * 40)
    
    # Show log breakdown
    print("\nLog Breakdown:")
    for log_type in set(logs):
        count = logs.count(log_type)
        print(f"  {log_type}: {count}")

# Test the function
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
detect_errors(logs)
