# 🚀 Python Practice Problems

## 📝 **1: Problem Statement 01_add_two_numbers.md** 🔢

Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

- 🖊 Prompt the user to enter the first number.
- ⌨️ Read the input and convert it to an integer.
- 🖊 Prompt the user to enter the second number.
- ⌨️ Read the input and convert it to an integer.
- ➕ Calculate the sum of the two numbers.
- 📢 Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the `main()` function guides the user through the process of entering two numbers and displays their sum.

---

## 🐾 **2: Problem Statement 02_agreement_bot.md** 🦊

Write a program that asks the user what their favorite animal is, and then always responds with:

> **"My favorite animal is also ___!"** 🦁 (The blank should be filled in with the user-inputted animal.)

**Example Run:**
```
What's your favorite animal? cow
My favorite animal is also cow!
```

---

## 🌡 **3: Problem Statement 03_fahrenheit_to_celsius.md** 🌍

Write a program that prompts the user for a temperature in Fahrenheit and outputs the temperature converted to Celsius.

🌡 The equation to convert Fahrenheit to Celsius is:
```
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
```

**Example Run:**
```
Enter temperature in Fahrenheit: 76
Temperature: 76.0F = 24.44C
```

---

## 🎂 **4: Problem Statement 04_how_old_are_they.md** 👶👦👨

Write a program to solve this age-related riddle! The ages of friends are:

- Anton is **21** years old.
- Beth is **6** years older than Anton.
- Chen is **20** years older than Beth.
- Drew is **as old as Chen's age plus Anton's age**.
- Ethan is **the same age as Chen**.

Your program should store each person's age in a variable and print their names and ages.

**Example Output:**
```
Anton is 21
Beth is 27
Chen is 47
Drew is 68
Ethan is 47
```

---

## 📐 **5: Problem Statement 05_triangle_perimeter.md** 📏

Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (sum of all sides).

**Example Run:**
```
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5
```

---

## 🔢 **6: Problem Statement 06_square_number.md** 🟦

Ask the user for a number and print its square (the number multiplied by itself).

**Example Run:**
```
Type a number to see its square: 4
4.0 squared is 16.0
```

---

## 🖥 **Code Example for All Problems** 🏆
```python
def main():
    # Problem 1: Add Two Numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is:", num1 + num2)

    # Problem 2: Agreement Bot
    animal = input("What's your favorite animal? ")
    print("My favorite animal is also " + animal + "!")

    # Problem 3: Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print("Temperature:", fahrenheit, "F =", celsius, "C")

    # Problem 4: Age Riddle
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen
    print(f"Anton is {anton}\nBeth is {beth}\nChen is {chen}\nDrew is {drew}\nEthan is {ethan}")

    # Problem 5: Triangle Perimeter
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    print("The perimeter of the triangle is", side1 + side2 + side3)

    # Problem 6: Square Number
    num = float(input("Type a number to see its square: "))
    print(f"{num} squared is {num ** 2}")

if __name__ == "__main__":
    main()
```
---
🎯 **Happy Coding!** 🚀













