import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    if city.lower() not in ['chicago', 'new york city', 'washington']:
        city = 'invalid city name'

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month_number = []
    for i in range(1,13):
        month_number.append(i)
    month_dict = {name: value for name, value in zip(month_name_list, month_number)}
    
    if month == 'all':
        month = month_number
    else:
        if type(month) == list:
            month = [month_dict[m.lower()] for m in month]
        else:
            month = month_dict[month.lower()]
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dow_name_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    dow_number = []
    for i in range(0,7):
        dow_number.append(i)
    dow_dict = {name: value for name, value in zip(dow_name_list, dow_number)}
    
    if day == 'all':
        day = [i for i in range(0,7)]
    else:
        if type(day) == list:
            day = [dow_dict[m.lower()] for m in day]
        else:
            day = dow_dict[day.lower()]
        
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
    
    if city == 'invalid city name':
        return 'please check city name and retry'
    else:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Start_Month'] = df['Start Time'].dt.month
        df['Start_Day'] = df['Start Time'].dt.dayofweek
        df['Start_Hour'] = df['Start Time'].dt.hour
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['End_Month'] = df['End Time'].dt.month
        df['End_Day'] = df['End Time'].dt.dayofweek
        df['End_Hour'] = df['End Time'].dt.hour
        df = df.query(f'Start_Month == {month}').query(f'Start_Day == {day}')

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    mcm = df['Start_Month'].mode().values[0]
    print(f'The most common month is {mcm}')

    # TO DO: display the most common day of week

    dow_name_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    dow_number = [i for i in range(0,7)]
    dow_dict2 = {name: value for name, value in zip(dow_number, dow_name_list)}
    
    mcd = dow_dict2[df['Start_Day'].mode().values[0]]
    print(f'The most common day of week is {mcd}')
    
    # TO DO: display the most common start hour

    mch = df['Start_Hour'].mode().values[0]
    print(f'The most common hour is {mch}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcss = df['Start Station'].mode().values[0]
    print(f'The most common start station is {mcss}')

    # TO DO: display most commonly used end station
    mces = df['End Station'].mode().values[0]
    print(f'The most common end station is {mces}')

    # TO DO: display most frequent combination of start station and end station trip
    start_end = "from " + df['Start Station'] + " to " + df['End Station']
    mcsec = start_end.mode().values[0]
    print(f'frequent combination of start station and end station trip is {mcsec}')    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    ttt = df['Trip Duration'].sum()
    print(f'Total travel time is {ttt}')

    # TO DO: display mean travel time

    mtt = df['Trip Duration'].mean()
    print(f'Mean travel time is {mtt}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:')
    print(df['User Type'].value_counts())
    print('')
    
    # TO DO: Display counts of gender
    print('Counts of gender types:')
    print(df['Gender'].value_counts())
    print('')

    # TO DO: Display earliest, most recent, and most common year of birth
    print(f'The earliest birth year: {int(df["Birth Year"].min())}')
    print(f'The most recent birth year: {int(df["Birth Year"].max())}')
    print(f'The most common birth year: {df["Birth Year"].mode().values[0].astype(int)}')
    print('')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# In[37]:


def main():
    while True:
        raw_city = input('\nPlease enter the name of city(e.g., chicago, new york city, washington) that you want to analyze.\n')
        raw_month = input('\nPlease enter a name of a month(e.g., january) that you want to analyze. Please type "all" if you want to include all days of week.\n')
        raw_day = input('\nPlease enter a day of week name(e.g., monday) that you want to analyze. Please type all if you want to include all days of week.\n')                 
        city, month, day = get_filters(raw_city, raw_month, raw_day)
        if city == 'invalid city name':
            raw_city = input('\nPlease enter valid city name.\n')
            city, month, day = get_filters(raw_city, raw_month, raw_day)
            
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print('User stats for Washington is not available')
        
        # Printing 5 rows in the raw data upon user's request
        display_raw = input('\nWould you like to see 5 rows of raw trip data? Enter yes or no.\n')

        if display_raw.lower() == 'yes':
            start_row_index = 0
            end_row_index = 5
            while end_row_index <= len(df):
                print(df.iloc[start_row_index:end_row_index,:])
                continue_input = input("\nDo you wish to see next 5 rows? Enter yes or no.\n")
                if continue_input.lower() != 'yes':
                    break
                else:
                    start_row_index += 5
                    end_row_index += 5
                    print(df.iloc[start_row_index:end_row_index,:])
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()