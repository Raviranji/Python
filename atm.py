balance = int(input("Enter balance: "))
withdrawal = int(input("Enter withdrawal: "))

if withdrawal % 100 != 0:
    print("Withdrawal failed: Amount must be a multiple of 100")

elif withdrawal > balance:
    print("Withdrawal failed: Insufficient balance")

elif balance - withdrawal < 500:
    print("Withdrawal failed: Minimum balance should be 500")

else:
    balance -= withdrawal
    print("Withdrawal successful")
    print(f"Remaining balance: {balance}")
