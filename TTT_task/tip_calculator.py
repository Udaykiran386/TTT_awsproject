def validate_bill_amount(value):
    try:
        bill = float(value)
    except (TypeError, ValueError):
        raise ValueError("Bill amount must be a valid number.")

    if bill <= 0:
        raise ValueError("Bill amount must be greater than 0.")

    return bill


def validate_tip_percentage(value):
    try:
        percentage = float(value)
    except (TypeError, ValueError):
        raise ValueError("Tip percentage must be a valid number.")

    if percentage < 0 or percentage > 100:
        raise ValueError("Tip percentage must be between 0 and 100.")

    return percentage


def calculate_tip(bill, tip_percent):
    bill = validate_bill_amount(bill)
    tip_percent = validate_tip_percentage(tip_percent)

    tip_amount = bill * (tip_percent / 100)
    total_amount = bill + tip_amount

    return tip_amount, total_amount


def main():
    try:
        bill = input("Enter the bill amount: ")
        tip_percent = input("Enter the tip percentage: ")

        tip_amount, total_amount = calculate_tip(bill, tip_percent)

        print(f"Tip amount: ${tip_amount:.2f}")
        print(f"Total amount: ${total_amount:.2f}")
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()