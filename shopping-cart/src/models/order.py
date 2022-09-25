async def get_order_by_id(order_collection, order_id):
    try:
        data = await order_collection.find_one({'_id': order_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order_by_id.error: {e}')


async def get_order_by_email(order_collection, email):
    try:
        data = await order_collection.find_one({'user.email': email})
        if data:
            return data
    except Exception as e:
        print(f'get_order_by_email.error: {e}')


async def get_order_by_user_id(order_collection, user_id):
    try:
        data = await order_collection.find_one({'user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order_by_user_id.error: {e}')


async def create_order(order_collection, order):
    try:
        order = await order_collection.insert_one(order)

        if order.inserted_id:
            order = await get_order_by_id(order_collection, order.inserted_id)
            return order

    except Exception as e:
        print(f'create_order.error: {e}')


async def insert_new_order(order_collection, order_id, new_object_order):
    try:
        order = await order_collection.update_one(
            {"_id": order_id},
            {"$set": new_object_order},
        )
        if order.modified_count:
            order = await get_order_by_id(order_collection, order_id)
            return order

    except Exception as e:
        print(f'insert_new_order.error: {e}')


async def delete_order(order_collection, order_id):
    try:
        order = await order_collection.delete_one(
            {'_id': order_id}
        )
        if order.deleted_count:
            return {'status': 'order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')
