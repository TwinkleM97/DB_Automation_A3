# PROG8850 – Assignment 3: Web App + Selenium Automation

**Student**: Twinkle Mishra  
**Course**: PROG8850 – Database Automation and Scripting  
**Assignment**: Assignment 3 – Automating Login UI and Testing with Selenium  
**Date**: July 06, 2025

---

## Objective

To build a simple web application with:
- A login & registration form
- MySQL backend for storing users
- UI validation and welcome screen
- Automated Selenium test to validate the workflow

---
## Important Note

Passwords are stored in plaintext only to meet assignment requirements (for easy DB visibility). This is insecure in real-world applications and secured hashed using scrypt should be used, which is a secure practice for real applications but is not required for this assignment

---

## Project Structure

```
PROG8850-Assignment3/
├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── welcome.html
├── tests/
│   └── test_login.py
├── .env
├── requirements.txt
├── docker-compose.yml
├── init.sql
├── run_xvfb.sh
└── README.md
```

---

## Prerequisites

Install the following dependencies **inside your Codespace or local system**:

### Python Dependencies - This is required for all app.py related dependency modules.

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
flask
mysql-connector-python
python-dotenv
selenium
webdriver-manager
```

## 🛠️ Environment Setup

Create the `.env` file in the root directory by running the following command:

```bash
echo -e "DB_HOST=127.0.0.1\nDB_PORT=3306\nDB_USER=student\nDB_PASS=studentpass\nDB_NAME=prog8850_db" > .env
```

### System Dependencies for Selenium (Ubuntu/Debian)

These are required for headless browser automation.

```bash
sudo apt update && sudo apt install -y   wget curl gnupg unzip xvfb libxi6 libgconf-2-4 libnss3 libxss1 libappindicator1 libindicator7   fonts-liberation libatk-bridge2.0-0 libgtk-3-0

# Download Chrome manually (not committed due to GitHub limits)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install Chrome
sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt -f install -y
```

---

## MySQL Setup

```bash
docker-compose up -d
```

- DB Name: `prog8850_db`
- User: `devuser`
- Pass: `devpass`

To manually inspect the DB:

```bash
docker exec -it mysql-a3 mysql -u root -prootpass -D prog8850_db
SELECT * FROM users;
```

---

## Flask Web App

```bash
python app/app.py
```

- Registration: `http://localhost:5000/register`
- Login: `http://localhost:5000/login`

---

## Selenium Test

To run the automated test (make sure Flask app and DB are running):

```bash
# Optional (if using Codespaces)
./run_xvfb.sh

# OR directly
python tests/test_login.py
```

It will:
1. Register a new user
2. Log in as that user
3. Check welcome screen
4. Verify user in MySQL

---

## Required Screenshots (for report)

1. `docker ps` showing DB running
2. Flask app running (terminal)
3. Login/register form in browser
4. DB check (`SELECT * FROM users`)
5. Selenium test output (passed)
6. GitHub repo push

---

## Notes

- Make sure `.env` contains DB credentials:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=prog8850_db
DB_USER=devuser
DB_PASS=devpass
```

- `.deb` Chrome file was excluded from GitHub due to >100MB. Download it manually as shown.

---


