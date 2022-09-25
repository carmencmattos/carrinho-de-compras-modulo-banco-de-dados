
from src.models.product import (
    create_product,
    get_product_by_code,
    insert_new_product,
    delete_product
)


from src.server.database import connect_db, db, disconnect_db


async def product_crud():
    print(" #1 Create Product \n #2 Read Product \n #3 Update Product \n #4 Delete Product")
    option = input("Entre com a opção de CRUD: ")

    await connect_db()
    product_collection = db.product_collection

    product = {
        "name": "Bicicleta Aro 29 Freio a Disco 21M. Velox Branca/Verde - Ello Bike",
        "description": "Bicicleta produzida com materiais de qualidade e foi criada pensando nas pessoas que desejam praticar o ciclismo e ter uma vida saudável sem abrir mão de conforto um excelente custo x benefício.",
        "price": 898.2,
        "image": "https://a-static.mlcdn.com.br/800x560/bicicleta-aro-29-freio-a-disco-21m-velox-branca-verde-ello-bike/ellobike/6344175219/b84d5dd41098961b4c2f397af40db4ce.jpg",
        "code": 97880.0
    }

    new_product = {
        "_id": "632b9a9ebccec08091827701",
        "name": "Fritadeira Elétrica sem Óleo/Air Fryer Nell Fit - Preto 3,2L com Timer",
        "description": "A fritadeira elétrica Nell Fit é um eletroportátil que não pode faltar na sua cozinha. O produto proporciona uma alimentação mais saudável, pois não utiliza óleo/Air Fryer em seu processo de cozimento. A fritadeira na cor preta é compacta e produzida em PP, ocupando menos espaço, possui luz indicadora de funcionamento, controle de temperatura, cesta removível antiaderente, capacidade total de 4,2L e cesto com capacidade de 3,2L. Sua alça fria garante maior segurança ao manusear a fritadeira e além disso, ela possui timer de 30 minutos sonoro e com desligamento automático. Agora é só preparar batatinha frita, coxinha, bolinha de queijo e pastel na sua fritadeira elétrica!",
        "price": 369.0,
        "image": "https://a-static.mlcdn.com.br/800x560/fritadeira-eletrica-sem-oleo-air-fryer-nell-fit-preto-32l-com-timer/magazineluiza/222479100/64ef4d6200a6efc6cce6d265588910a9.jpg",
        "code": 222479100.0
    }

    if option == '1':
        # create product
        product = await create_product(
            product_collection,
            product
        )
        print(product)

    elif option == '2':
        # get product
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )
        print(product)

    elif option == '3':
        # insert new product
        product = await insert_new_product(
            product_collection,
            new_product["code"],
        )
        print(new_product)

        # get new product
        new_product = await get_product_by_code(
            product_collection,
            product["code"]
        )
        print(product)

    elif option == '4':
        # delete
        product = await get_product_by_code(
            product_collection,
            product["code"]
        )

        result = await delete_product(
            product_collection,
            product["code"]
        )

        print(result)

    await disconnect_db()
