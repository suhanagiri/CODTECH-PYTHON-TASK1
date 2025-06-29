import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key from OpenWeatherMap
API_KEY = 'your_api_key_here'
CITY = 'Delhi'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def parse_weather_data(data):
    forecast_list = data['list']
    df = pd.DataFrame([{
        'datetime': item['dt_txt'],
        'temperature': item['main']['temp'],
        'humidity': item['main']['humidity']
    } for item in forecast_list])
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def visualize_weather(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='datetime', y='temperature', data=df, marker='o', label='Temperature (°C)')
    sns.lineplot(x='datetime', y='humidity', data=df, marker='s', label='Humidity (%)')
    plt.title(f'5-Day Weather Forecast for {CITY}')
    plt.xlabel('Date & Time')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sample_output.png")
    plt.show()

def main():
    data = fetch_weather_data()
    if data:
        df = parse_weather_data(data)
        visualize_weather(df)

if __name__ == "__main__":
    main()
