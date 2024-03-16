def fun(string):
    """функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    string_up = str(string).upper()
    return string_up

def fun2(string):
    """которая делает заглавными первые буквы каждого слова в строке"""
    string_1=str(string).split(' ')
    return " ".join(string_1).title()

