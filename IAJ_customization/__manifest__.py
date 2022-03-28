# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'IAJ-customization',
    'version': '12.0.1.0.0',
    'author': 'PESOL','CRITEAN'
    'website': 'http://pesol.es','http://www.critean.com'
    'category': 'Custom',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'crm',
        'partner_contact_gender',
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/crm_lead_view.xml',
    ],
    'installable': True,
}
