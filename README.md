# E-commerce flask app with Database using Custom Object Relational Mapper
This is an ORM (Object Relational Mapper) built from scratch using Python. It is acts as an interface between a relational database such as SQL and an object-oriented program.

# Video Presentation
https://drive.google.com/drive/folders/1w7yylv2CrS47gVvFBde4o44J96gQbbHV?usp=sharing

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)


## Introduction

This is a Flask-based backend application for an e-commerce website. The application interacts with an SQLite database using a custom ORM (Object-Relational Mapping) to perform CRUD operations on products, users, and orders. The app fetches product data from an external API and stores it in the database, allowing users to browse products, sign up, and place orders.

## Features

- Fetch product data from an external API and store it in the database.
- Retrieve product information from the database.
- Add user details and orders to the database.
- Empty the shopping cart by deleting orders from the database.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/overlordiam/Custom_ORM.git
   cd Custom_ORM
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   ```

## Usage

  1. Start the Flask server:
     
     ```bash
     python main.py
     ```

  2. Access the endpoints using a web client or API client like Postman.

## Endpoints

1. Fetch Product Data and Store in Database

    - Endpoint: /
    - Method: POST
    - Description: Fetch product data from an external API and store it in the "products" table of the database.

2. Get Products

    - Endpoint: /products
    - Method: POST
    - Description: Retrieve product information from the "products" table of the database.

3. Empty Cart

    - Endpoint: /emptyCart
    - Method: POST
    - Description: Delete all orders from the "orders" table to empty the shopping cart.

4. Sign Up

    - Endpoint: /signUp
    - Method: POST
    - Description: Add user details to the "users" table of the database.

5. Add Orders

    - Endpoint: /addOrders
    - Method: POST
    - Description: Add orders to the "orders" table of the database.

## Tests

  The application includes test cases to verify the functionality of the 
  API endpoints. Run the tests using the following command:
  
    ```bash
    python All_test.py
    ```

## Database

The application uses an SQLite database named "APP2.db" to store product, user, and order data.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your requirements.

## Credits

This project is developed and maintained by Overlordiam.

