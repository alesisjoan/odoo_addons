# -*- coding: utf-8 -*-
# (C) 2013 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Assets Management",
    "version": "0.2",
    "license": 'AGPL-3',
    "depends": [
        "account",
    ],
    "author": "Smile",
    "description": """Financial and accounting asset management

This module allows to manage:
* assets and categories
* decomposable assets
* amortizations (ie periodic depreciations) and depreciations (exceptional)
* accounting and fiscal depreciation methods
* assets sale/scrapping
* out of heritage
* asset decomposition
* asset modification
* reporting
* transfer depreciation in amortization (French law)

WARNING: This module is not compatible with account_asset, so uninstall it
before installing this one.

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
    """,
    "website": "http://www.smile.fr",
    "category": "Accounting & Finance",
    "sequence": 32,
    "data": [
        "security/account_asset_security.xml",
        "security/ir.model.access.csv",

        "data/account_asset_depreciation_methods.xml",
        "data/account_asset_sequence.xml",

        "views/account_asset_depreciation_method_view.xml",
        "views/account_asset_category_view.xml",
        "views/account_asset_depreciation_line_view.xml",
        "views/account_asset_history_view.xml",
        "views/account_asset_asset_view.xml",
        "views/account_invoice_line_view.xml",
        "views/res_company_view.xml",
        "views/menus.xml",

        "wizard/account_asset_split_wizard_view.xml",
    ],
    "demo": [],
    'test': [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
