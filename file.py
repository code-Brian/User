# Here we go!!
# Assignment: User
# For this assignment, you will create the user class and add a couple methods!
# Attributes:
'''
On instantiation of a user, the following attributes should be passed in as arguments:
first_name
last_name
email
age

Also include default attributes:
is_rewards_member - default value of False
gold_card_points = 0

Methods:
display_info(self) Have this method print all of the users' details on separate lines
enroll(self) Have this method change the users' member status to True and set their gold card points to 200.
spend_points(self, amount) Have this method decrease the users' points by the amount specified.

Ninja Bonuses 
Add logic in the enroll method to check if they are a member already, and if they are,
print "User already a member", and return False. Otherwise, return True.

Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately. 
'''

class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.member = False
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(f"is member: {self.member}")
    
    def enroll(self):
        if (self.member):
            print(f"{self.first_name} is already a member")
        else:
            self.member = True
            print(f"{self.first_name} is now a member. Welcome to the club! Help yourself to punch and pie.")


brian = User("Brian","Denmark", "brian@gmail.com", 31)

print(brian.display_info())
brian.enroll()
print(brian.display_info())
brian.enroll()