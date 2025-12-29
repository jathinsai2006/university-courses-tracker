🎓 University Courses Tracker Dashboard

A full-stack data-driven dashboard application that tracks university courses and visualizes course credit distribution in real time.
This project demonstrates backend API development, database integration, and interactive analytics dashboards using modern Python frameworks.
📌 Project Overview

The University Courses Tracker is designed to manage academic course data and provide meaningful visual insights through an interactive dashboard.

The system consists of:

A RESTful backend API to perform CRUD operations on course data

A relational database to persist course information

An analytics dashboard that dynamically reflects backend data changes

This project was developed as part of an Advanced Programming and Database Systems / Data Visualization academic requirement.

Architecture Flow:

Dash Dashboard (Frontend)
        ↓ REST API Calls
FastAPI Backend (CRUD APIs)
        ↓ ORM
SQLite Database

🚀 Key Features
🔹 Backend (FastAPI)

RESTful API for managing university courses

CRUD operations (Create, Read, Delete)

SQLAlchemy ORM integration

SQLite database for lightweight persistence

Automatic API documentation using Swagger UI

🔹 Database

Relational schema using SQLAlchemy models

Course attributes:

Course Code

Course Name

Instructor

Credits

🔹 Dashboard (Dash + Plotly)

Live data fetched from FastAPI backend

Interactive bar chart (credits per course)

Pie chart for credit distribution

Editable table for updating instructor names

Filters by instructor and course

Auto-refresh every 5 seconds


project/
│
├── backend/
│   ├── main.py          # FastAPI application
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── seed_data.py     # Sample data insertion
│   └── courses.db       # SQLite database
│
├── dashboard/
│   └── app.py           # Dash analytics dashboard
│
└── README.md


⚙️ Setup Instructions
1️⃣ Install Dependencies
pip install fastapi uvicorn sqlalchemy dash plotly pandas requests

2️⃣ Run Backend API
uvicorn backend.main:app --reload

API runs at: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

3️⃣ (Optional) Seed Sample Data
python backend/seed_data.py

4️⃣ Run Dashboard
python dashboard/app.py
Dashboard runs at: http://127.0.0.1:8050





🎯 Learning Outcomes
Practical understanding of REST APIs

ORM-based database design

Backend–frontend integration

Real-time dashboard development

Data visualization and storytelling

End-to-end full-stack workflow

📌 Future Enhancements

Update & authentication endpoints

JWT-based role management

PostgreSQL integration

Cloud deployment

Advanced analytics (KPIs, trends)

