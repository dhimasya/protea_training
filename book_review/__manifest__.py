{
    'name': 'Book Review',
    'version': '1.0',
    'description': 'Book Review Addons',
    'summary': 'Book Review Function',
    'author': 'Portcities, Ltd',
    'website': 'https://portcities.net',
    'license': 'LGPL-3',
    'category': 'Library',
    'depends': [
        'base',
        'library',
    ],
    'data': [
        'data/ir_cron.xml',
        'security/ir.model.access.csv',
        'views/book_review_views.xml',
        'views/book_views.xml',
    ],
    'auto_install': False,
    'application': False,
}