# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) CREAR NODO
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def crear_nodo(dato=None, nodo_izq=None, nodo_der=None):
    return {
        "dato": dato,
        "nodo_izq": nodo_izq,
        "nodo_der": nodo_der
    }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2) AGREGAR UN NODO AL ARBOL BINARIO
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def agregar_nodo(nodo, nodo_nuevo):
    if nodo["dato"] is None:
        nodo["dato"] = nodo_nuevo["dato"]
        nodo["nodo_izq"] = nodo_nuevo["nodo_izq"]
        nodo["nodo_der"] = nodo_nuevo["nodo_der"]
    else:
        if nodo_nuevo["dato"] < nodo["dato"]:
            if nodo["nodo_izq"] is None:
                nodo["nodo_izq"] = nodo_nuevo
            else:
                agregar_nodo(nodo["nodo_izq"], nodo_nuevo)
        elif nodo_nuevo["dato"] > nodo["dato"]:
            if nodo["nodo_der"] is None:
                nodo["nodo_der"] = nodo_nuevo
            else:
                agregar_nodo(nodo["nodo_der"], nodo_nuevo)
        else:
            print(f"Se descarta dato duplicado {nodo_nuevo['dato']}")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3) LEER UN ARBOL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.1) IN ORDER
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_arbol_in_orden(nodo):
    if (nodo is None):
        return []
    izq = leer_arbol_pre_orden(nodo["nodo_izq"])
    der = leer_arbol_pre_orden(nodo["nodo_der"])
    return izq + [nodo["dato"]] + der


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.2) PRE ORDER
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_arbol_pre_orden(nodo):
    if (nodo is None):
        return []
    izq = leer_arbol_pre_orden(nodo["nodo_izq"])
    der = leer_arbol_pre_orden(nodo["nodo_der"])
    return [nodo["dato"]] + izq + der


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.3) POST ORDER
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_arbol_post_orden(nodo):
    if (nodo is None):
        return []
    izq = leer_arbol_pre_orden(nodo["nodo_izq"])
    der = leer_arbol_pre_orden(nodo["nodo_der"])
    return izq + der + [nodo["dato"]]


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4) BUSCAR UN NODO EN EL ARBOL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def buscar_nodo(nodo, dato):
    if nodo["dato"] is None:
        return None
    else:
        if dato < nodo["dato"]:
            return buscar_nodo(nodo["nodo_izq"], dato)
        elif dato > nodo["dato"]:
            return buscar_nodo(nodo["nodo_der"], dato)
        else:
            return nodo


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5) ELIMINAR UN NODO EN EL ARBOL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def eliminar_nodo(nodo, dato):
    if nodo is None:
        return None

    if dato < nodo["dato"]:
        nodo["nodo_izq"] = eliminar_nodo(nodo["nodo_izq"], dato)
    elif dato > nodo["dato"]:
        nodo["nodo_der"] = eliminar_nodo(nodo["nodo_der"], dato)
    else:
        # Caso 1: sin hijos
        if nodo["nodo_izq"] is None and nodo["nodo_der"] is None:
            return None
        # Caso 2: un hijo
        elif nodo["nodo_izq"] is None:
            return nodo["nodo_der"]
        elif nodo["nodo_der"] is None:
            return nodo["nodo_izq"]
        # Caso 3: dos hijos
        sucesor = nodo_minimo(nodo["nodo_der"])
        nodo["dato"] = sucesor["dato"]
        nodo["nodo_der"] = eliminar_nodo(nodo["nodo_der"], sucesor["dato"])

    return nodo


def nodo_minimo(nodo):
    actual = nodo
    while actual["nodo_izq"] is not None:
        actual = actual["nodo_izq"]
    return actual


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6) CALCULAR GRADO ARBOL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calcular_grado_nodo(nodo):
    grado_nodo = 0
    if nodo["nodo_izq"] is not None:
        grado_nodo += 1
    if nodo["nodo_der"] is not None:
        grado_nodo += 1
    return grado_nodo


def calcular_grado_arbol_post_orden(nodo, grado_max=0):
    if (nodo is None):
        return 0
    calcular_grado_arbol_post_orden(nodo["nodo_izq"], grado_max)
    calcular_grado_arbol_post_orden(nodo["nodo_der"], grado_max)
    return max(grado_max, calcular_grado_nodo(nodo))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6) CALCULAR PESO ARBOL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calcular_peso_post_orden(nodo):
    if (nodo is None):
        return 0
    izq = calcular_peso_post_orden(nodo["nodo_izq"])
    der = calcular_peso_post_orden(nodo["nodo_der"])
    return izq + der + 1
