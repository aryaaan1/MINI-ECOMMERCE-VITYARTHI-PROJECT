# Mini E-Commerce Management System

## Overview

The Mini E-Commerce Management System is a Python-based application that simulates the basic workflow of an online shopping system.

The application allows users to view products, search for products, add products to a shopping cart, enter customer information, validate the information, and create orders. Completed orders are stored in a JSON file.

## Features

- Display available products
- Search for products
- Add products to the shopping cart
- Manage cart quantities
- Collect customer information
- Validate customer name, phone number, and address
- Generate order IDs
- Create and save orders
- Store order information in `orders.json`
- Unit and validation testing using pytest

## Technologies Used

- Python
- JSON
- Pytest
- Git/GitHub

## Project Structure

```text
MINI-ECOMMERCE-VITYARTHI-PROJECT/
│
├── main.py
├── products.py
├── search.py
├── cart.py
├── customer.py
├── validation.py
├── orders.py
├── orders.json
├── statement.md
├── README.md
│
└── tests/
    ├── test_validation.py
    └── test_orders.py

Description of Modules
main.py
Controls the main flow of the application and connects the different modules.
products.py
Contains the product information and product-related operations.
search.py
Provides product searching functionality.
cart.py
Handles adding products to the shopping cart and managing cart items.
customer.py
Handles customer information used during the ordering process.
validation.py
Validates customer information such as name, phone number, and address.
orders.py
Handles order creation, order ID generation, loading existing orders, and saving new orders.
orders.json
Stores the completed order information.

Start
  |
  v
Display Products
  |
  v
Search for Product
  |
  v
Add Product to Cart
  |
  v
Manage Cart
  |
  v
Enter Customer Information
  |
  v
Validate Information
  |
  v
Create Order
  |
  v
Generate Order ID
  |
  v
Save Order to orders.json
  |
  v
Order Completed


Installation
1. Install Python
Install Python 3 or later on your system.
2. Clone the Repository
git clone <https://github.com/aryaaan1/MINI-ECOMMERCE-VITYARTHI-PROJECT>
3. Open the Project Directory
cd MINI-ECOMMERCE-VITYARTHI-PROJECT
4. Install Testing Dependency
pip install pytest
Running the Application
Run the main program using:
python main.py
Follow the instructions displayed in the terminal.
Testing
The project contains tests for validation and order-related functionality.
The test files are located inside the tests folder:
tests/
├── test_validation.py
└── test_orders.py
To run the tests:
python -m pytest tests/
Individual test files can also be executed:
python -m pytest tests/test_validation.py
python -m pytest tests/test_orders.py
Data Storage
The project uses a JSON file for storing completed orders.
orders.json
Each order contains information such as the order ID, customer details, ordered products, quantities, and total amount.
Input Validation
The application validates important customer information before processing an order.
Examples include:
Valid customer name
Valid phone number
Non-empty address
Invalid input is rejected instead of being stored as a completed order.
Testing Approach
The project uses basic unit and validation tests with pytest.
The tests check both valid and invalid inputs and verify important order operations such as:
Loading orders
Generating order IDs
Creating and saving orders
Validating customer information
Limitations
The current version is a simple standalone e-commerce application. It does not include:
Online payment processing
User authentication
Real-time inventory management
Online database connectivity
Delivery tracking
Cloud deployment
Future Enhancements
Possible future improvements include:
Adding a graphical or web-based interface
Adding user authentication
Adding a database such as SQLite or MySQL
Adding online payment integration
Adding inventory management
Adding order status and delivery tracking
Adding an administrator dashboard
Project Purpose
This project was developed as part of the VITyarthi Build Your Own Project evaluation to apply Python programming concepts in a practical e-commerce application.