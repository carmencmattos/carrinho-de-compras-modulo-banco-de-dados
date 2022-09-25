from src.models.user import (
    get_user_by_email
)

from src.models.address import (
    get_address_by_user_id,
    create_address,
    insert_new_address,
    get_adresses,
    delete_address
)

from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    print(" #1 Create Address \n #2 Read Address \n #3 Delete Address")
    option = input("Entre com a opção de CRUD: ")

    await connect_db()
    users_collection = db.users_collection
    address_collection = db.address_collection

    user = {
        "email": "lu_domagalu@gmail.com",
    }

    address = {
        "street": "Castelo Branco",
        "cep": "21210-210",
        "district": "Ilha das Flores",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "is_delivery": True,
    }

    new_address = {
        "street": "Floresta Azul",
        "cep": "21210-000",
        "district": "Cacuia",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "is_delivery": False,
    }

    if option == '1':
        # create address
        # get address
        user = await get_user_by_email(
            users_collection,
            user["email"],
        )

        # user_address
        user_address = await get_address_by_user_id(
            address_collection,
            user["_id"]
        )

        if user_address:
            updated_address = await insert_new_address(
                address_collection,
                user_address["_id"],
                new_address
            )
            print(updated_address)
        else:
            user_address_info = {'user': user, 'address': [address]}

            address = await create_address(
                address_collection,
                user_address_info
            )
            print(address)

    elif option == '2':
        # get address
        user = await get_user_by_email(
            users_collection,
            user["email"],
        )

        # user_address
        user_address = await get_address_by_user_id(
            address_collection,
            user["_id"]
        )

        # get_adresses
        adresses = await get_adresses(
            address_collection,
            skip=0,
            limit=3
        )
        print(adresses)

    elif option == '3':
        # get address
        user = await get_user_by_email(
            users_collection,
            user["email"]
        )

        user_address = await get_address_by_user_id(
            address_collection,
            user["_id"]
        )

        # delete_address
        result = await delete_address(
            address_collection,
            user_address["_id"]
        )
        print(result)

    await disconnect_db()
