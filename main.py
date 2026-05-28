# =============================================================================
# OPERACIONES BASE: VALIDACIONES Y FACTORIALES
# =============================================================================

import time 

def validar_entradas(n, r=0):
    """ 
    Esta función valida que los parámetros cumplan con las restricciones matemáticas de la 
    combinatoria, entonces valida que n y r sean enteros no negativos y que r sea menor o igual 
    que n.
    """
    # 1. Validación de tipos de datos
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError("Error: Los parámetros n y r deben ser números enteros.")

    # 2. Validación de que no sean negativos
    if n < 0 or r < 0: 
        raise ValueError("Error: los valores no pueden ser negativos, deben ser mayor o igual a 0, por favor digite nuevamente.")

    # 3. Validación de tamaños
    if r > n:
        raise ValueError(f"Error matemático: El tamaño del subconjunto (r = {r}) "
                         f"no puede ser mayor que el conjunto total (n = {n}).")
    return True


def factorial_iterativo(n):
    """ Esta función calcula n! mediante un ciclo for """
    if n == 0 or n == 1:
        return 1 
    resultado = 1 
    for i in range(2, n + 1):
        resultado *= i 
    return resultado 


def factorial_recursivo(n):
    """ Esta función calcula n! mediante recursión """
    # Caso base
    if n == 0 or n == 1: 
        return 1 
    # Caso recursivo
    return n * factorial_recursivo(n - 1) 


# =============================================================================
# PROBLEMA 1: CALCULADORA GENERAL DE PERMUTACIÓN Y K-PERMUTACIONES 
# =============================================================================

def calcular_permutacion(n, r, usar_recursivo=False):
    """
    Calcula P(n, r) = n! / (n-r)! y retorna el resultado y los factoriales intermedios.
    """
    # Se validan las entradas antes de hacer los cálculos 
    validar_entradas(n, r) 
    
    # Se selecciona el algoritmo de factorial según corresponda
    if usar_recursivo:
        fact_n = factorial_recursivo(n)
        fact_n_r = factorial_recursivo(n - r) 
    else:
        fact_n = factorial_iterativo(n)
        fact_n_r = factorial_iterativo(n - r)

    # Se aplica la fórmula general de la k-permutación
    resultado = fact_n // fact_n_r
    return resultado, fact_n, fact_n_r


def mostrar_problema_1(n, r, usar_recursivo=False):
    """ Esta función muestra en consola la resolución interactiva del problema 1 """
    print("\n" + "="*80)
    print("1. TÍTULO: Calculadora general de permutaciones y k-permutaciones")
    print("="*80)
    print("\n2. DESCRIPCIÓN MATEMÁTICA:")
    print("   Una k-permutación es una disposición lineal de r objetos elegidos de un")
    print("   conjunto de n objetos distintos. Aquí el ORDEN de los elementos SÍ importa.")
      
    print("\n3. FÓRMULA USADA:")
    print("   P(n, r) = n! / (n - r)!")
      
    print("\n4. EXPLICACIÓN DEL ALGORITMO:")
    print("   1. Se verifica que n >= 0, r >= 0 y r <= n mediante validaciones robustas.")
    print("   2. Se calcula el factorial del total (n!) de forma iterativa o recursiva.")
    print("   3. Se calcula el factorial de la diferencia (n - r)!.")
    print("   4. Se divide n! entre (n - r)! mediante división entera para precisión absoluta.")
      
    print("\n5. CÓDIGO EN ACCIÓN (PROCEDIMIENTO PASO A PASO):")
    try:
        resultado, fact_n, fact_n_r = calcular_permutacion(n, r, usar_recursivo)
        modo = "RECURSIVO" if usar_recursivo else "ITERATIVO"
        print(f"   -> Modo de cálculo: {modo}")
        print(f"   -> Parámetros ingresados: n = {n}, r = {r}")
        print(f"   -> Operación: P({n}, {r}) = {n}! / ({n} - {r})!")
        print(f"   -> Paso A (Calcular n!): {n}! = {fact_n}")
        print(f"   -> Paso B (Calcular (n-r)!): {n-r}! = {fact_n_r}")
        print(f"   -> Paso C (División final): {fact_n} / {fact_n_r}")
        print(f"   -> [RESULTADO]: P({n}, {r}) = {resultado}")
    except (ValueError, TypeError) as e:
        print(f"   [ERROR DETECTADO]: {e}")

    print("\n7. COMENTARIOS SOBRE LA EFICIENCIA DEL ALGORITMO:")
    print("   - Versión Iterativa: Complejidad Temporal O(n) pues ejecuta un bucle proporcional a n.")
    print("     Complejidad Espacial O(1) al usar variables fijas. Muy eficiente en memoria.")


