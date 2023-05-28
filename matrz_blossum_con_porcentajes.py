import sys
import math
import argparse
# todas las clases devuelven algo que se imprime en el archivo de salida


def funcion_final(combinaciones, proporcion_observada, proporcion_par_esperada, letras):
    logggg = [0]*len(combinaciones)
    for i in range(len(combinaciones)):

        a = proporcion_observada[i]
        b = proporcion_par_esperada[i]
        if a > 0 and b > 0:
            # print(a, " ", b)
            logggg[i] = 2 * math.log2(a/b)
        else:
            logggg[i] = 0

    # print('\n\n\n')
    # print(logggg)
    log_redondeado = [round(elemento) for elemento in logggg]
    # print(combinaciones)
    # print(log_redondeado)
    # Calcular el tamaño de la matriz
    nn = int((2 * len(log_redondeado) + 1) ** 0.5)
    # print("nnn:", nn)

    matriz_final = []
    titulos = ['-']
    for i in letras:
        titulos.append(i)
    matriz_final.append(titulos)
    for i in range(nn):
        lista1 = []
        lista1.append(letras[i])
        for j in range(nn):
            combi = letras[i] + '-' + letras[j]
            combi2 = letras[j] + '-' + letras[i]
            # print(combi, combi2)
            for letra in range(len(combinaciones)):
                if combi == combinaciones[letra] or combi2 == combinaciones[letra]:
                    lista1.append(log_redondeado[letra])
        matriz_final.append(lista1)
        # print()

    for linea in matriz_final:
        print(linea)


def num_combinar_letras_solo_repeticiones(combinaciones, mr, mnr):
    # mr = matriz_repeticiones
    # mnr = matriz no repeticiones
    # print('\n\n\n')
    # print(mnr)
    # print(len(mnr))
    # print(combinaciones)
    num_combinaciones = [0]*len(combinaciones)
    for i in range(len(mr)):
        # print("fila: ", mr[i])
        for j in range(len(mnr)):
           # if (matrix[j][0] != 0):  # cuando solo tiene una fila esta linea se vuelve 0
         #   print("fila 2: ", mnr[j])
            for k in range(len(mr[0])):
                combi = mr[i][k] + '-' + mnr[j][k]
                combi2 = mnr[j][k] + '-' + mr[i][k]
          #      print("\t", combi, combi2)
                for l in range(len(combinaciones)):
                    if (combi == combinaciones[l] or combi2 == combinaciones[l]):
                        # esto es solo porque no hay repeticiones
                        num_combinaciones[l] += 1
           #             print(num_combinaciones)
    # print(combinaciones)
    # print(num_combinaciones)
    return (num_combinaciones)


def proporciones_esperadas(num_letras, combinaciones, total_letras, letras):
    num_proporciones_esperadas = [0]*len(combinaciones)
    for i in range(len(combinaciones)):
        # esos numeor son seguros
        # ya que combinaciones tiene la forma A-A
        # print(combinaciones[i][0], combinaciones[i][2])
        for j in range(len(letras)):
            if combinaciones[i][0] == letras[j]:
                # print("combinaciones1",
                #     combinaciones[i][0], letras[j], num_letras[j], total_letras)
                esperado1 = num_letras[j]/total_letras
            if combinaciones[i][2] == letras[j]:
                # print("combinaciones2",
                #     combinaciones[i][2], letras[j], num_letras[j], total_letras)
                esperado2 = num_letras[j]/total_letras
            if combinaciones[i][0] != combinaciones[i][2]:
                esperado3 = 2
            else:
                esperado3 = 1
        # print(esperado1, esperado2, esperado3)
        num_proporciones_esperadas[i] = (esperado1*esperado2)*esperado3
    print(letras)
    print(num_letras)
    print(num_proporciones_esperadas)
    return num_proporciones_esperadas


def proporciones_observadas(num_objetos, divisor):
    lista_proporcion = [valor/divisor for valor in num_objetos]
    return lista_proporcion


