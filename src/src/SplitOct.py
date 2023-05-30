# Alexandre Gurchumelia
#
# v0.0          2019 May 24
# v0.1          2019 Dec 25
# v0.2          2020 Dec 28
# v0.3          2021 Feb 15
# v0.4          2021 May 04
# v0.5          2021 Dec 28
# v0.6          2022 Feb 08
# v0.7          2022 Apr 19
# v0.8          2022 Jun 29
# v0.9          2022 Aug 15
# v0.10         2022 Aug 30
# v0.11         2023 Mar 28
# v0.12         2023 Mar 30
# v0.13         2023 Apr 27
# v0.14         2023 May 25

import sympy as syp

def version():
    return '0.14'

_o1s, _j1s, _j2s, _j3s, _oIs, _J1s, _J2s, _J3s, = syp.symbols(
    '1 j_1 j_2 j_3 I J_1 J_2 J_3', real=True)

_ous = [_o1s, _j1s, _j2s, _j3s, _oIs, _J1s, _J2s, _J3s] # octonionic unit symbols

def _append_string(s, t):
    if t == '0': return s
    if s == '0': return t    
    if t[0] == '-': return s + ' ' + t
    else: return s + ' + ' + t
    
class SplitOctonion():
    # factor = True
    def __init__(self, x):
        if hasattr(x, '__len__'):
            if len(x) != 8:
                raise ValueError('SplitOctonion must be 8 dimensional')
            self.x = x
        else:
            self.x = [x, 0, 0, 0, 0, 0, 0, 0]
    # (1, j1, j2, j3, I, J1, J2, J3)
    
    def __getitem__(self, item):
         return self.x[item]
    
    def __setitem__(self, item, newvalue):
        if type(item) != int:
            raise ValueError('Index must be an integer')
        if not (0 <= item and item < 8):
            raise ValueError('Index must from 0 to 7')
        self.x[item] = newvalue
    
    def simplify(self):
        for n in range(8):
            self[n] = syp.simplify(self[n])
        return self
        
    def real(self):
        return self[0]
    def imag(self):
        return SplitOctonion([0,*self[1:]])
    def j1(self):
        return self[1]
    def j2(self):
        return self[2]
    def j3(self):
        return self[3]
    def I(self):
        return self[4]
    def J1(self):
        return self[5]
    def J2(self):
        return self[6]
    def J3(self):
        return self[7]
    
    def conj(self):
        return SplitOctonion([
            self.real(),
           -self.j1(),
           -self.j2(),
           -self.j3(),
           -self.I(),
           -self.J1(),
           -self.J2(),
           -self.J3()])
    
    def dot(self, other):
        if (type(other) != SplitOctonion):
            raise ValueError('Dot product can only be calculated with SplitOctonion')
        # return syp.Rational(1,2)*(self.conj()*other + other.conj()*self).x[0]
        return syp.simplify(
               self[0]*other[0] + \
               self[1]*other[1] + \
               self[2]*other[2] + \
               self[3]*other[3] - \
               self[4]*other[4] - \
               self[5]*other[5] - \
               self[6]*other[6] - \
               self[7]*other[7])
            
    
    def quadrance(self):
        # return syp.simplify((self*self.conj()).real())
        # return syp.simplify((self*self.conj()).real())
        return self.dot(self)
    
    def inv(self):
        m = self.quadrance()
        if m == 0:
            raise ZeroDivisionError('Division by zero devisor')
        else:
            return self.conj()/m
    
    def conj_j(self):
        return SplitOctonion([
            self.real(),
           -self.j1(),
           -self.j2(),
           -self.j3(),
            self.I(),
            self.J1(),
            self.J2(),
            self.J3()])
    
    def conj_I(self):
        return SplitOctonion([
            self.real(),
            self.j1(),
            self.j2(),
            self.j3(),
           -self.I(),
            self.J1(),
            self.J2(),
            self.J3()])
    
    def conj_J(self):
        return SplitOctonion([
            self.real(),
            self.j1(),
            self.j2(),
            self.j3(),
            self.I(),
           -self.J1(),
           -self.J2(),
           -self.J3()])
    
    def star(self):
        return SplitOctonion([
            self.real(),
            self.j1(),
            self.j2(),
            self.j3(),
           -self.I(),
           -self.J1(),
           -self.J2(),
           -self.J3()])
    
    def __neg__(self):
        return SplitOctonion([
           -self[0],
           -self[1],
           -self[2],
           -self[3],
           -self[4],
           -self[5],
           -self[6],
           -self[7]])
    
    def __add__(self, other):
        if type(other) == SplitOctonion:
            return SplitOctonion([
                self[0] + other[0],
                self[1] + other[1],
                self[2] + other[2],
                self[3] + other[3],
                self[4] + other[4],
                self[5] + other[5],
                self[6] + other[6],
                self[7] + other[7]]).simplify()
        else:
            return SplitOctonion([
                syp.simplify(self[0] + other),
                self[1],
                self[2],
                self[3],
                self[4],
                self[5],
                self[6],
                self[7]])

    def __sub__(self, other):
        if type(other) == SplitOctonion:
            return SplitOctonion([
                self[0] - other[0],
                self[1] - other[1],
                self[2] - other[2],
                self[3] - other[3],
                self[4] - other[4],
                self[5] - other[5],
                self[6] - other[6],
                self[7] - other[7]]).simplify()
        else:
            return SplitOctonion([
                syp.simplify(self[0] - other),
                self[1],
                self[2],
                self[3],
                self[4],
                self[5],
                self[6],
                self[7]])
    
    def __mul__(self, other):
        x = self.x
        if type(other) == SplitOctonion:
            y = other.x
            result = SplitOctonion([# x times y
                # our basis
                x[0]*y[0] - x[1]*y[1] - x[2]*y[2] - x[3]*y[3] + x[4]*y[4] + x[5]*y[5] + x[6]*y[6] + x[7]*y[7], # 1      0
                x[0]*y[1] + x[1]*y[0] + x[2]*y[3] - x[3]*y[2] - x[4]*y[5] + x[5]*y[4] + x[6]*y[7] - x[7]*y[6], # j1     1
                x[0]*y[2] - x[1]*y[3] + x[2]*y[0] + x[3]*y[1] - x[4]*y[6] - x[5]*y[7] + x[6]*y[4] + x[7]*y[5], # j2     2
                x[0]*y[3] + x[1]*y[2] - x[2]*y[1] + x[3]*y[0] - x[4]*y[7] + x[5]*y[6] - x[6]*y[5] + x[7]*y[4], # j3     3
                x[0]*y[4] - x[1]*y[5] - x[2]*y[6] - x[3]*y[7] + x[4]*y[0] + x[5]*y[1] + x[6]*y[2] + x[7]*y[3], # I      4
                x[0]*y[5] + x[1]*y[4] - x[2]*y[7] + x[3]*y[6] - x[4]*y[1] + x[5]*y[0] - x[6]*y[3] + x[7]*y[2], # J1     5
                x[0]*y[6] + x[1]*y[7] + x[2]*y[4] - x[3]*y[5] - x[4]*y[2] + x[5]*y[3] + x[6]*y[0] - x[7]*y[1], # J2     6
                x[0]*y[7] - x[1]*y[6] + x[2]*y[5] + x[3]*y[4] - x[4]*y[3] - x[5]*y[2] + x[6]*y[1] + x[7]*y[0]  # J3     7
                
                # wikipedia basis
                # x[0]*y[0] - x[1]*y[1] - x[2]*y[2] - x[3]*y[3] + x[4]*y[4] + x[5]*y[5] + x[6]*y[6] + x[7]*y[7], # 1      0
                # x[0]*y[1] + x[1]*y[0] + x[2]*y[3] - x[3]*y[2] + x[4]*y[5] - x[5]*y[4] + x[6]*y[7] - x[7]*y[6], # j1     1
                # x[0]*y[2] - x[1]*y[3] + x[2]*y[0] + x[3]*y[1] + x[4]*y[6] - x[5]*y[7] - x[6]*y[4] + x[7]*y[5], # j2     2
                # x[0]*y[3] + x[1]*y[2] - x[2]*y[1] + x[3]*y[0] + x[4]*y[7] + x[5]*y[6] - x[6]*y[5] - x[7]*y[4], # j3     3
                # x[0]*y[4] + x[1]*y[5] + x[2]*y[6] + x[3]*y[7] + x[4]*y[0] - x[5]*y[1] - x[6]*y[2] - x[7]*y[3], # I      4
                # x[0]*y[5] - x[1]*y[4] - x[2]*y[7] + x[3]*y[6] + x[4]*y[1] + x[5]*y[0] - x[6]*y[3] + x[7]*y[2], # J1     5
                # x[0]*y[6] + x[1]*y[7] - x[2]*y[4] - x[3]*y[5] + x[4]*y[2] + x[5]*y[3] + x[6]*y[0] - x[7]*y[1], # J2     6
                # x[0]*y[7] - x[1]*y[6] + x[2]*y[5] - x[3]*y[4] + x[4]*y[3] - x[5]*y[2] + x[6]*y[1] + x[7]*y[0]  # J3     7
            ])
            return result.simplify()
        else:
            return SplitOctonion([
                x[0]*other,
                x[1]*other,
                x[2]*other,
                x[3]*other,
                x[4]*other,
                x[5]*other,
                x[6]*other,
                x[7]*other]).simplify()
    
    def LeftDerivative(self, other):
        # (d/d other) of self
        x = self.x
        if type(other) == SplitOctonion:
            y = other.x
            result = SplitOctonion([
                syp.diff(x[0], y[0]) - syp.diff(x[1], y[1]) - syp.diff(x[2], y[2]) - syp.diff(x[3], y[3]) + syp.diff(x[4], y[4]) + syp.diff(x[5], y[5]) + syp.diff(x[6], y[6]) + syp.diff(x[7], y[7]),
                syp.diff(x[0], y[1]) + syp.diff(x[1], y[0]) - syp.diff(x[2], y[3]) + syp.diff(x[3], y[2]) + syp.diff(x[4], y[5]) - syp.diff(x[5], y[4]) - syp.diff(x[6], y[7]) + syp.diff(x[7], y[6]),
                syp.diff(x[0], y[2]) + syp.diff(x[1], y[3]) + syp.diff(x[2], y[0]) - syp.diff(x[3], y[1]) + syp.diff(x[4], y[6]) + syp.diff(x[5], y[7]) - syp.diff(x[6], y[4]) - syp.diff(x[7], y[5]),
                syp.diff(x[0], y[3]) - syp.diff(x[1], y[2]) + syp.diff(x[2], y[1]) + syp.diff(x[3], y[0]) + syp.diff(x[4], y[7]) - syp.diff(x[5], y[6]) + syp.diff(x[6], y[5]) - syp.diff(x[7], y[4]),                
                syp.diff(x[0], y[4]) + syp.diff(x[1], y[5]) + syp.diff(x[2], y[6]) + syp.diff(x[3], y[7]) + syp.diff(x[4], y[0]) - syp.diff(x[5], y[1]) - syp.diff(x[6], y[2]) - syp.diff(x[7], y[3]),
                syp.diff(x[0], y[5]) - syp.diff(x[1], y[4]) + syp.diff(x[2], y[7]) - syp.diff(x[3], y[6]) + syp.diff(x[4], y[1]) + syp.diff(x[5], y[0]) + syp.diff(x[6], y[3]) - syp.diff(x[7], y[2]),
                syp.diff(x[0], y[6]) - syp.diff(x[1], y[7]) - syp.diff(x[2], y[4]) + syp.diff(x[3], y[5]) + syp.diff(x[4], y[2]) - syp.diff(x[5], y[3]) + syp.diff(x[6], y[0]) + syp.diff(x[7], y[1]),
                syp.diff(x[0], y[7]) + syp.diff(x[1], y[6]) - syp.diff(x[2], y[5]) - syp.diff(x[3], y[4]) + syp.diff(x[4], y[3]) + syp.diff(x[5], y[2]) - syp.diff(x[6], y[1]) + syp.diff(x[7], y[0])
            ])/2
        else:
            result = SplitOctonion([syp.diff(x_n, other) for x_in in x])
        return result.simplify()
    
    def __truediv__(self, other):
        if type(other) == SplitOctonion:
            raise Exception('Division not supported, use .inv() instead')
        else:
            return SplitOctonion([
                self[0]/other,
                self[1]/other,
                self[2]/other,
                self[3]/other,
                self[4]/other,
                self[5]/other,
                self[6]/other,
                self[7]/other]).simplify()
    
    def __radd__(self, other):
        return self.__add__(other).simplify()
    
    def __rsub__(self, other):
        return SplitOctonion([
           syp.simplify(-self[0] + other),
           -self[1],
           -self[2],
           -self[3],
           -self[4],
           -self[5],
           -self[6],
           -self[7]])
    
    def __rmul__(self, other):
        return SplitOctonion([
            other*self[0],
            other*self[1],
            other*self[2],
            other*self[3],
            other*self[4],
            other*self[5],
            other*self[6],
            other*self[7]]).simplify()
    
    def _repr_latex_0(self):
        output = str(syp.printing.latex(self[0]))
        for n in range(1, 8):
            output = _append_string(output,
                str(syp.printing.latex(
                    syp.factor(self[n]*_ous[n])
                ))
            )
        return '$' + output + '$'
    
    def __repr__0(self):
        output = self[0].__repr__()
        output = _append_string(output,
            (self[1]*_j1s + self[2]*_j2s + self[3]*_j3s).__repr__())
        output = _append_string(output,
            (self[4]*_oIs).__repr__())
        output = _append_string(output,
            (self[5]*_J1s + self[6]*_J2s + self[7]*_J3s).__repr__())
        return output
    
    def _repr_latex_(self):
        return '$' + self.__repr__() + '$'
    
    def __repr__(self):
        output = str(syp.printing.latex(self[0]))
        for n in range(1, 8):
            output = _append_string(output,
                str(syp.printing.latex(
                    syp.factor(self[n]*_ous[n])
                ))
            )
        return output
    
    # def __repr__0(self):
    #     return (self[0] + \
    #             self[1]*_j1s + self[2]*_j2s + self[3]*_j3s + \
    #             self[4]*_oIs +\
    #             self[5]*_J1s + self[6]*_J2s + self[7]*_J3s).__repr__()
    
    def __eq__(self, other):
        if type(other) != SplitOctonion:
            other = SplitOctonion([other, 0, 0, 0, 0, 0, 0, 0])
        for (a, b) in zip(self.x, other.x):
            if syp.simplify(a - b) != 0:
                return False
        return True
    
    def copy(self):
        x = [component for component in self.x]
        return SplitOctonion(x)

def conj(x):
    if type(x) == SplitOctonion:
        return x.conj()
    else:
        return x

o1 = SplitOctonion(1)
j1 = SplitOctonion([0, 1, 0, 0, 0, 0, 0, 0])
j2 = SplitOctonion([0, 0, 1, 0, 0, 0, 0, 0])
j3 = SplitOctonion([0, 0, 0, 1, 0, 0, 0, 0])
oI = SplitOctonion([0, 0, 0, 0, 1, 0, 0, 0])
J1 = SplitOctonion([0, 0, 0, 0, 0, 1, 0, 0])
J2 = SplitOctonion([0, 0, 0, 0, 0, 0, 1, 0])
J3 = SplitOctonion([0, 0, 0, 0, 0, 0, 0, 1])

ounit = [o1, j1, j2, j3, oI, J1, J2, J3]