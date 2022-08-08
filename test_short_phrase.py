class TestShortPhrase:

    def test_check_phrase(self):
        phrase = input("Введите фразу короче 15 символов:")
        assert len(phrase) < 15, "Фраза длинее 15 символов"