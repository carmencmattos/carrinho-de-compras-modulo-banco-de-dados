from src.models.user import (
    get_user_by_email
)

from src.models.address import (
    get_address_by_user_id
)

from src.models.order import (
    get_order_by_email,
    get_order_by_user_id,
    create_order,
    insert_new_order,
    delete_order
)

from src.server.database import connect_db, db, disconnect_db


async def order_crud():
    print(" #1 Create Order \n #2 Read Order \n #3 Delete Order")
    option = input("Entre com a opção de CRUD: ")

    await connect_db()
    users_collection = db.users_collection
    address_collection = db.address_collection
    order_collection = db.order_collection

    email = "lu_domagalu@gmail.com"

    order = {
        "user": None,
        "price": 0.0,
        "paid": False,
        "address": None
    }

    new_order = {
        "user": None,
        "price": 10.0,
        "paid": True,
        "address": None
    }

    if option == '1':
        user = await get_user_by_email(users_collection, email)
        address = await get_address_by_user_id(
            address_collection, user["_id"])

        user_order = await get_order_by_user_id(order_collection, user["_id"])

        if user_order:
            updated_address = await insert_new_order(
                address_collection,
                user_order["_id"],
                new_order
            )
            print(updated_address)
        else:
            order["user"] = user
            order["address"] = address
            order = await create_order(order_collection, order)
            print(order)

    elif option == '2':
        user_order = await get_order_by_email(order_collection,
                                              email)
        print(user_order)

    elif option == '3':
        user_order = await get_order_by_email(order_collection,
                                              email)
        result = await delete_order(
            order_collection,
            user_order["_id"]
        )
        print(result)

    await disconnect_db()
