# -*- coding: utf-8 -*-
{
    'name': "Game Category",
    'summary': """Tutorial, Extended""",
    'author': "vyngt",
    'website': "https://www.mysite.com",

    'category': 'Services/Game',
    'version': '3.9',
    'depends': ['tutorial'],

    'data': [
        'security/ir.model.access.csv',
        'views/tag_view.xml',
        'views/game_view.xml',
        'views/menu_view.xml',
        'views/game_list_template.xml',
    ],
    'application': 'False',
}