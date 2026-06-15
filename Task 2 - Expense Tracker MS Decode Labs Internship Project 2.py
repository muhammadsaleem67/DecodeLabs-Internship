
print(" Welcome to the MS DecodeLabs Expense Tracker ")
print("Enter your expenses one by one. Type 'done' when you are finished.\n")
# 1. Initialize variable
total_spent = 0.0  
# 2. we Use a while loop for continuous data entry
while True:
    user_input = input("Enter an expense amount (e.g., 100, 50, 20): ")
    # it also Check if the user wants to exit the loop
    if user_input.lower() == 'done':
        break
    try:
        # Convert the text input into a decimal number (float)
        new_expense = float(user_input)
        # 3. The Accumulator Logic: total = total + new_expense
        total_spent += new_expense 
        print(f"Expense added. Current running total: ${total_spent:.2f}\n") 
    except ValueError:
        # Handle cases where the user types words instead of numbers
        print(" Invalid input! Please enter a numerical value or type 'done'.\n")
# 4. Display the final result when the loop ends
print("\n" + "="*30)
print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
print("="*30)
