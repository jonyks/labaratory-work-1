a=int(input('Введите a: '))
b=int(input('Введите b: '))
if a-b>0:
    c=a-b
else: c=b-a
print('Сумма= '+str(a+b), 'Разность= '+str(a-b),'Произведение= '+str(a*b),'Среднее арифмитическое= '+str((a+b)/2),'Разница= '+str(c),'Деление с плавающей точкой= '+format(a/b,'.2f'), sep='\n')