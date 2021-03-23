from odoo import _, api, fields, models

class Book(models.Model):
    _name = 'book'
    _description = 'Book'
    # _rec_name = 'alt_name'

    # alt_name = fields.Char()
    name = fields.Char()
    author_id = fields.Many2one('author')
    page_count = fields.Integer()
    edition = fields.Integer()
    isbn = fields.Char()


    