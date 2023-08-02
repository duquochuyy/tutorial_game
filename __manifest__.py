# -*- coding: utf-8 -*-
{
    'name': "Tutorial Application By Huy",

    'summary': "Tutorial Application",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        "security/tutorial_security.xml",
        "security/ir.model.access.csv",
        "views/game_view.xml",
        "views/menu_view.xml",
        "views/game_list_template.xml",
    ],
    "application": True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
