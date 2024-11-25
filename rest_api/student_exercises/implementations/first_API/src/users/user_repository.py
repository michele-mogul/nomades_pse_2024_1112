"""
Repository for User using firebase database
"""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.firestore_database import db, DocumentReference, DocumentSnapshot

from user import User

class UserRepository():
  def __init__(self):
    self.collection = db.collection('users')
  
  def get_all(self) -> list[User]:
    users: list[User] = []
    for user in self.collection.get():
      user_data: dict = user.to_dict()
      user_data.update({"id": user.id})
      u: User = User.from_dict(user_data)
      # u.id = user.id
      users.append(u)
    return users
  
  def get_one(self, id: str) -> User:
    user_query: DocumentSnapshot = self.collection.document(id).get()

    if not user_query.exists:
      raise ValueError(f"User with id {id} not found")
    
    return User.from_dict(user_query.to_dict())
  
  
  def add_user(self, user: User) -> User:
    """
    Insert a user in the database
    Note that, the received user in parameters doesn't have an id
    The id should be added to the retunred user after the creation in the database
    This function should check that the user is fully complete (no class attributes with "")

    Args:
        user (User): The user to add in database (without id)
    
    Returns:
        User: The user with the id added
    """
    pass

  def update_user(self, user: User) -> User:
    """
    Update a user in the database, the user in parameters contains the id
    The user in parameters has some values set to "" these bvalues are not to be udpated

    Args:
        user (User): The user to update in database

    Raises:
        ValueError: If the user doesn't exist

    Returns:
        User: The user updated
    """
  
    pass

  def delete_user(self, id: str) -> None:
    pass

  def get_user_by_username(self, username: str) -> User:
    pass