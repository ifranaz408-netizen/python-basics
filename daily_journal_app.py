import datetime

print("=========================================")
print("  Welcome to Day 8 of: Daily Journal App")
print("=========================================")

while True:
    print("\n--- MAIN MENU ---")
    print("1. Write a new entry ")
    print("2. View past entries ")
    print("3. Exit ")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        # Step 1 & 2: Time aur input lena
        current_time = datetime.datetime.now()
        formated_time = current_time.strftime("%d_%m_%Y %I:%M %p")
        user_input = input("\nWrite your thoughts for today: ")
        final_entry = f"[{formated_time}] - {user_input}\n"
        
        # Step 3: File mein save karna
        with open("journal_file.txt", "a") as my_file:
            my_file.write(final_entry)
        print(" Your entry has been saved successfully!")
        
    elif choice == "2":
        print("\n--- Reading current entries from file ---")
        # Step 4: Try-Except lagakar file ko read karna
        try:
            with open("journal_file.txt", "r") as my_file: 
                content = my_file.read()
                if content.strip() == "":
                    print("Diary is empty right now!")
                else:
                    print(content)
        except FileNotFoundError: 
            print("Oops! No journal file found yet. Write an entry first!")
            
    elif choice == "3":
        print("\nThank you for using Daily Journal App. Allah Hafiz! ")
        break  # Loop ko break karke program band kar dega
        
    else:
        print(" Invalid Choice! Please enter 1, 2, or 3.")
      
