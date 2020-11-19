import unittest
from decimal import Decimal
from unittest.mock import MagicMock, patch

from simulation.balancer_math import BalancerMath


class TestBalancerMath(unittest.TestCase):
    def test_calc_spot_price_50_50_no_fee(self):
        w_50_50_no_fee_1 = {
            'tb_i': Decimal('10'),
            'tw_i': Decimal('20'),
            'tb_o': Decimal('5'),
            'tw_o': Decimal('20'),
            'fee': Decimal('0'),
            'price': Decimal('2')
        }
        price = BalancerMath.calc_spot_price(token_balance_in=w_50_50_no_fee_1['tb_i'], token_weight_in=w_50_50_no_fee_1['tw_i'],
                                             token_balance_out=w_50_50_no_fee_1['tb_o'], token_weight_out=w_50_50_no_fee_1['tw_o'],
                                             swap_fee=w_50_50_no_fee_1['fee'])

        self.assertEqual(price, w_50_50_no_fee_1['price'])

    def test_calc_spot_price_lbp_sim(self):
        # https://docs.google.com/spreadsheets/d/1t6VsMJF8lh4xuH_rfPNdT5DM3nY4orF9KFOj2HdMmuY/edit#gid=1392289526
        params = {
            'tb_i': Decimal('1333333'),
            'tw_i': Decimal('4'),
            'tb_o': Decimal('7500000'),
            'tw_o': Decimal('36'),
            'fee': Decimal('0.0001'),
            'price': Decimal('1.6')
        }
        price = BalancerMath.calc_spot_price(token_balance_in=params['tb_i'], token_weight_in=params['tw_i'],
                                             token_balance_out=params['tb_o'], token_weight_out=params['tw_o'], swap_fee=params['fee'])

        self.assertAlmostEqual(price, params['price'], 3)

    def test_calc_out_given_in_no_fee(self):
        params = {
            'ta_i': Decimal('1'),
            'tb_i': Decimal('10'),
            'tw_i': Decimal('20'),
            'tb_o': Decimal('100'),
            'tw_o': Decimal('20'),
            'fee': Decimal('0'),
            'ta_o': Decimal('9.0909090909090909')
        }
        token_amount_out = BalancerMath.calc_out_given_in(token_amount_in=params['ta_i'], token_weight_in=params['tw_i'],
                                                          token_balance_in=params['tb_i'], token_weight_out=params['tw_o'],
                                                          token_balance_out=params['tb_o'],
                                                          swap_fee=params['fee'])

        self.assertAlmostEqual(token_amount_out, params['ta_o'], 3)

    def test_calc_out_given_in_fee(self):
        params = {
            'ta_i': Decimal('1'),
            'tb_i': Decimal('10'),
            'tw_i': Decimal('10'),
            'tb_o': Decimal('100'),
            'tw_o': Decimal('30'),
            'fee': Decimal('0.1'),
            'ta_o': Decimal('2.8317232565404336')
        }
        token_amount_out = BalancerMath.calc_out_given_in(token_amount_in=params['ta_i'], token_weight_in=params['tw_i'],
                                                          token_balance_in=params['tb_i'], token_weight_out=params['tw_o'],
                                                          token_balance_out=params['tb_o'],
                                                          swap_fee=params['fee'])

        self.assertAlmostEqual(token_amount_out, params['ta_o'], 7)

    def test_calc_in_given_out(self):
        params = {
            'ta_o': Decimal('1'),
            'tb_i': Decimal('10'),
            'tw_i': Decimal('10'),
            'tb_o': Decimal('100'),
            'tw_o': Decimal('30'),
            'fee': Decimal('0.1'),
            'ta_i': Decimal('0.340112801426272844')
        }
        token_amount_in = BalancerMath.calc_in_given_out(token_amount_out=params['ta_o'], token_weight_in=params['tw_i'],
                                                         token_balance_in=params['tb_i'], token_weight_out=params['tw_o'],
                                                         token_balance_out=params['tb_o'],
                                                         swap_fee=params['fee'])

        self.assertAlmostEqual(token_amount_in, params['ta_i'], 7)

    @unittest.skip("need test data")
    def test_calc_pool_out_given_single_in(self):

        params = {
            'ta_i': Decimal('888'),
            'tb_i': Decimal('36'),
            'tw_i': Decimal('13'),
            'tw': Decimal('40'),
            'p_s': Decimal('10000'),
            'pa_o': Decimal('0.340112801426272844'),
            'fee': Decimal('0.08')
        }
        pool_amount_out = BalancerMath.calc_pool_out_given_single_in(token_weight_in=params['tw_i'], token_balance_in=params['tb_i'],
                                                                     pool_supply=params['p_s'], total_weight=params['t_w'],
                                                                     token_amount_in=params['ta_i'], swap_fee=Decimal['fee'])

        self.assertAlmostEqual(pool_amount_out, params['pa_o'], 7)

    @unittest.skip("need test data")
    def test_calc_single_in_given_pool_out(self):
        i = 2

    @unittest.skip("need test data")
    def test_calc_single_out_given_pool_in(self):
        i = 2

    @unittest.skip("need test data")
    def test_calc_pool_in_given_single_out(self):
        i = 2


if __name__ == '__main__':
    unittest.main()
