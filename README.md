# `code-binary-system`


Esto lo he hecho con fines educativo cuando estaba en clases de Arquitectura del Computador y quise realizar mi propio algoritmo.

Te permite convertir números decimales a binarios y viceversa.

## Instalación

```cmd
pip install binary_system
```

## Uso

Para convertir un número decimal a binario, se puede llamar a la función `number_to_binary()` y proporcionar el número como argumento. La función devolverá una cadena de texto que representa el número en su forma binaria.

```py
from binary_system import Binary

binary = Binary()
result = binary.number_to_binary(10) # Convierte el número 10 a binario
print(result) # Imprime "1010"
```

Para convertir un número binario a decimal, se puede llamar a la función `binary_to_number()` y proporcionar la cadena de texto binaria como argumento. La función devolverá el número decimal correspondiente.

```py
from binary_system import Binary

binary = Binary()
result = binary.binary_to_number('1010') # Convierte la cadena de texto "1010" a decimal
print(result) # Imprime "10"
```