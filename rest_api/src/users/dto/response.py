from marshmallow import Schema, fields


class UserResponseSchema(Schema):
    id = fields.Int()
    username = fields.String()


class UserDataResponseSchema(UserResponseSchema):
    email = fields.String()
    firstname = fields.String()
    lastname = fields.String()


class UserListResponseSchema(Schema):
    users = fields.Nested(UserResponseSchema, many=True)


class UserListDataResponseSchema(Schema):
    users = fields.Nested(UserDataResponseSchema, many=True)
