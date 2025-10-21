#---------- PARCIAL 2 ---------
#Autor : juan jose herrera largo 

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS 
# ===========================================================================
import os 
def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones matemáticas con validación.
    
    Args:
        operacion: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
        a: Primer número (int o float)
        b: Segundo número (int o float)x
    
    Returns:
        float: Resultado con 2 decimales de precisión
    
    Raises:
        ValueError: Si la operación es inválida o tipos incorrectos
        ZeroDivisionError: Si intenta dividir por cero
    """

    #  Validar tipos de datos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los parámetros deben ser numéricos (int o float)")

    #  Definir operaciones válidas
    operaciones_validas = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multiplicacion": lambda x, y: x * y,
        "division": lambda x, y: x / y,
        "potencia": lambda x, y: x ** y,
        "modulo": lambda x, y: x % y
    }

    #  Validar que la operación exista
    if operacion not in operaciones_validas:
        raise ValueError(
            f"Operación inválida: '{operacion}'. Operaciones válidas: suma, resta, multiplicacion, division, potencia, modulo"
        )

    #  Evitar división o módulo entre cero
    if operacion in ("division", "modulo") and b == 0:
        raise ZeroDivisionError(f"No se puede realizar {operacion} por cero")

    #  Calcular resultado
    resultado = operaciones_validas[operacion](a, b)

    #  Retornar con 2 decimales
    return round(resultado, 2)

# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES 
# ===========================================================================

class ValidadorPassword:
    """Validador de contraseñas con reglas configurables."""
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        """
        Inicializa el validador con reglas específicas.
        """
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        self.caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        Retorna (True, []) si cumple todo,
        o (False, [lista de errores]) si no cumple alguna condición.
        """
        errores = []

        #  Validar tipo
        if not isinstance(password, str):
            return (False, ["La contraseña debe ser una cadena de texto (str)"])

        #  Longitud mínima
        if len(password) < self.min_longitud:
            errores.append(f"Longitud mínima no cumplida (mínimo {self.min_longitud} caracteres)")

        #  Mayúscula
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Falta al menos una letra mayúscula")

        #  Minúscula
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Falta al menos una letra minúscula")

        #  Número
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Falta al menos un número")

        #  Carácter especial
        if self.requiere_especial and not any(c in self.caracteres_especiales for c in password):
            errores.append("Falta al menos un carácter especial")

        #  Resultado final
        if errores:
            return (False, errores)
        return (True, [])

    def es_fuerte(self, password):
        """
        Determina si el password es fuerte:
        - Mínimo 12 caracteres
        - Contiene mayúsculas, minúsculas, números y caracteres especiales
        """
        return (
            isinstance(password, str)
            and len(password) >= 12
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in self.caracteres_especiales for c in password)
        )


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS 
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario.
        Estructura: {codigo: {'nombre', 'precio', 'cantidad', 'categoria'}}
        """
        # TODO: Inicializar estructuras de datos
        self.inventario = {}
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un producto al inventario.
        
        Raises:
            ValueError: Si el código ya existe
        """
        # TODO: Implementar
        if codigo in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' ya existe.")
        
        self.inventario[codigo] = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad),
            "categoria": categoria
        }
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        
        Args:
            cantidad_cambio: Positivo para añadir, negativo para reducir
        
        Raises:
            ValueError: Si producto no existe o stock resultante sería negativo
        """
        # TODO: Implementar
        if codigo not in self.inventario:
            raise ValueError(f"El producto '{codigo}' no existe en el inventario.")
        
        nueva_cantidad = self.inventario[codigo]["cantidad"] + cantidad_cambio
        if nueva_cantidad < 0:
            raise ValueError("El stock no puede ser negativo.")
        
        self.inventario[codigo]["cantidad"] = nueva_cantidad
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Returns:
            list: Lista de tuplas (codigo, nombre, precio)
        """
        # TODO: Implementar
        return [
            (codigo, datos["nombre"], datos["precio"])
            for codigo, datos in self.inventario.items()
            if datos["categoria"].lower() == categoria.lower()
        ]
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite.
        
        Returns:
            dict: {codigo: cantidad} de productos bajo el límite
        """
        # TODO: Implementar
        return {
            codigo: datos["cantidad"]
            for codigo, datos in self.inventario.items()
            if datos["cantidad"] < limite
        }
    
    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de (precio * cantidad) de todos los productos
        """
        # TODO: Implementar
        return sum(
            datos["precio"] * datos["cantidad"]
            for datos in self.inventario.values()
        )
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        
        Returns:
            list: Lista de tuplas (codigo, valor_total) ordenadas descendentemente
        """
        # TODO: Implementar
        productos_valorados = [
            (codigo, datos["precio"] * datos["cantidad"])
            for codigo, datos in self.inventario.items()
        ]
        productos_ordenados = sorted(
            productos_valorados,
            key=lambda x: x[1],
            reverse=True
        )
        return productos_ordenados[:n]
    
    
# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si divisible por 100: no bisiesto
    - EXCEPTO si divisible por 400: bisiesto
    
    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False


def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    
    Args:
        mes: Número del mes (1-12)
        anio: Año (considera bisiestos)
    
    Returns:
        int: Número de días en el mes
    
    Raises:
        ValueError: Si mes es inválido (no está entre 1 y 12)
    """
    if mes < 1 or mes > 12:
        raise ValueError("Mes inválido. Debe estar entre 1 y 12.")

    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_por_mes[mes]


