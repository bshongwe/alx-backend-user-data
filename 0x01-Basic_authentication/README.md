# 🚀🔑0x01. Basic authentication 🛡️🔐
Simple HTTP API for playing with `User` model.
<br></br>

## Files
### `models/`
- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model
<br></br>
### `api/v1`
- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints
<br></br>

## Setup

```
$ pip3 install -r requirements.txt
```
<br></br>

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
<br></br>

## Routes
- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Background Context 📚
In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API.

> **Note:** In the industry, you should not implement your own Basic authentication system. Instead, use a module or framework that provides it for you (e.g., Flask-HTTPAuth in Python-Flask). Here, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Resources 📖

Read or watch:
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)
<br></br>

## Learning Objectives 🎯
By the end of this project, you should be able to explain to anyone, without the help of Google:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header
<br></br>

## Requirements ✅
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method.
<br></br>

## Project Outline 📝

| Task # | Task Name                            | Description                                                                                                                                                                                                                                                                          |
|--------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Simple-basic-API                     | Download and start the project from `archive.zip`. Setup and start the server. <br> **Usage:** `curl "http://0.0.0.0:5000/api/v1/status" -vvv`                                                                                                                                        |
| 1      | Error handler: Unauthorized          | Add a new error handler for 401 status code in `api/v1/app.py`. <br> Add a new endpoint in `api/v1/views/index.py` to test the 401 error.                                                                                                                                             |
| 2      | Error handler: Forbidden             | Add a new error handler for 403 status code in `api/v1/app.py`. <br> Add a new endpoint in `api/v1/views/index.py` to test the 403 error.                                                                                                                                            |
| 3      | Auth class                           | Create a folder `api/v1/auth`. <br> Create a class `Auth` in `api/v1/auth/auth.py`.                                                                                                                                                                                                  |
| 4      | Define which routes don't need auth  | Update `require_auth` method in `Auth` to handle paths that don't require authentication.                                                                                                                                                                                            |
| 5      | Request validation                   | Update `authorization_header` method in `Auth` to return the value of the `Authorization` header. <br> Update `api/v1/app.py` to filter requests using `before_request`.                                                                                                              |
| 6      | Basic auth                           | Create a class `BasicAuth` that inherits from `Auth`. <br> Update `api/v1/app.py` to use `BasicAuth` based on environment variable `AUTH_TYPE`.                                                                                                                                       |
| 7      | Basic - Base64 part                  | Add `extract_base64_authorization_header` method in `BasicAuth`.                                                                                                                                                                                                                      |
| 8      | Basic - Base64 decode                | Add `decode_base64_authorization_header` method in `BasicAuth`.                                                                                                                                                                                                                       |
| 9      | Basic - User credentials             | Add `extract_user_credentials` method in `BasicAuth`.                                                                                                                                                                                                                                 |
| 10     | Basic - User object                  | Add `user_object_from_credentials` method in `BasicAuth`.                                                                                                                                                                                                                             |
| 11     | Basic - Overload current_user        | Overload `current_user` method in `BasicAuth` to retrieve the `User` instance for a request.                                                                                                                                                                                          |
| 12     | Basic - Allow password with ":"      | Improve the method `extract_user_credentials` in `BasicAuth` to allow passwords containing `:`.                                                                                                                                                                                       |
| 13     | Require auth with stars              | Improve `require_auth` method in `Auth` by allowing `*` at the end of excluded paths. <br> **Example for `excluded_paths = ["/api/v1/stat*"]`:** <br> `/api/v1/users` will return `True`, <br> `/api/v1/status` will return `False`, <br> `/api/v1/stats` will return `False`.          |
<br></br>

## Setup & Usage <i>(revised)</i> ⚙️

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bshongwe/alx-backend-user-data.git
   ```

2. **Navigate to project directory:**
   ```sh
   cd 0x01-Basic_authentication
   ```

3. **Install dependencies:**
   ```sh
   pip3 install -r requirements.txt
   ```

4. **Run the application:**
   ```sh
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

5. **Test the endpoints:**
   ```sh
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

## Author 👨‍💻
```
- **Ernest B. Shongwe**
```
