# Inventory Management System

A modular **Inventory Management System** built with **Python and SQLite**, designed to help small businesses manage products, suppliers, purchases, and sales.

The project was initially developed as a **command-line application**, with a focus on database management, CRUD operations, SQL queries, and object-oriented programming.

---

## Features

* Add, update, delete, and view products
* Manage supplier information
* Record purchases and sales
* Track product quantities and stock levels
* Automatically update stock quantities
* Identify low-stock products
* View product and sales information
* SQLite database integration
* Modular structure based on **Object-Oriented Programming (OOP)** principles

---

## Tech Stack

| Category          | Tools / Technologies                               |
| ----------------- | -------------------------------------------------- |
| **Language**      | Python 3                                           |
| **Database**      | SQLite                                             |
| **Database Tool** | SQLiteStudio                                       |
| **Libraries**     | `sqlite3`, `tabulate`                              |
| **Concepts**      | CRUD Operations, SQL Queries, OOP, Database Design |

---

## Database Design

The system uses SQLite to manage the following main entities:

* **Products** — Stores product information, prices, and stock quantities.
* **Suppliers** — Stores supplier information.
* **Purchases** — Records product purchases and their associated suppliers.
* **Sales** — Records product sales and selling prices.

The database uses **primary keys, foreign keys, unique constraints, and data validation** to maintain data integrity.

---

## Project Structure

The application follows a modular structure that separates database operations and application logic, making the code easier to maintain and extend.

---

## Future Improvements

The project can be extended into a web-based inventory management application using:

* **Flask**
* **Jinja2**
* Web-based user interface
* RESTful API endpoints
* Authentication and authorization
* Improved reporting and analytics

---

## Project Status

**Current Version:** Command-Line Application

The current implementation focuses on the core inventory management functionality using **Python and SQLite**. Web-based functionality is planned as a future improvement.

---

## Purpose

This project was developed to strengthen practical understanding of:

* Python programming
* Object-Oriented Programming
* SQL and relational databases
* SQLite database management
* CRUD operations
* Database relationships
* Modular software design
