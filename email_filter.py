print("Welcome to DAY 6: Dynamic Domain Extractor ")
print("---------------------------------------------")

# Step 1: Get bulk email input from the user
raw_input = input("Enter your emails (separated by commas): ")

# Step 2: Convert the string into a list of emails
email_list = raw_input.split(',')

# Step 3: List comprehension to clean spaces (.strip) and extract domain ([1])
domains = [email.strip().split('@')[1] for email in email_list if '@' in email]

# Step 4: Display the final results professionally
print("\n--- Results ---")
print("Total Emails Entered:", len(email_list))
print("Extracted Domains:   ", domains)