def comparar_casos_permutaciones():
    """ Compara los casos numéricos específicos requeridos por la guía """
    print("\n" + "-"*80)
    print("REQUISITO GUÍA: COMPARACIÓN DE CASOS FIJOS DEL ENUNCIADO")
    print("-"*80)
    casos = [(10, 3), (20, 5)]
    for n, r in casos:
        res, _, _ = calcular_permutacion(n, r)
        print(f"   Caso numérico: P({n}, {r}) = {res}")


def comparar_extension_opcional_p1(n_grande=500):
    """
    Extensión opcional: Compara el rendimiento y límites de la versión recursiva vs iterativa.
    """
    print("\n" + "-"*80)
    print("EXTENSIÓN OPCIONAL: COMPARACIÓN FACTORIAL ITERATIVO VS RECURSIVO")
    print("-"*80)
    print(f"   Evaluando n = {n_grande} para medir tiempos de ejecución...")
    
    # Medición Iterativa
    inicio_it = time.perf_counter()
    _ = factorial_iterativo(n_grande)
    fin_it = time.perf_counter()
    tiempo_it = fin_it - inicio_it
    
    # Medición Recursiva
    inicio_rec = time.perf_counter()
    try:
        _ = factorial_recursivo(n_grande)
        fin_rec = time.perf_counter()
        tiempo_rec = fin_rec - inicio_rec
        status_rec = f"{tiempo_rec:.6f} segundos"
    except RecursionError:
        status_rec = "ERROR: Desbordamiento de pila (Stack Overflow)"

    print(f"   -> Tiempo Factorial Iterativo: {tiempo_it:.6f} segundos (Espacio O(1))")
    print(f"   -> Tiempo Factorial Recursivo: {status_rec} (Espacio O(n))")
    print("   -> Conclusión: El enfoque iterativo es más seguro y eficiente para valores grandes")
    print("                  en Python debido al límite de recursión de la pila del sistema.")


# =============================================================================
# PROBLEMA 2: CALCULADORA GENERAL DE COMBINACIONES
# =============================================================================

def calcular_combinacion(n, r):
    """ Calcula C(n, r) = n! / (r! * (n-r)!) usando división entera. """
    validar_entradas(n, r)
    fact_n = factorial_iterativo(n)
    fact_r = factorial_iterativo(r)
    fact_n_r = factorial_iterativo(n - r)
    return fact_n // (fact_r * fact_n_r)


def verificar_identidad_simetria(n, r):
    """ Verifica automáticamente la identidad combinatoria: C(n, r) == C(n, n - r). """
    validar_entradas(n, r)
    c_n_r = calcular_combinacion(n, r)
    c_n_nr = calcular_combinacion(n, n - r)
    return c_n_r, c_n_nr, (c_n_r == c_n_nr)


def obtener_fila_pascal(n):
    """ Genera la fila n del Triángulo de Pascal (indexado desde 0). """
    if n < 0:
        raise ValueError("Error: El número de fila de Pascal debe ser un entero no negativo.")
    fila = []
    for k in range(n + 1):
        fila.append(calcular_combinacion(n, k))
    return fila