def num_combinar_letras_sin_repeticiones(combinaciones, matrix, rep):

    num_combinaciones = [0]*len(combinaciones)
    for i in range(len(matrix)):
        # print("fila: ", matrix[i])
        for j in range(i+1, len(matrix)):
           # if (matrix[j][0] != 0):  # cuando solo tiene una fila esta linea se vuelve 0
            # print("fila 2: ", matrix[j])
            for k in range(len(matrix[0])):
                combi = matrix[i][k] + '-' + matrix[j][k]
                combi2 = matrix[j][k] + '-' + matrix[i][k]
                # print("\t", combi, combi2)
                for l in range(len(combinaciones)):
                    if (combi == combinaciones[l] or combi2 == combinaciones[l]):
                        # esto es solo porque no hay repeticiones
                        num_combinaciones[l] += 1
    # print(combinaciones)
    # print(num_combinaciones)
    num_combinaciones_final = [valor*rep for valor in num_combinaciones]
    return num_combinaciones_final


def combinar_letras(letras):
    # print(letras)
    combinaciones = []

    # El 2do bucle vades dede la pisición i hasta el
    # fina de letras, así evitar repeticiones
    # comninaciones[] es solo para obtener el orden
    for i in range(len(letras)):
        for j in range(i, len(letras)):
            combinacion = letras[i] + '-' + letras[j]
            combinaciones.append(combinacion)
    print(combinaciones)
    return combinaciones


def lo_que_salga(matrix):
    # w*n(n-1)/2
    n = len(matrix)
    w = len(matrix[0])
    pares_totales = w*n*(n-1)/2
    # print("numero de secuencias: ", n, "numero de columnas: ", w)
    # print("pares totales: ", pares_totales)

    return n, w, pares_totales


def separacion(lista_identidad, matrix, porcentaje_identidad):
    matriz_repetida = []
    matriz_no_repetida = []

    # esta pare pregunta si hay repetidas segun nuestro porcentaje de identidad o no
    for i in range(len(lista_identidad)):
        if lista_identidad[i] == 1:
            # print("Esta fila es 'única'")
            matriz_no_repetida.append(matrix[i])
        elif (lista_identidad[i] > 1):
            # print("Esta lista no es 'única'")
            matriz_repetida.append(matrix[i])

    # nos va a servir paa hacer las cuentas despues
    # ya que se asingna valores diferentes tanto a los pares como a las
    # observaciones
    # para matriz_repetida todo va a valer 1
    # para la matriz no repetioda todo va  a valer los mismo que el largo de la matriz repetida
    # ej: en el archvo 6 con P=0.75 hay 2 repetidas, entonces esas 2 valen 1 y la otra vale 2
    # ej: en el archivo5 hay 4repetidos entonces esas 4 valen 1 y las otras 4
    # ej: si no hay repetidas entonces tdodo vale 1
    print("matriz no repetida")
    for i in matriz_no_repetida:
        print(i)
    print("matriz repetida")
    for i in matriz_repetida:
        print(i)

    matriz_caso = matriz_no_repetida
    caso = False

    '''
    se coloca puntaje de identidad ==1 porque así inmediatamente sabemos 
    que se están buscando fila iguales, en cambio con alguno menor
    se permiten filas con pequeñas diferencias

    esta parte pregunta si estna buscando filas iguales
    caso 1: si
    -  pregunta si despues de todo hay filas repetidas
        caso 1.1: si
        - añade solo una de esas filas a la matriz caso
            que en este punto solo tiene las no repetidasd
            y devuelve una matriz sencilla para que no haya que preocuparse de las replicas
        caso 1.2: no
        - devuelve la matriz caso sin modificaciones
    caso 2: no
        - no hace nada

    al final devleve
    - caso: 
        - true: no hay que preocuparse de la sreplicas porque estpa solucionado
        - false: si hayq eu preocuparse d elas replicas
    - matriz caso: sivre para cuando acso es true
    - matriz repetido y matriz no repetida: sirve para cuando caso es false 
    '''
    if (porcentaje_identidad == 1):
        caso = True
        if (len(matriz_repetida) > 0):
            matriz_caso.append(matriz_repetida[0])

            print("La parte que está repetida tiene una identidad de ",
                  porcentaje_identidad)
            print("\nEntonces se conserva solo una de las listas repetidas")
    else:
        print("El porcentaje de identidad no es 1 por l tanto no se ")
        print("eliminan filas, el procedimiento va a ir por otro camino")

    print("matriz caso")
    for i in matriz_caso:
        print(i)

    return matriz_caso, caso, matriz_repetida, matriz_no_repetida


