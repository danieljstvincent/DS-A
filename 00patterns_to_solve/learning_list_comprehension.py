squares = [x**2 for x in range(10)]
print(squares)

celsius = [0, 10,20, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit)

evens = [num for num in range(20) if num % 2 == 0]
print(evens)