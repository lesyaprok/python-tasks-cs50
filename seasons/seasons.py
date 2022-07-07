from datetime import date, timedelta
import inflect
import sys

def main():
    date_of_birth = input("Date of Birth: ")
    seasons = Seasons(date_of_birth)
    print(seasons.number_to_words())

class Seasons:
    def __init__(self, date_of_birth):
        try:
            self.date_of_birth = date.fromisoformat(date_of_birth)
        except ValueError:
            sys.exit("Invalid date")
    def get_date(self):
        return date.today()
    def get_delta(self):
        return self.get_date() - self.date_of_birth
    def get_minutes(self):
        return int((timedelta(days = self.get_delta().days).total_seconds()) / 60)
    def number_to_words(self):
        p = inflect.engine()
        minutes = self.get_minutes()
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()
