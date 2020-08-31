
from odoo import fields,models, api

class Partner (models.Model):
    _inherit = 'res.partner'

    #add field to check if it is instructor or not
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('my_module.session', string="Attended Sessions", readonly=True)