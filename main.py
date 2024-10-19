import weather

def display_menu():
    print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print("\t1. Set data filename")
    print("\t2. Add weather data")
    print("\t3. Print daily report")
    print("\t4. Print historical report")
    print("\t9. Exit the program")
    choice = input("\n\tEnter menu choice: ")
    return choice

def main():
    filename = None
    weather_data = []
    historical_data = []

    while True:
        menu_choice = display_menu()
        if menu_choice == '1':
            filename = input("\nEnter data filename: ")
        elif menu_choice == '2':
            date = input("\nEnter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temperature = float(input("Enter temperature: "))
            humidity = float(input("Enter humidity: "))
            rainfall = float(input("Enter rainfall: "))
            add_weather_data(weather_data, date, time, temperature, humidity, rainfall)
        elif menu_choice == '3':
            date = input("\nEnter date (YYYYMMDD): ")
            daily_report_data = [entry for entry in weather_data if entry['date'] == date]
            print_daily_report(date, daily_report_data)
        elif menu_choice == '4':
            print_historical_report(historical_data)
        elif menu_choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
