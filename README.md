# PAE Finance Tracker

A personal finance tracker API built with Django REST Framework, designed to help users manage their income, expenses, and accounts — including Ghanaian-specific account types like Mobile Money (MoMo) and Susu.

---

## Features

- **Multi-Account Support** — Track Bank accounts, Mobile Money (MoMo), Susu/Savings Groups, and Physical Cash
- **Income Tracking** — Record income from salary, business, gifts, and more
- **Expense Tracking** — Log expenses by category (Food, Transport, Rent, MoMo Fees, etc.)
- **Automatic Balance Updates** — Account balances update automatically when income or expenses are recorded
- **Financial Reports** — Get a summary of total income, expenses, net savings, and breakdowns by category
- **Budget Management** — Set spending limits per category (daily, weekly, monthly)
- **Savings Goals** — Create and track progress toward savings targets
- **JWT Authentication** — Secure token-based authentication for all endpoints
- **Transaction Requests** — Send and receive money requests between users

---

## Tech Stack

- **Backend:** Python, Django 6.0, Django REST Framework
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Database:** SQLite (development)
- **Language:** Python 3.13

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone [https://github.com/PadmoreAe/PAE_Finance_Tracker.git]
cd PAE_Finance_Tracker

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Get access & refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

### Accounts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/balance/total/` | Get total balance across all accounts |

### Expenses & Income
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/expenses/` | List or create expenses |
| GET/POST | `/api/income/` | List or create income records |

### Reports
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/reports/` | Financial summary report |

### Budgets & Savings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/budgets/` | List or create budgets |
| GET/POST | `/api/savings-goals/` | List or create savings goals |

---

## Authentication

All endpoints require a Bearer token. To authenticate:

```bash
# Get token
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'

# Use token
curl http://127.0.0.1:8000/api/reports/ \
  -H "Authorization: Bearer your_access_token"
```

---

## Example Response

### `GET /api/reports/`
```json
{
  "actual_balance": 9990000.00,
  "total_income_recorded": 0.00,
  "total_expenses_recorded": 10000.00,
  "net_from_transactions": -10000.00,
  "expenses_by_category": [
    { "category": "OTHER", "total": 10000.00 }
  ],
  "income_by_source": []
}
```

---

## Project Structure

```
PAE_Finance_Tracker/
├── accounts/        # Account models (Bank, MoMo, Susu, Cash)
├── expenses/        # Expense & Income models, Reports
├── budgets/         # Budget & Savings Goal models
├── social/          # Transaction requests between users
├── users/           # Custom user model
└── pae_finance/     # Project settings & URLs
```

---

## Author

**Padmore Aduseiening**
Built as part of the ALX Backend Capstone Project — 2026









<!-- # PAE Finance Tracker

PAE Finance Tracker is a robust Backend API. It's built with Django and Django REST Framework. The goal is to help users manage multi-currency expenses, set budgets, and interact with others regarding shared costs.

## Features
- **User Authentication**: Secure JWT-based login and registration.
- **Expense Management**: CRUD (Create, Read, Update, Delete) for tracking expenses.
- **Smart Categorization**: Organize expenses by categories like Family, Transport, and Utilities.
- **Multi-Currency Support**: Integrated with ExchangeRate-API to handle global transactions.
- **Social Interaction**: Peer-to-peer transaction requests and chat notes.

## Tech Stack
- **Framework**: Django 5.x
- **API**: Django REST Framework (DRF)
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Authentication**: SimpleJWT
- **External API**: ExchangeRate-API

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/PadmoreAe/PAE_Finance_Tracker.git]
   cd PAE_Finance_Tracker
2. **Set up a Virtual Environment**
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. **Install Dependencies**
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers requests
   pip install -r requirements.txt
4. **Apply Migrations**
   python manage.py migrate
5. **Run the Server**
   python manage.py runserver -->