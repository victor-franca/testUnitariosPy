import pytest
from calculadora import Calculadora

calc = Calculadora ()

def test_adicao_numeros_positivos():
    assert calc.adicao(2, 3) == 5
    
def test_adicao_numero_positivo_numero_negativo():     
    assert calc.adicao(2,-3) == -1

def test_adicao_numeros_negativos():    
    assert calc.adicao(-5,-6) == -11
     
def test_subtracao_numeros_positivos():
    assert calc.subtracao(5,3) == 2
      
def test_subtracao_numero_positivo_numero_negativo():
    assert calc.subtracao(5,-3) == 8
    
def test_subtracao_numeros_negativos():
    assert calc.subtracao(-6,-3) == -3
    
    
def test_multiplicacao_numeros_positivos():
    assert calc.multiplicacao(5,3) == 15
    
    
def test_multiplicacao_numero_positivo_numero_negativo():
    assert calc.multiplicacao(5,-3) == -15
    

def test_multiplicacao_numeros_negativos():
    assert calc.multiplicacao(-6,-3) == 18
    
    
def test_multiplicacao_numero_por_zero():
    assert calc.multiplicacao(6,0) == 0

def test_divisao_numeros_positivos():
    assert calc.divisao(10,2) == 5
    
    
def test_divisao_numero_positivo_numero_negativo():
    assert calc.divisao(25,-5) == -5
    

def test_divisao_numeros_negativos():
    assert calc.divisao(-40,-4) == 10
    
    
def test_divisao_numero_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
       calc.divisao(6,0) == 0

def test_divisao_dividendo_por_zero():
    assert calc.divisao(0,6) == 0
    
def test_fatorial_numero_positivo():
    assert calc.fatorial(3)==6

def test_fatorial_numero_um ():
    assert calc.fatorial(1)==1

def test_fatorial_numero_zero():
    assert calc.fatorial(0)==1

def test_fatorial_numero_negativo():
    with pytest.raises(ValueError, match="Fatorial de números negativos não é definido."):
        assert calc.fatorial(-2)==0
        
def test_potencia_numero_positivo():
    assert calc.potencia(2,3)==8
    
def test_potencia_exponte_zero():
    assert calc.potencia(2,0)==1
    
def test_potencia_exponte_negativo():
    assert calc.potencia(2,-3)==0.125
    
def test_potencia_base_negativo():
    assert calc.potencia(-2,3)==-8
    
def test_potencia_base_e_expoente_negativos():
    assert calc.potencia(-1,-5)==-1
    