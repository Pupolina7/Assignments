# Python labs
import contextlib
import io
import math
import time
from random import random

from numpy import int64

import newLibrary

# Lab 08.06.23(2)
print()


# Task 1
def apply_operation(operations):
    results = []
    for i, operation in enumerate(operations):
        func = operation['func']
        args = operation.get('args', ())
        kwargs = operation.get('kwargs', {})
        result = func(*args, **kwargs)
        results.append(result)
    return results


def add(a, b):
    return a + b


def square(a):
    return a ** 2


operations = [
    {'func': add, 'args': (1, 2)},
    {'func': square, 'args': (3,)}
]


# print(apply_operation(operations))


# Task 2
def composed(*func):
    result = []

    def reverse(a):
        for i in reversed(func):
            result.append(i(a))
        return result

    return reverse


def add(a):
    return a + a


def square(a):
    return a ** 2


composed_function = composed(add, square)


# print(composed_function(9))


# Task 3
def function(func, n):
    def inner(*args, **kwargs):
        for i in range(n):
            func(*args, **kwargs)

    return inner


def inno(s):
    print(s)


rep = function(inno, 8)
# rep("Happy birthday inno")

# Lab 14.06.23(3)
# Task 1
list_of_strings = ["dnjvn", "jsdbdv", "nvjdb", "nvidnvqid", "dnjvn", "nvidnvqid", "nvidnvqid"]
answer = {}
for x in list_of_strings:
    if x in answer.keys():
        answer[x] = answer.get(x) + 1
    else:
        answer.update({x: 1})
# print(answer)
# print(type(list(answer.items())[0]))
sorted_answer = dict(sorted(answer.items(), key=lambda a: a[1], reverse=True))
# print(sorted_answer)

# Task 2
input = [1, 4, 8, 13, 890, 376]
newList = filter(lambda x: x % 2 == 0, input)
lst = [x ** 2 for x in input if x % 2 == 0]
answer = list(map(lambda a: a ** 2, newList))
# print(answer)
sum_squares = lambda lst: sum(lst)


# print(sum_squares(answer))

# Task 3
def functionTime(*fib):
    def wrapper(*fib):
        start = time.time()
        fibonacci(*fib)
        end = time.time()
        return end - start

    return wrapper(*fib)


# @decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Lab 20.06.23(5)
# Task 1
class MultipleChoiceQuestion:
    def __int__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(i + 1, ') ', choice)

    def check_answer(self, answer):
        return answer == self.answer


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, choices, answer):
        multipleChoiceQuestion = MultipleChoiceQuestion(question, choices, answer)
        self.questions.append(multipleChoiceQuestion)

    def take_quiz(self):
        self.num_correct = 0
        student_answers = []
        for question in self.questions:
            question.display_question()
            user_answer = input("Your answer: ")
            student_answers.append(user_answer)
            if question.check_answer(user_answer):
                self.num_correct += 1
        return student_answers

    def grade_quiz(self):
        print("Your garde is: ", self.num_correct / len(self.questions) * 100)


quiz = Quiz()


# quiz.add_question("")


# Task 2
def add_prefix(prefix):
    print(prefix)

    def decorator(cls):
        class DecoratedClass:
            def __init__(self, *args, **kwargs):
                self.instance = cls(*args, **kwargs)

        for name, value in vars(cls).items():
            if callable(value):
                setattr(DecoratedClass, f"{prefix}{name}", value)

        return DecoratedClass

    return decorator


# @add_prefix("pre_")
class A:
    def hello(self):
        print("Hello, world!")

    def greet(self, name):
        print(f"Hello, ", name, "!")


# obj = A()
# obj.pre_hello()


# Lab 22.06.23(6)
# Task 1
class ValidateInputs:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        if not all(isinstance(arg, int) and arg > 0 for arg in args):
            raise ValueError("All arguments must be positive integers")
        return self.func(*args)


@ValidateInputs
def divide_numbers(a, b):
    return a / b


# try:
#     print(divide_numbers(3, 8))
#     print(divide_numbers(389, 8))
#     print(divide_numbers(3.9, 8))
# except ValueError as ve:
#     print(ve)


# Task 2
def prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def prime_generator():
    a = 2
    while True:
        if prime(a):
            yield a
        a += 1


primeGenerator = prime_generator()


# for _ in range(12):
#     print(primeGenerator.__next__())


# Task 3
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h / 2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


shapes = [Rectangle(5, 4), Rectangle(8, 5), Circle(3), Triangle(2, 9)]


# for shape in shapes:
#     print("Area: ", shape.area())


# Task 4
class A:
    def hi(self):
        print("Hi i am A")


class B(A):
    def hi(self):
        print("Hi i am B")

    def by(self):
        print("by i am B")


