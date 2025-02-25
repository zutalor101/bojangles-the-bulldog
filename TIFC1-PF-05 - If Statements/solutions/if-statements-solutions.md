# Exercise 5: If Statements

Please work through as many of the following exercises as you’re able to in the allotted time and upload the results of the last task you were able to complete.

### 1.	
Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

 <img src="imgs/example.jpg" width="400" />

- Look closely at your results, and make sure you understand why each line evaluates to True or False. 

- Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

```py
# Test 1: True - checking equality of strings
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")  # True

# Test 2: False - checking equality of strings
print("Is car == 'toyota'? I predict False.")
print(car == "toyota")  # False

# Test 3: True - checking inequality of numbers
age = 25
print("Is age != 30? I predict True.")
print(age != 30)  # True

# Test 4: False - checking greater than comparison of numbers
print("Is age > 30? I predict False.")
print(age > 30)  # False

# Test 5: True - checking if a number is within a range
print("Is age >= 18 and age <= 30? I predict True.")
print(age >= 18 and age <= 30)  # True

# Test 6: False - checking if a number is less than a value
print("Is age < 18? I predict False.")
print(age < 18)  # False

# Test 7: True - checking if a value exists in a list
favorite_fruits = ["apple", "banana", "mango"]
print("Is 'banana' in favorite_fruits? I predict True.")
print("banana" in favorite_fruits)  # True

# Test 8: False - checking if a value does not exist in a list
print("Is 'grape' not in favorite_fruits? I predict False.")
print("grape" not in favorite_fruits)  # True (but we predict False, thus incorrect)

# Test 9: True - case-insensitive string comparison using lower()
food = "Pizza"
print("Is food.lower() == 'pizza'? I predict True.")
print(food.lower() == "pizza")  # True

# Test 10: False - checking a string starts with a particular substring
print("Does 'subaru' start with 't'? I predict False.")
print(car.startswith("t"))  # False
```

### 2.	
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then: 

- If the person is less than 2 years old, print a message that the person is a baby. 
- If the person is at least 2 years old but less than 4, print a message that the person is a toddler. 
- If the person is at least 4 years old but less than 13, print a message that the person is a kid. 
- If the person is at least 13 years old but less than 20, print a message that the person is a teenager. 
- If the person is at least 20 years old but less than 65, print a message that the person is an adult. 
-	If the person is 65 or older, print a message that the person is an elder.

```py
# Set a value for the variable age
age = 30

# Use if-elif-else to determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
```

### 3. 
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list. 
- Make a list of your three favorite fruits and call it favorite_fruits. 
- Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

```py
 # Step 1: Make a list of your three favorite fruits
favorite_fruits = ["banana", "mango", "apple"]

# Step 2: Write five independent if statements to check for certain fruits
if "banana" in favorite_fruits:
    print("You really like bananas!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "grape" not in favorite_fruits:
    print("It seems you don't like grapes!")

if "pineapple" not in favorite_fruits:
    print("It seems you don't like pineapples!")
```

### 4.	
Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user: 

- If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report? 
- Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again

```py
# List of usernames including 'admin'
usernames = ["alice", "bob", "charlie", "admin", "dave"]

# Loop through the list and print a greeting for each user
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again.")
```

## Stretch and Challenge: 
Add an if test to make sure the list of users is not empty. 

If the list is empty, print the message We need to find some users! 
Remove all of the usernames from your list, and make sure the correct message is printed

```py
# List of usernames including 'admin'
usernames = ["alice", "bob", "charlie", "admin", "dave"]

# Check if the list is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through the list and print a greeting for each user
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.capitalize()}, thank you for logging in again.")

# redefine the list as empty
usernames = []

# Check if the list is empty again
if not usernames:
    print("We need to find some users!")
```

### 5.
Do the following to create a program that simulates how websites ensure that everyone has a unique username. 

- Make a list of five or more usernames called current_users. 
- Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list. 
- Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available. 
- Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.


# Stretch and Challenge

If you complete the previous steps within the allotted time please move on to the following.

Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3. 

- Store the numbers 1 through 9 in a list. 
- Loop through the list. 
- Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

```py
# List of numbers 1 through 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list and print the proper ordinal ending
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
```
At this point, you’re a more capable programmer than you were when you started this course!

Now that you have a better sense of how real-world situations are modeled in programs, you might be thinking of some problems you could solve with your own programs. Record any ideas you have about problems you might want to solve as your programming skills continue to improve. Consider:
- Games you might want to write 
- Data sets you might want to explore 
- Web applications you’d like to create, and so on...

One of your ideas could be a project you can work on once you are in the post-programme phase!
