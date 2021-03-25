from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import UserError


class Transaction(models.Model):
    _name = 'transaction'
    _description = 'book transaction'

    name = fields.Char('Number')
    date = fields.Date(default=datetime.now())
    book_id = fields.Many2one('book')
    partner_id = fields.Many2one('res.partner')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], default='draft')


    @api.model
    def create(self, vals):
        res = super(Transaction, self).create(vals)
        res.check_value()
        return res

    def write(self, vals):
        res = super(Transaction, self).write(vals)
        self.check_value()
        return res

    def unlink(self):
        if self.state == 'done':
            raise UserError('Failed to remove the transaction, already done')
        res = super(Transaction, self).unlink()
        return res

    def check_value(self):
        if not self.name:
            raise UserError('Failed to save transaction, Number is emtpy')
        if not self.date:
            raise UserError('Failed to save transaction, Date is emtpy')
        if not self.book_id:
            raise UserError('Failed to save transaction, Book is emtpy')
        if not self.partner_id:
            raise UserError('Failed to save transaction, Partner is emtpy')

    def action_validate(self):
        view_id = self.env.ref('library.transaction_validate_wizard_view_form').id
        return {'type': 'ir.actions.act_window',
                'name': 'Validate',
                'res_model': 'transaction.validate.wizard',
                'target': 'new',
                'view_mode': 'form',
                'views': [[view_id, 'form']],
                'context': self._context,
        }

    def _action_validate(self):
        self.env['transaction.history'].create({
            'transaction_id': self.id,
            'book_id': self.book_id.id,
            'date': self.date,
        })
        self.state = 'done'
        return True

    def action_print(self):
        act = self.env.ref('library.transaction_report_action').report_action(self)
        return act
