import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from rb_tree import RedBlackTree, Node, BLACK, RED, NIL
NIL = RedBlackTree.NIL_LEAF

def time_tree_creator(onelist):
    start_time = time.time()
    counter = 0
    size = len(onelist)
    tree = RedBlackTree()
    while(counter < size):
        tree.add(onelist[counter])
        counter+=1
    endtime = time.time() - start_time
    return endtime

os.system('clear')
print("================================================\n")
print("============= Comparação Arvore VP =============\n")
print("================================================\n")

print("           Selecione o Tamanho do Vetor         \n")
print("   1)10000 Elementos\n")
print("   2)100000 Elementos\n")
print("   3)1000000 Elementos\n")

print("================================================\n")
print("                  github.com/fepas              \n")
print("================================================\n")

option = int(input("Insira uma opcao valida: "))

if option == 1:
    list_repeat1 = np.random.randint(10, size=10)
    list_repeat1 = list_repeat1.tolist()

    list_repeat2 = np.random.randint(100, size=100)
    list_repeat2 = list_repeat2.tolist()

    list_repeat3 = np.random.randint(1000, size=1000)
    list_repeat3 = list_repeat3.tolist()

    list_repeat4 = np.random.randint(10000, size=10000)
    list_repeat4 = list_repeat4.tolist()

        #Creating lists of random elements that can not be repeated

    list_no_repeat1 = random.sample(range(1,11), 10)

    list_no_repeat2 = random.sample(range(1,101), 100)

    list_no_repeat3 = random.sample(range(1,1001), 1000)

    list_no_repeat4 = random.sample(range(1,10001), 10000)






    final_arr_1 = [0]

    final_arr_1.append(time_tree_creator(list_repeat1))
    final_arr_1.append(time_tree_creator(list_repeat2))
    final_arr_1.append(time_tree_creator(list_repeat3))
    final_arr_1.append(time_tree_creator(list_repeat4))



    final_arr_2 = [0]
    final_arr_2.append(time_tree_creator(list_no_repeat1))
    final_arr_2.append(time_tree_creator(list_no_repeat2))
    final_arr_2.append(time_tree_creator(list_no_repeat3))
    final_arr_2.append(time_tree_creator(list_no_repeat4))


    y = [0, 10, 100, 1000 , 10000]


    plt.plot(final_arr_1, y, color='red')
    plt.plot(final_arr_2, y, color='blue')
    plt.title("Comparação criação Arvore VP números aleatórios")
    red_patch = mpatches.Patch(color='red', label='Com repetição')
    blue_patch = mpatches.Patch(color='blue', label='Sem repetição')
    plt.legend(handles=[red_patch, blue_patch])
    plt.xlabel('Tempo(s)')
    plt.ylabel('Tamanho do vetor')
    plt.show()

if option == 2:

    list_repeat1 = np.random.randint(10, size=10)
    list_repeat1 = list_repeat1.tolist()

    list_repeat2 = np.random.randint(100, size=100)
    list_repeat2 = list_repeat2.tolist()

    list_repeat3 = np.random.randint(1000, size=1000)
    list_repeat3 = list_repeat3.tolist()

    list_repeat4 = np.random.randint(10000, size=10000)
    list_repeat4 = list_repeat4.tolist()

    list_repeat5 = np.random.randint(100000, size=100000)
    list_repeat5 = list_repeat5.tolist()



        #Creating lists of random elements that can not be repeated

    list_no_repeat1 = random.sample(range(1,11), 10)

    list_no_repeat2 = random.sample(range(1,101), 100)

    list_no_repeat3 = random.sample(range(1,1001), 1000)

    list_no_repeat4 = random.sample(range(1,10001), 10000)

    list_no_repeat5 = random.sample(range(1,100001), 100000)




    final_arr_1 = [0]

    final_arr_1.append(time_tree_creator(list_repeat1))
    final_arr_1.append(time_tree_creator(list_repeat2))
    final_arr_1.append(time_tree_creator(list_repeat3))
    final_arr_1.append(time_tree_creator(list_repeat4))
    final_arr_1.append(time_tree_creator(list_repeat5))


    final_arr_2 = [0]
    final_arr_2.append(time_tree_creator(list_no_repeat1))
    final_arr_2.append(time_tree_creator(list_no_repeat2))
    final_arr_2.append(time_tree_creator(list_no_repeat3))
    final_arr_2.append(time_tree_creator(list_no_repeat4))
    final_arr_2.append(time_tree_creator(list_no_repeat5))


    y = [0, 10, 100, 1000 , 10000, 100000]


    plt.plot(final_arr_1, y, color='red')
    plt.plot(final_arr_2, y, color='blue')
    plt.title("Comparação criação Arvore VP números aleatórios")
    red_patch = mpatches.Patch(color='red', label='Com repetição')
    blue_patch = mpatches.Patch(color='blue', label='Sem repetição')
    plt.legend(handles=[red_patch, blue_patch])
    plt.xlabel('Tempo(s)')
    plt.ylabel('Tamanho do vetor')
    plt.show()


if option == 3:

    list_repeat1 = np.random.randint(10, size=10)
    list_repeat1 = list_repeat1.tolist()

    list_repeat2 = np.random.randint(100, size=100)
    list_repeat2 = list_repeat2.tolist()

    list_repeat3 = np.random.randint(1000, size=1000)
    list_repeat3 = list_repeat3.tolist()

    list_repeat4 = np.random.randint(10000, size=10000)
    list_repeat4 = list_repeat4.tolist()

    list_repeat5 = np.random.randint(100000, size=100000)
    list_repeat5 = list_repeat5.tolist()

    list_repeat6 = np.random.randint(1000000, size=1000000)
    list_repeat6 = list_repeat6.tolist()



        #Creating lists of random elements that can not be repeated

    list_no_repeat1 = random.sample(range(1,11), 10)

    list_no_repeat2 = random.sample(range(1,101), 100)

    list_no_repeat3 = random.sample(range(1,1001), 1000)

    list_no_repeat4 = random.sample(range(1,10001), 10000)

    list_no_repeat5 = random.sample(range(1,100001), 100000)

    list_no_repeat6 = random.sample(range(1,1000001), 1000000)




    final_arr_1 = [0]

    final_arr_1.append(time_tree_creator(list_repeat1))
    final_arr_1.append(time_tree_creator(list_repeat2))
    final_arr_1.append(time_tree_creator(list_repeat3))
    final_arr_1.append(time_tree_creator(list_repeat4))
    final_arr_1.append(time_tree_creator(list_repeat5))
    final_arr_1.append(time_tree_creator(list_repeat6))


    final_arr_2 = [0]
    final_arr_2.append(time_tree_creator(list_no_repeat1))
    final_arr_2.append(time_tree_creator(list_no_repeat2))
    final_arr_2.append(time_tree_creator(list_no_repeat3))
    final_arr_2.append(time_tree_creator(list_no_repeat4))
    final_arr_2.append(time_tree_creator(list_no_repeat5))
    final_arr_2.append(time_tree_creator(list_no_repeat6))

    y = [0, 10, 100, 1000 , 10000, 100000, 1000000]


    plt.plot(final_arr_1, y, color='red')
    plt.plot(final_arr_2, y, color='blue')
    plt.title("Comparação criação Arvore VP números aleatórios")
    red_patch = mpatches.Patch(color='red', label='Com repetição')
    blue_patch = mpatches.Patch(color='blue', label='Sem repetição')
    plt.legend(handles=[red_patch, blue_patch])
    plt.xlabel('Tempo(s)')
    plt.ylabel('Tamanho do vetor')
    plt.show()
