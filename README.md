# DJANGO_CRM

DJANGO_CRM is a basic Customer Relationship Management (CRM) web application built with Django that i built while learning django.

## Features

- User Authentication: Secure user registration and login,logout functionality using Django's built-in authentication system.
- Customer Management: create,read, update, and delete customer information/records, including contact details,address,etc.
- Superuser Access: Certain features like adding, updating and deleting a user detail are restricted to superusers (administrators) for added security and control.
- Normal user: They can only view user details

## Installation

To get the project up and running, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/abhishekghimire40/Django_CRM.git
```

2. Navigate to the project directory:

```bash
cd DJANGO_CRM
```

3. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use "venv\Scripts\activate"
```

4. Install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

5. Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser account (if needed):

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Contributing

Contributions are welcome! If you find a bug or have an enhancement idea, please open an issue or submit a pull request. You can also add functionality, make project your own and add it to your github.