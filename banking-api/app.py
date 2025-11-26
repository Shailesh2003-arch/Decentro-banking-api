from flask import Flask
from routes.users import user_routes
from routes.accounts import account_routes
from routes.transactions import transaction_routes

app = Flask("Decentro");


app.register_blueprint(user_routes)
app.register_blueprint(account_routes)
app.register_blueprint(transaction_routes)


if __name__ == "__main__":
    app.run(debug=True)