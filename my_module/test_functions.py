from functions import *

def test_decoded_program():
    assert decoded_program("Êë®¢Ë¢êñòç¢ûñ÷¢çðìñûçæ¢öêëõ¢òôñéôãï£") == ("Hi, I hope you enjoyed this program!")
    assert callable(decoded_program)

def test_encoded_program():
    assert encoded_program("password") == ("òãõõùñôæ")
    assert callable(encoded_program)

def test_password_func():
    assert isinstance(password_func(1,5), str)
    assert isinstance(password_func(4,3), str)
    assert callable(password_func)
    
def test_topic_generator():
    assert callable(topic_generator)
    
    


    
