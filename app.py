from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Use your Oracle Cloud username, password, and the TNS name from the tnsnames.ora file in the unzipped wallet.
connection_string = "ADMIN/***@project_medium"
conn = cx_Oracle.connect(connection_string)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT product_name, product_type, quantity FROM inventory")
    inventory_data = cursor.fetchall()
    formatted_inventory = [{"product_name": item[0], "product_type": item[1], "quantity": item[2]} for item in inventory_data]
    return render_template('index.html', inventory_data=formatted_inventory)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        quantity = request.form['quantity']

        sql = "INSERT INTO inventory (product_name, product_type, quantity) VALUES (:1, :2, :3)"
        cursor.execute(sql, (product_name, product_type, quantity))
        conn.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    # For simplicity, I'm not including this functionality now as it's a bit more complex with the database.
    # This would require fetching the current item from the database, presenting it in an HTML form,
    # then updating the database based on user input.
    pass

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    # Similarly, this requires more logic to handle deletion from the database. 
    # Typically, this would involve a SQL DELETE command based on a primary key (id) for the item.
    pass

@app.route('/change_quantity/<int:item_id>/<int:quantity_change>', methods=['POST'])
def change_quantity(item_id, quantity_change):
    # This would also require more logic with the database, involving a SQL UPDATE command.
    pass

@app.teardown_appcontext
def shutdown_session(exception=None):
    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
