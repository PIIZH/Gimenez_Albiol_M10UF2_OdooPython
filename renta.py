# -*- coding: utf-8 -*-

from openerp import models, fields, api

class renta(models.Model):
     _name = 'renta.renta'
     _salaryB = 'renta.salary'

     name = fields.Char(string = "DNI de la persona que realitza la renta: ", required = True)
     salaryB = fields.Float(string = "Salari brut mensual: ", required = True) # salari brut mensual - Float
     children = fields.Integer(string = "Quants fills tens: ", required = True) # fills totals - Integer
     childrenUp = fields.Boolean(string = "Tens fills majors d'edat dependents? ", default = False) # fills majors edat - Boolean
     childrenDown = fields.Boolean(string = "Tens fills amb discapacitats? ", default = False) # fills amb descapacitat - Boolean
     parent = fields.Boolean(string = "Tens pares dependents? ", default = False, comput="calcSalaryAnual") # pares que son dependents - Boolean
     
     
     @api.one
     def calcSalaryAnual():
		 salaryB = 4000
		 return null
