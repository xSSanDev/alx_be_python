def safe_divide(numerator, denominator):
    try:
        # Attempt to convert numerator to a float
        num = float(numerator)
        # Attempt to convert denominator to a float
        denom = float(denominator)
        # Perform the division
        result = num / denom
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    except ValueError:
        # Handle non-numeric input
        return "Error : Please enter numeric values only."
    # Return the result if no exceptions were raised
    return f"The resut of the division is : {result}"