# Task 4: Message Length Analyzer
# Real-World Application: Text filtering and validation systems

def analyze_messages(messages):
    """
    Analyze message lengths and flag long messages
    
    Args:
        messages: List of text messages
    
    Returns:
        None (prints analysis)
    """
    max_length = 10
    
    print("=" * 50)
    print("MESSAGE LENGTH ANALYSIS")
    print("=" * 50)
    
    for i, message in enumerate(messages, 1):
        length = len(message)
        flag = "⚠️ LONG MESSAGE" if length > max_length else "✓"
        print(f"Message {i}: '{message}'")
        print(f"  Length: {length} characters {flag}")
        print()
    
    print("=" * 50)

# Test the function
messages = ["Hi", "Welcome to the platform", "OK"]
analyze_messages(messages)
