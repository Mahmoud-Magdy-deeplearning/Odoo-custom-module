# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'trial.wizard'
    _description = 'trial.wizard is a  simple wizard'

    def _default_session(self):
        return sef.env['trial.session'].browse(self.context.get('active_id'))

    name = fields.Char()
    description = fields.Text()
    session_id = fields.Many2one('trial.session', string="Session", required=True)
    course_id = fields.Many2one('trial.course', ondelete='set null', string="Course name")
