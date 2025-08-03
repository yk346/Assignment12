DockerHub repository:
https://hub.docker.com/repository/docker/yk346/601_module12/general

FastAPI Calculator - Integration Testing & Manual API Guide
📋 Prerequisites
Ensure you have the following installed:

Python 3.12+

PostgreSQL running and database created (fastapi_db)

Redis running (for token blacklisting)

Node.js (optional, for Playwright browsers installation)

📦 Python Environment Setup
bash
Copy
Edit
# Clone repository and navigate into it
git clone <your-repo-url>
cd module12_is601

# Setup Python Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install Dependencies
pip install -r requirements.txt

# Install Playwright Browsers (if not already)
playwright install
🧪 Running Integration Tests (E2E)
The integration tests will:

Spin up a FastAPI test server

Initialize a test PostgreSQL database

Mock or use Redis for JWT blacklisting

Perform HTTP requests to endpoints /auth/register, /auth/login, /calculator/* etc.

Run Tests:
bash
Copy
Edit
pytest -s tests/e2e/
Optional Pytest Flags:
--preserve-db: Prevent test database cleanup after tests.

--run-slow: Run tests marked as "slow" (UI automation, etc.)

Example:

bash
Copy
Edit
pytest -s tests/e2e/ --preserve-db --run-slow
🐞 Debugging Test Failures (Common)
Problem	Solution
HTTP 500 on /auth/register	Ensure Redis is running (docker run -p 6379:6379 redis)
PostgreSQL Connection Error	Ensure PostgreSQL is running and DATABASE_URL is correct in .env
Playwright Errors	Run playwright install to ensure browsers are installed

🌐 Manual API Testing via OpenAPI (Swagger UI)
You can manually test the API through the Swagger UI provided by FastAPI.

Steps:
Run FastAPI Server Locally

bash
Copy
Edit
uvicorn app.main:app --reload
By default, it will be available at: http://127.0.0.1:8000

Access Swagger UI
Open in browser: http://127.0.0.1:8000/docs

Manual API Flow to Test:

POST /auth/register: Register a new user.

POST /auth/login: Get Access & Refresh Tokens.

Authorize: Click "Authorize" button in Swagger UI and input:

php-template
Copy
Edit
Bearer <access_token>
Perform Calculator Operations:

POST /calculator/ to create a calculation.

GET /calculator/ to list all calculations.

PUT /calculator/{id} to update a calculation.

DELETE /calculator/{id} to delete.

Token Blacklisting (Optional)

POST /auth/logout to blacklist a token.

After logout, the access token should be invalid for protected routes.

📝 .env Example Configuration
env
Copy
Edit
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
REDIS_URL=redis://localhost:6379/0
JWT_SECRET_KEY=your-super-secret-key
JWT_REFRESH_SECRET_KEY=your-refresh-secret-key
🚀 Useful Commands
Command	Description
uvicorn app.main:app --reload	Run FastAPI server locally
pytest -s tests/e2e/	Run integration tests
docker run -p 6379:6379 redis	Run Redis locally via Docker
playwright install	Install Playwright browsers

✅ Manual Test Scenarios (Checklist)
 User Registration (/auth/register)

 User Login (/auth/login)

 Token-protected access to /calculator/

 Token invalidation on /auth/logout

 CRUD operations on Calculator via /calculator/

 Redis blacklisting functionality (if active)

 

# 📦 Project Setup

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
