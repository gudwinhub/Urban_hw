import modulpack

print(dir(modulpack))  # список атрибутов и иметодов объекта modulpac

# callable позволяет проверить является ли переменная функций
print(callable(modulpack.prnt))
#  в данном случае мы получим True - т.е prnt является функцией
#  применив эту функцию к переменной verbl получим False - т.е это переменная а не функция

modulpack.prnt()
print(modulpack.verbl)
