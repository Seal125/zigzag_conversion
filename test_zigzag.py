from zigzag import convert

def test_convert():
    assert convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'