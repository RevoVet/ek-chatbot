from fastapi import FastAPI
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.responses import JSONResponse


from ek_chatbot.chat_engine import generate_response


app = FastAPI()


def get_db_connection():
    conn = psycopg2.connect(host='localhost', dbname='sales_db', user='sd', password='pilsener')
    return conn


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/products", response_class=JSONResponse)
def read_products():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products


@app.post("/chat")
async def chat(user_input: str):
    response = await generate_response(user_input)
    return {"response": response}


# for local development, need to adjust for python
# const db = new Pool({
# user: '', // your PostgreSQL username, e.g., 'postgres'
# host: 'localhost',
# database: 'legaldb',
# password: '', // leave empty if no password is set
# port: 5432, // default PostgreSQL port
# });
