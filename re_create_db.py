from app import db, app

try:
    input("CONFIRM? [Enter To Confirm] \n >> ")
    with app.app_context():
        db.drop_all()
        db.create_all()

except Exception as _:
    print(_)
