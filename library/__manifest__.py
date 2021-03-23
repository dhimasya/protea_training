{
    'name': 'Library',
    'version': '1.0',
    'description': 'Library Management',
    'summary': 'Library management',
    'author': 'Portcities, Ltd',
    'website': 'https://portcities.net',
    'license': 'LGPL-3',
    'category': 'Library',
    'depends': [
        'base',
        'board',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/transaction_views.xml',
        'views/transaction_history_views.xml',
        'wizard/transaction_validate_wizard_views.xml',
        'views/book_board.xml',
    ],
    'auto_install': False,
    'application': True,
}