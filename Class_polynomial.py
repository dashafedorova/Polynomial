class Polynomial(object):

    # constructor
    def __init__(self, coefs):
        self.coeffs = []
        self.degree = 0
        if isinstance(coefs, list):
            if not coefs:
                self.coeffs = [0]
            else:
                for elem in coefs:
                    if not isinstance(elem, (int)):
                        raise ValueError('Polynomial coeffs should have int type!', elem, coefs)
                        break;
                else:
                    self.coeffs = coefs
        elif isinstance(coefs, Polynomial):
            self.coeffs = coefs.coeffs[:]
        elif isinstance(coefs, (int)):
            self.coeffs.append(coefs)
        else:
            raise ValueError('Incorrect polynomial parameters', coefs, coefs)

        if self.coeffs:
            self.degree = len(self.coeffs) - 1
        else:
            self.degree = 0

        if self.coeffs:
            while len(self.coeffs) > 1 and self.coeffs[0] == 0:
                self.coeffs.pop(0)
        self.degree = len(self.coeffs) - 1 if len(self.coeffs) >= 1 else 0

    # sum
    def __add__(self, obj):
        res = []
        if isinstance(obj, (int)):
            if self.coeffs:
                res = self.coeffs[:]
                res[-1] += obj
            else:
                res = obj
        elif isinstance(obj, Polynomial):
            if self.degree > obj.degree:
                res = self.coeffs[:]
                i = 0
                while i <= obj.degree:
                    res[i + self.degree - obj.degree] += obj.coeffs[i]
                    i += 1
            else:
                res = obj.coeffs[:]
                i = 0
                while i <= self.degree:
                    res[i + obj.degree - self.degree] += self.coeffs[i]
                    i += 1

        else:
            raise TypeError('Adding: Incorrect type of value. int type is expected.', obj)
        return Polynomial(res)

    def __radd__(self, obj):
        return self + obj


    # negative
    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coeffs])


    # subtraction
    def __sub__(self, obj):
        if isinstance(obj, (int, Polynomial)):
            return self.__add__(-obj)
        else:
            raise TypeError('Subtracting: Incorrect type of value. int type is expected.', obj)


    def __rsub__(self, obj):
        if isinstance(obj, (int, Polynomial)):
            return (self.__neg__()).__add__(obj)
        else:
            raise TypeError("Subtracting: Incorrect type of value. int type is expected.")

    # eguals
    def __eq__(self, obj):
        if isinstance(obj, Polynomial):
            return self.coeffs == obj.coeffs
        elif isinstance(obj, (int)):
            return self.degree == 0 and self.coeffs[0] == obj
        elif isinstance(obj, str):
            return str(self) == obj
        else:
            return False


    def __ne__(self, obj):
        return not self.__eq__(obj)


    # multiplication
    def __mul__(self, obj):
        if isinstance(obj, (int)):
            return Polynomial([coeff * obj for coeff in self.coeffs])
        elif isinstance(obj, Polynomial):
            res = [0] * (self.degree + obj.degree + 1)
            for self_pow, self_coeff in enumerate(self.coeffs):
                for obj_pow, obj_coeff in enumerate(obj.coeffs):
                    res[self_pow + obj_pow] += self_coeff * obj_coeff
        else:
            raise TypeError('Multiplication: Incorrect type of value. int type is expected.', obj)
        return Polynomial(res)


    def __rmul__(self, other):
        return self * other


    # toString
    def __str__(self):
        res = ""
        for pow, coeff in enumerate(self.coeffs):
            if coeff:
                if self.degree == 0:
                    res += str(coeff)
                else:
                    if abs(coeff) == 1:
                        if not (self.degree == pow):
                            res += ("+x" if coeff > 0 else "-x") + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
                        else:
                            res += ("+" if coeff > 0 else "-") + str(abs(coeff))
                    else:
                        res += ("+" if coeff > 0 else "-") + str(abs(coeff))
                        if not (self.degree == pow):
                            res += "x" + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
        if res:
            return res.lstrip("+")
        else:
            return "0"
