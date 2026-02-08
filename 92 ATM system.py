def atm_system():
    balance = 1000
    pin = "1234"
    
    entered_pin = input("Enter PIN: ")
    
    if entered_pin != pin:
        print("Invalid PIN!")
        return
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(f"Balance: ${balance}")
            
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
            
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn ${amount}. New balance: ${balance}")
            else:
                print("Insufficient balance!")
                
        elif choice == '4':
            print("Thank you!")
            break
