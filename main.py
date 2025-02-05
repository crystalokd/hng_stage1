from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum([d ** len(digits) for d in digits]) == n

def get_fun_fact(n: int) -> str:
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    if response.status_code == 200:
        return response.json().get("text", "No fun fact found.")
    return "No fun fact available."

@app.get("/api/classify-number", response_model=NumberResponse)
def classify_number(number: int = Query(..., description="The number to classify")):
    try:
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(map(int, str(abs(number)))),
            "fun_fact": get_fun_fact(number)
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer.")

@app.get("/api/classify-number", response_model=dict)
def bad_request_handler(number: str):
    if not number.isdigit():
        return {"number": number, "error": True}
