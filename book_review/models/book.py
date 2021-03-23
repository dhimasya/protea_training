from odoo import fields, models


class Book(models.Model):
    _inherit = 'book'

    review_ids = fields.One2many('book.review', 'book_id')