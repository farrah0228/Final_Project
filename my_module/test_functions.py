from functions import *
def test_encoded_program():
    assert decoded_program("Êë®¢Ë¢êñòç¢ûñ÷¢çðìñûçæ¢öêëõ¢òôñéôãï£") == ("Hi, I hope you enjoyed this program!")

def test_password_func():
    assert encoded_program("password") == ("òãõõùñôæ")
    