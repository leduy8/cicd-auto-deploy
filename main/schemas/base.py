from marshmallow import EXCLUDE, Schema, fields


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class PaginationSchema(BaseSchema):
    page_size = fields.Integer()
    page = fields.Integer()
    total = fields.Integer()
