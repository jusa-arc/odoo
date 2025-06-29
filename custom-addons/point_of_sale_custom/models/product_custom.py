from odoo import models, fields

class ProductTemplateLibrary(models.Model):
    _inherit = 'product.template'

    # custom para libreria
    autor = fields.Char(string='Autor', required=False)
    editorial = fields.Char(string='Editorial', required=False)
    isbn = fields.Char(string='ISBN', required=False)
    clave_sat = fields.Char(string="clave SAT", required=False)