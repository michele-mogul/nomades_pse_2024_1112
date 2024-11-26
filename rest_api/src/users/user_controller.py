from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from rest_api.src.users.dto.request import UserQueryArgsSchema, UserDataUpdateRequestSchema, UserDataCreateRequestSchema
from rest_api.src.users.dto.response import UserDataResponseSchema, UserListDataResponseSchema
from rest_api.src.users.user import User as UserModel
from rest_api.src.users.user_repository import UserRepository

user_blp = Blueprint("user", "user", url_prefix="/user", description="Operations on user")

class ItemNotFoundError(Exception):
    pass


@user_blp.route("/<user_id>")
class UserById(MethodView):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__()

    @user_blp.arguments(UserQueryArgsSchema, location="query")
    @user_blp.response(200, UserDataResponseSchema)
    def get(self, user_id):
        """
        :param user_id: The unique identifier of the user to retrieve.
        :return: The user object if found, otherwise raises a 404 error if the user is not found.
        """
        try:
            item = self.repository.get_user(user_id)
            return item
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @user_blp.arguments(UserDataUpdateRequestSchema)
    @user_blp.response(200, UserDataResponseSchema)
    def put(self, update_data, user_id):
        """
        :param update_data: Dictionary containing the data to update the user with.
        :param user_id: ID of the user to be updated.
        :return: Updated user object if update is successful, otherwise raises an error if the user is not found.
        """
        try:
            item = self.repository.get_user(user_id)
            item.update(update_data)
            self.repository.update_user(item)
            return item
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @user_blp.arguments(UserDataUpdateRequestSchema)
    @user_blp.response(200, UserDataResponseSchema)
    def post(self, update_data, user_id):
        """
        :param update_data: Dictionary containing the data to update the user with.
        :param user_id: ID of the user to be updated.
        :return: Updated user object if update is successful, otherwise raises an error if the user is not found.
        """
        try:
            new_user = User.from_dict(update_data)
            return self.repository.create_user(new_user)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @user_blp.response(204)
    def delete(self, user_id):
        """
        :param user_id: The unique identifier of the user to be deleted.
        :return: None. A 204 No Content status code indicates successful deletion.

        """
        try:
            self.repository.delete_user(user_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@user_blp.route("/")
class User(MethodView):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__()

    @user_blp.arguments(UserDataCreateRequestSchema)
    @user_blp.response(200, UserDataResponseSchema)
    def post(self, update_data):
        """
        :param update_data: Dictionary containing the data to update the user with.
        :param user_id: ID of the user to be updated.
        :return: Updated user object if update is successful, otherwise raises an error if the user is not found.
        """
        try:
            new_user = UserModel.from_dict(update_data)
            return self.repository.create_user(new_user)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@user_blp.route("/get_all_users")
class GetAllUsers(MethodView):
    def __init__(self):
        self.repository = UserRepository()
        super().__init__()

    @user_blp.response(200, UserListDataResponseSchema)
    def post(self, update_data):
        """
        :param update_data: Dictionary containing the data to update the user with.
        :param user_id: ID of the user to be updated.
        :return: Updated user object if update is successful, otherwise raises an error if the user is not found.
        """
        try:
            new_user = UserModel.from_dict(update_data)
            return self.repository.create_user(new_user)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
