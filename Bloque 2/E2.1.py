"""Estadísticas de una lista de notas: media, máximo, mínimo
y cuántas aprobadas, sin usar statistics."""
ls=[1,2,3,4,5,6,7,8,9]

media= sum(ls)/len(ls)
maximo= max(ls)
minimo= min(ls)
aprobados= len([nota for nota in ls if nota>=5])

print(media,maximo,minimo,aprobados) 