from marshmallow import Schema, fields


class UserQueryArgsSchema(Schema):
    user_id = fields.String()


class UserDataCreateRequestSchema(Schema):
    email = fields.String()
    username = fields.String()
    firstname = fields.String()
    lastname = fields.String()


class UserDataUpdateRequestSchema(UserDataCreateRequestSchema):
    id = fields.Int()
