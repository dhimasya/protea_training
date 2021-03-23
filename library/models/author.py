from odoo import _, api, fields, models

class Author(models.Model):
    _name = 'author'
    _description = 'Author'

    name = fields.Char()


    