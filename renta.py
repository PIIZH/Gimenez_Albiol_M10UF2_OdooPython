# -*- coding: utf-8 -*-

from openerp import models, fields, api

class renta(models.Model):
     _name = 'renta.renta'
     _salaryB = 'renta.salary'

     dni = fields.Char(string = "DNI de la persona que realitza la renta: ", required = True) # DNI - String
     salaryB = fields.Float(string = "Salari brut mensual: ", required = True) # salari brut mensual - Float
     #valueIM = fields.Float(string = "Valor immobiliari: ", required = True) # valor immobiliari
     #valueMB = fields.Float(string = "Valor mobiliari: ", required = True) # valor mobiliari
     
     #stateAlone = fields.Boolean(string = "Solter/a ", required = False, default = True)
     #stateMarried = fields.Boolean(string = "Casat/ada ", required = False)
     #stateDead = fields.Boolean(string = "Vidu/a ", required = False)
     
     #children = fields.Integer(string = "Fills menors a 3 anys: ", required = False) # fills < 3 - Integer
     #childrenOld = fields.Integer(string = "Fills igual o majors a 3 anys: ", required = False) # fills >= 3 - Integer
     #parent = fields.Integer(string = "Pares majors de 56 ", default = False) # pares > 56 - Integer
     #parentOld = fields.Integer(string = "Pares majors de 76 ", default = False) # pares > 76 - Integer
     
     # childrenDown = fields.Boolean(string = "Tens fills amb discapacitats? ", default = False) # fills amb discapacitat - Boolean
     
     
     @api.one
     def calcSalaryAnual(self):
		 self.dni = 'test'
