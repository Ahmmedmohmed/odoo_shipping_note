from odoo import models, fields

class ShippingNote(models.Model):
    _name = 'custom.shipping.note'
    _description = 'Shipping Note'

    name = fields.Char(string="Reference")
    description = fields.Text(string="Description")