from odoo import models, fields

class ProductTemplateLibrary(models.Model):
    _inherit = 'product.template'

    # custom para libreria
    isbn = fields.Char(string='ISBN', required=False)