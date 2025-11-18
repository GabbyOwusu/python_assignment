

# Build a basic inventory system for a small shop using Python. It will allow users to:

# View all items

# Add a new item

# Update item stock

# Delete an item

#  ** Calculate total stock value


'''
 Inventory structure 
  {
    item_name: 'Nike shoe',
    price:'35000',
    stock_count: 1
  }
'''


class InventoryItem():
    name: str
    price: str
    stock_count: str

    def __init__(self, name, price, stock_count) -> None:
        self.name = name
        self.price = price
        self.stock_count = stock_count

    def convert_to_string(self, index) -> None:
        print(
            f'Item {index}\n'
            f'Name{self.name}\n'
            f'Price {self.price}\n'
            f'Stock count {self.stock_count}\n'
        )


inventory_items: list[InventoryItem] = []

inventory_options = [
    '1. View all items',
    '2. Add a new item',
    '3. Update item',
    '4. Delete item',
    '5. Exit',
]


print('Welcome to my shop.')


def greet_user():
    print(
        f'What would you like to do?\n{'\n'.join(inventory_options)}\n'
    )
    user_selection = input('Select an option: ')
    if user_selection == '1':
        return view_all_items()
    elif user_selection == '2':
        return add_item()
    elif user_selection == '3':
        return update_item_stock()
    elif user_selection == '4':
        return delete_item()
    elif user_selection == '5':
        print('Thank you for shopping with us')
        return
    else:
        print('Invalid input, kindly select a number')
        return greet_user()


def view_all_items():
    print('Here is a list of all items in your inventory\n')
    for index, item in enumerate(inventory_items):
        print(item.convert_to_string(index))
    return greet_user()


def add_item():
    item_name = input('Please provide the name of the item you want to add:')
    item_price = input('How much does this item cost?:')
    stock = input('How much stock is currently available?:')

    inventory_items.append(InventoryItem(
        name=item_name, price=item_price, stock_count=stock
    ))

    print(f'{item_name} has been successfully added to your inventory\n')
    return view_all_items()


def update_item_stock():

    list_all_inventory_items()

    selected_index = int(input('Select the item you want to update'))

    updated_name = input("Set a new name for this item (Press N to skip):")
    updated_price = input('Set a new price for this item (Press N to skip):')
    updated_stock = input(
        'Set the stock count for this item (Press N to skip):')

    if updated_name != 'N'.lower():
        inventory_items[selected_index].name = updated_name

    if updated_stock != 'N'.lower():
        inventory_items[selected_index].stock_count = updated_stock

    if updated_price != 'N'.lower():
        inventory_items[selected_index].price = updated_price

    return view_all_items()


def delete_item():
    list_all_inventory_items()

    selected_index = int(input('Select the item you want to delete'))

    del inventory_items[selected_index]

    print("Your item has been deleted successfully")

    return view_all_items()


def list_all_inventory_items():
    for index, item in enumerate(inventory_items):
        print(f'{index}. {item.name}')


greet_user()
