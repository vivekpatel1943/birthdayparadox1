import datetime
import random

def generate_days(num_of_birthdays):
    # group_size = int(input("How many days should i generate: "))

    start_date = datetime.date(2023, 1, 1) 
    end_date = datetime.date(2023, 12, 31)

    delta = datetime.timedelta(days=1)

    days_in_2023 = []

    while start_date <= end_date:
        # to generate all the days of the year
        formatted_day = start_date.strftime('%b %d')
        days_in_2023.append(formatted_day)
        start_date+=delta
    # return days_in_2023

    # to generate required number of days of the year in a random fashion
    birthdays = [random.choice(days_in_2023) for i in range(num_of_birthdays)]
    return birthdays

# print (generate_days(group_size))

# now we we will be using for loops to see which day has been repeated more than once.
group_size = int(input("How many birthdays should i generate: "))
def matching_birthdays():
    
    birthdays = generate_days(group_size)
    print(birthdays)
    for day in birthdays:
        if birthdays.count(day) >= 2:
            return True
                
# result = matching_birthdays()
# print(f"In this simulation multiple people have their birthday on {result}.")

    

# now we can find that on which day multiple people have their birthdays.
# now i need to make a program to run this simulation multiple times.
# to do that i think i need to run the matching_birthdays() function again and again.

number_of_simulations = int(input("How many simulations should i run? "))

def simulations_100k():
    count = 0

    
   
    for i in range(number_of_simulations):
        result = matching_birthdays()
        if result == True:
            count+=1
        elif number_of_simulations == 1000:
            print("1000")
        elif number_of_simulations == 10000:
            print("10,000")
        elif number_of_simulations == 50000:
            print("50,000")
    print(count)



    print(f"so the chance of two people having the same birthdays in a group of {group_size} people is {(count/number_of_simulations)*100}percent.")

simulations_100k()


