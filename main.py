def calculate_discount(cart_total, quantities, wrapped_gifts):
    discount_amount = 0
    # flat_10_discount
    if cart_total > 200:
        discount_amount = min(discount_amount, 10)  
    # bulk_5_discount
    for quantity in quantities:
        if quantity > 10:
            discount_amount = max(discount_amount, 0.05 * quantity)
    # bulk_10_discount
    total_quantity = sum(quantities)
    if total_quantity > 20:
        discount_amount = max(discount_amount, 0.10 * cart_total)
    # tiered_50_discount
    if total_quantity > 30 and any(quantity > 15 for quantity in quantities):
        tiered_discount = 0.50 * sum(max(0, quantity - 15) for quantity in quantities)
        discount_amount = max(discount_amount, tiered_discount)
    return discount_amount

def main():
    products = {'Product A': 20, 'Product B': 40, 'Product C': 50}
    quantities = []
    wrapped_gifts = []
    for product in products:
        quantity = int(input(f"Enter quantity for {product}: "))
        is_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == 'yes'
        quantities.append(quantity)
        wrapped_gifts.append(is_wrapped)
    subtotal = sum(quantity * price for quantity, price in zip(quantities, products.values()))
    discount_amount = calculate_discount(subtotal, quantities, wrapped_gifts)
    gift_wrap_fee = sum(1 for wrapped in wrapped_gifts if wrapped)
    shipping_fee = (sum(quantities) + 9) // 10 * 5 
    total = subtotal - discount_amount + gift_wrap_fee + shipping_fee
    print("\nInvoice Details:")
    for product, quantity, wrapped in zip(products.keys(), quantities, wrapped_gifts):
        print(f"{product} - Quantity: {quantity}, Total: ${quantity * products[product]}{' (Gift Wrapped)' if wrapped else ''}")

    print("\nSubtotal: $", subtotal)
    print(f"Discount Applied: ${discount_amount} ({'No Discount' if discount_amount == 0 else 'Discount Applied'})")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Shipping Fee: ${shipping_fee}")
    print("\nTotal: $", total)

if __name__ == "__main__":
    main()
