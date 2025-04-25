

Ticket Booking System
This is a Ticket Booking System built using Django for managing shows, bookings, and user authentication. The system allows users to view available shows, book tickets, and view their booking history. Administrators can manage shows and view all bookings via an Admin Panel.

Features
User Features:
User Authentication:

Register a new user account.

Login and logout functionality.

Ticket Booking:

View a list of available shows.

Book tickets for selected shows (choose the number of seats).

View the booking history of past reservations.

Admin Features:
Show Management:

Admin can add, edit, or delete shows.

Admin can view all the bookings made by users.

Setup and Installation
1. Clone the Repository
First, clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Priyank-Jain-254/Book_Ticket.git
cd Book_Ticket
2. Create a Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment to manage dependencies. Create and activate one as follows:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Install the required dependencies using requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Docker (Optional)
If you want to use Docker for environment setup, you can build and run the Docker containers.

Build Docker Image:
bash
Copy
Edit
docker build -t ticketbooking .
Run Docker Containers:
bash
Copy
Edit
docker-compose up --build
This command will build and run the containers for both the Django app and the PostgreSQL database.

5. Set Up the Database
Run Django's database migrations to set up the required tables:

bash
Copy
Edit
python manage.py migrate
6. Create Superuser for Admin Access
To access the admin panel, you need to create a superuser account:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up the admin username, email, and password.

7. Run the Application
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
This will start the server locally at http://127.0.0.1:8000/.

Access the Admin Panel
Once the server is running, you can access the Admin Panel at:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
Log in using the superuser credentials you created earlier to manage shows and view bookings.

Project Structure
php
Copy
Edit
Book_Ticket/
    ├── app_name/                  # Your Django application(s) folder
    ├── Dockerfile                 # Docker configuration file for the app
    ├── docker-compose.yml         # Docker Compose configuration for the app & database
    ├── Jenkinsfile                # CI/CD pipeline configuration for Jenkins
    ├── requirements.txt           # Python dependencies for the project
    ├── manage.py                 # Django management script
    ├── templates/                 # HTML templates for the application
    ├── static/                    # Static files (CSS, JS, images)
    └── db.sqlite3                # SQLite database (if not using Docker)
Technologies Used
Python 3.11+

Django 4.x+

PostgreSQL (or SQLite during development)

Docker (for containerization)

Jenkins (for CI/CD)

Features Implemented
User Authentication: Custom login and registration without using Django forms.

Ticket Booking: Users can book tickets for available shows.

Session-based Cart: Uses Django sessions to store ticket booking information.

Admin Panel: Admin can add, edit, delete shows and view all user bookings.

Manual HTML Forms: Form handling is done manually (no Django forms).

How to Use
User Flow:
Register: Create an account if you don't have one.

Login: Log into your account to access booking features.

Browse Shows: View the list of available shows.

Book Tickets: Select a show and book tickets.

View Bookings: Check your booking history.

Admin Flow:
Login: Use the superuser account to log into the admin panel.

Manage Shows: Add, edit, or delete shows from the admin interface.

View All Bookings: View all user bookings for events.

Future Improvements
Email Verification: Implement email verification for user registration.

Seat Reservation System: Allow users to select specific seats instead of just the number of seats.

Search Functionality: Add a search feature to filter shows based on date, venue, etc.

Multiple Languages: Add multi-language support for a broader user base.

