import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import DocumentReference

cred = credentials.Certificate("./pse-2024-1112-firebase-adminsdk-2ei3u-f102112b1d.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def __get_user_document(uid) -> DocumentReference:
    return db.collection('users').document(uid)


def user_exists(uid) -> bool:
    return __get_user_document(uid).get().exists


def read_users() -> list[dict]:
    return [user.to_dict() for user in db.collection('users').stream()]


def read_user(uid) -> dict:
    return __get_user_document(uid).get().to_dict()


def write_user(uid, pwd, salt) -> None:
    __get_user_document(uid).set(document_data={'uid': uid, 'pwd': pwd, 'salt': salt, 'test2': 2})


def delete_user(uid) -> None:
    if user_exists(uid):
        db.collection('users').document(uid).delete()


def update_user(uid, pwd, salt) -> None:
    user = __get_user_document(uid)
    if user.get().exists:
        __get_user_document(uid).update({'pwd': pwd, 'salt': salt})


if __name__ == '__main__':
    print(write_user('asasdasdas', 'asdasdasd', 'asdasdasd'))
