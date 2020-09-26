from flask import Blueprint, Flask, render_template
from repositories import user_repository
from controllers.transactions_controller import transactions_blueprint
from controllers.users_controller import users_blueprint
from controllers.merchants_controller import merchants_blueprint

app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(merchants_blueprint)

@app.route("/")
def main():
    all_users = user_repository.select_all()
    return render_template('index.html', all_users = all_users)

if __name__ == '__main__':
    app.run()