import pytest
import wifi_password

def test_correct_password():
    test_cases =  (
        ('asd ASDEASER asda sd', 'aAas'),
        ('1aasd 3asdff 5as asd',   '135a'),
        ("Ich ess gerne Schnitzel", "IegS"),
        ("asd xddfdf asasd asd", "aaa"),  # if a word starts with x it is omitted
        ('ASDAS asdads asda B', 'aaaa'),
    )

    for test in test_cases:
        password =  wifi_password.generate_password(test[0])
        assert password == test[1], 'generated password OK'
            
