[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LOFF_BgH)

# Flask User Registration System

This Flask application implements a user registration system with basic encryption for passwords.

## Assumptions

1. **Encryption Method:** Passwords are encrypted using a Caesar shift (Caesar cipher) with a fixed shift value. Could have implemented SHA256 encryption which is safer but stuck with Caesar shift.

2. **User Routing:** User details are accessed based on the user's email. The route `/user/<user_email>` retrieves and displays user details based on the provided email.