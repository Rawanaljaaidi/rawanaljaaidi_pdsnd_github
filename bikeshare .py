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
    while True:
       city= input('please enter name of city:  ').lower()
       if city not in CITY_DATA.keys():
          print("please choose only one of the three city {chicago,new york city, washington}")
          continue
       else:
          break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input("please enter a month or choose all: ").lower()
        if month not in ["january","february", "march", "april", "may", "june", "all"]:
           print("please choose all or the correct month fron january to june")
           continue
        else:
            break
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("please enter a day or choose all:  ").lower()
        if day not in ["sunday", "monday", "tuesday", "wednesday", "thuraday", "friday", "saturday","all"]:
           print("please choose all or the correct day name")
           continue
        else:
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != "all":
        months = ["january","february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != "all":
     df = df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    hour = pd.to_datetime(df['Start Time']).dt.hour
    common_month = df['month'].mode()[0]
    print(f"the most common month is {common_month}")

    # TO DO: display the most common day of week
    print(f"the most common day of week is {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    print(f"the most common start hour is {hour.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start = df['Start Station'].mode()[0]
    print(f"most commonly start station is {commonly_start}")

    # TO DO: display most commonly used end station
    commonly_end = df['End Station'].mode()[0]
    print(f"most commonly end station is {commonly_end}")

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + "to" + df['End Station']
    print(f"most frequent combination of start and end station trip is {df['comb'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"total travel time is {df['Trip Duration'].sum()} seconds")

    # TO DO: display mean travel time
    print(f"mean travel time is {df['Trip Duration'].mean()} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    Start_time = time.time()

    # TO DO: Display counts of user types
    print(f"the counts of user types {df['User Type'].value_counts()}")

    # TO DO: Display counts of gender
    if 'Gender' in df and 'Birth Year' in df:
         print(f"the counts of gender user types {df['Gender'].value_counts()}")


    # TO DO: Display earliest, most recent, and most common year of birth
    
    print(f"the earlist year of birth is {df['Birth Year'].min()}")
    print(f"the most recent year of birth is {df['Birth Year'].max()}")
    print(f"the most common year of birth is {df['Birth Year'].mode()[0]}")
    
    print("\nThis took %s seconds." % (time.time() - Start_time))
    print('-'*40)

def display_raw(df):
   view_data = input['\nWould you like to view 5 rows of indivdual trip data? Enter yes or no\n']
   start_loc = 0
   view_display = False
   if view_data == "yes":
       view_display = True
    
       while(view_display):
         print(df.iloc[start_loc:start_loc+5])
         start_loc += 5
         view_display = input("Do you wish to continue?: ").lower()
         if view_data == "yes":
           view_display = True
         else:
            view_display = False                     
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
