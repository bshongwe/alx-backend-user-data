# 👤 0x00-personal_data 🔒

### Description
🔐 This project focuses on handling personal data securely in a back-end authentication system. It covers topics such as personally identifiable information (PII), log filtering, password encryption, and database authentication using environment variables.

### Learning Objectives
🧠 Understanding personally identifiable information (PII) and non-PII  
🔍 Implementing a log filter to obfuscate PII fields  
🔒 Encrypting passwords securely using bcrypt  
🔑 Authenticating to a database using environment variables  

### Resources
📚 [What Is PII, non-PII, and Personal Data?](https://www.balbix.com/blog/what-is-pii-non-pii-personal-data/)  
📖 [Logging documentation](https://docs.python.org/3/library/logging.html)  
🔐 [bcrypt package](https://pypi.org/project/bcrypt/)  
📝 [Logging to Files, Setting Levels, and Formatting](https://realpython.com/python-logging/)  

### Requirements
- Operating system: Ubuntu 18.04 LTS  
- Python version: 3.7  
- Code style: PEP 8 (pycodestyle version 2.5)  
- All files should be executable  
- Documentation should be present for modules, classes, and functions  
- Use type annotations for functions  
- Ensure all files end with a newline  

# Tasks
### Task 0. Regex-ing:
   - Script: `filtered_logger.py`
   - Description: Implements a function to obfuscate sensitive data in log messages using regular expressions. 🔒
<br></br>

### Task 1.Log formatter:
   - Script: `filtered_logger.py`
   - Description: Provides a custom log formatter class for redacting sensitive information in log records. 📝
<br></br>

### Task 2. Create logger:
   - Script: `filtered_logger.py`
   - Description: Implements a function to create a logger object with specific configurations for handling personal data securely. 📜
<br></br>

### Task 3. Connect to secure database:
   - Script: `filtered_logger.py`
   - Description: Connects to a secure database to read user data, using environment variables to store database credentials securely. 🛡️
<br></br>

### Task 4. Read and filter data:
   - Script: `filtered_logger.py`
   - Description: Reads user data from a database and logs it after filtering sensitive information. 🕵️‍♂️
<br></br>

### Task 5. Encrypting passwords:
   - Script: `encrypt_password.py`
   - Description: Provides functions to hash passwords securely using bcrypt. 🔐
<br></br>

### Task 6. Check valid password:
   - Script: `encrypt_password.py`
   - Description: Implements a function to validate passwords against their hashed versions securely using bcrypt. ✅
<br></br>

# Edge Test Files:
Edge test files for edge cases and additional scenarios for each task:
### Task 0:
-	**file:** `/task-0/main.py`
-	**test:** `./main.py`
<br></br>

### Task 1:
-	**file:** `/task-1/main.py`
-       **test:** `./main.py`
<br></br>

### Task 2:
-	**file:** `/task-2/main.py`
-       **test:** `./main.py`
<br></br>

### Task 3:
-	**files:** `/task-3/main.sql`, `task-3/main.py`
-       **tests:** `cat main.sql | mysql -uroot -p`, `echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db`, `./main.py`
<br></br>

### Task 4:
-	**file:** `/task4/main.sql`
-	**tests:** `cat main.sql | mysql -uroot -p`, `echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db`, `PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py`
<br></br>

### Task 5:
-	**file:** `main.py`
-	**test:** `./main.py`
<br></br>

### Task 6:
-	**file:** `/task-6/main.py`
-	**test:** `./main.py`
<br></br>

### Files
- **filtered_logger.py:** Contains functions for logging and filtering sensitive information.  
- **encrypt_password.py:** Contains functions for hashing and validating passwords.

