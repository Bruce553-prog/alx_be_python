def safe_divide(numerator, denominator):
    """
    Performs division safely with error handling.
    Returns the result or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
