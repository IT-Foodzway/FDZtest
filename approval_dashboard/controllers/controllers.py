# -*- coding: utf-8 -*-
# from odoo import http


# class ApprovalDashboard(http.Controller):
#     @http.route('/approval_dashboard/approval_dashboard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approval_dashboard/approval_dashboard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('approval_dashboard.listing', {
#             'root': '/approval_dashboard/approval_dashboard',
#             'objects': http.request.env['approval_dashboard.approval_dashboard'].search([]),
#         })

#     @http.route('/approval_dashboard/approval_dashboard/objects/<model("approval_dashboard.approval_dashboard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approval_dashboard.object', {
#             'object': obj
#         })
