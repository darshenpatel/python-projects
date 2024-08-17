from weatherAPI import get_weather, get_weather_details, Weather


def main():
    city: str = input('Enter a city: ')

    # Get the current weather details
    current_weather: dict = get_weather(city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)

    # Get the current days
    date_format: str = '%m/%d/%y'
    days: list[str] = sorted(({f'{date.date:{date_format}}' for date in weather_details}))
    print(days)

    for day in days:
        print('-----')
        print(day)

        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{date_format}}' == day]
        for weather in grouped:
            print(weather)


if __name__ == '__main__':
    main()
