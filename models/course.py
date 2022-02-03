# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Course(models.Model):
    _name = 'trial.course'
    _description = 'trial.course is a model in trial module'

    name = fields.Char()
    value = fields.Integer(string="attendees")
    description = fields.Text()
    session_ids = fields.One2many('trial.session', 'course_id', string="sessions" )
    value2 = fields.Integer(computer="_value_pc")
    _sql_constraints = [
        ('name_description_CHECK',
         'CHECK(name!=description)',
         'Name and description should not be the same'),
        ('name_UNIQUE_CHECK',
         'UNIQUE(name)',
         'name should be unique'
         )
    ]

    # sql constraint will be assigned in postgres and you can not remove it in future
    # you can replace it by python constraint like
    '''
         @api.constrains('date_end')
         def _check_date_end(self):
             for record in self:
                 if record.date_end < fields.Date.today():
                     raise ValidationError("The end date cannot be set in the past")
             all records passed the test, don't return anything
    '''
    # or you can change 2nd item in every tuple to --> CHECK(1=1)


# act as event listener
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

