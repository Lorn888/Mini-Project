product_list = ["coke-zero", "corona", "water", "sprite"]
orders_list = []

main_menu_options = ["0-Exit App", "1-Product Menu", "2-Orders Menu"]

product_menu_options = [
    "0-Return to the Main Menu",
    "1-Products List",
    "2-Create New Produc",
    "3-Update EXisting Product",
    "4-Delete Product",
]

orders_menu_options = [
    "0-Return to the Main Menu",
    "1-Print orders dictionary",
    "2-Create a new order",
    "3-Update Existing Order Status",
    "4-Update Existing Order" "5-Delete Order",
]

print(main_menu_options)

while True:
    main_menu_input = int(input("Chose from the above 3 options '0-2'"))
    if main_menu_input == 0:
        break
    elif main_menu_input == 1:
        while True:
            print(product_menu_options)
            product_menu_input = int(input("Chose from above product menu"))

            if product_menu_input == 0:
                break

            elif product_menu_input == 1:
                print(product_list)

            elif product_menu_input == 2:
                new_product_input = input("type the name of the new product")
                product_list.append(new_product_input)

            elif product_menu_input == 3:

                for product in product_list:
                    print(f"{product_list.index(product)}-{product}")
                product_to_update_input = int(input("Chose the product to update"))
                new_product_name = input("Type the name of the new product")
                product_list[product_to_update_input] = new_product_name
                print(product_list)

            elif product_menu_input == 4:
                for product in product_list:
                    print(f"{product_list.index(product)}-{product}")
                product_to_delete = int(input("Chose the product to delete"))
                product_list.remove(product_list[product_to_delete])
                print(product_list)
    elif main_menu_input == 2:
        while True:
            print(orders_menu_options)
            orders_menu_input = int(input("Chose from above Orders Menu"))
            if orders_menu_input == 0:
                break
            elif orders_menu_input == 1:
                print(orders_list)
                # Orders list or orders dictionary?
            elif orders_menu_input == 2:
                customer_name_input = input("Insert Customer name eg.'Harry Potter'")
                # name_list = customer_name_input.split(" ")
                # print(name_list)
                customer_adress_input = input(
                    "Insert Customer adress eg.'Unit 2, 12 Main Street, LONDON, WH1 2ER'"
                )
                customer_phone_input = input(
                    "Insert Customer phone number eg.'0789887334'"
                )
                # last_dig = (customer_phone_input[-4:])
                # print([last_dig])
                order_status = "PREPARING"
                # customer_order_id = f"{name_list[0]}-{name_list[1]}-{last_dig}"
                # orders_list.append

                customer_order = {
                    "name": customer_name_input,
                    "adress": customer_adress_input,
                    "phone": customer_phone_input,
                    "order status": order_status,
                }
                orders_list.append(customer_order)

                
