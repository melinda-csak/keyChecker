#example of how to import a method from an other file
from ShapeCalculator import ShapeCalculator

class Main:

    # initialize parameters used in Main class
    def __init__(self):
        #next two lines are examples
        self.rectangle_width = 5
        self.rectangle_height = 10

        # TODO: add needed parameters:

    # call the imported method and write the variable value
    def run(self):
        #next two lines are examples
        area = ShapeCalculator.calculate_area_rectangle(self.rectangle_width, self.rectangle_height)
        print(f"The area of the rectangle is: {area}")

        # TODO: return the result of the key-checking:


# the following block is a common idiom in Python
# it allows you to check if the script is being run directly (not imported as a module)
# if it's the main script being executed, it creates an instance of the Main class and calls the run method on that instance
if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()