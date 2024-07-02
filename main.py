import random


def bubble(numbers):
    n = len(numbers)
    # Loop through the list from the first element to the second to last element
    for i in range(n-1):
        # Compare current element with the next element
        if numbers[i] > numbers[i+1]:
            # Swap if current element is greater than the next element
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


def main():
    numbers = [2, 3, 0, 5, 4]
    print(numbers)
    bubble(numbers)
    print(numbers)    # must be [2, 0, 3, 4, 5]

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    bubble(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
