# Number Classification API

A simple RESTful API that classifies a given number based on its mathematical properties and returns an interesting fact about it. Built with **FastAPI** and deployed to a publicly accessible endpoint.

---

## 🚀 Features
- Classifies numbers as **prime**, **perfect**, **armstrong**, **even**, or **odd**
- Calculates the **digit sum** of the number
- Fetches a **fun fact** from [Numbers API](http://numbersapi.com/)
- Handles **CORS** for cross-origin requests
- Returns data in **JSON format**

---

## 📊 API Specification

### ✅ **Endpoint**
```
GET /api/classify-number?number=371
```

### 📥 **Query Parameter**
| Parameter | Type   | Description               | Required |
|-----------|--------|---------------------------|----------|
| `number`  | Integer | The number to classify    | Yes      |

### 📤 **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### ⚠️ **Error Response (400 Bad Request)**
```json
{
    "number": "abc",
    "error": true
}
```

---

## ⚙️ Setup Instructions

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

### 2️⃣ **Create & Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install fastapi uvicorn requests
```

### 4️⃣ **Run the API Locally**
```bash
uvicorn main:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

---

## 🌐 Deployment
- Deploy the API to platforms like **Render**, **Railway**, or **Vercel**.
- Ensure the deployed link is publicly accessible.

### Example Render Deployment:
1. Create a free account on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Set build and run commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`

---

## 📚 References
- [Fun Fact API - Numbers API](http://numbersapi.com/)
- [Parity (Mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Parity_(mathematics))
- [Hire Python Developers - HNG](https://hng.tech/hire/python-developers)

---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a Pull Request.

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 🚀 Author
- **Your Name** - [Crystal Okedi](https://github.com/crystalokd)
- **Email:** crystalokd@gmail.com

