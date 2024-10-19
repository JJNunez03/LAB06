import json
import os
import calendar

def read_data(filename: str) -> dict:
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data: dict, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(data: dict, date: str) -> int:
    max_temp = None
    for key, readings in data.items():
        if key.startswith(date):
            if max_temp is None or readings['t'] > max_temp:
                max_temp = readings['t']
    return max_temp if max_temp is not None else float('-inf')

def min_temperature(data: dict, date: str) -> int:
    min_temp = None
    for key, readings in data.items():
        if key.startswith(date):
            if min_temp is None or readings['t'] < min_temp:
                min_temp = readings['t']
    return min_temp if min_temp is not None else float('inf')

def max_humidity(data: dict, date: str) -> int:
    max_hum = None
    for key, readings in data.items():
        if key.startswith(date):
            if max_hum is None or readings['h'] > max_hum:
                max_hum = readings['h']
    return max_hum if max_hum is not None else float('-inf')

def min_humidity(data: dict, date: str) -> int:
    min_hum = None
    for key, readings in data.items():
        if key.startswith(date):
            if min_hum is None or readings['h'] < min_hum:
                min_hum = readings['h']
    return min_hum if min_hum is not None else float('inf')

def tot_rain(data: dict, date: str) -> float:
    total_rain = 0.0
    for key, readings in data.items():
        if key.startswith(date):
            total_rain += readings['r']
    return total_rain

def report_daily(data: dict, date: str) -> str:
    report_lines = [
        "========================= DAILY REPORT ========================",
        "Date                      Time  Temperature  Humidity  Rainfall",
        "====================  ========  ===========  ========  ======== "
    ]
    
    for key, readings in data.items():
        if key.startswith(date):
            formatted_date = f"{calendar.month_name[int(key[4:6])]} {int(key[6:8])}, {key[0:4]}"
            time = key[8:14]
            temp = readings['t']
            hum = readings['h']
            rain = readings['r']
            report_lines.append(f"{formatted_date:<20} {time:<8} {temp:<12} {hum:<8} {rain:<8.2f}")
    
    return "\n".join(report_lines)

def report_historical(data: dict) -> str:
    report_lines = [
        "============================== HISTORICAL REPORT ===========================",
        "              Minimum      Maximum   Minumum   Maximum     Total",
        "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall",
        "====================  ===========  ===========  ========  ========  ======== "
    ]
    
    dates = set(key[:8] for key in data.keys())
    for date in sorted(dates):
        min_temp = min_temperature(data, date)
        max_temp = max_temperature(data, date)
        min_hum = min_humidity(data, date)
        max_hum = max_humidity(data, date)
        total_rain = tot_rain(data, date)

        formatted_date = f"{calendar.month_name[int(date[4:6])]} {int(date[6:8])}, {date[:4]}"
        report_lines.append(f"{formatted_date:<20} {min_temp:<12} {max_temp:<12} {min_hum:<8} {max_hum:<8} {total_rain:<8.2f}")

    return "\n".join(report_lines)

def add_weather_data(data, date, time, temperature, humidity, rainfall):
    data.append({
        'date': date,
        'time': time,
        'temperature': temperature,
        'humidity': humidity,
        'rainfall': rainfall
    })

def print_daily_report(date, weather_data):
    print("========================= DAILY REPORT ========================")
    print(f"{'Date':<25}{'Time':<10}{'Temperature':<12}{'Humidity':<10}{'Rainfall':<10}")
    print("="*65)
    for entry in weather_data:
        print(f"{entry['date']:<25}{entry['time']:<10}{entry['temperature']:<12}{entry['humidity']:<10}{entry['rainfall']:<10.2f}")

def print_historical_report(historical_data):
    print("============================== HISTORICAL REPORT ===========================")
    print(f"{'Date':<22}{'Minimum':<12}{'Maximum':<12}{'Minumum':<12}{'Maximum':<12}{'Total':<10}")
    print("="*70)
    for entry in historical_data:
        print(f"{entry['date']:<22}{entry['min_temp']:<12}{entry['max_temp']:<12}{entry['min_humidity']:<12}{entry['max_humidity']:<12}{entry['total_rainfall']:<10.2f}")

