# university-courses-tracker
FastAPI + SQLAlchemy + Dash project
# University Courses Tracker 📚

## 📌 Project Description
The **University Courses Tracker** is a full-stack, data-driven dashboard application.
It demonstrates **RESTful API development**, **database integration**, and **real-time analytics visualization**.

The backend is developed using **FastAPI** and **SQLAlchemy**, while the analytics dashboard
is built using **Plotly and Dash**. Any CRUD operation performed through the API is
immediately reflected in the dashboard.

This project was developed as part of the subject  
**Advanced Programming and Database Systems**.

---

## 🛠 Technology Stack

### Backend
- FastAPI
- SQLAlchemy (ORM)
- SQLite (Database)

### Frontend / Dashboard
- Plotly
- Dash

### Tools & Utilities
- Swagger UI (API documentation & testing)
- GitHub (Version control)

---


pip install fastapi uvicorn sqlalchemy pydantic dash plotly
2️⃣ Install Required Packages
pip install fastapi uvicorn sqlalchemy pydantic dash plotly

3️⃣ Seed the Database (Optional)
python seed_data.py

4️⃣ Run Backend Server
uvicorn main:app --reload


Backend will run at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

5️⃣ Run Dashboard
python dashboard.py


Dashboard will run at:
http://127.0.0.1:8050

🔗 API Documentation (Swagger)

FastAPI automatically generates interactive API documentation using Swagger UI.

Available Endpoints
🔹 GET /courses

Fetch all course records from the database.

🔹 POST /courses

Add a new course.

Request Body Example

{
  "course_code": "CS101",
  "course_name": "Data Structures",
  "instructor": "Dr Smith",
  "credits": 4
}

🔹 GET /courses/{id}

Fetch a course by its ID.

Returns 404 Not Found if the course does not exist.

🔹 DELETE /courses/{id}

Delete a course by its ID.
