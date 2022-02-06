x = 'programacion'

# Ayudín:
#  p   r   o   g   r   a   m   a   c   i   o   n
#  0   1   2   3   4   5   6   7   8   9   10  11
# -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

print( x[0:8] )
print( x[4:8] )

# Se pueden usar signos negativos para referir los índices desde el final para atras
print( x[-7:-4] )

# Se puede omitir el parametro de fin para seguir hasta el final
print( x[8: ])

# Se puede omitir el parametro de inicio para comenzar desde el principio
print( x[ :8])