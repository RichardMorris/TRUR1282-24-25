class fraction:

    def __init__(self, numerator, denominator): # constructor used to create the object​
        self._num = numerator # private fields, prevent modification
        self._den = denominator
        self._reduce()

    def _reduce(self):       # internal private method hidden 
        gcd1 = self._num
        gcd2 = self._den
        while (gcd2 != 0):
            (gcd1,gcd2) = (gcd2, gcd1 % gcd2)
        self._num = self._num // gcd1 # floor division operator // 
        self._den = self._den // gcd1 # using just / gives floating point numbers

    def toString(self): # convert to a string, the __str__ magic method would be better​
        return str(self._num) + '/' + str(self._den)

    def __str__(self): # magic method to return a human readable string ​
        return str(self._num) + '/' + str(self._den)

    def __float__(self): # magic method to convert to floating point format
        return self._num / self._den
    
    def __int__(self): # magic method return integer component, the floor of the 
        return self._num // self._den
    
    def __repr__(self): # magic method to return an exact representation for debugging ​
        return str(self._num) + '/' + str(self._den)
        
    def add(self, other): # add two fractions and return a new fraction​
        return fraction(self._num * other._den + self._den * other._num, self._den * other._den)
    
    def __add__(self, other): # A magic method so f1 + f2 works​
        return fraction(self._num * other._den + self._den * other._num, self._den * other._den)

    def __sub__(self, other): # add two fractions and return a new fraction​
        return fraction(self._num * other._den - self._den * other._num, self._den * other._den)
    
    def __mul__(self,other):
        return fraction(self._num*other._num, self._den*other._den)
    
    def __truediv__(self,other):
        return fraction(self._num*other._den, self._den*other._numS)

    def __floordiv__(self,other):
        return fraction(self._num*other._den, self._den*other._numS)
        
    def __ge__(self, other):
        return self._num * other._den >= self._den * other._num

    def __gt__(self, other):
        return self._num * other._den > self._den * other._num

    def __le__(self, other):
        return self._num * other._den <= self._den * other._num

    def __lt__(self, other):
        return self._num * other._den < self._den * other._num

    def __eq__(self, other):
        return self._num * other._den == self._den * other._num

    def __ne__(self, other):
        return self._num * other._den != self._den * other._num
    
    def __hash__(self): # generate a hash code used when object is a key in a hash table
        return hash((self.num, self.den))
    
    def __getattr__(self, name): # allows use of frac.n, frac.d, frac.num, frac.den
        if name == 'n' or name == 'num' or name == 'numerator':
            return self._num
        if name == 'd' or name == 'den' or name == 'denominator':
            return self._den
        raise AttributeError
    
    #def __dir__(self):
     #   return ['n', 'num', 'numerator', 'd', 'den','denominator']



f1 = fraction(6,8)                # make a new fraction object​
print(f1.toString())             # call the toString method and print it out​
f2 = fraction(1,3)
print(f2)
print(f1+f2)
print(f1 >= f2)
print(f1 > f2)
print(f1 <= f2)
print(f1 < f2)
print(f1 == f2)
print(f1 != f2)
print(f1.n,f1.d)
print(type(f1))
#try:
#    print(f1.top)
#catch