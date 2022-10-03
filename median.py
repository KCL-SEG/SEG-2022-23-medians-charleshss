"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort() #sorts the input in order to calcualte the median
median = 0.0 #int
#check if the array has an odd numbered amount of values or not and
#calculate the median accordingly
def calcMedian():
    med = 0.0
    #use to calc the two middle numbers
    middle_lower = 0.0
    middle_higher = 0.0
    if len(numbers) % 2 == 0:
        middle_lower = numbers[(len(numbers) // 2) - 1]
        middle_higher = numbers[(len(numbers) // 2)]
        med = (middle_lower + middle_higher) / 2
    else:
        med = numbers[ len(numbers) // 2 ]
    return med

median = calcMedian()
print(median)
