def Find_Mean(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    average = total / len(numbers)
    return average


def Find_Median(numbers):
    numbers.sort()
    return numbers[int(len(numbers) / 2)]


def Find_Mode(numbers):
    most_frequent = numbers.count(numbers[0])
    for number in numbers:
        if numbers.count(number) > int(most_frequent):
            most_frequent = number
    return most_frequent


while True:
    text = input("Enter a list of numbers seperated by commas (Q to quit)\n").lower()

    if text == "q":
        break

    text = text.strip()
    list_of_numbers = text.split(",")

    print("Mean: {}".format(Find_Mean(list_of_numbers)))
    print("Median: {}".format(Find_Median(list_of_numbers)))
    print("Mode: {}".format(Find_Mode(list_of_numbers)))
