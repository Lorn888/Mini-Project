product_names = ["coke-zero", "corona", "water", "sprite"]


product_menu_options = ["0-Exit App","1-Print Products List","2-Create New Produc","3-Update EXisting Product"]

user_input= int(input("Please chose from the above options '0-4'"))

if user_input == 0:
    exit()
elif user_input == 1:
    print(product_menu_options)