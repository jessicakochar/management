import datetime


class ReservationLogger:

    def __init__(self, name=None, phone=None, mail=None, address=None, date_from=None, date_to=None, room_num=None,
                room_type=None,meals=None, comments=None):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address
        self.date_from = date_from
        self.date_to = date_to
        self.room_num = room_num
        self.room_type = room_type
        self.meals = meals
        self.comments = comments

        dt = str(datetime.datetime.today())
        idx = dt.rindex(".")
        self.log_time_stamp = dt[0: idx]

    def insert_sql_command(self):
        sql = "insert into ReservationLogger values(null, '{name}',{phone},'{mail}', {date_from},{date_to}, " \
              "{room_num},'{room_type}','{meals}','{comments}','{log_time_stamp}')".format_map(vars(self))
        return sql

    def fetch_sql_command(self):
        return "select * from ReservationLogger"
