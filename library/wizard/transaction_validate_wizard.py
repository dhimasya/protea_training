from odoo import api, fields, models


class TransactionValidateWizard(models.TransientModel):
    _name = 'transaction.validate.wizard'
    _description = 'validate wizard'

    transaction_id = fields.Many2one('transaction')

    @api.model
    def default_get(self, fields):
        res = super(TransactionValidateWizard, self).default_get(fields)
        res['transaction_id'] = self._context.get('active_id')
        return res
    
    def action_validate(self):
        print(self.transaction_id)
        self.transaction_id.action_validate()