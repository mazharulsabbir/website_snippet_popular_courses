from odoo import models, fields, api, _


class CustomAttendee(models.Model):
    _inherit = 'slide.channel'

    members_count = fields.Integer('Attendees count', compute='_compute_members_count', store=True)
