{
    'name': 'Employee Activity Report',
    'version': '1.0',
    'summary': 'Module for tracking employee activities across various modules',
    'author': 'SON ',
    'category': 'Human Resources',
    'depends': [
        'base',
        'hr',
        'sale',
        'purchase',
        'crm',
        'calendar',
        'hr_expense'],
    'data': [
        'security/employee_activity_security.xml',
        'security/ir.model.access.csv',
        'views/employee_activity_views.xml',
        'views/employee_activity_menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
