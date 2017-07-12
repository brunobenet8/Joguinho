#faz o loop e imprime tabuada do 1 ao 9
for i in range(1,10):
    
    print("---------Tabuada do {} ---------".format(i))
    for j in range(1,11):
        #imprime os numeros que serão multiplicados
        print("{} x {} = {}".format(i,j,i*j))