def definirIdentidad(matrix, porcentaje_identidad):
    identidad_por_columna = [0]*len(matrix)
    print("identidad por columna al principio: ", identidad_por_columna)
    for i in range(len(matrix)):
        contador_similitud_por_columna = [0]*len(matrix)
        # contador_similitud_por_columna[i] = 1
        # esto para compara con los demáas más adelante
        # ten en cuenta que solo hay un grupo similar y no varioos
        for j in range(len(matrix)):
            # print("estoy comparando ", matrix[i], " con", matrix[j])
            contador_similitud = 0
            for k in range(len(matrix[i])):
                if matrix[i][k] == matrix[j][k]:
                    contador_similitud += 1
            # print("contador identidad para este par de filas: ",
            #      contador_similitud)

            # print("hay una identidad de ", contador_similitud/(k+1))
            # print()
            if (contador_similitud/(k+1) >= porcentaje_identidad):
                contador_similitud_por_columna[j] = 1
        identidad_por_columna[i] = contador_similitud_por_columna

    # si sumo esto tendría el puntaje de las columnas
    puntaje = [0]*len(matrix)
    for c in range(len(identidad_por_columna)):
        print(identidad_por_columna[c])
        for i in identidad_por_columna[c]:
            # print(i)
            puntaje[c] += i

    # print("\nCuantas copias hay de esa columna?: ", puntaje)
    return puntaje


def letras_function(matrix):
    # identifica que letras existen
    objetos = []

    objetos.append(matrix[0][0])
    for i in matrix:
        for j in i:
            if j not in objetos:
                objetos.append(j)

    # print(objetos)

    return objetos


def contar_letras(objetos, matrix):
    num_objetos = [0]*len(objetos)
    for i in range(len(num_objetos)):
        for j in matrix:
            for k in j:
                if k == objetos[i]:
                    num_objetos[i] += 1
    # print(num_objetos)
    return num_objetos


def printar_matriz(matriz):
    for i in matriz:
        print(i)


