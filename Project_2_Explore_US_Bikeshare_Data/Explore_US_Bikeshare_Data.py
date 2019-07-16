import sys
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
    print("你好, 让我们探索美国共享单车数据吧!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_number = { 1: 'chicago', 2: 'new york city', 3: 'washington'}
            city_choose = int(input("""Which city do you want to analyze? Input:1 or 2 or 3.
(1 is Chicago, 2 is New York city, 3 is Washington)
你想分析哪个城市的数据? 输入:1 或者 2 或者 3. 
(1为芝加哥, 2为纽约, 3为华盛顿)\n> """))
            city = city_number[city_choose]
            print("The city you choose to view is {}!".format(city.lower()))
            print("您选择查看的城市是 {}!\n".format(city.lower()))
            break
        except ValueError:
            print("Oops!  That was wrong city name.  Try again\n注意! 你输入了错误的城市名。 请再试一次!")
        except KeyError:
            print("Oops!  That was wrong city.  Try again\n注意! 你输入了错误的城市。 请再试一次!")
        except:
            print("Unexpected error (未知错误):", sys.exc_info()[0])
            raise

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_number = { 0: 'all',
                      1: 'january',
                      2: 'february',
                      3: 'march',
                      4: 'april',
                      5: 'may',
                      6: 'june'}
            month_choose = int(input("""Which month do you want to analyze? Input range:0 ~ 6
(0 is all, 1 is january, 2 is february, 3 is march, 4 is april, 5 is may, 6 is june)
你想分析几月的数据？输入范围: 0 至 6. 
(0为全部, 1为一月, 2为二月, 3为三月, 4为四月, 5为五月, 6为六月)\n> """))
            month = month_number[month_choose]
            print("The month you choose to view is {}!".format(month.lower()))
            print("您选择查看的月份是 {}!\n".format(month.lower()))
            break
        except ValueError:
            print("Oops!  That was wrong month.  Try again\n注意! 你输入了错误的月份。 请再试一次!")
        except KeyError:
            print("Oops!  That was wrong month.  Try again\n注意! 你输入了错误的月份。 请再试一次!")
        except:
            print("Unexpected error (未知错误):", sys.exc_info()[0])
            raise

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_number = { 0: 'all',
                           1: 'monday',
                           2: 'tuesday',
                           3: 'wednesday',
                           4: 'thursday',
                           5: 'friday',
                           6: 'saturday',
                           7: 'sunday'}
            day_choose = int(input("""Which day do you want to analyze? Input range:0 ~ 7
(0 is all, 1 to 7 is Monday to Sunday)
你想分析星期几的数据？输入范围: 0 至 7. 
(0为全部, 1至7为周一至周日)\n> """))
            day = day_number[day_choose]
            print("The day you choose to view is {}!".format(day.lower()))
            print("您选择查看的星期是 {}!\n".format(day.lower()))
            break
        except ValueError:
            print("Oops!  That was wrong day.  Try again\n注意! 你输入了错误的星期。 请再试一次!")
        except KeyError:
            print("Oops!  That was wrong day.  Try again\n注意! 你输入了错误的星期。 请再试一次!")
        except:
            print("Unexpected error (未知错误):", sys.exc_info()[0])
            raise

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

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
    popular_month = df['month'].mode()
    print("The month in which users travel most often is {}.".format(popular_month[0]))
    print("用户最常出行的月份是: {} 月份。\n".format(popular_month[0]))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()
    print("The day in which users travel most often is {}.".format(popular_day_of_week[0]))
    print("用户一周最常出行的一天: {}\n".format(popular_day_of_week[0]))

    # TO DO: display the most common start hour
    df['hour'] = [i.hour for i in df['Start Time']]
    popular_hour = df['hour'].mode()
    print("The hour in which users travel most often is {}.".format(popular_hour[0]))
    print("用户最常出行的时间: {} 点钟。".format(popular_hour[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print("The Most Popular Start station: {}.".format(popular_start_station[0]))
    print("用户最常出发的站点是: ", popular_start_station[0])

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print("\nThe Most Popular End station: {}.".format(popular_end_station[0]))
    print("用户最常去的终点站是: ", popular_end_station[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['separator'] = ' ---> '
    df['popular_trip_temp'] = np.add(df['Start Station'], df['separator'])
    df['popular_trip'] = np.add(df['popular_trip_temp'], df['End Station'])
    popular_trip = df['popular_trip'].mode()
    print("\nThe Most Popular Trip: ", popular_trip[0])
    print("用户最常选择的行程是: ", popular_trip[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total Trip Duration: {}s.".format(total_travel_time))
    print("骑行总时长: {}秒 。\n".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean Trip Duration: {}s.".format(mean_travel_time))
    print("平均骑行时长: {}秒。".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types:\n用户类型与数量如下:\n{}\n\n".format(user_types))

    # TO DO: Display counts of gender
    if {'Gender'}.issubset(df.columns):
        gender = df['Gender'].value_counts()
        print("The counts of gender:\n用户性别与数量如下:\n{}\n\n".format(gender))
    else:
        print("Sorry, \'Gender\' column not exist.\n抱歉, \'Gender\' 列不存在。\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if {'Birth Year'}.issubset(df.columns):
        df['birth_year'] = df['Birth Year']
        earliest_birth_year = df['birth_year'].min()
        recent_birth_year = df['birth_year'].max()
        most_common_birth_year = df['birth_year'].mode()

        print('The earliest birth year: {}'.format(int(earliest_birth_year)))
        print('最早的出生年份: {}年'.format(int(earliest_birth_year)))
        print('The recent birth year: {}'.format(int(recent_birth_year)))
        print('最近的出生年份: {}年'.format(int(recent_birth_year)))
        print('The most common birth year: {}'.format(int(most_common_birth_year[0])))
        print('最多的出生年份: {}年'.format(int(most_common_birth_year[0])))
    else:
        print("Sorry, \'Birth Year\' column not exist.\n抱歉, \'Birth Year\'列不存在。")


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

