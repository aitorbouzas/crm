##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CRM Lead Sale Link',
    'version': '11.0.1.0.0',
    'author': "Savoir-faire Linux, "
              "AdaptiveCity"
              "Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'category': 'Others',
    'summary': 'CRM Lead Sale Link',
    'depends': [
        'sale_crm',
    ],
    'data': [
        'views/crm_lead_view.xml',
    ],
    'installable': True,
    'application': True,
}