class C(A):
    def hi(self):
        print("Hi i am C")

    def by(self):
        print("by i am C")


class D(B, C):
    def hi(self):
        print("hi i am D")


cls = D()

# cls.hi()
# cls.by()

# Lab 27.06.23(7)
# Task 1
# class PythonNotebook:
#     def __init__(self):
#         self._cells = []
#
#     def add_cell(self, code):
#         cell = Cell(code)
#         self._cells.append(cell)
#
#     def execute_cell(self, index):
#         if 0 <= index < len(self._cells):
#             cell = self._cells[index]
#             cell.execute()
#         else:
#             print("Invalid index!")
#
#     def show_output(self, index):
#         if 0 <= index < len(self._cells):
#             cell = self._cells[index]
#             if cell.output:
#                 for output in cell.output:
#                     print(output)
#             else:
#                 print("no output")
#

# class Cell:
#     def __init__(self, code):
#         self._code = code
#         self.output = []
#
#     def execute(self):
#         with contextlib.redirect_stdout(io.StringIO()) as output:
#             try:
#                 exec(self._code, globals())
#             except Exception as e:
#                 self.output.append(str(e))
#             else:
#                 self.output.append(output.getValue())
#
#     def clear_output(self):
#         self.output = []


# notebook = PythonNotebook()
# notebook.add_cell('a=4+3')
# notebook.add_cell('print(a)')
# notebook.execute_cell(0)
# notebook.execute_cell(1)

# Task 2
a = newLibrary.algorithm(1, 4, 7)
# print(a)
b = newLibrary.summ(3, 9)
# print(b)

# Lab 29.06.23(8)
# Local scope
var1 = 123


def test1():
    var2 = 333
    var1 = var2
    # print(var1)


test1()
# print(var1)

# Lab 04.07.23(9)
# Task 1
import numpy as np

arr = np.random.randint(1, 100, size=(5, 5))
# arr = np.reshape(rd, (5, 5))
# print(arr)
# print()
sortedArr = np.sort(arr, axis=0)
# print(sortedArr)
meanVal = np.mean(arr)
# print("\n", meanVal)
meanArr = np.where(sortedArr > meanVal, 0, sortedArr)
# print("\n", meanArr)
ans = np.dot(meanArr, meanVal.T)
# print("\n", ans)

# Task 2
import pandas as pd

# print("\n Task 2", "\n")
pan = pd.read_csv('data.csv')
# print(pan, "\n")
groupedData = pan.groupby('Category').agg({"Revenue": "sum", "Quantity": "sum"})
# print(groupedData, "\n")
groupedData["avgPrice"] = groupedData["Revenue"] / groupedData["Quantity"]
# print(groupedData["avgPrice"], "\n")
# print(groupedData["avgPrice"].idxmax())

# Task 3
print()
arr = np.random.randn((1000))
meanArr = np.mean(arr)
stdArr = np.std(arr)
count = np.sum(arr > (meanArr + stdArr))
# print(count)
normArr = (arr - meanArr) / stdArr
# print(normArr)

# Lab 06.07.23(10)
# Task 1
import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://reverehealth.com/live-better/do-your-makeup-habits-harm-your-skin/"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product listings
product_listings = soup.find_all('div', class_='product-listing')

# Iterate over the product listings and extract relevant information
for listing in product_listings:
    # Extract the product name
    product_name = listing.find('h2', class_='product-name').text.strip()

    # Extract the product price
    product_price = listing.find('span', class_='product-price').text.strip()

    # Extract the product description
    product_description = listing.find('p', class_='product-description').text.strip()

    # Print the extracted information
    # print("Product Name:", product_name)
    # print("Price:", product_price)
    # print("Description:", product_description)
    # print("----------")


# Task 2
def extract_links(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags and extract the href attribute
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return links


# Input the URL of the webpage
url = "https://reverehealth.com/live-better/do-your-makeup-habits-harm-your-skin/"

# Extract the links from the webpage
links = extract_links(url)

# Display the extracted links
# print("Extracted links:")
for link in links:
    # print(link)

# Task 3
    url = "https://en.wikipedia.org/wiki/List_of_programming_languages"
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table element with a specific CSS class
    table = soup.find('table', class_='wikitable sortable')

    # Find all rows in the table body
    rows = table.tbody.find_all('tr')

    # Iterate over the rows and extract relevant information
    for row in rows:
        # Find all columns in the row
        columns = row.find_all('td')

        # Extract and print the programming language name and its first appeared year
        if len(columns) >= 2:
            language = columns[1].text.strip()
            year = columns[2].text.strip()
            print("Language:", language)
            print("First appeared:", year)
            print("----------")
