# Monica Tjatindi - Budget Calculator 
# A simple script to calculate monthly savings 

def budget_calculator(): 
    try: 
        income = float(input("Enter your monthly income: ")) 
        expenses = float(input("Enter your monthly expenses: ")) 
        
        savings = income - expenses 
        
        print(f"\nYour monthly savings are: ${savings:.2f}") 
        if savings > 0: 
            print("✅ Great job! You're saving money.") 
        elif savings == 0: 
            print("⚖️ You're breaking even — no savings, no debt.") 
        else: print("⚠️ Careful! You're overspending.") 
    except ValueError: 
        print("Please enter valid numbers for income and expenses.") 
        
if __name__ == "__main__": 
    budget_calculator()