from google.cloud.firestore_v1 import DocumentSnapshot

from rest_api.config.firestore_database import db
from rest_api.src.users.user import User


class UserRepository:
    """
        class UserRepository:
        A repository class for managing user documents in a database collection.
    """

    def __init__(self):
        self.collection = db.collection('users')

    def get_user(self, user_id) -> User | None:
        """
        :param user_id: The unique identifier of the user to retrieve
        :return: A User object if the user exists, otherwise None
        :raises ValueError: If the user with the specified ID does not exist
        """
        user_snapshot: DocumentSnapshot = self.collection.document(user_id).get()
        if not user_snapshot.exists:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return User.from_dict(user_snapshot.to_dict())

    def get_all_users(self) -> list[User]:
        """
        Fetches all User documents from the collection and converts them to User objects.

        :return: A list of User objects retrieved from the collection.
        """
        return [User.from_dict(doc.to_dict()) for doc in self.collection.stream()]

    def create_user(self, user: User) -> User:
        """
        Creates an user document in the database collection.
        :param user: User object containing user details to be added to the database
        :return: User object that was added to the database
        """

        return self.collection.document().create(user.to_dict())

    def update_user(self, user: User) -> User:
        """
        Updates an user document in the database collection.
        :param user: User object to be updated in the collection
        :return: The result of the set operation which writes the user's updated data to the document
        """
        return self.collection.document(user.id).set(user.to_dict())

    def delete_user(self, user_id) -> None:
        """
        Deletes an user document from the database collection.
        :param user_id: The unique identifier of the user to be deleted.
        :return: None
        """
        self.collection.document(user_id).delete()


if __name__ == "__main__":
    print(
        UserRepository().get_all_users()
    )