def imprimir_triangulo_pascal_completo(n):
    """ Extensión opcional: Genera e imprime el Triángulo de Pascal centrado """
    if n < 0:
        print("   [ERROR]: n debe ser mayor o igual a 0.")
        return
    print(f"\n   [EXTENSIÓN OPCIONAL]: Triángulo de Pascal hasta la fila n = {n}:")
    triangulo = []
    for i in range(n + 1):
        triangulo.append(obtener_fila_pascal(i))
        
    ancho_maximo = len(" ".join(map(str, triangulo[-1])))
    
    for i, fila in enumerate(triangulo):
        fila_texto = " ".join(map(str, fila))
        print(f"   Fila {i:2d}: {fila_texto.center(ancho_maximo)}")


def mostrar_problema_2(n, r):
    """ Muestra en consola la resolución del Problema 2 cumpliendo la estructura de la guía. """
    print("\n" + "="*80)
    print("1. TÍTULO: Calculadora general de combinaciones")
    print("="*80)
    print("\n2. DESCRIPCIÓN MATEMÁTICA:")
    print("   Una combinación es una selección de r elementos de un conjunto de n")
    print("   objetos distintos donde el ORDEN NO IMPORTA. Al no importar el orden,")
    print("   se eliminan las ordenaciones redundantes dividiendo entre r!.")
    
    print("\n3. FÓRMULA USADA:")
    print("   C(n, r) = n! / (r! * (n - r)!)  también denotado como (n sobre r)")
    
    print("\n4. EXPLICACIÓN DEL ALGORITMO:")
    print("   1. Se validan las entradas (n >= 0, r >= 0, r <= n).")
    print("   2. Se calculan por separado n!, r! y (n - r)! de forma iterativa.")
    print("   3. Se multiplica r! por (n - r)! in el denominador.")
    print("   4. Se realiza la división entera del numerador entre el denominador.")
    
    print("\n5. CÓDIGO EN ACCIÓN (PROCEDIMIENTO PASO A PASO):")
    try:
        resultado = calcular_combinacion(n, r)
        print(f"   -> Parámetros ingresados: n = {n}, r = {r}")
        print(f"   -> Operación: C({n}, {r}) = {n}! / ({r}! * ({n} - {r})!)")
        print(f"   -> [RESULTADO]: C({n}, {r}) = {resultado}")
        
        val1, val2, cumple = verificar_identidad_simetria(n, r)
        print(f"\n   -> [VERIFICACIÓN DE IDENTIDAD DE SIMETRÍA]:")
        print(f"      ¿C({n}, {r}) == C({n}, {n}-{r})? -> ¿C({n}, {r}) == C({n}, {n-r})?")
        print(f"      Lado izquierdo C({n},{r}) = {val1}")
        print(f"      Lado derecho C({n},{n-r}) = {val2}")
        print(f"      ¿Se cumple la identidad?: {cumple}")
        
        fila_n = obtener_fila_pascal(n)
        print(f"\n   -> [FILA {n} DEL TRIÁNGULO DE PASCAL]:")
        print(f"      Los coeficientes son: {fila_n}")
        
    except (ValueError, TypeError) as e:
        print(f"   [ERROR DETECTADO]: {e}")
        
    print("\n7. COMENTARIOS SOBRE LA EFICIENCIA DEL ALGORITMO:")
    print("   - Complejidad Temporal: O(n) ya que se realizan tres cálculos de factorial independientes.")
    print("   - Complejidad Espacial: O(1) para el cálculo de combinaciones aislado.")
    print("   - Para el Triángulo de Pascal completo: Temporal O(n^2) y Espacial O(n^2).")


def ejecutar_bateria_pruebas_automaticas():
    """ Corre automáticamente el set de 5 pruebas exigido para validar robustez """
    print("\n" + "="*80)
    print("6. PRUEBAS: EJECUCIÓN DE LOS 5 CASOS DE EVALUACIÓN EXIGIDOS POR LA GUÍA")
    print("="*80)
    
    casos_prueba = [
        {"n": 7,  "r": 3, "desc": "Caso Estándar Normal"},
        {"n": 6,  "r": 0, "desc": "Caso Límite (r = 0)"},
        {"n": 4,  "r": 4, "desc": "Caso Límite (r = n)"},
        {"n": 0,  "r": 0, "desc": "Caso Extremo Mínimo Vacío (n=0, r=0)"},
        {"n": 3,  "r": 5, "desc": "Caso de Error Controlado (r > n)"}
    ]
    
    print(f"{'Escenario':<35} | {'Entradas':<12} | {'Resultado P(n,r)':<18} | {'Resultado C(n,r)':<18}")
    print("-" * 100)
    
    for i, caso in enumerate(casos_prueba, 1):
        n, r, desc = caso["n"], caso["r"], caso["desc"]
        label = f"Prueba {i}: {desc}"
        inputs_str = f"n={n}, r={r}"
        
        try:
            p_res, _, _ = calcular_permutacion(n, r)
            p_str = str(p_res)
        except (ValueError, TypeError):
            p_str = "ERROR CAPTURADO"
            
        try:
            c_res = calcular_combinacion(n, r)
            c_str = str(c_res)
        except (ValueError, TypeError):
            c_str = "ERROR CAPTURADO"
            
        print(f"{label:<35} | {inputs_str:<12} | {p_str:<18} | {c_str:<18}")


# =============================================================================
# INTERFAZ DE USUARIO POR CONSOLA (MENÚ INTERACTIVO)
# =============================================================================

def solicitar_entero(mensaje):
    """ Función auxiliar para leer enteros de forma segura impidiendo letras """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("   [ENTRADA INVÁLIDA]: Por favor, digite únicamente números enteros.")


def menu_interactivo():
    """ Controla la ejecución interactiva del sistema completo """
    while True:
        print("\n" + "#"*80)
        print("          SISTEMA CENTRAL INTERACTIVO DE CONTEO Y COMBINATORIA")
        print("                       MATEMÁTICAS DISCRETAS I")
        print("#"*80)
        print("   [1] Calcular PERMUTACIÓN P(n, r) con tus propios parámetros")
        print("   [2] Calcular COMBINACIÓN C(n, r) con tus propios parámetros")
        print("   [3] Imprimir un TRIÁNGULO DE PASCAL completo hasta fila n")
        print("   [4] Comparar rendimiento del Factorial (Iterativo vs Recursivo)")
        print("   [5] Ejecutar batería de 5 pruebas automáticas (Requisito de la guía)")
        print("   [6] Salir del programa")
        print("-" * 80)
        
        opcion = input("   Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            print("\n--- CALCULADORA DE PERMUTACIONES ---")
            n = solicitar_entero("   Ingrese el valor total del conjunto (n): ")
            r = solicitar_entero("   Ingrese el tamaño del subconjunto (r): ")
            rec = input("   ¿Desea usar algoritmo recursivo? (s/n): ").strip().lower() == 's'
            mostrar_problema_1(n, r, usar_recursivo=rec)
            
        elif opcion == "2":
            print("\n--- CALCULADORA DE COMBINACIONES ---")
            n = solicitar_entero("   Ingrese el valor total del conjunto (n): ")
            r = solicitar_entero("   Ingrese el tamaño del subconjunto (r): ")
            mostrar_problema_2(n, r)
            
        elif opcion == "3":
            print("\n--- GENERADOR DEL TRIÁNGULO DE PASCAL ---")
            n = solicitar_entero("   Ingrese hasta qué fila (n) desea construir el triángulo: ")
            imprimir_triangulo_pascal_completo(n)
            
        elif opcion == "4":
            print("\n--- COMPARATIVA DE RENDIMIENTO ---")
            n_grande = solicitar_entero("   Ingrese un número grande para evaluar el tiempo (ej. 500): ")
            comparar_extension_opcional_p1(n_grande)
            
        elif opcion == "5":
            print("\n--- EJECUCIÓN DE PRUEBAS DE LA GUÍA ---")
            comparar_casos_permutaciones()
            ejecutar_bateria_pruebas_automaticas()
            
        elif opcion == "6":
            print("\n   ¡Gracias por utilizar el sistema combinatorio! Finalizando ejecución...")
            print("#"*80 + "\n")
            break
        else:
            print("   [OPCIÓN INCORRECTA]: Seleccione un número válido entre 1 y 6.")
            
        input("\n   Presione ENTER para regresar al menú principal...")


if __name__ == "__main__":
    menu_interactivo()
