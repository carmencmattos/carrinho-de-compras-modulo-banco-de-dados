
async def get_address_by_user_id(address_collection, user_id):
    try:
        data = await address_collection.find_one({'user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')


async def create_address(address_collection, address):
    try:
        address = await address_collection.insert_one(address)

        if address.inserted_id:  # busca o id que acabei de criar
            # função para buscar endereço e retornar
            address = await get_address(address_collection, address.inserted_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')


async def insert_new_address(address_collection, address_id, new_object_address):
    try:
        address = await address_collection.update_one(
            {"_id": address_id},
            {
                '$addToSet': {
                    'address': new_object_address
                }
            }
        )
        if address.modified_count:
            # função para buscar endereço e retornar
            address = await get_address(address_collection, address_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')


async def get_address(address_collection, user_id):
    try:
        data = await address_collection.find_one({'_id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')


async def get_adresses(address_collection, skip, limit):  # paginação
    try:
        address_cursor = address_collection.find().skip(int(skip)).limit(int(limit))
        adresses = await address_cursor.to_list(length=int(limit))
        return adresses

    except Exception as e:
        print(f'get_adresses.error: {e}')


async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
