product_list = ["coke-zero", "corona", "water", "sprite"]

main_menu_options = ["0-Exit App", "1-Product Menu"]

product_menu_options = ["0-Return to the Main Menu","1-Products List","2-Create New Produc","3-Update EXisting Product"]

print(main_menu_options)

main_menu_input= int(input("Please chose from the above 2 options '0-1'"))

if main_menu_input == 0:
    exit()
elif main_menu_input == 1:
    print(product_menu_options)
    product_menu_input = input("Chose from above product menu")
    if product_menu_input == 0:
        # Figure out how to return to the main menu
        exit()
    elif product_menu_input == 1:
        print(product_list)



        