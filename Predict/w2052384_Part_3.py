# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solu􀆟on.
# - W3 Schools - Python
# - YouTube - To understand graphics
# - ChatGPT/ StackOverFlow - Search solutions for Errors

# Student Name: Jerome A.D. Fernando
# Student ID: w2052384
# Date: 05 / 12 / 2023

from graphics import *

# creating a dictionary for saving the result
histogram_output = {
    "progress": 0,
    "trailer": 0,
    "retriever": 0,
    "exclude": 0
}

# list to store the input progression data
progression_data = []


# func to rerun program based on users choice
def rerun_program():
    while True:
        choice = input("Do you want to predict progression for another student? (Enter 'y' to continue, 'q' to quit): ").lower()

        if choice in ['y','q']:
            return choice
        else:
            print("Invalid choice. Please enter ''y'' to continue or ''q'' to quit.\n")


def multiply_values(histogram_output, factor=20):

    multiplied_output = {}
    for x, y in histogram_output.items():
        multiplied_output[x] = 310 - (y * factor)
    return multiplied_output


# func to decide progress outcome
def outcome(valid_pass_mark, valid_defer_mark, valid_fail_mark):
    
    # deciding which progress outcome
    if valid_pass_mark == 120:
        histogram_output["progress"] += 1
        progression_data.append(("Progress", valid_pass_mark, valid_defer_mark, valid_fail_mark))
        print("Progress\n")
    elif valid_pass_mark == 100:
        histogram_output["trailer"] += 1
        progression_data.append(("Module_Trailer", valid_pass_mark, valid_defer_mark, valid_fail_mark))
        print("Module Trailer\n")
    elif valid_fail_mark in [80,100,120,]:
        histogram_output["exclude"] += 1
        progression_data.append(("Exclude", valid_pass_mark, valid_defer_mark, valid_fail_mark))
        print("Exclude\n")
    else:
        histogram_output["retriever"] += 1
        progression_data.append(("Module_Retriever", valid_pass_mark, valid_defer_mark, valid_fail_mark))
        print("Module Retriever\n")

        
# func to calculate the total of all 3 user inputs
def total(pass_mark, defer_mark, fail_mark):
    return pass_mark + defer_mark + fail_mark


# func to validate the total if it is equal to 120
def validating_total():        
    while True:
        # Getting user Inputs
        pass_mark = get_user_input("\nPlease enter your credits at pass: ")
        defer_mark = get_user_input("Please enter your credits at defer: ")
        fail_mark = get_user_input("Please enter your credits at fail: ")

        total_value = total(pass_mark, defer_mark, fail_mark)

        if total_value == 120:
            return pass_mark, defer_mark, fail_mark
            
        else:
            print(f"Error: Total is incorrect. Total is {total_value} but it should be 120.")

            
# func for validating the input for an integer and out of range
def validate_input(user_input):
    try:
        # converting the users input to an integer
        user_input = int(user_input)

        if user_input in range(0,121,20):
            return True
        
        else:
            print("Error: out of range [0,20,40,60,80,100,120]\n")
            return False

    except ValueError:
        print("Error: Integer required!\n")
        return False


# function to get the user input
def get_user_input(value):

    while True:
        user_input = input(value)

        if validate_input(user_input):
            return int(user_input)


def getting_height(multiplied_output):
    # Use a loop to collect only the values into a list
    return [value for key, value in multiplied_output.items()]


# Function to display stored progression data
# def display_progression_data():
#     print("\nDisplaying stored progression data:")
#     for data in progression_data:
#         print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")


# Writing the progression data into a file
def write_to_file():
    file = open("progression Data.txt", "w+")
    for data in progression_data:
        file.write(f"{data[0]} - {data[1]} | {data[2]} | {data[3]}\n")
    file.close()


def read_from_file():
    file = open("progression Data.txt", "r")
    data = file.readlines()
    for item in data:
        word = item.split()

        print(f"{word[0]} - {word[2]}, {word[4]}, {word[6]}")


