import re

def extract_email_or_phone(text):
    # Clean up the input by stripping unwanted characters (like trailing colons, spaces, angle brackets)
    text = text.strip().strip(':<>')

    # Regex pattern for email extraction, with or without angle brackets
    email_pattern = r'<?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)>?'
    
    # Regex pattern for 10-digit phone numbers
    phone_pattern_10 = r'(\d{3})(\d{3})(\d{4})'
    
    # Regex pattern for 11-digit phone numbers (with country code)
    phone_pattern_11 = r'(\d{1})(\d{3})(\d{3})(\d{4})'
    
    # Try to find an email first, with or without angle brackets
    email_match = re.search(email_pattern, text)
    
    # Check if the email contains only digits before the @ sign (potential phone number)
    if email_match:
        local_part = email_match.group(1).split('@')[0]
        if local_part.isdigit() and len(local_part) == 10:
            # If the local part is a 10-digit number, treat it as a phone number
            phone_match = re.search(phone_pattern_10, local_part)
            if phone_match:
                # Format the phone number as XXX*XXX*XXXX
                formatted_phone = f"{phone_match.group(1)}*{phone_match.group(2)}*{phone_match.group(3)}"
                return formatted_phone
        elif local_part.isdigit() and len(local_part) == 11:
            # If the local part is an 11-digit number, treat it as a phone number with country code
            phone_match = re.search(phone_pattern_11, local_part)
            if phone_match:
                # Format the phone number as 1*XXX*XXX*XXXX
                formatted_phone = f"{phone_match.group(1)}*{phone_match.group(2)}*{phone_match.group(3)}*{phone_match.group(4)}"
                return formatted_phone
        else:
            # Otherwise, return the cleaned-up email
            return email_match.group(1)
    
    # If no email or numeric email, try to find a phone number in the text
    phone_match_10 = re.search(phone_pattern_10, text)
    phone_match_11 = re.search(phone_pattern_11, text)
    
    if phone_match_11:
        # Format the phone number as 1*XXX*XXX*XXXX
        formatted_phone = f"{phone_match_11.group(1)}*{phone_match_11.group(2)}*{phone_match_11.group(3)}*{phone_match_11.group(4)}"
        return formatted_phone
    elif phone_match_10:
        # Format the phone number as XXX*XXX*XXXX
        formatted_phone = f"{phone_match_10.group(1)}*{phone_match_10.group(2)}*{phone_match_10.group(3)}"
        return formatted_phone
    
    return "No valid email or phone number found."

def main():
    while True:
        # Prompt user for input
        user_input = input("Please enter a line containing an email or phone number: ")

        # Clean and process the input
        result = extract_email_or_phone(user_input)

        # Output the cleaned result (no additional text)
        print(result)

        # Ask user if they want to start over or exit
        restart = input("Do you want to submit another entry? (y/n): ").strip().lower()
        if restart != 'y':
            print("Exiting the program. Goodbye!")
            break

# Run the main loop
main()