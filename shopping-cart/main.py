# -*- coding: utf-8 -*-
import asyncio

print(" #1 User \n #2 Address \n #3 Product \n #4 Order \n #5 Order Item")
option = input("Entre com a opção que deseja manipular: ")



loop = asyncio.get_event_loop()

if option == '1':
    from src.controllers.users import users_crud
    loop.run_until_complete(users_crud())
elif option == '2':
    from src.controllers.address import address_crud
    loop.run_until_complete(address_crud())
elif option == '3':
    from src.controllers.product import product_crud
    loop.run_until_complete(product_crud())
elif option == '4':
    from src.controllers.order import order_crud
    loop.run_until_complete(order_crud())
elif option == '5':
    from src.controllers.order_item import order_item_crud
    loop.run_until_complete(order_item_crud())

