from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Counter variable to generate sequential user IDs
user_counter = 1

# Function to encrypt the password using the Caesar shift
def encrypt_password(password):
    encrypted_password = ''.join(chr(ord(char) + 1) for char in password)
    return encrypted_password

# Saves user registration details to users.txt
def save_user_registration(name, email, password):
    global user_counter
    # Encrypt the password before saving
    encrypted_password = encrypt_password(password)
    user_data = {
        'id': user_counter,
        'name': name,
        'email': email,
        'password': encrypted_password
    }
    # Append user data to users.txt
    with open('users.txt', 'a') as file:
        file.write(json.dumps(user_data) + '\n')
    # Increment the counter for the next user
    user_counter += 1
    # Return the generated user_id
    return user_data['id']

# Retrieves user registration details based on email
def get_user_by_email(user_email):
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data.get('email') == user_email:
                return user_data

    return None  # If user not found

@app.route('/', methods=['GET', 'POST'])
def registration_page():
    message = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Save user registration details and get the generated user_id
        user_id = save_user_registration(name, email, password)
        message = "User added successfully!"
    # Render the registration form with the message
    return render_template('registration.html', message=message)

@app.route('/user/<user_email>')
def user_details(user_email):
    user_data = get_user_by_email(user_email)
    if user_data:
        # Display encrypted password
        return render_template('user_details.html', user_data=user_data)
    else:
        return "User not found."

if __name__ == '__main__':
    app.run()
