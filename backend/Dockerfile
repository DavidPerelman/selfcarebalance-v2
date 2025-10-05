FROM python:3.11-slim

# תיקיית עבודה
WORKDIR /app

# העתקת קבצי requirements והתקנת תלויות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד האפליקציה
COPY ./app ./app
COPY ./tests ./tests

# הפעלת השרת
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
