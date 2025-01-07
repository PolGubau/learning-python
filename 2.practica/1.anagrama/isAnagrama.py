#
 # Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.


def isAnagrama(str1:str,str2:str)->bool:
  # Elimina espacios y convierte a minúsculas
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()
  # Ordena las letras y compara
  return sorted(str1) == sorted(str2)


  
 