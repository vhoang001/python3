from flask import Flask, render_template

app = Flask(__name__)

# Assuming you have a list of pets in a variable called `pets`
pets = [
    {'name': 'Fido', 'image': 'fido.jpg', 'fact': 'Fido loves to fetch!'},
    # Add more pets here
]

@app.route('/pets/<int:index>')
def show_pet(index):
    pet = pets[index]
    return render_template('show_pet.html', pet=pet)

flask run --reload
