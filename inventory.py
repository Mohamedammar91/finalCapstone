from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
               In this function, you must initialise the following attributes:
                   ● country,
                   ● code,
                   ● product,
                   ● cost, and
                   ● quantity.
               '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        # Add the code to return the cost of the shoe in this method.
        return print(self.cost)




    def get_quantity(self):
        # Add the code to return the quantity of the shoes.
        return print(self.quantity)




    def __str__(self):
        # Add a code to returns a string representation of a class.

        return self.country+","+self.code+","+self.product+","+self.cost+","+self.quantity

        # f"Country : {self.country}  \nCode : {self.code}  \nProduct : {self.product}  "
        #                      f"\nThe Cost : {self.cost} \nQuantity : {self.quantity}")



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    file = open("inventory.txt", "r")
    read_file = file.readlines()
    for i in read_file:

        list_data = i.split(",")
        if list_data[0] == "Country":
            list_data.clear()
        else:
           while True:
            try:
               shoe_list.append(Shoe(list_data[0],list_data[1],list_data[2],list_data[3],list_data[4]))
               break
            except IndexError:
                print("missing data")
                break



def capture_shoes():
    pass
    #  This function will allow a user to capture data
    #     about a shoe and use this data to create a shoe object
    #     and append this object inside the shoe list.
    shoe_country = input("please enter shoe country: ")
    shoe_code = input("please enter shoe code: ")
    shoe_product = input("please enter shoe product: ")
    shoe_cost = input("please enter shoe cost: ")
    shoe_quantity = input("please enter shoe quantity: ")

    shoe_list.append(Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity))


def view_all():
    pass

    # This function will iterate over the shoes list and
    #     print the details of the shoes returned from the __str__
    #     function. Optional: you can organise your data in a table format
    #     by using Python’s tabulate module.
    for i in range(len(shoe_list)):
        shoe_details = (str(shoe_list[i])).split(",")

        shoe_table = [["Country : ", shoe_details[0]],
                      ["Code : ", shoe_details[1]],
                      ["Product: ", shoe_details[2]],
                      ["Cost : ", shoe_details[3]],
                      ["Quantity : ", shoe_details[4]]
                              ]
        print(tabulate(shoe_table,  tablefmt = "heavy_grid"))

def re_stock():
    pass

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # shoe_quantities is list have all shoes quantities
    shoe_quantities = []
    # loop through shoe list and get quantities of shoes and put in shoe_quantities
    for i in range(len(shoe_list)):
        shoe_details = (str(shoe_list[i])).split(",")
        shoe_quantities.append(int(shoe_details[-1]))
    print("this is quantities of all shoes objects in list")
    print(shoe_quantities)
    # put value to smaller number the first element
    smaller = shoe_quantities[0]
    # loop through the shoe_quantities and check the smallest number
    for i in range(len(shoe_quantities) - 1):
        if shoe_quantities[i] < shoe_quantities[i + 1]:
            if shoe_quantities[i] <= smaller:
                smaller = shoe_quantities[i]
        elif shoe_quantities[i] > shoe_quantities[i + 1]:
            if shoe_quantities[i + 1] <= smaller:
                smaller = shoe_quantities[i + 1]
    # the smallest number in list of quantity

    print(f"this lowest quantity in list: {smaller}")
    # index_number is  the location of the smallest number in the list
    index_number = 0
    for index ,i in enumerate(shoe_quantities):
        if i == smaller:
            index_number = index
    # index_number is the index of the Lowest quantity in the list

    print(f"this index of the oject in shoe list: {index_number}")
    # the shoe that has the lowest quantity in shoe list
    print(f"the shoe oject with lowest quantity is : {shoe_list[index_number]}")
    # ask the user if like to add more in quantity
    while True:
        # ask the user if they would like to add quantity in shoe
        user_input = input("Would you like to add more in quantity(yes/no): ")
        if user_input == "yes":
            while True:
                try:
                   add_quantity = int(input("how many quantity you like to add: ")) +int(smaller)
                   break
                except ValueError:
                    print("try Number!")
            # take the lowest quantity shoe from the list and put in list new edition
            new_edition = str(shoe_list[index_number]).split(",")
            # change to new quantity
            new_edition[-1] = str(add_quantity)+"\n"
            print(new_edition)
            # change in shoe list the new shoe object
            shoe_list[index_number]= ",".join(new_edition)
            print(shoe_list[index_number])
            break
        elif user_input == "no":
            # if they don't want to add quantity still need the shoe object in list(new edition)
            new_edition = str(shoe_list[index_number]).split(",")
            print(new_edition)
            break
        else:
            print("try again by (yes or no)")

    # open inventory txt and read the file and put the data in list (inventory_list)
    file = open("inventory.txt","r")
    read_file = file.readlines()
    inventory_list = []
    # loop through the readline and add it to list(inventory_list)
    for i in read_file:
        read_line = i.split(",")
        # if the country and code of the shoe object  matches edit it and add to the inventory_list
        if read_line[0] == new_edition[0] and read_line[1] == new_edition[1]:
            new_read_line = ",".join(new_edition)
            print(new_read_line)
            inventory_list.append(new_read_line)
        else:
            inventory_list.append(i)
    file.close()

    # write the lines in inventory_list in inventory.txt
    write_file = open("inventory.txt","w")
    for i in inventory_list:
        write_file.write(i)
        print(i)
    write_file.close()

