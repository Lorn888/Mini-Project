product_names = ["coke-zero", "corona", "water", "sprite"]

main_menu_options = ["0-Exit App", "1-Product Menu"]

product_menu_options = ["0-Exit App","1-Products List","2-Create New Produc","3-Update EXisting Product"]

print(main_menu_options)

user_input= int(input("Please chose from the above 2 options '0-1'"))

if user_input == 0:
    exit()
elif user_input == 1:
    print(product_menu_options)
    product_menu_inpout = input("Chose from above product menu")