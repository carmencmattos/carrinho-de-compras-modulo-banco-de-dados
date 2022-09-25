
import code

async def create_product(product_collection, product):
    try:
        product = await product_collection.insert_one(product)

        if product.inserted_id: #busca o id que acabei de criar
            product = await get_product_by_code(product_collection, product.inserted_id) 
            return product
        
    except Exception as e:
        print(f'create_product.error: {e}')

async def get_product_by_code(product_collection, code):
    try:
        data = await product_collection.find_one({'code': code})
        if data:
            return data
    except Exception as e:
        print(f'get_product.error: {e}')
        
async def insert_new_product(product_collection, product_id, object_id_product):
    try:
        product = await product_collection.update_one(
            {"_id": product_id},
            {
                '$addToSet': {
                'product': object_id_product
                }
            }
        )
        if product.modified_count:
            product = await get_product_by_code(product_collection, code) 
            return product
        
    except Exception as e:
        print(f'create_product.error: {e}')
        
        
async def delete_product(product_collection, code):
    try:
        product = await product_collection.delete_one(
            {'code': code}
        )
        if product.deleted_count:
            return {'status': 'Product deleted'} 
    except Exception as e:
        print(f'delete_user.error: {e}')
