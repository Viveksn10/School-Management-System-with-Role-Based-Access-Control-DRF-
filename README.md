# School Management System with Role-Based Access Control

## Description

This project is a **School Management System** built with Django Rest Framework (DRF). It provides role-based access control for managing student details, library history, and fees history. Different user roles such as Admin, Office Staff, and Librarian have distinct permissions and access to the system's features.

### Key Features

#### Role-Based Access Control (RBAC)
- **Admin**
  - Full system access.
  - Manage Office Staff and Librarian accounts.
  - Perform CRUD operations on students, library history, and fees history.
- **Office Staff**
  - Access to all student details.
  - Manage fees history.
  - View library records.
- **Librarian**
  - View-only access to library and student details.

#### CRUD Operations
- **Student Management**: Create, update, view, and delete student records.
- **Library History**: Manage borrowing records.
- **Fees History**: Manage fee records.

#### Authentication and Authorization
- User authentication with Django's default token-based authentication.
- Permissions are enforced using DRF's permissions and custom middleware.

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL or SQLite (default)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Viveksn10/School-Management-DRF-.git
   cd School-Management-DRF
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - Create a `.env` file in the root directory with the following variables:
     ```env
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3  # Change to your PostgreSQL URL if needed
     ```
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

### API Endpoints

The system is designed with RESTful principles. Below are some key endpoints:

#### Authentication
- `POST /login/`: Login and obtain an auth token.
- `POST /register/`: Register a new user (Admin, Office Staff, or Librarian).

#### Admin Endpoints
- `GET, POST, PUT, DELETE /users/`: Manage all users (Admin, Office Staff, Librarian).

#### Office Staff Endpoints
- `GET, POST, PUT, DELETE /students/`: Manage student records.
- `GET, POST, PUT, DELETE /fees-history/`: Manage fees history.

#### Librarian Endpoints
- `GET /library-history/`: View library borrowing records.

Refer to the API documentation for detailed specifications (provided by DRF's browsable API).

## Libraries Used

- **Backend**
  - Django Rest Framework
  - djangorestframework-tokenauth (Token-based Authentication)
  - psycopg2-binary (PostgreSQL support)

- **Utilities**
  - Python-dotenv (Environment variable management)
  - drf-yasg (API documentation)

## Contribution

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License.

### MIT License

```
MIT License

Copyright (c) 2024 VIVEK S NAIR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
