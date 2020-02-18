
x = '123+26'

y = []

z = [y.append(x[i]) if x[i].isdigit() else y.append('') for i in range(len(x))]
#####numbers
m = str()

for j in range(len(y)):
    while y[j].isdigit is True:
         m += y[j]       


for j in range(len(y)):
    if y[j].isdigit() == True :
        m += y[j]
    else:
        m += ' '

n = m.split(' ')
lst = []
for k in range(len(n)):
    lst.append(int(n[k]))
#####numbers



#####operators

y_op = []

z_op = [y_op.append('o') if x[i].isdigit() else y_op.append(x[i]) for i in range(len(x))]
for ii in range(len(y_op)):
    if y_op[ii] == '0':
        y_op.remove('o')

print(y_op)

##m_op = str()
##
##for j_op in range(len(y)):
##    while y[j_op].isdigit is False:
##         m_op += y[j_op]       
##
##
##for j_op in range(len(y)):
##    if y[j_op].isdigit() == False :
##        m_op += y[j_op]
##    else:
##        m_op += ' '
##n_op = m_op.split(' ')
##lst_op = []
##for k_op in range(len(n_op)):
##    lst_op.append(n_op[k_op])
#######operators
