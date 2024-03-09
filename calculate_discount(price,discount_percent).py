def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price=price * (1 - discount_percent / 100)
        return discounted_price
    else:
        final_price = price
    return final_price
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage(0-100):"))
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after discount: ${final_price:.2f}")