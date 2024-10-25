# Django Authentication API Documentation

## Introduction
This project provides a set of APIs for user authentication and authorization. It includes features for registering new users, logging in using username or email, logging out, password reset requests, and password reset confirmation.

### Key Features:
- User Registration with first name, last name, username, email, and password (with password confirmation).
- Login via username or email.
- Logout functionality that invalidates the token.
- Password reset via email.

---

## Installation

### 1. **Clone the repository**
```bash
https://github.com/A7med7777/marketGo.git
cd your-repo
```

### 2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set up `.env` file**
Create a `.env` file in the root directory and include your environment variables for sensitive information like the database, secret key, and SMTP settings.

Example `.env`:
```
SECRET_KEY=your_secret_key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True
```

### 5. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Run the development server**
```bash
python manage.py runserver
```

---

## API Endpoints

### 1. **User Registration**
Registers a new user with their details.

- **URL:** `/api/register/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "password123",
    "confirm_password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "user": {
      "first_name": "John",
      "last_name": "Doe",
      "username": "johndoe",
      "email": "johndoe@example.com"
    },
    "token": "abc123xyz"
  }
  ```
- **Validation:**
  - Password and confirm password must match.
  - Email must be unique.

### 2. **User Login**
Logs in a user with either their username or email and password.

- **URL:** `/api/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username_or_email": "johndoe",
    "password": "password123"
  }
  ```
  Or with email:
  ```json
  {
    "username_or_email": "johndoe@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "user": "johndoe",
    "token": "abc123xyz"
  }
  ```

### 3. **User Logout**
Logs out the currently authenticated user by deleting their token.

- **URL:** `/api/logout/`
- **Method:** `POST`
- **Headers:** 
  - `Authorization: Token your_token_here`
- **Response:**
  ```json
  {
    "message": "Successfully logged out."
  }
  ```

### 4. **Password Reset Request**
Sends a password reset email to the user.

- **URL:** `/api/password-reset/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "johndoe@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Password reset link has been sent to your email."
  }
  ```

### 5. **Password Reset Confirmation**
Resets the user's password using the token sent via email.

- **URL:** `/reset-password/<uidb64>/<token>/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "new_password": "newpassword123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Password has been reset successfully."
  }
  ```

---

## How to Test

### 1. **Using `curl`**
Test the API endpoints by using `curl` commands. For example:

- **Register:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/register/ \
       -H 'Content-Type: application/json' \
       -d '{
             "first_name": "John",
             "last_name": "Doe",
             "username": "johndoe",
             "email": "johndoe@example.com",
             "password": "password123",
             "confirm_password": "password123"
           }'
  ```

- **Login:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/login/ \
       -H 'Content-Type: application/json' \
       -d '{
             "username_or_email": "johndoe",
             "password": "password123"
           }'
  ```

- **Logout:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/logout/ \
       -H "Authorization: Token your_token_here"
  ```

### 2. **Using Postman**
You can also test the APIs using Postman:
1. Create new requests in Postman for each endpoint.
2. Set the method (`POST`), URL, headers, and body (JSON) as needed.

---

## SMTP Configuration for Production

Make sure to set up the following environment variables in your `.env` file for email functionality in production:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
```

This will enable the password reset functionality to work correctly by sending reset links to the user's email.

---

## License
This project is licensed under the MIT License.

---
