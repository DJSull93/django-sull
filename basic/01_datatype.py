# --------DATA TYPE--------
'''
Python has Five standard types
Scalar
    Numbers : int, float, complex
    String : str
Vector : List, tuple, Dictionary, Set

hello = 'Hello'
print(hello)
print(hello[1:6])


Python List
'''
# List example
ls = ['abcd', 786, 2.2222, 'john', 70.2]
tinyls = [123, 'john']

# ls 에 '100' 을 추가 - Create / Read
ls.append('100')
print(f'ls + 100 = {ls}')

# ls 와 tinyls 결합 - Update / Read
ls.extend(tinyls)
print(f'ls+tinyls = {ls}')

# ls 에서 786 제거 - Delete / Read
del ls[1]
print(f'delete 786 = {ls}')

# Tuple example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

# tp 에 '100' 을 추가 - Create / Read
tpp = list(tp)
tpp.append('100')
print(f'tp + 100 = {tuple(tpp)}')
# tp 와 tinytp 결합 - Update / Read
print(f'tp + tinytp = {tuple(tp+tinytp)}')
# tp 에서 786 제거 - Delete / Read
tpl = list(tp)
del tpl[1]
print(f'delete 786 = {tuple(tpl)}')
# Dictionary example
dt = {'abcd' : 786, 'john' : 70.2}
tinydt = {'홍' : '30세'}

# dt 에 key 'tom', value '100' 을 추가 - Create / Read
dt['tom'] = '100'
print(f'dt + 100 = {dt}')
# dt 와 tinydt 결합 - Update / Read
dt.update(tinydt)
print(f'dt + tinydt = {dt}')
# dt 에서 'abcd' 제거 - Delete / Read
del dt['abcd']
print(f'delete abcd = {dt}')