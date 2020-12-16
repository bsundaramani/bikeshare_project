import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Test1 for git project

def get_raw(df):
    # Ask user if they want to see first 5 lines in the raw dat
    raw = input('Do you want to see first 5 lines of raw data? Enter yes or no: ')
    line = 5
    if raw == 'yes':
        print(df.head(line))

        while True:
            question = input('Do you want to see more lines? Enter yes or no: ')
            line = line + 5
            if question == 'yes':
                print(df.iloc[[line, line+1, line+2, line+3, line+4]])
            else:
                break
    else:
        print('OK, no raw data needs to be displayed')



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter city: ')
    while True:
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print('Error')
            break
        else:
            city = city.lower()
            break

    # get user input for month (all, january, february, ... , june)
    month = input('Please enter month: ')
    while True:
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('error')
            break
        else:
            month = month.lower()
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter day of week: ')
    while True:
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('error')
            break
        else:
            day = day.lower()
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # Change name of month to month number (for example, january is 1)
        month = months.index(month) + 1
        # Filter column 'month' to match the month number from above line
        df = df[df['month'] == month]


    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # Change name of day to day number (for example, friday is 5)
        day = days.index(day) + 1
        # Filter column 'day_of_week' to match the day number from above line
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    pop_month = df['month'].mode()[0]
    print('most common month: ', pop_month)

    # display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print('most common day of week is: ', pop_day)

    # display the most common start hour
    pop_hr = df['hour'].mode()[0]
    print('most common start hour is: ', pop_hr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used end stations is: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used start station is: ', end_station)

    # display most frequent combination of start station and end station trip
    combine_station = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip \n: ', combine_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = sum(df['Trip Duration'])
    print('Total duration is: ', total_duration)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_type = df['User Type']
        user_count = user_type.value_counts()
        print('Counts of user types \n', user_count)
    except:
        print('\nNo User Type information')

    # Display counts of gender
    try:
        gender = df['Gender']
        gender_count = gender.value_counts()
        print('\nCounts of gender \n', gender_count)
    except:
        print('\nNo gender information')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', int(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', int(most_recent_year))

        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', int(most_common_year))
    except:
        print('\nNo Birth Year information')

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
        get_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
