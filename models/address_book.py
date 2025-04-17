from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.records.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)

                delta_days = (next_birthday - today).days
                if 0 <= delta_days <= 7:
                    if next_birthday.weekday() in [5, 6]:  # Weekend
                        next_birthday += timedelta(days=(7 - next_birthday.weekday()))
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": next_birthday.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays
