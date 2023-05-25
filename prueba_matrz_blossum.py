import sys
import math
# todas las clases devuelven algo que se imprime en el archivo de salida


def matriz_blossum(combinaciones, num_combinaciones, pt, letras, num_letras):
    proporcion_observada = [valor/pt for valor in num_combinaciones]
    total_leras = sum(num_letras)
    proporcion_letra = [valor/total_leras for valor in num_letras]
    # print("proporcipn objservada:", proporcion_observada)
    # print("total de letras", total_leras)
    # print("proprcion letras: ", proporcion_letra)

    # print('\n\n\n\nAquí está el error')
    proporcion_par_esperada = [0]*len(combinaciones)
    for i in range(len(letras)):
        for j in range(i, len(letras)):
            combinacion = letras[i] + '-' + letras[j]
            # print(letras[i], ": ", proporcion_letra[i],
            #      " ", letras[j], ": ", proporcion_letra[j])
            esperada = proporcion_letra[i] * \
                proporcion_letra[j]
            # print("Esperada actual: ", esperada)
            if letras[i] != letras[j]:
                # print("Nooooo")
                esperada = esperada*2
                # print("esperada ahoar es ", esperada)
            # print("esperada nueva: ", esperada)
            # print(combinacion, esperada)
            for k in range(len(combinaciones)):
                if combinacion == combinaciones[k]:
                    # print("SIIIIII")
                    # print('\ncombinacion + esperada')
                    # print(combinacion, esperada)
                    proporcion_par_esperada[k] = esperada
                    # print()

    # print("\n\npo\n\n")
    # print(proporcion_observada)
    # print("\n\npe\n\n")
    # print(proporcion_par_esperada)

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

    return proporcion_letra, proporcion_par_esperada, proporcion_observada, logggg, log_redondeado, matriz_final


def relacion(m_num_letras, letras, secuencias):
    combinaciones = []

    # El 2do bucle vades dede la pisición i hasta el
    # fina de letras, así evitar repeticiones
    # comninaciones[] es solo para obtener el orden
    for i in range(len(letras)):
        for j in range(i, len(letras)):
            combinacion = letras[i] + '-' + letras[j]
            combinaciones.append(combinacion)

    # se crea una lista rellebna de 0 con el larfo de combinaciones
    num_cominaciones = [0]*len(combinaciones)
    # print(combinaciones)
    # k = 2 por el tamaño del par
    k = 2
    total_combionaciones = 0

    '''
    esta parte recorre m_num_letras
    el primer for se encarga de contar cuantas
    combianciones existen etre las misma letas, A-A, B-A, C-C
    aplica factorial
    guarda el toal de combinacioens y cada una por comjunnto por separado en la lista 
    num_cominaciones[]
    ej 
    ['A-A', 'A-B', 'A-C', 'B-B', 'B-C', 'C-C']
    [15, 0, 0, 2, 0, 7]

    el segundo for se necuarga de conmbinar letras
    igual que como se hcieron las combacione arriba 
    con los bucles para evitar que se pase ppro un item 2 veces
    pero esta vez sin repeetir la letra, porque el anterior se encraga de A-A
    este solo de A-B, A-C y B-C
    y los garda de la misma manera que el anterior 
    asi pasa a 
    ['A-A', 'A-B', 'A-C', 'B-B', 'B-C', 'C-C']
    [15, 8, 4, 2, 0, 7]
    en ese caso no hay B-C

    '''
    # print(combinaciones)
    for line in m_num_letras:
        for l in range(len(line)):
            # print(line[l])
            # para contar combinaciones entre ellas
            if (line[l] > 0):
                num = math.comb(line[l], k)
                total_combionaciones += num
                # if line[l] == secuencias:
                letra_letra = letras[l] + '-' + letras[l]
                # print(letra_letra)
                for x in range(len(combinaciones)):

                    if letra_letra == combinaciones[x]:
                        # print(combinaciones[x], x)
                        num_cominaciones[x] += num
                        # print(num_cominaciones)

        for m in range(len(line)):
            for n in range(m+1, len(line)):
                # print(line[m], line[n])
                if line[n] != 0 and line[m] != 0 and line[n] != secuencias and line[m] != secuencias:
                    # print("si")
                    num = line[m]*line[n]
                    total_combionaciones += num
                    letra_letra = letras[m] + '-' + letras[n]
                    # print(letra_letra)
                    for x in range(len(combinaciones)):

                        if letra_letra == combinaciones[x]:
                            # print(combinaciones[x], x)
                            num_cominaciones[x] += num
                            # print(num_cominaciones)

    # print(combinaciones)
    # print(num_cominaciones)
    # print(total_combionaciones)

    return combinaciones, num_cominaciones


def contarLetrasPorColumna(matrix, letras):
    # transponer matriz
    filas = len(matrix)
    columnas = len(matrix[0])

    matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matrix[i][j]

    # for i in matriz_transpuesta:
    #    print(i)

    '''
    esta parte crea la lista principal de la matrix_num_letras
    el objetivo es guardar el n° de letras que hay en cada culumna de la matrix principal (no la transpuesta)
    para eso::
    - lee cada fila de la matriz transpuesta
    - crea una lista parra guardar los valores de cada letra para esa fila
    - lee la lista letras que contiene A B C
    - por cada letra de letras[] lee cada letra de la fila en que estpa metida
    - y va contando las letras
    ej: 
    letas = [ABC]
    fila AAAA
    if A = A:
        contador ++
    eso ocuure las 4 veces
    luego pasa a B y no cuenta nada
    entonces contador = 0
    lo mismo con C
    - el contador de cada elemento d ela lista letras se guarda en la lista 
    listaCuentaLetras[] quedando en toal [4, 0, 0]
    - esta al final se guarda em ña matrix_num_letras[][]
    - entonces por cdaa fila de la matriz transpueta se va a guardar una lista 
    en la matrix_num_letras con el numero de letras que hay
    - el orden del los numeros va a deoender de qué haya en la lista letras[]
    - en estra caso es ABC entonces el primer nuemro refiere al n° de As, el segundo, de Bs y el tercero de Cs

    '''
    matrix_num_letras = []

    for x in matriz_transpuesta:
        listaCuentaLetras = []
        for z in letras:
            cuentaz = 0
            for y in x:
                if y == z:
                    cuentaz += 1
            listaCuentaLetras.append(cuentaz)
        # print(listaCuentaLetras)
        matrix_num_letras.append(listaCuentaLetras)

    print("\nletras por columna: \n", letras)
    for x in matrix_num_letras:
        print(x)

    return matrix_num_letras, matriz_transpuesta


def letras_function(matrix):
    # identifica que letras existen
    objetos = []

    objetos.append(matrix[0][0])
    for i in matrix:
        for j in i:
            if j not in objetos:
                objetos.append(j)

    # print(objetos)
    num_objetos = [0]*len(objetos)
    for i in range(len(num_objetos)):
        for j in matrix:
            for k in j:
                if k == objetos[i]:
                    num_objetos[i] += 1
    # print(num_objetos)

    return objetos, num_objetos


def lo_que_salga(matrix):
    # w*n(n-1)/2
    n = len(matrix)
    w = len(matrix[0])
    pares_totales = w*n*(n-1)/2
    # print("numero de secuencias: ", n, "numero de columnas: ", w)
    # print("pares totales: ", pares_totales)

    return n, w, pares_totales


def main():

    # Verificar si se proporcionó el nombre del archivo como argumento
    if len(sys.argv) < 2:
        # print("Se debe proporcionar el nombre del archivo como argumento.")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = "resultados.txt"

    try:

        # print("Hola")

        # archivo = "archivo"
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
            matrix = [line.strip() for line in lines]

        for i in matrix:
            print(i)
        n, w, pt = lo_que_salga(matrix)
        letras, num_letras = letras_function(matrix)
        # print("cantdad de letras por clumna transpuesta")
        m_num_letras, m_transpuesta = contarLetrasPorColumna(matrix, letras)
        combinaciones, num_combinaciones = relacion(m_num_letras, letras, n)
        pro_letras, pro_par_esperada, pro_obs, logg, logg_redondeado, matriz_final = matriz_blossum(combinaciones, num_combinaciones,
                                                                                                    pt, letras, num_letras)

        with open(output_file_path, 'w') as output_file:
            for line in matrix:
                output_file.write(line + '\n')
            output_file.write('\n\nNúmero de secuencias: {}'.format(n))
            output_file.write('\nnumero de columnas: {}'.format(w))
            output_file.write('\nPares totales: {}'.format(pt))
            output_file.write('\nLetras encontradas: \n')
            for i in range(len(letras)):
                output_file.write('{} = {}\n'.format(
                    letras[i], num_letras[i]))
            output_file.write('\nMatriz transpuesta\n')
            for line in m_transpuesta:
                output_file.write(' '.join(map(str, line)) + '\n')
            output_file.write('\nNúmero de letras por columna de')
            output_file.write('\nla matriz original')
            output_file.write('\nen orden de la matriz transpuesta\n')
            output_file.write(
                '\nDe aquí en adelante todo se cuenta hacia los lados\n')
            output_file.write(' '.join(map(str, letras)) + '\n')
            for line in m_num_letras:
                output_file.write(' '.join(map(str, line)) + '\n')

            output_file.write('\nAquí empieza lo bueno')
            output_file.write('\nLetras observadas| proporción\n')
            for i in range(len(letras)):
                output_file.write(
                    '\t{} = {}\t\t|\t{}\n'.format(letras[i], num_letras[i], round(pro_letras[i], 3)))

            output_file.write('\ncombinacioens\t|')
            output_file.write('\nposibles sin\t|\tProporción\t|\tProporción')
            output_file.write('\nrepeticion\t\t|\tObservada\t|\tEsperadan\n')

            # output_file.write(' '.join(map(str, combinaciones)) + '\n')
            # output_file.write(' '.join(map(str, num_combinaciones)) + '\n')
            for i in range(len(combinaciones)):
                output_file.write('{} = {}\t\t\t|\t{}\t\t|\t{}\n'.format(
                    combinaciones[i], num_combinaciones[i], round(pro_obs[i], 3), round(pro_par_esperada[i], 3)))

            output_file.write(
                '\n2log2(proporción observada / porporción esperada)')
            output_file.write('\no mismo pero redondeado\n')
            for i in range(len(logg)):
                output_file.write('{} = {}\t\t|\t{}\n'.format(
                    combinaciones[i], logg[i], logg_redondeado[i]))

            output_file.write('\n\nmatriz blossum\n')
            for line in matriz_final:
                output_file.write(' '.join(map(str, line)) + '\n')

            # output_file.write("hola")

        print("Se ha creado el archivo", output_file_path,
              "y se ha escrito la matriz.")

    except FileNotFoundError:
        print("no se encontró el archivo: ", input_file_path)

    except IOError:
        print("Error al crear o abrir el archivo: ", output_file_path)


if __name__ == '__main__':
    main()
