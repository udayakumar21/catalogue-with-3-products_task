"# catalogue-with-3-products_task" 
Catalogue with 3 Products - Discount Program

This Python program simulates a shopping cart with three products and applies various discount rules based on the cart contents. The program also calculates gift wrap fees, shipping fees, and provides a detailed invoice for the user.
<br/>
 Products <br/>

- Product A: $20 <br/>
- Product B: $40<br/>
- Product C: $50<br/>
<br/>
# Discount Rules <br/>
<br/>
1. Flat 10% Discount**: If the cart total exceeds $200, apply a flat $10 discount on the cart total. <br/>
2. Bulk 5% Discount**: If the quantity of any single product exceeds 10 units, apply a 5% discount on that item's total price. <br/>
3. Bulk 10% Discount**: If the total quantity exceeds 20 units, apply a 10% discount on the cart total. <br/>
4. Tiered 50% Discount**: If the total quantity exceeds 30 units and any single product quantity is greater than 15, apply a 50% discount on products above 15 quantity. The first 15 quantities have the original price, and units above 15 will get a 50% discount. <br/>
<br/>
Note: Only one rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for the customer. <br/>
<br/>
# Fees <br/>
<br/>
- Gift Wrap Fee: $1 per unit. <br/>
- Shipping Fee: 10 units can be packed in one package, and the shipping fee for each package is $5. <br/>
<br/>
# Program Usage<br/>
<br/>
1. The program will prompt the user to enter the quantity of each product and whether the product is wrapped as a gift. <br/>
<br/>
2. It will then display the following details: <br/>
   - Product name, quantity, and total amount of that product.<br/>
   - Subtotal.<br/>
   - The applied discount rule and the discount amount.<br/>
   - Shipping fee and gift wrap fee.<br/>
   - Total amount.<br/>
<br/>
# How to Run the Program <br/> 
1.Clone this repository to your local machine.<br/> 
<br/>
2.Navigate to the project directory in your terminal.<br/> 
<br/>
3.Run the program using Python:<br/> 
<br/>
  python main.py <br/> 
  <br/>
4.Follow the prompts to enter product quantities and gift wrapping preferences.<br/> 
<br/>
5.The invoice details will be displayed in the terminal.<br/> 
<br/>
Code Structure<br/> 
main.py: Contains the main program logic.<br/> 
calculate_discount.py: Contains the function for calculating discounts.<br/> 
<br/>

<br/>


 
 