# Creating a graphics window
def create_histogram(values_list):

    # Extracting the values of histogram_output for displaying on histogram
    progress_v = histogram_output.get("progress", 0)
    trailer_v = histogram_output.get("trailer", 0)
    retriever_v = histogram_output.get("retriever", 0)
    exclude_v = histogram_output.get("exclude", 0)

    win = GraphWin("Histogram", 500, 500)
    label = Text(Point(250, 50), "Histogram Results")
    label.setSize(12)
    label.draw(win)

    box = Rectangle(Point(25, 310), Point(100, values_list[0]))  # Height is 1 * 20 = (350 - 20) = 330
    label = Text(Point(100, (values_list[0] - 15)), f"{progress_v}")
    label.setSize(10)
    label.draw(win)
    box.setFill("green")
    box.draw(win)
    box.move(40, 0)

    box = Rectangle(Point(100, 310), Point(175, values_list[1]))  # Height is 0 * 20 = (350 - 0)=  350
    label = Text(Point(200, (values_list[1] - 15)), f"{trailer_v}")
    label.setSize(10)
    label.draw(win)
    box.setFill("blue")
    box.draw(win)
    box.move(65, 0)

    box = Rectangle(Point(175, 310), Point(250, values_list[2]))  # Height is 18 * 20 = (350 - 180)= 120
    label = Text(Point(300, (values_list[2] - 15)), f"{retriever_v}")
    label.setSize(10)
    label.draw(win)
    box.setFill("yellow")
    box.draw(win)
    box.move(90, 0)

    box = Rectangle(Point(250, 310), Point(325, values_list[3]))  # Height is 2 * 20 =(350 - 20)= 280
    label = Text(Point(400, (values_list[3] - 15)), f"{exclude_v}")
    label.setSize(10)
    label.draw(win)
    box.setFill("red")
    box.draw(win)
    box.move(115, 0)

    line = Line(Point(50, 320, ), Point(450, 320))
    line.setWidth(3)
    line.draw(win)

    label = Text(Point(100, 350), "Progress")
    label.draw(win)
    label.setSize(10)

    label = Text(Point(200, 350), "Module\nTrailer")
    label.draw(win)
    label.setSize(10)

    label = Text(Point(300, 350), "Module\nRetriever")
    label.draw(win)
    label.setSize(10)

    label = Text(Point(400, 350), "Exclude")
    label.draw(win)
    label.setSize(10)

    # adding each value to the total_output
    total_output = 0
    for values in histogram_output.values():
        total_output += values

    label = Text(Point(100, 400), f"{total_output} Outcomes in total.")
    label.draw(win)
    label.setSize(10)

    # using a try except block to catch the error on close and pass on to the next function
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass


# Function to predict progression for student
def student_predict():
    valid_pass_mark, valid_defer_mark, valid_fail_mark = validating_total()

    outcome(valid_pass_mark, valid_defer_mark, valid_fail_mark)


# Function to predict progression for staff member
def staff_predict():

    while True:
        # Getting valid user inputs
        valid_pass_mark, valid_defer_mark, valid_fail_mark = validating_total()

        # checking outcome based on valid user inputs
        outcome(valid_pass_mark, valid_defer_mark, valid_fail_mark)

        # rerun program
        choice = rerun_program()

        if choice == 'q':
            print("\nThank you for using Predict!")

            multiplied_output = multiply_values(histogram_output)

            # getting the calculated height for drawing the histogram
            values_list = getting_height(multiplied_output)

            # Displaying progression data
            # display_progression_data()

            # writing and reading progression data from text file
            write_to_file()
            read_from_file()

            # Creating the Histogram
            create_histogram(values_list)
            break


# Setting a password for Staff member
def staff_pass():
    psw = "admin"
    while True:
        input_psw = input("Enter password: ").lower()

        if input_psw == psw:
            staff_predict()
            break
        else:
            print("Access denied! :)\n")


def main():
    print("====== Welcome to Predict! ======")
    print("Note: Please enter values of [0,20,40,60,80,100,120].")

    while True:
        print("\nAre you a Student or a Staff member? Please enter the option number:")
        print("1. Student")
        print("2. Staff")
        print("3. Exit\n")

        type_of_user = input("Enter option number: ")

        if type_of_user == '1':
            student_predict()

        elif type_of_user == '2':
            staff_pass()

        elif type_of_user == '3':
            print("Thank you for using Predict.")
            break
        else:
            print("Invalid Type of user! Please enter [1] for Student; [2] for Staff\n")


if __name__ == "__main__":
    main()