def search_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    input_user = input("please enter the code of shoe: ")
    shoe_split = []
    for i in shoe_list:
        shoe_split = str(i).split(",")
        if input_user == shoe_split[1]:
            shoe_table = [["Country : ", shoe_split[0]],
                          ["Code : ", shoe_split[1]],
                          ["Product: ", shoe_split[2]],
                          ["Cost : ", shoe_split[3]],
                          ["Quantity : ", shoe_split[4]]
                          ]
            print(tabulate(shoe_table, tablefmt="heavy_grid"))

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    total_shoes_value = 0
    for i in shoe_list:
        shoe_split = str(i).split(",")
        shoe_value = int(shoe_split[-2]) * int(shoe_split[-1])
        total_shoes_value += shoe_value
        shoe_table = [["Country : ", shoe_split[0]],
                      ["Code : ", shoe_split[1]],
                      ["Product: ", shoe_split[2]],
                      ["Cost : ", shoe_split[3]],
                      ["Quantity : ", shoe_split[4]]
                      ]
        print(tabulate(shoe_table, tablefmt="heavy_grid"))
        print(f"The Value of the shoes is: {shoe_value}")
        print("======================================")
    print(f"total shoes value: {total_shoes_value}")



def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe_details = []
    highest_shoe = []
    shoe_quantities = []
    shoes_lists = []
    # loop through shoe list and take all quantities in put in list (shoe_quantities)
    # take all shoes in shoe_list and put in nested list(shoes_lists)
    for i in shoe_list:
        shoe_details = (str(i)).split(",")
        # check each shoe putted in a list
       #  print(shoe_details)
        shoe_quantities.append(int(shoe_details[-1]))
        shoes_lists.append(shoe_details)
    # check shoe quantities list
    # print(shoe_quantities)
    print(f"shoes objects quantity list {shoe_quantities}")
    # set value for higher quantity as first value in list
    higher_quantity = shoe_quantities[0]
    # loop in shoe_quantities and check which bigger number and the bigger number assign to higher quantity
    for i in range (len(shoe_quantities)-1):
        if shoe_quantities[i]>= shoe_quantities[i+1]:
            if shoe_quantities[i]>= higher_quantity:
                higher_quantity = shoe_quantities[i]
        elif shoe_quantities[i+1] > shoe_quantities[i]:
            if shoe_quantities[i+1]> higher_quantity:
                higher_quantity = shoe_quantities[i+1]

    # check higher quantity
    print(f"highest shoe quantity is {higher_quantity}")
    # check nested list of all shoes
    # print(shoes_lists)
    # loop through shoes_lists when find same value of higher quantity print it as for sale with table
    for i in shoes_lists:
        if int(i[-1]) == int(higher_quantity):
            print(f"This shoe for sale:")
            shoe_table = [["Country : ", i[0]],
                          ["Code : ", i[1]],
                          ["Product: ", i[2]],
                          ["Cost : ", i[3]],
                          ["Quantity : ", i[4]]
                          ]
            print(tabulate(shoe_table, tablefmt="heavy_grid"))


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

read_shoes_data()

while True:
    user_input = input("please choice one of the following: "
                       "\n1- Capture Shoe(capture). 2- View All Shoes(view)"
                       "\n3- Restock of shoe(restock). 4- Search For Shoe(search) "
                       "\n5- the Value of all shoes(value). 6- highest Quantity for shoes(Quantity)"
                       "\nFor exit the app , press (exit):  ")


    if user_input == "capture":
        capture_shoes()
    elif user_input == "view":
        view_all()
    elif user_input == "restock":
        re_stock()
    elif user_input == "search":
        search_shoe()
    elif user_input == "value":
        value_per_item()
    elif user_input == "quantity":
        highest_qty()
    elif user_input == "exit":
        print("thanks you, bye bye!")
        exit()
    else:
        print("try Again from the followings ")

# capture_shoes()
# view_all()
# re_stock()
# search_shoe()
# value_per_item()
highest_qty()

