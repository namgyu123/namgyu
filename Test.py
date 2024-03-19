sample = [1, 11, 22, -20, 55, -33, 0, -5, 12, 35, 19, -9, -1, -100, 90]

numbers = [num for num in sample if num > 10 and num < 50]
print("10보다 크고 50보다 작은 값", numbers)