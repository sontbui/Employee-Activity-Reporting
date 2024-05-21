{
    'name': 'Employee DashBoard',
    'version': '1.0',
    'summary': 'Module for tracking employee activities across various modules',
    'author': 'SON',
    'category': 'Human Resources',
    'depends': [
        'base',
        'hr',
        'sale',
        'purchase',
        'crm',
        'calendar',
        'hr_expense'
    ],
    'data': [

        'views/employee_activity_views.xml',
        'views/employee_activity_menu.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
