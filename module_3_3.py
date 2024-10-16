
def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')


print_params()  
print_params(10) 
print_params(10, 'новая строка')  
print_params(b=25) 
print_params(c=[1, 2, 3])  

values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

print_params(*values_list)  
print_params(**values_dict) 

values_list_2 = ['элемент1', 100]
print_params(*values_list_2, 42) 
