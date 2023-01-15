from flask import *

from customerdb import Customer
from customersql import DataBaseHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()


@app.route("/")
def index():
    # return "Welcome to CMS App"
    return render_template("index.html")


@app.route("/add")
def add():
    # return "Welcome to CMS App"
    return render_template("add_customer.html")


@app.route("/view")
def view():
    logger_object = Customer()
    sql = logger_object.select_sql()

    rows = db_helper.read(sql)

    return render_template("view_customer.html", result=rows)


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remark=request.form["remark"])
    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)
    return cref.name+" Inserted Successfully..."


def main():
    app.run()


if __name__ == "__main__":
    main()