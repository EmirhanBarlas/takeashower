import datetime

def save_shower_log(days):
    with open('shower_log.txt', 'a') as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d')}: {days} days\n")

def calculate_percentage_difference():
    with open('shower_log.txt', 'r') as file:
        lines = file.readlines()
        total_days = sum(int(line.split(':')[1].strip().split()[0]) for line in lines)
        average_days = total_days / len(lines)
        target_days = 3
        percentage_difference = ((average_days - target_days) / target_days) * 100
        return percentage_difference

def main():
    days = int(input("Enter the number of days you took a shower: "))
    save_shower_log(days)
    if days % 3 == 0:
        print("You have reached the target number of days!")
    percentage_difference = calculate_percentage_difference()
    print(f"The percentage difference between the average shower days and the target is: {percentage_difference}%")

if __name__ == "__main__":
    main()
