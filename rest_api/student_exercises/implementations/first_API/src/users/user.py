class User():
  def __init__(self, 
               id: str = "",
               firstname: str = "",
               lastname: str = "",
               username: str = "",
               password: str = "",
               salt: str = ""
  ) -> None:
    self.id = id # firebase str id
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password
    self.salt = salt 
  
  @staticmethod
  def from_dict(data: dict[str, str]) -> "User":
    return User(
      id=data.get("id", ""),
      firstname=data.get("firstname", ""),
      lastname=data.get("lastname", ""),
      username=data.get("username", ""),
      password=data.get("password", ""),
      salt=data.get("salt", "")
    )
  
  def __repr__(self) -> str:
    return f"<User {self.username}>"

  def __str__(self) -> str:
    return self.__repr__()
  
  def to_dict(self) -> dict[str, str]:
    return {
      "id": self.id,
      "firstname": self.firstname,
      "lastname": self.lastname,
      "username": self.username,
      "password": self.password,
      "salt": self.salt
    }
