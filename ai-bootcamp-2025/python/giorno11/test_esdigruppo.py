from esdigruppo_140225 import esdigruppo

def test_esdigruppo_lista_vuota():
    """Test con una lista vuota."""
    assert esdigruppo([]) == {}


def test_esdigruppo_lista_singolo_elemento():
    """Test con una lista contenente un solo elemento."""
    assert esdigruppo(['Mario']) == {'Mario': 1}


def test_esdigruppo_elementi_unici():
    """Test con nomi unici."""
    input_dati = ['Mario', 'Luca', 'Giulia']
    risultato_atteso = {'Mario': 1, 'Luca': 1, 'Giulia': 1}
    assert esdigruppo(input_dati) == risultato_atteso
