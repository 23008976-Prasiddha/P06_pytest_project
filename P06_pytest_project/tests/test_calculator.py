from calculator.calculator import Calculator
import pytest #pytest is a library 

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        #arrange 
        a =7 
        b = 3
        cal = Calculator()
        #act 
        result = cal.subtract(a,b)
        #assert 
        expected = 4 
        assert result == expected 


    def test_multiply(self):
        #arrange 
        a =7 
        b = 3
        cal = Calculator()
        #act 
        result = cal.multiply(a,b)
        #assert 
        expected = 21 
        assert result == expected 



    def test_divide_normal(self):
        #arrange 
        a =6 
        b = 2
        cal = Calculator()
        #act 
        result = cal.divide(a,b)
        #assert 
        expected = 3 
        assert result == expected 


    def test_divide_by_zero(self):
        #arrange 
        a = 10 
        b = 0 
        cal = Calculator()
        #act and assert 
        with pytest.raises(ZeroDivisionError):
           cal.divide(a,b)
      

    

