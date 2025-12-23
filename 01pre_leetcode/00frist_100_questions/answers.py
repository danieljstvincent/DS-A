#question01

print("hello World")

#question02

def question2(a, b):
    total = a + b
    return total

#question03

def quesiton3(a, b):
    sum_all = a + b
    difference_all = a - b
    product_all = a ** b
    quotient = a % b

    all_totals = [sum_all, difference_all, product_all, quotient]

    return all_totals 

def question4( a)-> bool:
    even = 1 % 2 ==1
    return even



def question5(a, b, c):
    total = [a,b,c]
    return max(total), min(total)



# Question 6
def question6(input_string):
    counts = {'digits': 0,
              'letters': 0,
              'spaces': 0
    }

    for char in input_string:
        if char.isdigit():
            counts['digits'] += 1
        elif char.isalpha():
            counts['letters'] += 1
        elif char.isspace() :
            counts['spaces'] += 1

    return counts


print(question6("I am the real king of the 707"))

#question 7
def question7(input_string):
    return input_string[::-1]

def question8(s):
    lower_case = s.lower()
    upper_case = s.upper()
    title_case = s.title()


    return lower_case, upper_case, title_case

def question9(s):
    pointer = s[::-1]
    for letter in s:
        if letter == pointer:
            letter += 1
            pointer -= 1

        return True
    return False




print(question2(3, 100))
print(quesiton3(100, 100))
print(question4(31))
print(question5(1,2,3,))
print(question6("I am the real king of the 707"))
print(question7("batman"))
print(question8("batman"))
print(question9('racecassr'))