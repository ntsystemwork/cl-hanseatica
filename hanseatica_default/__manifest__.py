# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019 NT System Work (http://www.ntsystemwork.com)
#    All Rights Reserved.
#
# -----------------------------------------------------------------------------
{
    'name': 'hanseatica',
    'version': '12.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para hanseatica',
    'author': 'NT System Work',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        # si es enterprise poner standard_depends_ee si es community standard_depends_ce
        'standard_depends_xx',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # --------------------------------------------

    # port where odoo starts serving pages
    'port': '8069',
    'repos': [
        {'usr': 'ntsystemwork', 'repo': 'cl-hanseatica', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-odoo-argentina', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-sale', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
         'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
         'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-sale', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-odoo-support', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-partner-contact', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-web', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-tools', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-social', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-brand', 'branch': '12.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-ux', 'branch': '12.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '12.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],

}

