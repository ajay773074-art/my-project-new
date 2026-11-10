import requests

def get_weather(city_name, api_key):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            
            print(f"\n--- Weather in {city}, {country} ---")
            print(f"Temperature : {temp}°C (Feels like: {feels_like}°C)")
            print(f"Condition   : {description.capitalize()}")
            print(f"Humidity    : {humidity}%")
            print("-----------------------------------")
        else:
            print(f"\nError: City '{city_name}' not found or invalid API key.")
            
    except requests.exceptions.RequestException as e:
        print(f"\nConnection Error: {e}")

if __name__ == "__main__":
    print("=== Python Weather App ===")
    city = input("Enter city name: ").strip()
    
    # Aap yahan apni free API key daal sakte hain (openweathermap.org se milti hai)
    # Ya user se input le sakte hain
    api_key = input("Enter your OpenWeatherMap API Key (or press Enter to use default): ").strip()
    
    if not api_key:
        # Demo purpose ke liye placeholder (Real use ke liye apni key banani hogi)
        api_key = "your_api_key_here"
        
    get_weather(city, api_key)