def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    
    Args:
        mes: Mes (1-12)
        anio: Año
        dia_inicio: Día de la semana del primer día (0=Lunes, 6=Domingo)
    
    Returns:
        str: Calendario formateado
        
    Formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    encabezado = "Lu Ma Mi Ju Vi Sa Do"
    calendario = encabezado + "\n"

    # Asegurar que el día de inicio esté entre 0 y 6
    dia_inicio = dia_inicio % 7

    dias = dias_en_mes(mes, anio)
    calendario += "   " * dia_inicio  # Espacios iniciales

    dia_actual = 1
    posicion = dia_inicio

    while dia_actual <= dias:
        calendario += f"{dia_actual:2d}"
        if posicion != 6:
            calendario += " "  # Espacio entre días

        dia_actual += 1
        posicion = (posicion + 1) % 7

        if posicion == 0 and dia_actual <= dias:
            calendario += "\n"

    return calendario


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas.
    
    Args:
        ventas: Lista de dicts con 'producto', 'cantidad', 'precio', 'descuento'
    
    Returns:
        dict: {
            'total_ventas': float,
            'promedio_por_venta': float,
            'producto_mas_vendido': str,
            'venta_mayor': dict,
            'total_descuentos': float
        }
    """
    if not ventas:
        return {
            'total_ventas': 0.0,
            'promedio_por_venta': 0.0,
            'producto_mas_vendido': None,
            'venta_mayor': None,
            'total_descuentos': 0.0
        }

    total_ventas = 0
    total_descuentos = 0
    cantidad_por_producto = {}
    venta_mayor = None
    valor_max = 0

    for venta in ventas:
        cantidad = venta['cantidad']
        precio = venta['precio']
        descuento = venta['descuento']
        producto = venta['producto']

        valor = cantidad * precio * (1 - descuento)
        ahorro = cantidad * precio * descuento

        total_ventas += valor
        total_descuentos += ahorro
        cantidad_por_producto[producto] = cantidad_por_producto.get(producto, 0) + cantidad

        if valor > valor_max:
            valor_max = valor
            venta_mayor = venta

    producto_mas_vendido = max(cantidad_por_producto, key=cantidad_por_producto.get)
    promedio_por_venta = total_ventas / len(ventas)

    return {
        'total_ventas': round(total_ventas, 2),
        'promedio_por_venta': round(promedio_por_venta, 2),
        'producto_mas_vendido': producto_mas_vendido,
        'venta_mayor': venta_mayor,
        'total_descuentos': round(total_descuentos, 2)
    }


def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    
    Returns:
        dict: {
            'secuencias_ascendentes': int,
            'secuencias_descendentes': int,
            'longitud_max_ascendente': int,
            'longitud_max_descendente': int,
            'numeros_repetidos': dict
        }
    """
    if not numeros:
        return {
            'secuencias_ascendentes': 0,
            'secuencias_descendentes': 0,
            'longitud_max_ascendente': 0,
            'longitud_max_descendente': 0,
            'numeros_repetidos': {}
        }

    asc_actual = desc_actual = 1
    max_asc = max_desc = 1
    sec_asc = sec_desc = 0
    conteo = {}

    for i in range(1, len(numeros)):
        conteo[numeros[i - 1]] = conteo.get(numeros[i - 1], 0) + 1

        if numeros[i] > numeros[i - 1]:
            asc_actual += 1
            desc_actual = 1
            if asc_actual == 2:
                sec_asc += 1
        elif numeros[i] < numeros[i - 1]:
            desc_actual += 1
            asc_actual = 1
            if desc_actual == 2:
                sec_desc += 1
        else:
            asc_actual = desc_actual = 1

        max_asc = max(max_asc, asc_actual)
        max_desc = max(max_desc, desc_actual)

    conteo[numeros[-1]] = conteo.get(numeros[-1], 0) + 1
    repetidos = {num: c for num, c in conteo.items() if c > 1}

    return {
        'secuencias_ascendentes': sec_asc,
        'secuencias_descendentes': sec_desc,
        'longitud_max_ascendente': max_asc,
        'longitud_max_descendente': max_desc,
        'numeros_repetidos': repetidos
    }


