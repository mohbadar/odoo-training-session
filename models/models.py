# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = "my_module.course"
    _description = "Course Table"

    name = fields.Char(required=True, string="Title")
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete="set null", string="Responsible", index=True)
    session_ids = fields.One2many('my_module.session', 'course_id', string="Sessions")


class Session(models.Model):
    _name = "my_module.session"
    _description = "Session Table"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(help="Number of seats")
    description = fields.Text()
    course_id = fields.Many2one('my_module.course', ondelete="set null", string="Course ", index=True)
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    attendee_ids = fields.Many2many('res.partner',string="Attendees")