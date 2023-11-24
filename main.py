from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import psycopg2

app = FastAPI()

def db_config(host, database, user, password):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn

@app.post("/submit-student")
async def submit_form(
    id: int = Form(...),
    name: str = Form(...),
    standard: int = Form(...),
    gender: str = Form(...),
    mobile: int = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    try:
  
        conn = db_config(host='localhost', database='shahed', user='shahed', password='shahed')
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO user_data (id, name, standard, gender, mobile, email, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(insert_query, (id, name, standard, gender, mobile, email, password))
        conn.commit()

        return {
        "ID": id,
        "Name": name,
        "Standard": standard,
        "Gender": gender,
        "Mobile": mobile,
        "Email": email,
        "Password": password,
    }
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    finally:
        if conn:
            cursor.close()
            conn.close()

