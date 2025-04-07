# TechWave - Cataloguing Application

TechWave is a Django-based application designed to streamline inventory management, allowing employees, managers, suppliers, and IT officers to efficiently handle catalog items.

## Features

TechWave supports the following functionalities:

- **View Catalog Items**: Managers can view product details, including name, stock amount, and price, to manage inventory effectively.
- **Add New Products**: Suppliers can create new catalog listings with details like name and price.
- **Edit Products**: Inventory specialists can update product names, amounts, and prices as needed.
- **Delete Products**: Inventory specialists can remove discontinued items from the catalog.
- **Filter Catalog Items**: Employees can filter items by price, color, and stock amount to focus on specific products.
- **Sort Catalog Items**: Employees can sort items (e.g., by price) for easier navigation.
- **Secure Login**: Employees can log in to securely create, update, and delete catalog items.
- **User Management**: IT officers can add and remove employee logins to control system access.
- **Search Items**: Employees can query items by ID or name to quickly find specific products.
- **Upload Item Pictures**: Inventory specialists can upload images for visual browsing of catalog items.

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default, configurable to others like PostgreSQL)
- **Testing**: unittest, coverage.py

## Installation

Follow these steps to run TechWave from the provided ZIP file:

1. **Download and Unzip the File**  
   - Download `TechWave.zip` from [[Download Zip](https://github.com/kz4killua/techwave/blob/main/techwave.zip)].  
   - Extract the ZIP file to a folder on your computer (e.g., double-click or right-click and select "Extract All").

2. **Install Python (if not already installed)**  
   - TechWave requires Python 3.8+. Download and install it from [python.org](https://www.python.org/).  
   - Verify installation by opening a terminal (e.g., Command Prompt on Windows, Terminal on Mac) and typing `python --version` (or `python3 --version` on some systems).

3. **Open the Project Folder**  
   - Navigate to the extracted `TechWave` folder in a terminal:  
     - Command: `cd path/to/TechWave` (e.g., `cd Downloads/TechWave`).

4. **Set Up a Virtual Environment (Optional but Recommended)**  
   - Create a virtual environment: `python -m venv venv`.  
   - Activate it:  
     - Windows: `venv\Scripts\activate`  
     - Mac/Linux: `source venv/bin/activate`

5. **Install Dependencies**  
   - Run: `pip install -r requirements.txt` to install Django and other required packages.  
   - Note: If `requirements.txt` is missing, install Django manually with `pip install django`.

6. **Apply Database Migrations**  
   - Initialize the database: `python manage.py migrate`.  
   - This sets up the SQLite database included in the project.

7. **Create a Superuser (Admin Account)**  
   - Run: `python manage.py createsuperuser`.  
   - Follow the prompts to enter a username, email, and password. This account can manage users and items.

8. **Start the Application**  
   - Launch the server: `python manage.py runserver`.  
   - You’ll see output like "Starting development server at http://127.0.0.1:8000/".

## Usage

- Open your web browser and go to `http://127.0.0.1:8000/`.  
- Log in with the superuser credentials to access admin features (e.g., at `/admin`), or use the app as a regular user to manage catalog items.  
- Explore features like adding items, filtering, sorting, and uploading pictures via the interface.