def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Args:
        principal: Monto inicial
        tasa_anual: Tasa de interés (0.05 para 5%)
        anios: Número de años
        aporte_anual: Aporte adicional al inicio de cada año
    
    Returns:
        list: Lista de dicts con 'anio', 'balance', 'interes_ganado'
    """
    resultados = []
    balance = principal

    for anio in range(1, anios + 1):
        balance += aporte_anual
        interes = balance * tasa_anual
        balance += interes

        resultados.append({
            'anio': anio,
            'balance': round(balance, 2),
            'interes_ganado': round(interes, 2)
        })

    return resultados


from datetime import datetime, timedelta

# =====================================================================
# EXCEPCIONES PERSONALIZADAS
# =====================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")


# =====================================================================
# SISTEMA BIBLIOTECA
# =====================================================================

class SistemaBiblioteca:
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.contador_prestamos = 0

    # ==================== CATÁLOGO ====================

    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
            raise ValueError("ISBN debe ser un string de 13 dígitos")
        if not titulo or not autor:
            raise ValueError("Título y autor no pueden estar vacíos")
        if not (1000 <= anio <= datetime.now().year):
            raise ValueError("Año fuera de rango válido")
        if copias < 1:
            raise ValueError("Debe haber al menos una copia")
        if isbn in self.catalogo:
            raise KeyError("El libro ya existe en el catálogo")

        self.catalogo[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "categoria": categoria,
            "copias_total": copias,
            "copias_disponibles": copias,
            "prestamos_hist": 0
        }

    def actualizar_copias(self, isbn, cantidad_cambio):
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        nuevo_total = self.catalogo[isbn]["copias_total"] + cantidad_cambio
        if nuevo_total < 0:
            raise ValueError("No puede haber copias negativas")
        self.catalogo[isbn]["copias_total"] = nuevo_total
        self.catalogo[isbn]["copias_disponibles"] = max(
            0, self.catalogo[isbn]["copias_disponibles"] + cantidad_cambio
        )

    def buscar_libros(self, criterio="titulo", valor="", categoria=None):
        resultado = []
        for isbn, libro in self.catalogo.items():
            if categoria and libro["categoria"].lower() != categoria.lower():
                continue
            if valor.lower() in str(libro[criterio]).lower():
                resultado.append({**libro, "isbn": isbn})
        return resultado

    # ==================== USUARIOS ====================

    def registrar_usuario(self, id_usuario, nombre, email):
        if id_usuario in self.usuarios:
            raise ValueError("Usuario ya registrado")
        if not nombre:
            raise ValueError("Nombre vacío")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")

        self.usuarios[id_usuario] = {
            "nombre": nombre,
            "email": email,
            "fecha_registro": datetime.now(),
            "prestamos_activos": [],
            "historial": [],
            "multas_pendientes": 0.0
        }

    def obtener_estado_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        u = self.usuarios[id_usuario]
        puede_prestar = (
            len(u["prestamos_activos"]) < self.limite_prestamos
            and u["multas_pendientes"] <= 50
        )
        return {
            "nombre": u["nombre"],
            "prestamos_activos": len(u["prestamos_activos"]),
            "puede_prestar": puede_prestar,
            "multas_pendientes": u["multas_pendientes"]
        }

    # ==================== PRÉSTAMOS ====================

    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]

        if libro["copias_disponibles"] == 0:
            raise LibroNoDisponible(isbn, libro["titulo"])
        if len(usuario["prestamos_activos"]) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        if usuario["multas_pendientes"] > 50:
            raise ValueError("El usuario tiene multas pendientes mayores a $50")

        self.contador_prestamos += 1
        id_prestamo = f"P{self.contador_prestamos:04d}"
        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)

        self.prestamos[id_prestamo] = {
            "isbn": isbn,
            "id_usuario": id_usuario,
            "fecha_prestamo": fecha_prestamo,
            "fecha_vencimiento": fecha_vencimiento,
            "fecha_devolucion": None,
            "multa": 0.0
        }

        libro["copias_disponibles"] -= 1
        libro["prestamos_hist"] += 1
        usuario["prestamos_activos"].append(id_prestamo)
        usuario["historial"].append(id_prestamo)

        return id_prestamo

    def devolver_libro(self, id_prestamo):
        if id_prestamo not in self.prestamos:
            raise KeyError("Préstamo no encontrado")
        prestamo = self.prestamos[id_prestamo]
        if prestamo["fecha_devolucion"] is not None:
            raise ValueError("El libro ya fue devuelto")

        prestamo["fecha_devolucion"] = datetime.now()
        retraso = (prestamo["fecha_devolucion"] - prestamo["fecha_vencimiento"]).days
        dias_retraso = max(0, retraso)
        multa = dias_retraso * self.multa_por_dia
        prestamo["multa"] = multa

        libro = self.catalogo[prestamo["isbn"]]
        libro["copias_disponibles"] += 1

        usuario = self.usuarios[prestamo["id_usuario"]]
        if id_prestamo in usuario["prestamos_activos"]:
            usuario["prestamos_activos"].remove(id_prestamo)
        if multa > 0:
            usuario["multas_pendientes"] += multa

        return {
            "dias_retraso": dias_retraso,
            "multa": multa,
            "mensaje": "Devolución exitosa" if multa == 0 else f"Con multa de ${multa}"
        }

    def renovar_prestamo(self, id_prestamo):
        if id_prestamo not in self.prestamos:
            raise KeyError("Préstamo no existe")
        p = self.prestamos[id_prestamo]
        if p["fecha_devolucion"] is not None:
            raise ValueError("El préstamo ya fue devuelto")
        if datetime.now() > p["fecha_vencimiento"]:
            dias = (datetime.now() - p["fecha_vencimiento"]).days
            raise PrestamoVencido(id_prestamo, dias)

        p["fecha_vencimiento"] += timedelta(days=self.dias_prestamo)
        return f"Préstamo {id_prestamo} renovado hasta {p['fecha_vencimiento'].date()}"

    # ==================== REPORTES ====================

    def libros_mas_prestados(self, n=10):
        ranking = sorted(
            [(isbn, d["titulo"], d["prestamos_hist"]) for isbn, d in self.catalogo.items()],
            key=lambda x: x[2],
            reverse=True
        )
        return ranking[:n]

    def usuarios_mas_activos(self, n=5):
        ranking = sorted(
            [(uid, u["nombre"], len(u["historial"])) for uid, u in self.usuarios.items()],
            key=lambda x: x[2],
            reverse=True
        )
        return ranking[:n]

    def estadisticas_categoria(self, categoria):
        libros_cat = [d for d in self.catalogo.values() if d["categoria"].lower() == categoria.lower()]
        if not libros_cat:
            return {}

        total_libros = len(libros_cat)
        total_copias = sum(l["copias_total"] for l in libros_cat)
        copias_prestadas = sum(l["copias_total"] - l["copias_disponibles"] for l in libros_cat)
        tasa = (copias_prestadas / total_copias) * 100 if total_copias else 0
        mas_popular = max(libros_cat, key=lambda x: x["prestamos_hist"])["titulo"]

        return {
            "total_libros": total_libros,
            "total_copias": total_copias,
            "copias_prestadas": copias_prestadas,
            "tasa_prestamo": round(tasa, 2),
            "libro_mas_popular": mas_popular
        }

    def prestamos_vencidos(self):
        lista = []
        for pid, p in self.prestamos.items():
            if p["fecha_devolucion"] is None and datetime.now() > p["fecha_vencimiento"]:
                dias_retraso = (datetime.now() - p["fecha_vencimiento"]).days
                multa = dias_retraso * self.multa_por_dia
                lista.append({
                    "id_prestamo": pid,
                    "isbn": p["isbn"],
                    "titulo": self.catalogo[p["isbn"]]["titulo"],
                    "id_usuario": p["id_usuario"],
                    "dias_retraso": dias_retraso,
                    "multa_acumulada": multa
                })
        return lista

    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        multas = []
        for p in self.prestamos.values():
            if p["multa"] > 0:
                fecha = p["fecha_devolucion"] or datetime.now()
                if (not fecha_inicio or fecha >= fecha_inicio) and (not fecha_fin or fecha <= fecha_fin):
                    multas.append(p["multa"])
        total = sum(multas)
        promedio = total / len(multas) if multas else 0
        return {
            "total_multas": total,
            "prestamos_con_multa": len(multas),
            "promedio_multa": round(promedio, 2)
        }

    # ==================== UTILIDADES ====================

    def exportar_catalogo(self, archivo="catalogo.txt"):
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                for isbn, d in self.catalogo.items():
                    linea = f"{isbn}|{d['titulo']}|{d['autor']}|{d['anio']}|{d['categoria']}|{d['copias_total']}\n"
                    f.write(linea)
        except Exception as e:
            print(f"Error al exportar catálogo: {e}")

    def importar_catalogo(self, archivo="catalogo.txt"):
        resultado = {"exitosos": 0, "errores": []}
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for i, linea in enumerate(f, start=1):
                    try:
                        isbn, titulo, autor, anio, categoria, copias = linea.strip().split("|")
                        if isbn not in self.catalogo:
                            self.agregar_libro(isbn, titulo, autor, int(anio), categoria, int(copias))
                            resultado["exitosos"] += 1
                    except Exception as e:
                        resultado["errores"].append((i, str(e)))
        except FileNotFoundError:
            print("Archivo no encontrado")
        return resultado
    

# ===========================================================================
# GESTION DE RESTAURANTE
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        self.codigo_plato = codigo_plato
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")


class MesaNoDisponible(ErrorRestaurante):
    """Se lanza cuando la mesa está ocupada."""
    def __init__(self, numero_mesa, hora_disponible=None):
        self.numero_mesa = numero_mesa
        self.hora_disponible = hora_disponible
        msg = f"Mesa {numero_mesa} no disponible"
        if hora_disponible:
            msg += f"; disponible a las {hora_disponible}"
        super().__init__(msg)


class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    def __init__(self, numero_mesa, capacidad, comensales):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.comensales = comensales
        super().__init__(f"Mesa {numero_mesa} capacidad {capacidad}, comensales: {comensales}")


class PedidoInvalido(ErrorRestaurante):
    """Se lanza para pedidos con problemas."""
    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"Pedido inválido: {razon}")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""

    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.
        """
        # menú: codigo -> {nombre, categoria, precio, disponible, vendidos}
        self.menu = {}

        # mesas: numero -> {capacidad, ocupada, hora_reserva (str/None), comensales}
        self.mesas = {}
        for n in range(1, num_mesas + 1):
            self.mesas[n] = {"capacidad": 4, "ocupada": False, "hora_reserva": None, "comensales": 0}

        # pedidos: id_pedido -> {mesa, items: {codigo: qty}, creado, pagado, totals...}
        self.pedidos = {}
        self._contador_pedidos = 0

        # ventas diarias acumuladas (para reportes rápidos)
        # las ventas reales se reconducen desde pedidos pagados
        self.tasa_impuesto = float(tasa_impuesto)
        self.propina_sugerida = float(propina_sugerida)

    # --------------------- GESTIÓN DE MENÚ ---------------------

    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        Raises ValueError o KeyError si invalido o duplicado.
        """
        if not codigo or not isinstance(codigo, str):
            raise ValueError("Código inválido")
        if codigo in self.menu:
            raise KeyError(f"Código {codigo} ya existe en el menú")
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido")
        if precio is None or not (isinstance(precio, int) or isinstance(precio, float)) or precio < 0:
            raise ValueError("Precio inválido")
        self.menu[codigo] = {
            "nombre": nombre,
            "categoria": categoria or "",
            "precio": float(precio),
            "disponible": True,
            "vendidos": 0
        }

    def cambiar_disponibilidad(self, codigo, disponible):
        """
        Cambia disponibilidad de un plato.
        """
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        self.menu[codigo]["disponible"] = bool(disponible)

    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Busca platos por criterios. Solo devuelve platos disponibles.
        """
        resultados = []
        for codigo, d in self.menu.items():
            if not d["disponible"]:
                continue
            if categoria and d["categoria"].lower() != categoria.lower():
                continue
            if precio_max is not None and d["precio"] > precio_max:
                continue
            resultados.append({
                "codigo": codigo,
                "nombre": d["nombre"],
                "categoria": d["categoria"],
                "precio": d["precio"],
                "disponible": d["disponible"]
            })
        return resultados

    # --------------------- GESTIÓN DE MESAS ---------------------

    def configurar_mesa(self, numero, capacidad):
        """
        Configura capacidad de una mesa.
        """
        if not isinstance(numero, int) or numero < 1:
            raise ValueError("Número de mesa inválido")
        if not isinstance(capacidad, int) or capacidad < 1:
            raise ValueError("Capacidad inválida")
        if numero not in self.mesas:
            # añadir nueva mesa
            self.mesas[numero] = {"capacidad": capacidad, "ocupada": False, "hora_reserva": None, "comensales": 0}
        else:
            self.mesas[numero]["capacidad"] = capacidad

    def reservar_mesa(self, numero, comensales, hora=None):
        """
        Reserva una mesa.
        """
        if numero not in self.mesas:
            raise ValueError("Mesa no existe")
        mesa = self.mesas[numero]
        if mesa["ocupada"]:
            raise MesaNoDisponible(numero, mesa.get("hora_reserva"))
        if comensales > mesa["capacidad"]:
            raise CapacidadExcedida(numero, mesa["capacidad"], comensales)
        mesa["ocupada"] = True
        mesa["hora_reserva"] = hora or datetime.now().strftime("%H:%M")
        mesa["comensales"] = comensales
        return True

    def liberar_mesa(self, numero):
        """
        Libera una mesa.
        """
        if numero not in self.mesas:
            raise ValueError("Mesa no existe")
        mesa = self.mesas[numero]
        if not mesa["ocupada"]:
            raise ValueError("Mesa no está ocupada")
        mesa["ocupada"] = False
        mesa["hora_reserva"] = None
        mesa["comensales"] = 0
        return True

    def mesas_disponibles(self, comensales=1):
        """
        Lista mesas disponibles para N comensales.
        """
        disponibles = []
        for numero, mesa in self.mesas.items():
            if not mesa["ocupada"] and mesa["capacidad"] >= comensales:
                disponibles.append(numero)
        return disponibles

    # --------------------- GESTIÓN DE PEDIDOS ---------------------

    def _generar_id_pedido(self):
        self._contador_pedidos += 1
        return f"R{self._contador_pedidos:06d}"

    def crear_pedido(self, numero_mesa):
        """
        Crea un nuevo pedido para una mesa.
        """
        if numero_mesa not in self.mesas:
            raise ValueError("Mesa inexistente")
        mesa = self.mesas[numero_mesa]
        if not mesa["ocupada"]:
            raise ValueError("Mesa no está ocupada")
        id_pedido = self._generar_id_pedido()
        self.pedidos[id_pedido] = {
            "mesa": numero_mesa,
            "items": {},  # codigo -> cantidad
            "creado": datetime.now(),
            "pagado": False,
            "subtotal": 0.0,
            "impuesto": 0.0,
            "propina": 0.0,
            "total": 0.0
        }
        return id_pedido

    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """
        Agrega items al pedido.
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("Pedido ya pagado")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        plato = self.menu[codigo_plato]
        if not plato["disponible"]:
            raise ValueError("Plato no disponible")
        if cantidad < 1:
            raise ValueError("Cantidad inválida")
        pedido["items"][codigo_plato] = pedido["items"].get(codigo_plato, 0) + int(cantidad)
        return True

    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """
        Calcula total del pedido.
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        subtotal = 0.0
        for codigo, qty in pedido["items"].items():
            precio = self.menu[codigo]["precio"]
            subtotal += precio * qty
        impuesto = subtotal * self.tasa_impuesto
        propina_pct = (self.propina_sugerida if propina_porcentaje is None else propina_porcentaje)
        propina = subtotal * propina_pct
        total = subtotal + impuesto + propina
        # actualizar campos (no marca como pagado)
        pedido["subtotal"] = round(subtotal, 2)
        pedido["impuesto"] = round(impuesto, 2)
        pedido["propina"] = round(propina, 2)
        pedido["total"] = round(total, 2)
        return {
            "subtotal": pedido["subtotal"],
            "impuesto": pedido["impuesto"],
            "propina": pedido["propina"],
            "total": pedido["total"]
        }

    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """
        Procesa pago del pedido.
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("Pedido ya pagado")
        totals = self.calcular_total(id_pedido, propina_porcentaje)
        pedido["pagado"] = True
        # actualizar contadores de vendidos por plato
        for codigo, qty in pedido["items"].items():
            self.menu[codigo]["vendidos"] += qty
        return totals

    # --------------------- REPORTES Y ESTADÍSTICAS ---------------------

    def platos_mas_vendidos(self, n=5):
        ranking = sorted(
            [(cod, d["nombre"], d["vendidos"]) for cod, d in self.menu.items()],
            key=lambda x: x[2],
            reverse=True
        )
        return ranking[:n]

    def ventas_por_categoria(self):
        """
        Calcula ventas totales por categoría considerando pedidos pagados.
        """
        ventas_cat = {}
        for pedido in self.pedidos.values():
            if not pedido["pagado"]:
                continue
            for codigo, qty in pedido["items"].items():
                cat = self.menu[codigo]["categoria"]
                ventas_cat[cat] = ventas_cat.get(cat, 0.0) + self.menu[codigo]["precio"] * qty
        # redondeo
        return {k: round(v, 2) for k, v in ventas_cat.items()}

    def reporte_ventas_dia(self, fecha=None):
        """
        Genera reporte de ventas del día (por fecha; si None -> hoy).
        """
        fecha = fecha or datetime.now().date()
        total_ventas = 0.0
        total_impuestos = 0.0
        total_propinas = 0.0
        pedidos_contados = 0
        por_categoria = {}

        for pedido in self.pedidos.values():
            if not pedido["pagado"]:
                continue
            creado = pedido["creado"].date()
            if creado != fecha:
                continue
            pedidos_contados += 1
            total_ventas += pedido["subtotal"]
            total_impuestos += pedido["impuesto"]
            total_propinas += pedido["propina"]
            for codigo, qty in pedido["items"].items():
                cat = self.menu[codigo]["categoria"]
                por_categoria[cat] = por_categoria.get(cat, 0.0) + self.menu[codigo]["precio"] * qty

        return {
            "fecha": fecha.isoformat(),
            "pedidos": pedidos_contados,
            "ventas": round(total_ventas, 2),
            "impuestos": round(total_impuestos, 2),
            "propinas": round(total_propinas, 2),
            "por_categoria": {k: round(v, 2) for k, v in por_categoria.items()}
        }

    def estado_restaurante(self):
        """
        Resumen actual: mesas libres/ocupadas y pedidos abiertos.
        """
        mesas_ocupadas = [n for n, m in self.mesas.items() if m["ocupada"]]
        mesas_libres = [n for n, m in self.mesas.items() if not m["ocupada"]]
        pedidos_abiertos = [pid for pid, p in self.pedidos.items() if not p["pagado"]]
        return {
            "mesas_ocupadas": mesas_ocupadas,
            "mesas_libres": mesas_libres,
            "pedidos_abiertos": pedidos_abiertos,
            "total_menu": len(self.menu)
        }

    # --------------------- UTILIDADES ---------------------

    def exportar_menu(self, archivo='menu.txt'):
        """
        Exporta menú a archivo de texto.
        Formato: Codigo|Nombre|Categoria|Precio|Disponible
        """
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                for cod, d in self.menu.items():
                    linea = f"{cod}|{d['nombre']}|{d['categoria']}|{d['precio']}|{int(d['disponible'])}\n"
                    f.write(linea)
            return True
        except Exception as e:
            return False

    def importar_menu(self, archivo='menu.txt'):
        """
        Importa menú desde archivo de texto.
        Retorna {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        resultado = {"exitosos": 0, "errores": []}
        if not os.path.exists(archivo):
            resultado["errores"].append((0, "Archivo no encontrado"))
            return resultado
        with open(archivo, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split("|")
                if len(partes) != 5:
                    resultado["errores"].append((i, "Formato incorrecto"))
                    continue
                cod, nombre, categoria, precio_s, disp_s = partes
                try:
                    precio = float(precio_s)
                    disponible = bool(int(disp_s))
                    if cod in self.menu:
                        resultado["errores"].append((i, f"Código {cod} ya existe (saltado)"))
                        continue
                    self.menu[cod] = {
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": precio,
                        "disponible": disponible,
                        "vendidos": 0
                    }
                    resultado["exitosos"] += 1
                except Exception as e:
                    resultado["errores"].append((i, str(e)))
        return resultado


    

# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    # ===========================================================
    print("\nEjercicio 1: Calculadora Científica")
    # ===========================================================
    try:
        print(calculadora_cientifica("suma", 5, 3))          # 8.0
        print(calculadora_cientifica("resta", 10, 4))         # 6.0
        print(calculadora_cientifica("multiplicacion", 6, 7)) # 42.0
        print(calculadora_cientifica("division", 10, 2))      # 5.0
        print(calculadora_cientifica("potencia", 2, 3))       # 8.0
        print(calculadora_cientifica("modulo", 10, 3))        # 1.0
        
        # Casos de error
        try:
            calculadora_cientifica("raiz", 9, 2)
        except ValueError as e:
            print("Error esperado:", e)
            
        try:
            calculadora_cientifica("division", 10, 0)
        except ZeroDivisionError as e:
            print("Error esperado:", e)
    except Exception as e:
        print(" Error en pruebas de calculadora:", e)
    
    # ===========================================================
    print("\nEjercicio 2: Validador de Password")
    # ===========================================================
    try:
        validador = ValidadorPassword(min_longitud=8)
        print(validador.validar("Abc123!"))          # (False, ['Longitud mínima no cumplida'])
        print(validador.validar("Abc123!@"))         # (True, [])
        print(validador.validar("abcdefgh"))         # (False, [...])
        print(validador.es_fuerte("Abc123!@#$Xyz"))  # True
    except Exception as e:
        print(" Error en pruebas de ValidadorPassword:", e)
    
    # ===========================================================
    print("\nEjercicio 3: Gestor de Inventario")
    # ===========================================================
    try:
        inv = GestorInventario()
        inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
        inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
        inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")
        
        inv.actualizar_stock("P001", -3)  # reduce stock
        print(inv.productos_bajo_stock(10))  # {'P002': 5, 'P003': 8}
        print(inv.buscar_por_categoria("Accesorios"))  # [('P002', 'Mouse', 25.5), ('P003', 'Teclado', 85.0)]
        print(inv.valor_total_inventario())  # Total del inventario
        print(inv.top_productos(2))          # Top 2 productos más valiosos
    except Exception as e:
        print(" Error en pruebas de GestorInventario:", e)
    
    # ===========================================================
    print("\nEjercicio 4: Calendario")
    # ===========================================================
    try:
        print(es_bisiesto(2024))  # True
        print(es_bisiesto(2100))  # False
        print(es_bisiesto(2000))  # True
        
        print(dias_en_mes(2, 2024))  # 29
        print(dias_en_mes(2, 2023))  # 28
        
        print(generar_calendario(1, 2024, 0))  # Calendario enero 2024
    except Exception as e:
        print(" Error en pruebas de calendario:", e)
    
    # ===========================================================
    print("\nEjercicio 5: Análisis de Datos")
    # ===========================================================
    try:
        ventas = [
            {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
            {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
            {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
        ]
        print(analizar_ventas(ventas))
        
        numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
        print(encontrar_patrones(numeros))
        
        print(simular_crecimiento(1000, 0.05, 5, 100))
    except Exception as e:
        print("Error en pruebas de análisis de datos:", e)


# ==============================================================
# PRUEBA 1: AGREGAR LIBROS
# ==============================================================
def prueba_agregar_libros():
    print("\n" + "="*60)
    print(" TEST: Agregar Libros")
    print("="*60)

    biblioteca = SistemaBiblioteca()

    # Agregar libro válido
    biblioteca.agregar_libro("12345", "Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela", 3)
    assert "12345" in biblioteca.catalogo

    # Intentar agregar libro duplicado
    try:
        biblioteca.agregar_libro("12345", "Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela", 3)
    except ValueError:
        print("Detección correcta de ISBN duplicado")

    # ISBN inválido
    try:
        biblioteca.agregar_libro("", "Libro Inválido", "Autor", 2000, "Otro", 1)
    except ValueError:
        print("Detección de ISBN inválido")

    # Año inválido
    try:
        biblioteca.agregar_libro("99999", "Libro Futuro", "Autor", 3000, "Ciencia", 1)
    except ValueError:
        print("Detección de año inválido")

    print("Prueba completada")


# ==============================================================
# PRUEBA 2: REGISTRAR USUARIOS
# ==============================================================
def prueba_registrar_usuarios():
    print("\n" + "="*60)
    print(" TEST: Registrar Usuarios")
    print("="*60)

    biblioteca = SistemaBiblioteca()

    biblioteca.registrar_usuario("U001", "Juan", "juan@mail.com")
    assert "U001" in biblioteca.usuarios

    # Duplicado
    try:
        biblioteca.registrar_usuario("U001", "Juan", "juan@mail.com")
    except ValueError:
        print(" Usuario duplicado detectado")

    # Email inválido
    try:
        biblioteca.registrar_usuario("U002", "Pedro", "pedromail.com")
    except ValueError:
        print(" Email inválido detectado")

    print(" Prueba completada")


# ==============================================================
# PRUEBA 3: PRÉSTAMOS
# ==============================================================
def prueba_prestar_libros():
    print("\n" + "="*60)
    print(" TEST: Préstamos")
    print("="*60)

    biblioteca = SistemaBiblioteca(limite_prestamos=2)
    biblioteca.agregar_libro("111", "El Quijote", "Cervantes", 1605, "Novela", 1)
    biblioteca.registrar_usuario("U001", "Ana", "ana@mail.com")

    # Préstamo exitoso
    id_prestamo = biblioteca.prestar_libro("U001", "111")
    assert id_prestamo.startswith("P")

    # Intentar prestar libro sin copias
    try:
        biblioteca.prestar_libro("U001", "111")
    except LibroNoDisponible:
        print("Error de libro no disponible correcto")

    # Usuario no registrado
    try:
        biblioteca.prestar_libro("U999", "111")
    except UsuarioNoRegistrado:
        print("Error de usuario no registrado correcto")

    # Exceder límite
    biblioteca.agregar_libro("222", "La Odisea", "Homero", -700, "Épico", 1)
    biblioteca.agregar_libro("333", "Ilíada", "Homero", -800, "Épico", 1)
    biblioteca.prestar_libro("U001", "222")
    try:
        biblioteca.prestar_libro("U001", "333")
    except LimitePrestamosExcedido:
        print("Límite de préstamos excedido correcto")

    print("Prueba completada")


# ==============================================================
# PRUEBA 4: DEVOLUCIONES Y MULTAS
# ==============================================================
def prueba_devolver_libros():
    print("\n" + "="*60)
    print(" TEST: Devolución y Multas")
    print("="*60)

    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    biblioteca.agregar_libro("555", "Crónica de una muerte anunciada", "Gabo", 1981, "Novela", 1)
    biblioteca.registrar_usuario("U001", "Laura", "laura@mail.com")

    # Préstamo y devolución sin multa
    pid = biblioteca.prestar_libro("U001", "555")
    multa = biblioteca.devolver_libro(pid, datetime.now())
    assert multa == 0

    # Préstamo con retraso
    pid2 = biblioteca.prestar_libro("U001", "555")
    fecha_vencida = datetime.now() + timedelta(days=5)
    multa = biblioteca.devolver_libro(pid2, fecha_vencida)
    assert multa == 10  # 5 días * $2.0

    # Préstamo inexistente
    try:
        biblioteca.devolver_libro("P999999", datetime.now())
    except PrestamoVencido:
        pass
    except Exception:
        print(" Error de préstamo inexistente controlado")

    print("Prueba completada")


# ==============================================================
# PRUEBA 5: BÚSQUEDA DE LIBROS
# ==============================================================
def prueba_buscar_libros():
    print("\n" + "="*60)
    print(" TEST: Búsqueda de Libros")
    print("="*60)

    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("1", "El Principito", "Antoine", 1943, "Fantasía", 2)
    biblioteca.agregar_libro("2", "1984", "Orwell", 1949, "Distopía", 3)
    biblioteca.agregar_libro("3", "Animal Farm", "Orwell", 1945, "Satira", 1)

    assert len(biblioteca.buscar_libros(titulo="El")) == 1
    assert len(biblioteca.buscar_libros(autor="Orwell")) == 2
    assert len(biblioteca.buscar_libros(categoria="Satira")) == 1
    assert len(biblioteca.buscar_libros(titulo="Inexistente")) == 0

    print("Prueba completada")


# ==============================================================
# PRUEBA 6: EXCEPCIONES PERSONALIZADAS
# ==============================================================
def prueba_excepciones():
    print("\n" + "="*60)
    print(" TEST: Excepciones Personalizadas")
    print("="*60)

    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("1", "Libro", "Autor", 2000, "Drama", 0)
    biblioteca.registrar_usuario("U001", "Juan", "juan@mail.com")

    try:
        biblioteca.prestar_libro("U001", "2")
    except LibroNoEncontrado as e:
        print("LibroNoEncontrado lanzado:", e)

    try:
        biblioteca.prestar_libro("U001", "1")
    except LibroNoDisponible as e:
        print("LibroNoDisponible lanzado:", e)

    try:
        biblioteca.prestar_libro("U999", "1")
    except UsuarioNoRegistrado as e:
        print("UsuarioNoRegistrado lanzado:", e)

    print("Prueba completada")


# ==============================================================
# PRUEBA 7: REPORTE FINANCIERO
# ==============================================================
def prueba_reporte_financiero():
    print("\n" + "="*60)
    print(" TEST: Reporte Financiero")
    print("="*60)

    biblioteca = SistemaBiblioteca(multa_por_dia=1.5)
    biblioteca.agregar_libro("9", "Ensayo sobre la ceguera", "Saramago", 1995, "Ficción", 1)
    biblioteca.registrar_usuario("U001", "Luisa", "luisa@mail.com")

    pid = biblioteca.prestar_libro("U001", "9")
    biblioteca.devolver_libro(pid, datetime.now() + timedelta(days=3))
    reporte = biblioteca.reporte_financiero()

    assert reporte["total_multas"] >= 4.5
    print("Reporte financiero correcto")

    print("Prueba completada")


# ==============================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==============================================================
def ejecutar_todas_las_pruebas():
    print("\n" + "="*70)
    print(" SISTEMA DE BIBLIOTECA PRUEBAS ")
    print("="*70)

    pruebas = [
        prueba_agregar_libros,
        prueba_registrar_usuarios,
        prueba_prestar_libros,
        prueba_devolver_libros,
        prueba_buscar_libros,
        prueba_excepciones,
        prueba_reporte_financiero,
    ]

    exitosas = 0
    fallidas = 0

    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f" Error en {prueba.__name__}: {e}")
            fallidas += 1

    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f" Exitosas: {exitosas}/{len(pruebas)}")
    print(f" Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()


# ===========================================================================
# EJEMPLO / PRUEBAS BÁSICAS
# ===========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("=" * 70)
if __name__ == "__main__":
    rest = SistemaRestaurante(num_mesas=5)

    # Agregar platos
    rest.agregar_plato("P001", "Ceviche", "Mariscos", 18.0)
    rest.agregar_plato("P002", "Lomo Saltado", "Carnes", 22.0)
    rest.agregar_plato("P003", "Ensalada", "Vegetariano", 12.0)
    rest.agregar_plato("P004", "Papas Fritas", "Acompañamientos", 6.5)

    # Configurar mesas
    rest.configurar_mesa(1, 2)
    rest.configurar_mesa(2, 4)
    rest.configurar_mesa(3, 6)

    print("\nMesas disponibles para 4 comensales:", rest.mesas_disponibles(4))

    # Reservar mesa 2 para 3 comensales
    try:
        rest.reservar_mesa(2, 3, hora="20:00")
        print("Mesa 2 reservada")
    except Exception as e:
        print("Error reservar mesa:", e)

    # Crear pedido para la mesa 2
    pedido_id = rest.crear_pedido(2)
    print("Pedido creado:", pedido_id)

    # Agregar items
    rest.agregar_item(pedido_id, "P002", 2)  # 2 Lomo Saltado
    rest.agregar_item(pedido_id, "P004", 1)  # 1 Papas Fritas

    # Calcular y pagar
    totales = rest.calcular_total(pedido_id)
    print("Totales antes de pagar:", totales)
    pago = rest.pagar_pedido(pedido_id, propina_porcentaje=0.10)
    print("Pago realizado:", pago)

    # Estado y reportes
    print("Estado restaurante:", rest.estado_restaurante())
    print("Platos más vendidos:", rest.platos_mas_vendidos())
    print("Ventas por categoría:", rest.ventas_por_categoria())
    print("Reporte ventas hoy:", rest.reporte_ventas_dia())

    # Exportar e importar menu
    rest.exportar_menu("menu_test.txt")
    print("Importar resultado:", rest.importar_menu("menu_test.txt"))

    # Liberar mesa
    rest.liberar_mesa(2)
    print("Mesa 2 liberada")
    