def main():

    parser = argparse.ArgumentParser()

    # Agregar las opciones y argumentos esperados
    parser.add_argument('-a', '--archivo1', help='Nombre del archivo 1')
    parser.add_argument('-b', '--archivo2', default=None,
                        help='Nombre del archivo 2 (opcional)')
    parser.add_argument('-p', '--pidentidad', default=1.0,
                        type=float, help='Porcentaje identidad')
    parser.add_argument('-q', '--quieroidentidad', type=int,
                        help='Determinar si quiere usar el procentaje de identidad o no, 1= si, 0 = no')

    # Parsear los argumentos de línea de comandos
    args = parser.parse_args()

    # Acceder a los valores de los argumentos
    input_file_path = args.archivo1
    input_file_path2 = args.archivo2
    porcentaje_identidad = args.pidentidad
    quiero_identidad = args.quieroidentidad

    # Imprimir los valores de los argumentos
    print("Archivo 1:", input_file_path)
    print("Archivo 2:", input_file_path2)
    print("Porcentaje identidad:", porcentaje_identidad)

    '''
    LA idea de este programa es hacer todo pero más atomico

    pasos para cuando sean 2
    1 ) contar las letras totales
    2) hacer las combinaciones
    3) contar los pares (no la proporción) de las combinaciones (no repetidas) (rehacer?)
    4) lo mismo pero de los repetidos contra los no reptidos
    5) sumar las combinaciones de ambas
    6) con el toal de letras se pueden sacar las proporciones 
    7) con las proporciones se puede sacar el 2log2 y su redondeo
    8) luego se arma la matriz

    pasos cuando sea 1
    1) evaluar que solo exista una 
    2) buscar si hay reoetidas o no
    3) si no, seguir del 3 a 8
    4) si si, seguir del 3 al 8 para replicas


    a ver
    las comunes serían:
    1) averiguar que letras hay y cuantas  


    ya  ahora si enserio:
    1) averiguar si el primero está, y tiene o no repetidos 
    nota: si tienne reétidos se hace lo de multiplicar por el n° de reptidos
    nota2: sii no tinene repetdidos se va a multiplicar por uno
    2) averiguar si el segundo está 

    nota 3: entonces el paso principal es el 2


    
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()
        matrix_original = [line.strip() for line in lines]
    '''
    # matrix_secundaria = [0]
    if quiero_identidad == 1:
        if input_file_path2 == None:
            with open(input_file_path, 'r') as input_file:
                lines = input_file.readlines()
                matrix_original = [line.strip() for line in lines]
            printar_matriz(matriz=matrix_original)
            print("\nsolo tenemos una matriz\n")
            # print(len(matrix_secundaria))
            # letras = letras_function(matrix=matrix_original)
            # num_letras = contar_letras(objetos=letras, matrix=matrix_original)
            lista_identidad = definirIdentidad(
                matrix=matrix_original,
                porcentaje_identidad=porcentaje_identidad
            )
            print("Cuantas copias hay de cada fila: ", lista_identidad)

            matrix, caso, matrix_rep, matrix_no_rep = separacion(
                lista_identidad=lista_identidad,
                matrix=matrix_original,
                porcentaje_identidad=porcentaje_identidad
            )
            if (len(matrix_rep) > 0):
                repeticiones = len(matrix_rep)
            else:
                repeticiones = 1
            print("las sin repeticiones se multiplicarán por:", repeticiones)
            if caso:  # true
                # se hace todo con normalidad
                ''' n, w y pt solo sirven para imprimirlo despues
                letras son las letras que existen en la matrix
                num_letras es el conteo, sirve para obtene la proporción de letras
                combinaciones muetsra los pares de letras que pueden haber
                '''
                n, w, pt = lo_que_salga(matrix)
                letras = letras_function(matrix)
                num_letras = contar_letras(letras, matrix)
                total_letras = sum(num_letras)
                print("total_letras", total_letras)
                combinaciones = combinar_letras(letras)
                num_combinaciones = num_combinar_letras_sin_repeticiones(
                    combinaciones=combinaciones, matrix=matrix, rep=repeticiones)
                proporcion_combinaciones_observadas = proporciones_observadas(
                    num_objetos=num_combinaciones, divisor=pt)
                proporcion_combinaciones_esperadas = proporciones_esperadas(
                    num_letras=num_letras, combinaciones=combinaciones, total_letras=total_letras, letras=letras)
                funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                              proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras)

            else:
                ''' esta parte es solo para obtener los totales 
                suponiendo que si hay copias, porque al final hay que multiplicarlo por
                len(matrix_rep)'''
                print("holaaaaaa")
                a = [0]*len(matrix[0])
                temp = []
                for i in matrix_no_rep:
                    temp.append(i)
                temp.append(a)
                # print(temp)
                n, w, pt = lo_que_salga(temp)
                print("pt:", pt, w, n)
                letras = letras_function(matrix=matrix_original)
                combinaciones = combinar_letras(letras=letras)
                # tengo que combinar la matriz que no tienen repeticiones
                num_combinaciones = num_combinar_letras_sin_repeticiones(
                    matrix=matrix_no_rep, combinaciones=combinaciones, rep=repeticiones)
                num_combinaciones_repetidas = num_combinar_letras_solo_repeticiones(
                    combinaciones=combinaciones, mr=matrix_rep, mnr=matrix_no_rep)
                num_combinaciones_total = [0]*len(num_combinaciones)
                for i in range(len(num_combinaciones)):
                    num_combinaciones_total[i] = num_combinaciones[i] + \
                        num_combinaciones_repetidas[i]
                print("total combinaciones:", num_combinaciones_total)
                num_letras_repetidas = contar_letras(letras, matrix_rep)
                num_letras_no_repetidas = contar_letras(letras, matrix_no_rep)
                num_letras_no_repetidas_final = [
                    valor*repeticiones for valor in num_letras_no_repetidas]
                print(num_letras_repetidas, num_letras_no_repetidas_final)
                num_letras_final = [0]*len(num_letras_repetidas)
                for i in range(len(num_letras_repetidas)):
                    num_letras_final[i] = num_letras_repetidas[i] + \
                        num_letras_no_repetidas_final[i]
                print(letras)
                print("num letras = ", num_letras_final)
                total_letras = sum(num_letras_final)
                print("total de letras:", total_letras)
                proporcion_combinaciones_observadas = proporciones_observadas(
                    num_objetos=num_combinaciones_total, divisor=pt*repeticiones)
                proporcion_combinaciones_esperadas = proporciones_esperadas(
                    num_letras=num_letras_final, combinaciones=combinaciones, total_letras=total_letras, letras=letras)
                funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                              proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras)
                # print(proporcion_combinaciones_observadas)
                # print(proporcion_combinaciones_esperadas)

                # aun no lo veo
                # recueda hacer las cosa por separada
                # cuando se multiplique los numero

        else:
            '''
            En este punto estás pensado
            ¿Y si hacemso un for?
            pero las matrices no tienen porqué tener las misma dimensiones
            y mi poco conocimiento de la smmatrices no me permite unirca en una matriz tridimencional

            yo se que todo se ve más bonito con un for
            pero no me da
            '''
            with open(input_file_path2, 'r') as input_file2, open(input_file_path, 'r') as input_file:
                lines = input_file.readlines()
                matrix_primaria = [line.strip() for line in lines]
                lines2 = input_file2.readlines()
                matrix_secundaria = [line.strip() for line in lines2]

            lista_identidad1 = definirIdentidad(
                matrix=matrix_primaria,
                porcentaje_identidad=porcentaje_identidad
            )
            lista_identidad2 = definirIdentidad(
                matrix=matrix_secundaria,
                porcentaje_identidad=porcentaje_identidad
            )
            print("Cuantas copias hay de cada fila(1): ", lista_identidad1)
            print("Cuantas copias hay de cada fila(2): ", lista_identidad2)

            matrix_caso1, caso1, matrix_rep1, matrix_no_rep1 = separacion(
                lista_identidad=lista_identidad1,
                matrix=matrix_primaria,
                porcentaje_identidad=porcentaje_identidad
            )

            matrix_caso2, caso2, matrix_rep2, matrix_no_rep2 = separacion(
                lista_identidad=lista_identidad2,
                matrix=matrix_secundaria,
                porcentaje_identidad=porcentaje_identidad
            )
            if (len(matrix_rep1) > 0):
                repeticiones = len(matrix_rep1)
            else:
                repeticiones = 1
            print("repeticiones:", repeticiones)
            '''
            Aquí empiezanlos lios
            casosooo
            - 1 false y 2 false:
            en ambas hay repeticiones e identidad no es 1
            idealmente tiene que repetirse la misma cantidad de columnas
                - contar por separado las letras 
                - multiplicarlas por separado pensando en cuantas repeticones hay
                - por separadoooo
                - hasta aqí podemos obtener letras, num_letras, proporcion_num_letras
                - falta w(n(n--1)/2) (eso se hace para ambas y después se suma) 
                la suma de esto va a a servir paa la proporción de pares
                - luego se cuentan las parejas
                    - por separado para multiĺicar por len(matrix_rep) las que estén en 
                    filas unicas
                    - cuando estén por separado se suman
                - cuando esté la suma podemos sacar proporcion pares tanto observado como esperados
                    - observados: la suma(1 y 2) / [la suma de w(n(n--1)/2)(1y2) *len(matrix_rep)]
                    - esperadoS: igual que el normal: proporcion de letras se muñtiĺican
                    y si son diferentes se multiĺica por 2 ademas 
                    el camino e sel mismo de quí en adelante
            
            - 1 false y 2 true or 1 true y 2 false:
            no existe, ya que true depende del porcentaje de identidad y ese es igual para los 2

            - 1 true y 1 true:
            se sigue el camino simple, el de la primerisima opcion(if)
            pero sumando cosas
            - w*n*(n-1)/2 ||| no habría que multiplicarlo por len(matrix_rep)
            - pares
            - letras
            - total letras (depende de latras así que es lo mismo)

            caso extra 
            - 1 fals y 2 false con difernetes repeticiones 
                - buscar un minimo comun multiplo y ese va a ser el nuevo len(matrix-rep)

            
            '''
            if caso1 and caso2:
                repeticiones = 1  # porque casosgnifica que no hay repeticiones o que ya la arreglaron
                print("fijate aqui")
                n1, w1, pt1 = lo_que_salga(matrix_caso1)
                n2, w2, pt2 = lo_que_salga(matrix_caso2)
                pt_final = pt1+pt2
                print("pares totales finales:", pt_final)

                letras1 = letras_function(matrix_caso1)
                letras2 = letras_function(matrix_caso2)

                letras_final = []
                for i in letras1:
                    if i not in letras_final:
                        letras_final.append(i)
                for i in letras2:
                    if i not in letras_final:
                        letras_final.append(i)

                print("letras finales")
                print(letras1, letras2, letras_final)

                num_letras1 = contar_letras(letras_final, matrix_caso1)
                num_letras2 = contar_letras(letras_final, matrix_caso2)
                num_letras_total = [0]*len(num_letras1)
                for i in range(len(num_letras1)):
                    num_letras_total[i] = num_letras1[i] + \
                        num_letras2[i]

                print("num_letras finales")
                print(num_letras_total)
                total_letras = sum(num_letras1) + sum(num_letras2)
                print("total_letras", total_letras)
                combinaciones = combinar_letras(letras_final)
                num_combinaciones1 = num_combinar_letras_sin_repeticiones(
                    combinaciones=combinaciones, matrix=matrix_caso1, rep=repeticiones)
                num_combinaciones2 = num_combinar_letras_sin_repeticiones(
                    combinaciones=combinaciones, matrix=matrix_caso2, rep=repeticiones)
                num_combinaciones_total = [0]*len(num_combinaciones1)
                for i in range(len(num_combinaciones1)):
                    num_combinaciones_total[i] = num_combinaciones1[i] + \
                        num_combinaciones2[i]
                print("combinaciones por letra")
                print(num_combinaciones_total)

                proporcion_combinaciones_observadas = proporciones_observadas(
                    num_objetos=num_combinaciones_total, divisor=pt_final)
                print(proporcion_combinaciones_observadas)
                proporcion_combinaciones_esperadas = proporciones_esperadas(
                    num_letras=num_letras_total, combinaciones=combinaciones, total_letras=total_letras, letras=letras_final)

                funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                              proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras_final)
            else:
                print("rep1:", matrix_rep1, "rep2:", matrix_rep2)
                if (len(matrix_rep1) == len(matrix_rep2)):
                    repeticiones = len(matrix_rep1)
                else:
                    repeticiones = max(len(matrix_rep1), len(matrix_rep2))

                print("fijate aqui")
                a = [0]*len(matrix_caso1[0])
                temp1 = []
                for i in matrix_no_rep1:
                    temp1.append(i)
                temp1.append(a)
                b = [0]*len(matrix_caso2[0])
                temp2 = []
                for i in matrix_no_rep2:
                    temp2.append(i)
                temp2.append(b)
                n1, w1, pt1 = lo_que_salga(temp1)
                n2, w2, pt2 = lo_que_salga(temp2)
                pt_final = (pt1+pt2)*repeticiones
                print("pares totales finales:", pt_final)

                letras1 = letras_function(matrix_primaria)
                letras2 = letras_function(matrix_secundaria)

                letras_final = []
                for i in letras1:
                    if i not in letras_final:
                        letras_final.append(i)
                for j in letras2:
                    if j not in letras_final:
                        letras_final.append(j)
                print("letras finales")
                print(letras1, letras2, letras_final)
                combinaciones = combinar_letras(letras_final)
                print(combinaciones)

                num_combinaciones1 = num_combinar_letras_sin_repeticiones(
                    matrix=matrix_no_rep1, combinaciones=combinaciones, rep=repeticiones)
                num_combinaciones_repetidas1 = num_combinar_letras_solo_repeticiones(
                    combinaciones=combinaciones, mr=matrix_rep1, mnr=matrix_no_rep1)
                num_combinaciones2 = num_combinar_letras_sin_repeticiones(
                    matrix=matrix_no_rep2, combinaciones=combinaciones, rep=repeticiones)
                num_combinaciones_repetidas2 = num_combinar_letras_solo_repeticiones(
                    combinaciones=combinaciones, mr=matrix_rep2, mnr=matrix_no_rep2)
                num_combinaciones_total = [0]*len(num_combinaciones1)
                for i in range(len(num_combinaciones1)):
                    num_combinaciones_total[i] = num_combinaciones1[i] + \
                        num_combinaciones_repetidas1[i] + \
                        num_combinaciones2[i] + \
                        num_combinaciones_repetidas2[i]
                print("total combinaciones:", num_combinaciones_total)

                num_letras_repetidas1 = contar_letras(
                    letras_final, matrix_rep1)
                num_letras_no_repetidas1 = contar_letras(
                    letras_final, matrix_no_rep1)
                num_letras_no_repetidas_final1 = [
                    valor*repeticiones for valor in num_letras_no_repetidas1]
                num_letras_repetidas2 = contar_letras(
                    letras_final, matrix_rep2)
                num_letras_no_repetidas2 = contar_letras(
                    letras_final, matrix_no_rep2)
                num_letras_no_repetidas_final2 = [
                    valor*repeticiones for valor in num_letras_no_repetidas2]
                print(num_letras_repetidas1, num_letras_no_repetidas_final1,
                      num_letras_no_repetidas2, num_letras_no_repetidas_final2)
                num_letras_final = [0]*len(num_letras_repetidas1)
                for i in range(len(num_letras_repetidas1)):
                    num_letras_final[i] = num_letras_repetidas1[i] + \
                        num_letras_no_repetidas_final1[i] +\
                        num_letras_repetidas2[i] +\
                        num_letras_no_repetidas_final2[i]
                print(letras_final)
                print(num_letras_final)
                total_letras = sum(num_letras_final)
                print("Total letras", total_letras)

                proporcion_combinaciones_observadas = proporciones_observadas(
                    num_objetos=num_combinaciones_total, divisor=pt_final)
                proporcion_combinaciones_esperadas = proporciones_esperadas(
                    num_letras=num_letras_final, combinaciones=combinaciones, total_letras=total_letras, letras=letras_final)
                # print(proporcion_combinaciones_observadas)
                # print(proporcion_combinaciones_esperadas)

                funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                              proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras_final)
    else:
        if input_file_path2 == None:
            with open(input_file_path, 'r') as input_file:
                lines = input_file.readlines()
                matrix_original = [line.strip() for line in lines]
            printar_matriz(matriz=matrix_original)
            print("\nsolo tenemos una matriz\n")
            # print(len(matrix_secundaria))
            # letras = letras_function(matrix=matrix_original)
            # num_letras = contar_letras(objetos=letras, matrix=matrix_original)
            '''lista_identidad = definirIdentidad(
                matrix=matrix_original,
                porcentaje_identidad=porcentaje_identidad
            )
            print("Cuantas copias hay de cada fila: ", lista_identidad)

            matrix, caso, matrix_rep, matrix_no_rep = separacion(
                lista_identidad=lista_identidad,
                matrix=matrix_original,
                porcentaje_identidad=porcentaje_identidad
            )
            if (len(matrix_rep) > 0):
                repeticiones = len(matrix_rep)
            else:
                repeticiones = 1
            print("las sin repeticiones se multiplicarán por:", repeticiones)'''

            n, w, pt = lo_que_salga(matrix_original)
            letras = letras_function(matrix_original)
            num_letras = contar_letras(letras, matrix_original)
            total_letras = sum(num_letras)
            print("total_letras", total_letras)
            combinaciones = combinar_letras(letras)
            num_combinaciones = num_combinar_letras_sin_repeticiones(
                combinaciones=combinaciones, matrix=matrix_original, rep=1)
            proporcion_combinaciones_observadas = proporciones_observadas(
                num_objetos=num_combinaciones, divisor=pt)
            proporcion_combinaciones_esperadas = proporciones_esperadas(
                num_letras=num_letras, combinaciones=combinaciones, total_letras=total_letras, letras=letras)
            funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                          proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras)
        else:
            with open(input_file_path2, 'r') as input_file2, open(input_file_path, 'r') as input_file:
                lines = input_file.readlines()
                matrix_primaria = [line.strip() for line in lines]
                lines2 = input_file2.readlines()
                matrix_secundaria = [line.strip() for line in lines2]

            '''lista_identidad1 = definirIdentidad(
                matrix=matrix_primaria,
                porcentaje_identidad=porcentaje_identidad
            )
            lista_identidad2 = definirIdentidad(
                matrix=matrix_secundaria,
                porcentaje_identidad=porcentaje_identidad
            )
            print("Cuantas copias hay de cada fila(1): ", lista_identidad1)
            print("Cuantas copias hay de cada fila(2): ", lista_identidad2)

            matrix_caso1, caso1, matrix_rep1, matrix_no_rep1 = separacion(
                lista_identidad=lista_identidad1,
                matrix=matrix_primaria,
                porcentaje_identidad=porcentaje_identidad
            )

            matrix_caso2, caso2, matrix_rep2, matrix_no_rep2 = separacion(
                lista_identidad=lista_identidad2,
                matrix=matrix_secundaria,
                porcentaje_identidad=porcentaje_identidad
            )
            if (len(matrix_rep1) > 0):
                repeticiones = len(matrix_rep1)
            else:
                repeticiones = 1
            print("repeticiones:", repeticiones)
            '''

            repeticiones = 1  # porque casosgnifica que no hay repeticiones o que ya la arreglaron
            print("fijate aqui")
            n1, w1, pt1 = lo_que_salga(matrix_primaria)
            n2, w2, pt2 = lo_que_salga(matrix_secundaria)
            pt_final = pt1+pt2
            print("pares totales finales:", pt_final)

            letras1 = letras_function(matrix_primaria)
            letras2 = letras_function(matrix_secundaria)

            letras_final = []
            for i in letras1:
                if i not in letras_final:
                    letras_final.append(i)
            for i in letras2:
                if i not in letras_final:
                    letras_final.append(i)

            print("letras finales")
            print(letras1, letras2, letras_final)

            num_letras1 = contar_letras(letras_final, matrix_primaria)
            num_letras2 = contar_letras(letras_final, matrix_secundaria)
            num_letras_total = [0]*len(num_letras1)
            for i in range(len(num_letras1)):
                num_letras_total[i] = num_letras1[i] + \
                    num_letras2[i]

            print("num_letras finales")
            print(num_letras_total)
            total_letras = sum(num_letras1) + sum(num_letras2)
            print("total_letras", total_letras)
            combinaciones = combinar_letras(letras_final)
            num_combinaciones1 = num_combinar_letras_sin_repeticiones(
                combinaciones=combinaciones, matrix=matrix_primaria, rep=repeticiones)
            num_combinaciones2 = num_combinar_letras_sin_repeticiones(
                combinaciones=combinaciones, matrix=matrix_secundaria, rep=repeticiones)
            num_combinaciones_total = [0]*len(num_combinaciones1)
            for i in range(len(num_combinaciones1)):
                num_combinaciones_total[i] = num_combinaciones1[i] + \
                    num_combinaciones2[i]
            print("combinaciones por letra")
            print(num_combinaciones_total)

            proporcion_combinaciones_observadas = proporciones_observadas(
                num_objetos=num_combinaciones_total, divisor=pt_final)
            print(proporcion_combinaciones_observadas)
            proporcion_combinaciones_esperadas = proporciones_esperadas(
                num_letras=num_letras_total, combinaciones=combinaciones, total_letras=total_letras, letras=letras_final)

            funcion_final(combinaciones=combinaciones, proporcion_observada=proporcion_combinaciones_observadas,
                          proporcion_par_esperada=proporcion_combinaciones_esperadas, letras=letras_final)


if __name__ == '__main__':
    print("Hola",
          "\nEste programa fue desarrollado por Valery Chaparro",
          "\nNo ha domrido mucho así que no se esforzó por meter todo a matrices mas grandes",
          "\nTengo entendido que se puede, pero como puede observar solo son 2 matrices",
          "\nespero en un uturo ceracno optimizarlo para tratar a varias matrices en una sola matriz 3D",
          "\n\nNota: revisar el lunes")
    main()
