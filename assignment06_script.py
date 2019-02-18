# ---------------------------------------
# Title:  Assignment06 script (To Do List with Functions and Classes)
# Name:  Kyle Chan
# Date:  Feb 17, 2019
# Course:  Intro to Python
# Comments:  This code goes with Intro
# to Python Class Assignment06
# This assignment adds onto what we did with Assignment05
# Create Python script file that manages a To Do list
# Store data in a Python Dictionary
# Create conditional loop with user options
# Save file to Todo.txt
# However we will use functions and classes to make our code more streamlined
# We will start with using the Assignment05_answer.py from class


#-- Data --#
# declare variables and constants
filename = "C:\_PythonClass\Assignment06\Todo.txt"  # name of text file of todolist
table = []  # empty table for list

#-- Processing & Input/Output --#
# Create class to put all functions in
class todoList(object):

    # Create Functions needed for program
    # This function reads the file Todo.txt into a python dictionary and passes the file name as a parameter
    @staticmethod
    def read_file(filename, table):
        objFile = open(filename, "r")
        for line in objFile:
            strData = line.split(",")  # readline() reads a line of the data into 2 elements
            dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
            table.append(dicRow)
        objFile.close()
        return table

    # This function prints the menu of options
    @staticmethod
    def print_menu():
        print("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Exit Program
        """)
        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()  # adding a new line
        return strChoice

    # This function shows the current items in the table and passes the lstTable as parameter
    @staticmethod
    def show_data(table):
        print("******* The current items ToDo are: *******")
        for row in table:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    # This function adds a new item to the list table and passes lstTable as parameter
    @staticmethod
    def add_item(table):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        table.append(dicRow)
        for dicRow in table:
            print(dicRow)
        return table

    # This functions removes an item from the list table and passes lstTable as parameter
    @staticmethod
    def remove_item(table):
        # 5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(table)):
            if (strKeyToRemove == str(
                    list(dict(table[intRowNumber]).values())[0])):  # the values function creates a list!
                del table[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        # 5b-Update user on the status
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        return table

    # This functions save the data from list table into objfile
    # 5b Ask if they want save that data
    @staticmethod
    def save_file(table, filename):
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(filename, "w")
            for dicRow in table:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")


#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
lstTable = todoList.read_file(filename,table)

while(True):

    # Step 2
    # Display a menu of choices to the user
    strChoice_selection = todoList.print_menu()

    # Step 3
    # Show the current items in the table
    if (strChoice_selection.strip() == '1'):
        todoList.show_data(lstTable)

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice_selection.strip() == '2'):
        lstTable = todoList.add_item(lstTable)

        #4a Show the current items in the table
        todoList.show_data(lstTable)


    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice_selection.strip() == '3'):
        lstTable = todoList.remove_item(lstTable)

        #5c Show the current items in the table
        todoList.show_data(lstTable)

   # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice_selection.strip() == '4'):
        todoList.show_data(lstTable)

        # Ask if they want to save data
        todoList.save_file(lstTable,filename)
        continue  # to show the menu
    elif (strChoice_selection.strip() == '5'):
        break  #and Exit the program


