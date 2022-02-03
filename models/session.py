# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'trial.session'
    _description = 'trial.session is a model in trial module'
    name = fields.Char()
    description = fields.Text()
    course_id = fields.Many2one('trial.course', ondelete='set null', string="Course name")

