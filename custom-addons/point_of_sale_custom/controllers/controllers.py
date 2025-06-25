# -*- coding: utf-8 -*-
# from odoo import http


# class PointOfSaleCustom(http.Controller):
#     @http.route('/point_of_sale_custom/point_of_sale_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/point_of_sale_custom/point_of_sale_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('point_of_sale_custom.listing', {
#             'root': '/point_of_sale_custom/point_of_sale_custom',
#             'objects': http.request.env['point_of_sale_custom.point_of_sale_custom'].search([]),
#         })

#     @http.route('/point_of_sale_custom/point_of_sale_custom/objects/<model("point_of_sale_custom.point_of_sale_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('point_of_sale_custom.object', {
#             'object': obj
#         })

