**🌱 Mini Banking API**

_A tiny but powerful banking backend built using Flask + MongoDB, created to practice:_

- REST API design
- MongoDB operations
- Clean backend structure
- Account management logic
- Transaction handling

This project helps you understand real-world backend fundamentals in the simplest way.

🚀 Features

- 👤 Create User
- 🏦 Create Bank Account
- 💰 Deposit Money
- 💸 Withdraw Money
- 📊 Check Balance
- 📜 Transaction History
- 🗄 MongoDB Integration (PyMongo)
- 🧪 Fully testable with Postman

🧩 Tech Stack

- Python 3.10+
- Flask
- PyMongo
- MongoDB (Local or Cloud)
- Postman for API testing

⚙️ Installation & Setup

1️⃣ Clone the repository

```
git clone https://github.com/Shailesh2003-arch/Decentro-banking-api.git

```

2️⃣ Install dependencies

```
pip install -r requirements.txt
```

3️⃣ Start MongoDB locally

4️⃣ Run the server

```
cd banking-api
flask run --debug
```

Server starts at:
http://127.0.0.1:5000

📌 API Documentation
_Below is the complete API reference for testing your routes._

👤 1. Create User

**POST /users**

_Request Body (json)_

```
{
  "name": "Shaill",
  "email": "shaill@example.com"
}

```

_Response_

```
{
    "_id": "69268..............",
    "email": "shaill@example.com",
    "name": "Shaill"
}
```

🏦 2. Create Account

**POST /accounts**

_Request Body (json)_

```
{
  "userId": "67a12bd..."
}
```

_Response_

```
{
    "_id": "6926...................",
    "balance": 0,
    "userId": "6926................."
}
```

💰 3. Deposit Money

**POST /transactions/deposit**

_Request Body(json)_

```
{
    "accountId":"6926..........",
    "amount":500
}
```

_Response_

```
{
    "newBalance": 500
}

```

💸 4. Withdraw Money

**POST /transactions/withdrawl**

_Request Body(json)_

```
{
"accountId":"69267c4931fca9561c47e93a",
"amount":300
}
```

_Response_

```
{
    "newBalance": 200
}
```

🧮 5. Check Balance

**GET /accounts/<accountId>/balance**

**Example:**

```
/accounts/673fd.../balance
```

🧮 6. Transfer funds from account to another

**POST /transactions/transfer**

_Request Body(json)_

```
{
    "from":"6926..................",
    "to":"6926..................",
    "amount":100
}

```

_Response_

```
{
    "message": "Transfer successful"
}
```

📜 7. Transaction History

**GET /transactions/<accountId>**

🧪 Testing with Postman

- Open Postman
- Create a new Collection named Banking API
- Add each endpoint

Start with:
Create User → copy userId (\_id)
Create Account → paste userId (\_id)
Deposit → Withdraw → Check Balance → Transfer funds → Transaction-history

🧑‍💻 Contributing

Feel free to fork the repo, create a feature branch, and submit a pull request.

⭐ Like the project?

Give it a star on GitHub - your support means a lot ✨
