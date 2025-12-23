from backend.database import SessionLocal, engine
from backend.models import Base, Course
import random

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Course).delete()
db.commit()

# Insert 25 courses with RANDOM credits
for i in range(1, 26):
    course = Course(
        course_code=f"CS{i:03}",
        course_name=f"Course {i}",
        instructor=f"Dr Instructor {i % 5 + 1}",
        credits=random.randint(1, 5)   # 🔥 random credits
    )
    db.add(course)

db.commit()
db.close()

print("25 COURSES INSERTED WITH RANDOM CREDITS")