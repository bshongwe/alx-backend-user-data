# 🔒🧑 0x02. Session authentication 🛡️💻
`Back-end` `Authentification`
<br></br>

## Background Context 📚
In this project, we will implement Session Authentication. Although in real-world applications, it is advised to use existing modules or frameworks for session authentication (e.g., Flask-HTTPAuth in Python-Flask), this project aims to understand the mechanism by implementing it step-by-step.
<br></br>
## Resources 📖
Read or watch:
- REST API Authentication Mechanisms - Only the session auth part
- HTTP Cookie
- Flask
- Flask Cookie

## Learning Objectives 🎯
By the end of this project, you should be able to explain the following concepts without using Google:
- What authentication means 🔐
- What session authentication means 📂
- What cookies are 🍪
- How to send cookies 📤
- How to parse cookies 📥
<br></br>

## Requirements ✅
### Python Scripts 🐍
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (using `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have documentation (using `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions (inside and outside a class) should have documentation (using `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
<br></br>

## Tasks 📋
### Task 0. Et moi et moi et moi! 👥
- Copy all your work from the 0x06. Basic authentication project into this new folder.
- Add a new endpoint: `GET /users/me` to retrieve the authenticated User object.
  - Update `@app.before_request` in `api/v1/app.py` to assign the result of `auth.current_user(request)` to `request.current_user`.
  - Update the method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
    - If `<user_id>` is equal to `me` and `request.current_user` is `None`, abort with a 404 error.
    - If `<user_id>` is equal to `me` and `request.current_user` is not `None`, return the authenticated User in a JSON response.
<br></br>
### Task 1. Empty Session ➖
- Create a class `SessionAuth` that inherits from `Auth`.
- Update `api/v1/app.py` to use a `SessionAuth` instance for the variable `auth` depending on the value of the environment variable `AUTH_TYPE`.
<br></br>
### Task 2. Create a Session 🆕
- Update `SessionAuth` class:
  - Create a class attribute `user_id_by_session_id` initialized by an empty dictionary.
  - Create an instance method `create_session(self, user_id: str = None) -> str` that creates a Session ID for a user_id.
<br></br>
### Task 3. User ID for Session ID 🔑
- Update `SessionAuth` class:
  - Create an instance method `user_id_for_session_id(self, session_id: str = None) -> str` that returns a User ID based on a Session ID.
<br></br>
### Task 4. Session Cookie 🍪
- Update `api/v1/auth/auth.py` by adding the method `session_cookie(self, request=None)` that returns a cookie value from a request.
<br></br>
### Task 5. Before Request 🚧
- Update the `@app.before_request` method in `api/v1/app.py`:
  - Add the URL path `/api/v1/auth_session/login/` to the list of excluded paths.
  - If `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`, abort with a 401 error.
<br></br>
### Task 6. Use Session ID for Identifying a User 🆔
- Update `SessionAuth` class:
  - Create an instance method `current_user(self, request=None)` that returns a User instance based on a cookie value.
<br></br>
### Task 7. New View for Session Authentication 🌐
- Create a new Flask view in `api/v1/views/session_auth.py` that handles all routes for the Session authentication.
- Add a route `POST /auth_session/login` for logging in a user.
<br></br>
### Task 8. Logout 🚪
- Update the `SessionAuth` class by adding a new method `destroy_session(self, request=None)` that deletes the user session / logout.
- Add a new route `DELETE /api/v1/auth_session/logout` in `api/v1/views/session_auth.py`.
<br></br>
### Task9. Expiration ⏳
- Create a class `SessionExpAuth` that inherits from `SessionAuth` in `api/v1/auth/session_exp_auth.py`.
- Add session expiration functionality to `SessionExpAuth`.
<br></br>
### Task 10. Sessions in Database 💾
- Create a new model `UserSession` in `models/user_session.py` that inherits from `Base`.
- Create a new authentication class `SessionDBAuth` in `api/v1/auth/session_db_auth.py` that inherits from `SessionExpAuth`.
- Update `api/v1/app.py` to instantiate `auth` with `SessionDBAuth` if the environment variable `AUTH_TYPE` is equal to `session_db_auth`.
<br></br>
## Repository 🗂️
- GitHub repository: `alx-backend-user-data`
- Directory: `0x02-Session_authentication`

### Files 📂
- `api/v1/app.py`
- `api/v1/views/users.py`
- `api/v1/auth/session_auth.py`
- `api/v1/auth/auth.py`
- `api/v1/views/session_auth.py`
- `api/v1/views/__init__.py`
- `api/v1/auth/session_exp_auth.py`
- `api/v1/auth/session_db_auth.py`
- `models/user_session.py`


