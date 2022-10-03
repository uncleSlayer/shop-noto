from flask import request, jsonify, session
from shop import app, db


# signup api
@app.route('/signup-info', methods = ['POST'])
def signup():

    from shop import bcrypt
    from shop.database.model import Users

    resp = request.get_json()

    name = resp['username']
    email_id = resp['emailId']
    password = resp['password']
    repassword = resp['password']

    if password == repassword:

        pw_hash = bcrypt.generate_password_hash(password)

        if Users.query.filter(Users.email == email_id).first():
            print('does not look good')
        else:
            try:
                user = Users(username = name, email = email_id, password_hash = pw_hash)
                db.session.add(user)
                db.session.commit()

                print('things done')

                try:
                    return jsonify({
                    'message': 'signup successful. redirecting to the loign route.'
                })

                except Exception as e:
                    return jsonify({
                        'message': e
                    })

            except Exception as e:
                print(e)

# login api
@app.route('/login-info', methods = ['post'])
def login():
    from shop.database.model import Users

    resp = request.get_json()

    email = resp['email']
    password = resp['password']

    user_hashed_pass = Users.query.filter(Users.email == email).first().password_hash

    if password == user_hashed_pass:
        session['is_logged_in'] = True
    else:
        return jsonify({
            'message': 'password did not match'
        })

    # token = 

    return jsonify({
        'message': 'login data sent to back end. verification pending.'
    })