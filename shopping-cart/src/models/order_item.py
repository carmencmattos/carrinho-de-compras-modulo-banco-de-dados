async def get_order_item_by_id(order_item_collection, order_item_id):
    try:
        data = await order_item_collection.find_one({'_id': order_item_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order_item_by_id.error: {e}')


async def get_order_itens_by_email(order_item_collection, order_collection, email):
    try:
        order = await order_collection.find_one({'user.email': email})
        order_itens = await order_item_collection.find({'order._id': order["_id"]})
        if order_itens:
            return order_itens
    except Exception as e:
        print(f'get_order_itens_by_email.error: {e}')


async def get_order_itens_by_order_id(order_item_collection, order_id):
    try:
        order_itens = await order_item_collection.find({'order._id': order_id})
        if order_itens:
            return order_itens
    except Exception as e:
        print(f'get_order_itens_by_order_id.error: {e}')


async def create_order_item(order_item_collection, order):
    try:
        order_item = await order_item_collection.insert_one(order)

        if order_item.inserted_id:
            order_item = await get_order_item_by_id(order_item_collection, order_item.inserted_id)
            return order_item

    except Exception as e:
        print(f'create_order_item.error: {e}')


async def delete_order_item(order_item_collection, order_item_id):
    try:
        orde_item = await order_item_collection.delete_one(
            {'_id': order_item_id}
        )
        if orde_item.deleted_count:
            return {'status': 'order deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')
