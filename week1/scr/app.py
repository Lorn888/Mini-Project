product_list = ["coke-zero", "corona", "water", "sprite"]

main_menu_options = ["0-Exit App", "1-Product Menu"]

product_menu_options = ["0-Return to the Main Menu","1-Products List","2-Create New Produc","3-Update EXisting Product"]

print(main_menu_options)

main_menu_input= int(input("Chose from the above 2 options '0-1'"))

if main_menu_input == 0:
    exit()
elif main_menu_input == 1:
    print(product_menu_options)
    product_menu_input = int(input("Chose from above product menu"))
    if product_menu_input == 0:
        # Figure out how to return to the main menu
        exit()
    elif product_menu_input == 1:
        print(product_list)
    elif product_menu_input == 2:
        new_product_input = input("type the name of the product")
        product_list.append(new_product_input)
    elif product_menu_input == 3:
        for product in product_list:
            print(f"{product_list.index(product)}-{product}")
        product_to_update_input = int(input("Chose the product to update"))
        new_product_name = input("Type the name of the new product")
        product_list[product_to_update_input] = new_product_name
        print(product_list)

        