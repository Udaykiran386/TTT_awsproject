def calculate_tip(bill_amount, tip_percent):
    if bill_amount < 0:
        raise ValueError("Bill amount cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percentage cannot be negative.")
    return bill_amount * (tip_percent / 100)


def calculate_total(bill_amount, tip_percent):
    return bill_amount + calculate_tip(bill_amount, tip_percent)


def calculate_per_person(bill_amount, tip_percent, people):
    if people <= 0:
        raise ValueError("People must be greater than 0.")
    total = calculate_total(bill_amount, tip_percent)
    return total / people


def print_example(name, bill_amount, tip_percent, people=1):
    tip = calculate_tip(bill_amount, tip_percent)
    total = calculate_total(bill_amount, tip_percent)
    each_person = calculate_per_person(bill_amount, tip_percent, people)

    print(f"{name}:")
    print(f"  Bill: ${bill_amount:.2f}")
    print(f"  Tip ({tip_percent}%): ${tip:.2f}")
    print(f"  Total: ${total:.2f}")
    if people > 1:
        print(f"  Per person: ${each_person:.2f}")
    print("-" * 30)


if __name__ == "__main__":
    examples = [
        ("Casual lunch", 42.50, 15, 2),
        ("Dinner date", 86.00, 20, 2),
        ("Friends dinner", 160.00, 18, 4),
    ]

    for example in examples:
        print_example(*example)