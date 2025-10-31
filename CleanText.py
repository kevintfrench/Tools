product = 'InsertText'

# Define clean_text function
def clean_text(text, lower=True):
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behavior
print(clean_text(product))