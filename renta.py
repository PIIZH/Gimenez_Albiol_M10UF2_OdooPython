# -*- coding: utf-8 -*-

from openerp import models, fields, api

class renta(models.Model):
     _name = 'renta.renta'
     _salaryB = 'renta.salary'
   
     name = fields.Char(string = "DNI de la persona que realitza la renta: ", required = True) 
     salaryB = fields.Float(string = "Salari brut mensual: ", required = True) 
          
     children = fields.Integer(string = "Número de fills ", required = False) 
     parent = fields.Boolean(string = "Tens alguna ancia residint en el teu domicili? ", default = False)
     
     childrenDown = fields.Boolean(string = "Tens fills amb discapacitats? ", default = False) 
     
     result = fields.Float(string = "Resultat del cálcul: ", default = 0, readonly = True) 
     
     @api.one
     def calcRenta(self):
		 _percentNorm = 1 
		 _cashFills = 0
		 _disca = 0
		 if len(self.name)!=9:
			self.name = "DNI mal introduit"
			 
		 elif (self.salaryB *14)> 0 and (self.salaryB *14)<12451:
			_percentNorm = 19.5
		 
		 elif (self.salaryB *14)> 12451 and (self.salaryB *14) < 20200:
			_percentNorm = 24.5
		 
		 elif(self.salaryB *14) > 20201 and(self.salaryB *14) < 35200:
			_percentNorm = 30.5
		 
		 elif (self.salaryB *14) > 35201 and (self.salaryB *14) < 60000:
			_percentNorm = 38
		 
		 elif (self.salaryB *14) > 60001:
			_percentNorm = 46
		 
		 if self.children >= 5:
			_cashFills = 5*150
		 
		 else:
			_cashFills = self.children*150
		 
		 if self.parent and (self.salaryB*14)<24020:
			 _percentNorm -= 10.05
		
		 if self.childrenDown and (self.salaryB*14)>=30000:
			_disca = 300
		 
		 else: 
			_percentNorm -= 10
		 	
		 self.result = format(((self.salaryB *14)-(_percentNorm*(self.salaryB *14))/100)+_cashFills+_disca,'.0f') 
		
					
					
		 
