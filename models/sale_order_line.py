from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_shipping_note = fields.Char(string="Shipping Note")

    def _prepare_invoice_line(self, line):
        res = super()._prepare_invoice_line(line)
        res['shipping_note'] = line.shipping_note
        return res