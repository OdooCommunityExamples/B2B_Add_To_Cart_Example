{
    'name': 'B2B Add To Cart Example',
    'description': 'This module is in answer to Tiberius Onerous's question here:
https://www.odoo.com/forum/help-1/question/how-to-remove-pricing-for-not-logged-in-users-on-e-commerce-website-for-distributor-business-to-business-sales-52924',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch',
    'depends': ['product','sale','website_sale'],
    'data': [
        'views/B2B_Add_To_Cart.xml',
    ],
    'application': True,
}
