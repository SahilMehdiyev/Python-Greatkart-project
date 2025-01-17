# Python GreatKart Project

Welcome to the **Python GreatKart Project**! This repository contains a fully-featured eCommerce application built using the Python Django framework.

---

## Overview

GreatKart is an eCommerce application developed with the Python Django framework. It includes features such as a custom user model, product categories, shopping carts with item incrementing, decrementing, and removal functionalities, unlimited product image galleries, order processing, payment integration, and post-order operations like stock management and order confirmation emails. Additionally, it offers a review and rating system with interactive star ratings, and user account functionalities for profile management.

---

## Features

- **Custom User Model**: Manage user authentication and profiles.
- **Product Management**: Create and manage product categories and items.
- **Shopping Cart**: Add, remove, and adjust quantities of items in the cart.
- **Product Image Gallery**: Upload and display multiple images per product.
- **Order Processing**: Handle order creation, payment integration, and order completion.
- **Review and Rating System**: Allow customers to leave reviews and rate products.
- **User Account Management**: Enable users to edit profiles, change passwords, and view order history.

---

## Technologies Used

- **Python**: Programming language used for development.
- **Django**: High-level Python web framework.
- **HTML/CSS/JavaScript**: Front-end technologies for the user interface.
- **Bootstrap**: Responsive design framework for a polished UI.
- **PostgreSQL**: Database for storing application data.
- **Stripe**: Payment gateway integration for processing transactions.
- **Docker**: Containerization for simplified deployment.
- **Poetry**: Dependency management tool for Python.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SahilMehdiyev/Python-Greatkart-project.git
   cd Python-Greatkart-project
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Set up the environment**:
   - Create a `.env` file in the project root directory and add necessary environment variables.
   - Refer to `.env.example` for guidance.

4. **Run Docker containers**:
   Use Docker to start required services like the database:
   ```bash
   docker-compose up -d
   ```

5. **Apply database migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   poetry run python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   poetry run python manage.py runserver
   ```

---

## Usage

- Access the site locally at `http://127.0.0.1:8000/`.
- Use the admin panel for managing products, orders, and user accounts at `http://127.0.0.1:8000/admin/`.
- Explore the interactive eCommerce functionalities like adding products to the cart, completing orders, and reviewing products.

---

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

Please ensure your contributions align with the project's goals and maintain clean, modular code.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or feedback, feel free to reach out:

- **Author**: Sahil Mehdiyev
- **GitHub**: [SahilMehdiyev](https://github.com/SahilMehdiyev)

---

Happy building your eCommerce platform! 🚀
