import sqlite3

class CarDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                make TEXT,
                model TEXT,
                year INTEGER,
                color TEXT
            )
        ''')
        self.conn.commit()

    def add_car(self, make, model, year, color):
        self.cursor.execute('INSERT INTO cars (make, model, year, color) VALUES (?, ?, ?, ?)', (make, model, year, color))
        self.conn.commit()

    def get_cars(self):
        self.cursor.execute('SELECT * FROM cars')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

def main():
    db_name = "car_database.db"
    car_db = CarDatabase(db_name)

    while True:
        print("\n1. Add Car")
        print("2. View Cars")
        print("3. Exit")
        choice = input("\nSelect an option (1/2/3): ")

        if choice == "1":
            make = input("Enter the car's make: ")
            model = input("Enter the car's model: ")
            year = input("Enter the car's year: ")
            color = input("Enter the car's color: ")
            car_db.add_car(make, model, year, color)
            print("\nCar added successfully.")
        elif choice == "2":
            cars = car_db.get_cars()
            if cars:
                print("\nList of Cars:")
                for car in cars:
                    print(f"ID: {car[0]}, Make: {car[1]}, Model: {car[2]}, Year: {car[3]}, Color: {car[4]}")
            else:
                print("\nNo cars in the database.")
        elif choice == "3":
            car_db.close()
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
