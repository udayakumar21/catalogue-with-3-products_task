    def calculate_discount(cart_total, q, wrapped_gifts):
    dis_amount = 0
    # flat_10_discount
    if cart_total > 200:
        dis_amount = min(dis_amount, 10)  
    # bulk_5_discount
    for quantity in q:
        if quantity > 10:
            dis_amount = max(dis_amount, 0.05 * quantity)
    # bulk_10_discount
    total_quantity = sum(q)
    if total_quantity > 20:
        dis_amount = max(dis_amount, 0.10 * cart_total)
    # tiered_50_discount
    if total_quantity > 30 and any(quantity > 15 for quantity in q):
        tiered_discount = 0.50 * sum(max(0, quantity - 15) for quantity in q)
        dis_amount = max(dis_amount, tiered_discount)
    return dis_amount

def main():
    p= {'Product A': 20, 'Product B': 40, 'Product C': 50}
    q = []
    wrapped_gifts = []
    for product in p:
        quantity = int(input(f"Enter quantity for {product}: "))
        is_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == 'yes'
        q.append(quantity)
        wrapped_gifts.append(is_wrapped)
    subtotal = sum(quantity * price for quantity, price in zip(q, p.values()))
    dis_amount = calculate_discount(subtotal, q, wrapped_gifts)
    gift_wrap_fee = sum(1 for wrapped in wrapped_gifts if wrapped)
    shipping_fee = (sum(q) + 9) // 10 * 5 
    total = subtotal - dis_amount + gift_wrap_fee + shipping_fee
    print("\nInvoice Details:")
    for product, quantity, wrapped in zip(p.keys(), q, wrapped_gifts):
        print(f"{product} - Quantity: {quantity}, Total: ${quantity * p[product]}{' (Gift Wrapped)' if wrapped else ''}")
    print("\nSubtotal: $", subtotal)
    print(f"Discount Applied: ${dis_amount} ({'No Discount' if dis_amount == 0 else 'Discount Applied'})")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Shipping Fee: ${shipping_fee}")
    print("\nTotal: $", total)

if __name__ == "__main__":
    main()
