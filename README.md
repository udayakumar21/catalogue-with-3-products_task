"# catalogue-with-3-products_task" 
# Catalogue with 3 Products - Discount Program

This Python program simulates a shopping cart with three products and applies various discount rules based on the cart contents. The program also calculates gift wrap fees, shipping fees, and provides a detailed invoice for the user.

## Products

- Product A: $20 <br/>
- Product B: $40<br/>
- Product C: $50<br/>

## Discount Rules

1. **Flat 10% Discount**: If the cart total exceeds $200, apply a flat $10 discount on the cart total.
2. **Bulk 5% Discount**: If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price.
3. **Bulk 10% Discount**: If the total quantity exceeds 20 units, apply a 10% discount on the cart total.
4. **Tiered 50% Discount**: If the total quantity exceeds 30 units and any single product quantity is greater than 15, apply a 50% discount on products above 15 quantity. The first 15 quantities have the original price, and units above 15 will get a 50% discount.

Note: Only one rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for the customer.

## Fees

- Gift Wrap Fee: $1 per unit.
- Shipping Fee: 10 units can be packed in one package, and the shipping fee for each package is $5.

## Program Usage

1. The program will prompt the user to enter the quantity of each product and whether the product is wrapped as a gift.

2. It will then display the following details:
   - Product name, quantity, and total amount of that product.
   - Subtotal.
   - The applied discount rule and the discount amount.
   - Shipping fee and gift wrap fee.
   - Total amount.

## How to Run the Program

1. Clone the repository:
   git clone https://github.com/udayakumar21/catalogue-with-3-products_task.git

   cd catalogue-with-3-products_task
   python main.py



 
 
