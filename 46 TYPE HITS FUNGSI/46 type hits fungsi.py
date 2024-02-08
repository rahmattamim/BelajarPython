'''TYPE HINTS UNTUK FUNGSI'''

# bentuk standar fungsi

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(parameter)
    
fungsi(1)
fungsi("kilaa")
fungsi(True)
'''
# penggunaan type hints
import string

def sepuluh_pangkat(argument:int)->int:
    '''funsi dengan hints'''
    output = 10**argument
    return output

hasil = sepuluh_pangkat(2)
print(hasil)

def display(argument:string):
    print(argument)
    
display("Kilaa")