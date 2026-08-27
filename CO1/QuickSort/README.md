**README – Delivery Order Route Priority** 

**1. Project Title**
Delivery Order Route Priority using Quick Sort

**2. Description**
This Python program stores delivery orders along with their delivery distance and sorts the orders based on distance using the Quick Sort algorithm.

The order with the shortest delivery distance will appear first, helping to prioritize nearby deliveries.

**3. Objective**
Accept the number of delivery orders.
Store the Order ID and Delivery Distance.
Sort the delivery orders based on distance.
Display the orders from shortest distance to longest distance.
Prevent invalid inputs such as zero/negative number of orders and negative distances.
**4. Algorithm **
Quick Sort

Quick Sort works by:

Selecting a pivot element.
Comparing other elements with the pivot.
Placing smaller elements before the pivot.
Placing larger elements after the pivot.
Recursively sorting the left and right portions.
In this program, the delivery distance is used for comparison.

**5. Input**
The program takes:

Number of delivery orders
Order ID
Delivery distance in kilometers
Example:

Enter number of delivery orders: 3

Enter order ID 1: ORD101
Enter delivery distance for ORD101 (km): 15

Enter order ID 2: ORD102
Enter delivery distance for ORD102 (km): 5

Enter order ID 3: ORD103
Enter delivery distance for ORD103 (km): 10

**6. Output**
--- ORDERS SORTED BY DELIVERY DISTANCE ---

Order ORD102 - 5 km
Order ORD103 - 10 km
Order ORD101 - 15 km
7. Main Functions
    quick_sort()
  def quick_sort(orders, low, high):
This function recursively sorts the delivery orders.

partition()
def partition(orders, low, high):
This function selects the pivot and arranges the orders around the pivot.

main()
def main():
This function:

Gets input from the user
Stores the orders
Calls Quick Sort
Displays the sorted result
8. Data Structure
A list of dictionaries is used to store the orders.

Example:

orders = [
    {"id": "ORD101", "distance": 15},
    {"id": "ORD102", "distance": 5}
]
9. Validation
The program checks:

if n <= 0:
to make sure the number of orders is greater than zero.

It also checks:

if distance < 0:
to prevent negative delivery distances.

**10. Time Complexity**
Best/Average Case: O(n log n)
Worst Case: O(n²)
Space Complexity: O(log n) on average because of recursion.
11. How to Run
Open the Python file in VS Code.
Open the Terminal.
Run the program using:
python QuickSort_DeliveryOrders.py
Enter the required delivery order details.
The program displays the orders sorted by delivery distance.
12. Conclusion
The program demonstrates how the Quick Sort algorithm can be applied to a real-world delivery system to prioritize orders based on delivery distance.
