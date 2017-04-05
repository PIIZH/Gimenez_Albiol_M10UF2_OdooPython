# -*- coding: utf-8 -*-
{
    'name': "renta",

    'summary': """
        Calcula la renta d'una persona""",

    'description': """
        Modul dedicat al calcul de la renta per una persona en base a uns parámetres
    """,

    'author': "Gerard Albiol y Miquel Giménez",
    'website': "www.travisy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/renta.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'aplication': True,
}
