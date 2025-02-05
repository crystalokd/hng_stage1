from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import requests
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    num = abs(n)
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

# Check if a number is perfect
def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Calculate the digit sum
def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

# Fetch fun fact from Numbers API
def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
        else:
            return "No fun fact available."
    except:
        return "No fun fact available."

# Main API endpoint
@app.get("/api/classify-number")
def classify_number(number: Union[int, str], response: Response):
    try:
        number = int(number)
    except ValueError:
        response.status_code = 400
        return {"number": number, "error": True}

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    response.status_code = 200
    return result
    
@app.get("/api/classify-number", response_model=dict)
def bad_request_handler(number: str):
    if not number.isdigit():
        return {"number": number, "error": True}
