# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class test_city_county(TransactionCase):
    '''测试省市县'''
    def test_onchange_partner(self):
        '''测试partner的onchange'''
        self.env['partner'].onchange_partner_id()
#         self.partner_address = self.env['res.partner'].create(dict(name = 'jd.address',
#                                                                email = 'd@d',
#                                                                ))
#         self.env['partner'].onchange_partner_id()
