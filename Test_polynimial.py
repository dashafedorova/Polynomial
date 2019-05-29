import unittest

from Class_polynomial import Polynomial

class Test_polynomial(unittest.TestCase):
    def test_init_empty_list(self):
        p=Polynomial([])
        self.assertEqual(p.coeffs,[0])
        self.assertEqual(p.degree, 0)

    def test_init_zero_degree(self):
        p = Polynomial([5])
        self.assertEqual(p.coeffs, [5])
        self.assertEqual(p.degree, 0)

    def test_init_polynom_monom(self):
        p = Polynomial([4, 0])
        self.assertEqual(p.coeffs, [4, 0])
        self.assertEqual(p.degree, 1)

    def test_init_values_coeffs(self):
        p = Polynomial([3, 2, 1])
        self.assertEqual(p.coeffs, [3, 2, 1])
        self.assertEqual(p.degree, 2)

    def test_init_bad_case(self):
        with self.assertRaises(Exception) as exc:
            p0 = Polynomial([1, 2, 3, 'x'])
        self.assertEqual(str(exc.exception), "('Polynomial coeffs should have int type!', 'x', [1, 2, 3, 'x'])")
        with self.assertRaises(Exception) as exc:
            p1 = Polynomial('x')
        self.assertEqual(str(exc.exception), "('Incorrect polynomial parameters', 'x', 'x')")


    def test_init_polynomial_equal(self):
        p0 = Polynomial([7, 8, 3, 2, 4])
        p1 = Polynomial(p0)
        p2 = Polynomial([0])
        p3 = Polynomial(p2)

        self.assertEqual(p1.coeffs, [7, 8, 3, 2, 4])
        self.assertEqual(p1.degree, 4)
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_init_coeffs_isnull(self):
        p0 = Polynomial([0, 0, 1])
        p1 = Polynomial([0, 1, 0, 3])
        p2 = Polynomial([0, 0, 0, 0])
        self.assertEqual(p0.coeffs, [1])
        self.assertEqual(p0.degree, 0)
        self.assertEqual(p1.coeffs, [1, 0, 3])
        self.assertEqual(p1.degree, 2)
        self.assertEqual(p2.coeffs, [0])
        self.assertEqual(p2.degree, 0)

    # Adding tests
    def test_add_polynomial(self):
        p0 = Polynomial([1, 1])
        p1 = Polynomial([5, 1, 3, 2])
        p2 = Polynomial([6, -2, 3, -3])

        res0 = p0 + p1
        res1 = p0 + p2
        self.assertEqual(res0.coeffs, [5, 1, 4, 3])
        self.assertEqual(res1.coeffs, [6, -2, 4, -2])

    def test_add_res_isnull(self):
        p0 = Polynomial([5, 3])
        p1 = Polynomial([-5, -3])
        p2 = Polynomial([4, 1, -5, -3])
        p3 = Polynomial([4, -1, -5, 3])

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3
        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res1.coeffs, [4, 1, 0, 0])
        self.assertEqual(res2.coeffs, [4, -1, 0, 6])

    def test_add_pol_isnull(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])

        res0 = p0 + p1
        self.assertEqual(res0.coeffs, [4, 1, 2, 3])

    def test_add_const(self):
        p0 = Polynomial([3, 2, 1, 4])
        p1 = Polynomial(5)
        p2 = Polynomial(-4)
        p3 = 5
        p4 = -4

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3
        res3 = p0 + p4
        self.assertEqual(res0.coeffs, [3, 2, 1, 9])
        self.assertEqual(res1.coeffs, [3, 2, 1, 0])
        self.assertEqual(res2.coeffs, [3, 2, 1, 9])
        self.assertEqual(res3.coeffs, [3, 2, 1, 0])

    def test_radd(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([1, 2])
        p2 = 8
        p3 = 0

        res0 = p1 + p0
        res1 = p2 + p0
        res2 = p3 + p0
        self.assertEqual(res0.coeffs, [4, 1, 3, 5])
        self.assertEqual(res1.coeffs, [4, 1, 2, 11])
        self.assertEqual(res2.coeffs, [4, 1, 2, 3])


    def test_add_bad_case(self):
        p0 = Polynomial([3, 2, 4, 1])
        p1 = "3x^3+2x^2+4x+1"

        with self.assertRaises(Exception) as context:
            res0 = p0 + p1
        self.assertEqual(str(context.exception),"('Adding: Incorrect type of value. int type is expected.', '3x^3+2x^2+4x+1')")

    def test_sub_pol(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([4, -1, 2, -1])
        p3 = Polynomial([4, 1, 2, 3])
        p4 = Polynomial([7])
        p5 = 7

        res0 = p0 - p1
        res1 = p0 - p2
        res2 = p0 - p3
        res3 = p0 - p4
        res4 = p0 - p5
        self.assertEqual(res0.coeffs, [4, 1, 0, 0])
        self.assertEqual(res1.coeffs, [2, 0, 4])
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res3.coeffs, [4, 1, 2, -4])
        self.assertEqual(res4.coeffs, [4, 1, 2, -4])

    def test_sub_res_isnull(self):
        p0 = Polynomial([2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([4, 1, 2, 3])
        p3 = Polynomial([4, -1, 2, 3])

        res0 = p0 - p1
        res1 = p0 - p2
        res2 = p0 - p3
        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res1.coeffs, [-4, -1, 0, 0])
        self.assertEqual(res2.coeffs, [-4, 1, 0, 0])

    def test_sub_pol_isnull(self):
        p0 = Polynomial([3, 2, 2, 3])
        p1 = Polynomial([])

        res0 = p0 - p1
        self.assertEqual(res0.coeffs, [3, 2, 2, 3])

    def test_rsub(self):
        p0 = Polynomial([5, 1, 2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([])
        p3 = 13
        p4 = 0

        res0 = p1 - p0
        res1 = p2 - p0
        res2 = p3 - p0
        res3 = p4 - p0
        self.assertEqual(res0.coeffs, [-5, -1, 0, 0])
        self.assertEqual(res1.coeffs, [-5, -1, -2, -3])
        self.assertEqual(res2.coeffs, [-5, -1, -2, 10])
        self.assertEqual(res3.coeffs, [-5, -1, -2, -3])

    def test_sub_bad_case(self):
        p0 = Polynomial([3, 1, 2, 1])
        p1 = "3x^3+x^2+2x+1"

        with self.assertRaises(Exception) as context:
            res = p0 - p1
        self.assertEqual(str(context.exception),
                         "('Subtracting: Incorrect type of value. int type is expected.', '3x^3+x^2+2x+1')")

    def test_equal(self):
        p0 = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([5])
        p3 = 5

        self.assertTrue(p0 == p1)
        self.assertTrue(p2 == p3)

    def test_not_equal(self):
        p0 = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 3])

        self.assertFalse(p0 == p1)

    def test_mul(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([-2, -3])
        p2 = Polynomial([4, 5])
        p3 = Polynomial([1, 1, 1])
        p4 = Polynomial([3, 2, 5])
        p5 = Polynomial([0, 0])
        p6 = Polynomial([1, 2])
        p7 = 4
        res0 = p0 * p1
        res1 = p2 * p3
        res2 = p4 * p5
        res3 = p5 * p6
        self.assertEqual(res0.coeffs, [-8, -14, -7, -12,-9])
        self.assertEqual(res1.coeffs, [4,9,9,5])
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res3.coeffs, [0])


    def test_mul_pol_isnull(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])

        res0 = p0 * p1
        self.assertEqual(res0.coeffs, [0])


    def test_rmul(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])
        p2 = Polynomial([3])
        p3 = Polynomial(0)
        p4 = 3

        res0 = p1 * p0
        res1 = p2 * p0
        res2 = p3 * p0
        res3 = p4 * p0
        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res1.coeffs, [12, 3, 6, 9])
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res3.coeffs, [12,3,6,9])

    def test_mul_str_bad_case(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = "4x^3+x^2+2x+3"

        with self.assertRaises(Exception) as context:
            res = p0 * p1
        self.assertEqual(str(context.exception),"('Multiplication: Incorrect type of value. int type is expected.', '4x^3+x^2+2x+3')")

    def test_str_pol(self):
        p0 = Polynomial([0, 0, 0, 0])
        p1 = Polynomial([4, 1, 2, 3])
        p2 = Polynomial([-4, -3, -2, -1])
        p3 = Polynomial([2, 1])
        p4 = Polynomial([7])
        p5 = Polynomial([0])
        p6 = Polynomial([])

        self.assertEqual(str(p0), "0")
        self.assertEqual(str(p1), "4x^3+x^2+2x+3")
        self.assertEqual(str(p2), "-4x^3-3x^2-2x-1")
        self.assertEqual(str(p3), "2x+1")
        self.assertEqual(str(p4), "7")
        self.assertEqual(str(p5), "0")
        self.assertEqual(str(p6), "0")

    def test_str_coeff_isnull(self):
        p0 = Polynomial([3, 1, 2, 0])
        p1 = Polynomial([3, 1, 0, 3])
        p2 = Polynomial([4, 0, 2, 3])
        p3 = Polynomial([0, 1, 2, 3])
        p4 = Polynomial([4, 0, 0, 1])
        p5 = Polynomial([0, 0, 0, 1])
        p6 = Polynomial([0, 0, 0, 0])

        self.assertEqual(str(p0), "3x^3+x^2+2x")
        self.assertEqual(str(p1), "3x^3+x^2+3")
        self.assertEqual(str(p2), "4x^3+2x+3")
        self.assertEqual(str(p3), "x^2+2x+3")
        self.assertEqual(str(p4), "4x^3+1")
        self.assertEqual(str(p5), "1")
        self.assertEqual(str(p6), "0")

    def test_str_neg_null(self):
        p0 = Polynomial([-4, -1, -2, 0])
        p1 = Polynomial([-4, -1, 0, -3])
        p2 = Polynomial([-4, 0, -2, -3])
        p3 = Polynomial([0, -1, -2, -3])
        p4 = Polynomial([-4, 0, 0, -1])
        p5 = Polynomial([0, 0, 0, -1])
        p6 = Polynomial([0, 0, 0, 0])

        self.assertEqual(str(p0), "-4x^3-x^2-2x")
        self.assertEqual(str(p1), "-4x^3-x^2-3")
        self.assertEqual(str(p2), "-4x^3-2x-3")
        self.assertEqual(str(p3), "-x^2-2x-3")
        self.assertEqual(str(p4), "-4x^3-1")
        self.assertEqual(str(p5), "-1")
        self.assertEqual(str(p6), "0")

if __name__=='__main__':
    unittest.main()