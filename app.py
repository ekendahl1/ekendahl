from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define your inventory data (e.g., as a list of dictionaries)
inventory_data = [
    {"product_name": "Shoes", "product_type": "Footwear", "quantity": 10},
    {"product_name": "Pants", "product_type": "Apparel", "quantity": 15},
    # Add more inventory items here
]

# Debug print to check the contents of inventory_data
print("Inventory Data:", inventory_data)

@app.route('/')
def index():
    print("Rendering index.html with inventory data:", inventory_data)
    return render_template('index.html', inventory_data=inventory_data)

# Add routes and functions for adding, editing, and deleting items here

# Function to add a new item to the inventory
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Get values from the form
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        quantity = request.form['quantity']

        # Create a dictionary for the new item
        new_item = {
            "product_name": product_name,
            "product_type": product_type,
            "quantity": quantity
        }

        # Append the new item to the inventory_data list
        inventory_data.append(new_item)

        # Redirect back to the homepage (or inventory list)
        return redirect(url_for('index'))

    return render_template('add.html')  # Create an HTML template for the "Add Item" form

# Function to edit an existing item in the inventory
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if request.method == 'POST':
        # Get values from the form
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        quantity = request.form['quantity']

        # Update the item in the inventory_data list
        inventory_data[item_id]['product_name'] = product_name
        inventory_data[item_id]['product_type'] = product_type
        inventory_data[item_id]['quantity'] = quantity

        # Redirect back to the homepage (or inventory list)
        return redirect(url_for('index'))

    return render_template('edit.html', item=inventory_data[item_id])  # Create an HTML template for the "Edit Item" form

# Function to delete an item from the inventory
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    # Remove the item from the inventory_data list
    del inventory_data[item_id]

    # Redirect back to the homepage (or inventory list)
    return redirect(url_for('index'))

# Function to handle changes in inventory quantity
@app.route('/change_quantity/<int:item_id>/<int:quantity_change>', methods=['POST'])
def change_quantity(item_id, quantity_change):
    # Change the quantity of the item in the inventory_data list
    inventory_data[item_id]['quantity'] += quantity_change

    # Redirect back to the homepage (or inventory list)
    return redirect(url_for('index'))

