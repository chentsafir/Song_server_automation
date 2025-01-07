from infra import crud_api
api = crud_api.CrudApi()


def send_add_user(user):
    user.prepare_for_add_user - >מנקה את כל השדות שלא רלונטיים ליירת יוסר , רק זמנית לפני השליחה לא משפיע על קלאס עצמו (לא חייב כרגע - זה ללימוד והבנה)
    r = api.post(endpoint="/users/add_user",data=user.to_json())
    return r