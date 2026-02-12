# Task 3: Simple Data Cleaner
# Real-World Application: Data preprocessing before analysis

def clean_names(names):
    """
    Clean and standardize user names
    
    Args:
        names: List of names with inconsistent formatting
    
    Returns:
        List of cleaned names
    """
    cleaned_names = []
    
    for name in names:
        # Remove extra spaces and convert to lowercase
        cleaned_name = name.strip().lower()
        cleaned_names.append(cleaned_name)
    
    return cleaned_names

# Test the function
names = [" Alice ", "bob", " CHARLIE "]

print("Original Names:", names)
print("Cleaned Names:", clean_names(names))
