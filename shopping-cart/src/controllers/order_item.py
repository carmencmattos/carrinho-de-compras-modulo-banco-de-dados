from src.models.user import (
    get_user_by_email
)

from src.models.order_item import (
    get_order_itens_by_email,
    create_order_item,
    delete_order_item
)

from src.models.order import (
    get_order_by_user_id,
    insert_new_order
)

from src.models.product import (
    get_product_by_code
)


from src.server.database import connect_db, db, disconnect_db


async def order_item_crud():
    print(" #1 Create order item  \n #2 Update order item  \n #3 Read order item \n #4 Delete order item")
    option = input("Entre com a opção de CRUD: ")

    await connect_db()
    users_collection = db.users_collection
    order_items_collection = db.order_items_collection
    order_collection = db.order_collection
    product_collection = db.product_collection

    email = "lu_domagalu@gmail.com"

    product_1 = {
        "code": 222479100,
    }

    product_2 = {
        "code": 97880,
    }

    new_order_item = {
        "order": None,
        "product": None,
    }

    if option == '1':
        user = await get_user_by_email(users_collection, email)
        product = await get_product_by_code(product_collection, product_1["code"])
        order = await get_order_by_user_id(order_collection, user["_id"])
        new_order_item["order"] = order
        new_order_item["product"] = product
        order_item = await create_order_item(order_items_collection, new_order_item)
        order["price"] = order["price"] + product["price"]
        order = await insert_new_order(order_collection, order["_id"], order)
        print(order_item)

    elif option == '2':
        user = await get_user_by_email(users_collection, email)
        product = await get_product_by_code(product_collection, product_2["code"])
        order = await get_order_by_user_id(order_collection, user["_id"])
        new_order_item["order"] = order
        new_order_item["product"] = product
        order_item = await create_order_item(order_items_collection, new_order_item)
        order["price"] = order["price"] + product["price"]
        order = await insert_new_order(order_collection, order["_id"], order)
        print(order_item)

    elif option == '3':
        order_itens = await get_order_itens_by_email(order_items_collection, order_collection, email)
        print(order_itens)

    elif option == '4':
        user = await get_user_by_email(users_collection, email)
        order_itens = await get_order_itens_by_email(order_items_collection, order_collection, email)
        order = await get_order_by_user_id(order_collection, user["_id"])
        order["price"] = order["price"] - product["price"]
        order = await insert_new_order(order_collection, order["_id"], order)
        result = await delete_order_item(order_items_collection, order_itens[0]["_id"])
        print(result)

    await disconnect_db()
