# Project Statement

## Project Title

Mini E-Commerce Management System

## 1. Problem Statement

Small e-commerce applications need a simple way to manage products, search for items, maintain a shopping cart, collect customer information, and create orders. Without an organized system, handling product information, customer details, cart items, and orders manually can lead to errors and make the purchasing process inefficient.

The objective of this project is to develop a simple Python-based e-commerce system that provides a structured workflow for browsing products, searching for products, adding items to a cart, validating customer information, and creating and storing orders.

## 2. Scope of the Project

The project focuses on the basic operations required in a small e-commerce application.

The system covers:

- Product management and product display
- Searching for products
- Adding and managing products in a shopping cart
- Collecting customer information
- Validating customer name, phone number, and address
- Generating unique order IDs
- Creating and saving customer orders
- Storing order information in a JSON file

The project is designed as a simple standalone Python application and does not currently include online payment processing, real-time inventory synchronization, or a cloud-based database.

## 3. Target Users

The intended users of the system are:

- Customers who want to browse and purchase products
- Small-scale sellers who need a basic way to manage orders
- Students and beginners learning Python programming and software development concepts

## 4. High-Level Features

### Product Management

The system provides product information that can be displayed to the user during the shopping process.

### Product Search

Users can search for products based on available product information.

### Shopping Cart

Users can add products to their cart and manage the quantities of selected products before placing an order.

### Customer Information

The system collects customer details such as name, phone number, and address.

### Input Validation

Customer information is validated before an order is processed. Invalid information is rejected to reduce incorrect data entry.

### Order Management

The system generates an order ID and creates an order containing customer information and selected products.

### Order Storage

Completed orders are stored in `orders.json`, allowing order information to be retained after the program finishes.

## 5. Project Objective

The main objective of the project is to demonstrate the use of Python programming concepts to build a modular e-commerce application with a clear user workflow, input validation, order processing, and persistent data storage.