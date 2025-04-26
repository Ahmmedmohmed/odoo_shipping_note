from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    x_shipping_note = fields.Char(string="Shipping Note")
