from flask import *

from Reservation_Logger import Reservation_Logger
from ReservationLogger import ReservationLogger

web_app = Flask("Hotel Management")
r_log = Reservation_Logger()


@web_app.route("/home_page")
def home():
    return render_template("home.html")


@web_app.route("/add")
def add_reservation_log():
    return render_template("add_reservation_log.html")


@web_app.route("/cancel")
def delete_reservation_log():
    return render_template("delete_reservation_log.html")


@web_app.route("/employee")
def employee_login():
    return render_template("employee_login.html")


@web_app.route("/about")
def about():
    return render_template("about.html")


@web_app.route("/logs")
def view_logs():
    reservation_obj = ReservationLogger()
    sql = reservation_obj.fetch_sql_command()
    rows = r_log.read(sql)
    return render_template("view_logs.html", result=rows)


@web_app.route("/save", methods=["POST"])
def save_data():
    print("Save Reservation Logs Executed...")

    reservation_data_object = ReservationLogger(name=request.form['name'],
                                                phone=int(request.form['phone']),
                                                mail=request.form['mail'],
                                                address=request.form['address'],
                                                date_from=request.form['Reservation From'],
                                                date_to=request.form['Reservation To'],
                                                room_num=int(request.form['Number of Rooms']),
                                                room_type=request.form['Type of Room'],
                                                meals=request.form['Meals'],
                                                comments=request.form['Comments'],)

    print(reservation_data_object)
    sql = reservation_data_object.insert_sql_command()
    print("SQL IS:", sql)
    r_log.write(sql)

    return "Reservation is done :) \n Enjoy your stay!!!"


def main():
    web_app.run()


if __name__ == '__main__':
    main()
