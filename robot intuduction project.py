# Defining a Robot class
class Robot:
    # Constructor method to initialize the robot's attributes
    def __init__(self, name, model, year_of_creation):
        self.name = name
        self.model = model
        self.year_of_creation = year_of_creation
    
    # Method to introduce the robot
    def introduce(self):
        print(f"Hello! I am {self.name}, a {self.model} model robot.")
        print(f"I was created in the year {self.year_of_creation}.")
    
    # Method to describe what the robot can do
    def abilities(self):
        print(f"{self.name} can perform various tasks like data analysis, conversation, and providing assistance.")

# Creating an instance of the Robot class
my_robot = Robot("ChatGPT", "AI Assistant", 2024)

# Introducing the robot and its abilities
my_robot.introduce()
my_robot.abilities()
