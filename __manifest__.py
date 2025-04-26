{
    'name': 'Custom Shipping Note',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Adds custom shipping note field to sale and invoice lines',
    'author': 'Ahmed Developer',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'security/ir.model.access.csv',
     #   'views/shipping_note_views.xml',
    ],
    'installable': True,
    'application': False,
}
