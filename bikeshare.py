"""
This is my Udacity project based on Python and its Pandas package.
With this code, you can view bikeshare data for US cities by month and day of week.
"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city == 'chicago':
            print('Thank you for choosing Chicago!\n')
        elif city == 'new york city':
            print('Thank you for choosing New York City!\n')
        elif city == 'washington':
            print('Thank you for choosing Washington!\n')
        else:
            print("I do not understand this choice. Please try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ''
    while month not in month_list:
        month = input('Which month? January, February, March, April, May, or June? Or how about all?\n').lower()
        if month == 'january':
            print('Thank you for choosing January!\n')
        elif month == 'february':
            print('Thank you for choosing February!\n')
        elif month == 'march':
            print('Thank you for choosing March!\n')
        elif month == 'april':
            print('Thank you for choosing April!\n')
        elif month == 'may':
            print('Thank you for choosing May!\n')
        elif month == 'june':
            print('Thank you for choosing June!\n')
        elif month == 'all':
            print('Thanks! I will show you the data for all the months we have (January to June). Coming right up!\n')
        else:
            print("I do not understand this choice. Please try again.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    while day not in day_list:
        day = input('Would you like to see data for a specific day of the week? Type the name of the day (e. g. "Monday") or just answer "all".\n').lower()
        if day == 'monday':
            print('Thank you for choosing Monday!\n')
        elif day == 'tuesday':
            print('Thank you for choosing Tuesday!\n')
        elif day == 'wednesday':
            print('Thank you for choosing Wednesday!\n')
        elif day == 'thursday':
            print('Thank you for choosing Thursday!\n')
        elif day == 'friday':
            print('Thank you for choosing Friday!\n')
        elif day == 'saturday':
            print('Thank you for choosing Saturday!\n')
        elif day == 'sunday':
            print('Thank you for choosing Sunday!\n')
        elif day == 'all':
            print('Thanks! I will show you the data for all the days of the week. Here you go!\n')
        else:
            print("I do not understand this choice. Please try again.\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month for Travel:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day of Week for Travel:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent Start Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most Frequent Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Breakdown of user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Breakdown of user gender:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].mean()
        recent_yob = df['Birth Year'].mean()
        common_yob = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', earliest_yob)
        print('Most recent year of birth:', recent_yob)
        print('Most common year of birth:', common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
