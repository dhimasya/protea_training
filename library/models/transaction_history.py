from datetime import datetime

from odoo import fields, models


class TransactionHistory(models.Model):
    _name = 'transaction.history'
    _description = 'book transaction'

    transaction_id = fields.Many2one('transaction')
    name = fields.Char(related='transaction_id.name', store=True)
    date = fields.Date()
    book_id = fields.Many2one('book')
