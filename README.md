# PAE Finance Tracker

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
   python manage.py runserver
