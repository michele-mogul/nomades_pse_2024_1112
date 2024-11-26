class User():
    """
        class User():

        Represents a user object with various attributes such as id, firstname, lastname, username, email, password, and salt.

        Attributes:
            id (str): The user's unique identifier.
            firstname (str): The user's first name.
            lastname (str): The user's last name.
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.
            salt (str): The salt used for hashing the user's password.
    """

    def __init__(self, id: str, firstname: str, lastname: str, username: str, email: str, password: str, salt: str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self) -> str:
        return f"{self.to_dict()}"

    def __str__(self) -> str:
        return self.__repr__()

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "fullname": f"{self.firstname} {self.lastname}",
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "salt": self.salt
        }

    @staticmethod
    def from_dict(data: dict) -> "User":
        return User(
            id=data["id"] if "id" in data else None,
            firstname=data["firstname"],
            lastname=data["lastname"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
            salt=data["salt"]
        )

    def update(self, data: dict) -> None:
        for key, value in data.items():
            setattr(self, key, value)


if __name__ == "__main__":
    user = User(
        id="123",
        firstname="John",
        lastname="Doe",
        username="johndoe",
        email="<EMAIL>",
        password="<PASSWORD>",
        salt="1234567890"
    )
    print(user)
