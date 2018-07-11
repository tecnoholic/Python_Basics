# EXAMEN INICIAL DE UN ARCHIVO DE DATOS CSV
# -----------------------------------------

# 1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS: Pandas, Seaborn Y Matplotlib:
# ---------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 2. CONVERTIMOS EL ARCHIVO CSV EN VARIABLES DEL TIPO DATAFRAME:
# --------------------------------------------------------------
# Éstas es la ruta del archivo:
ruta_del_archivo_original = 'C:\\Users\\Usuario\PYTHON\Data\\melb_data.csv'

# Nota: Si en la ruta del archivo aparece la secuencia '\u' o '\n' saldra un mensaje de
# error en el IDE de PyCharm debido es interpretado como un caracter de escape del tipo
# Unicode. La solución es añadir otra barra invertida '\' como se ha hecho arriba.

# Ésta es la variable DataFrame en la que lo hemos almacenado:
Datos_origen = pd.read_csv(ruta_del_archivo_original)
# Para leer una archivo Excel haríamos pd.read_excel()


# 3. INFORMACIÓN GENERAL SOBRE LOS DATOS DEL ARCHIVO:
# ---------------------------------------------------
print ("INFORMACIÓN GENERAL SOBRE EL ARCHIVO DE DATOS ORIGINAL:")
print ("-------------------------------------------------------")
# La instrucción que nos ofrece la información más general es el método .info():
print (Datos_origen.info())
# Incluye info sobre el número de filas y columnas, el tipo de datos utilizado y
# su cantidad, los valores NaN que hay en cada columna y el tamaño en disco del
# archivo.

# Otros métodos para extraer información similiar son los siguientes:
print ("El archivo de datos original es un tabla de ", Datos_origen.shape, "(filas,columnas)")
print ("Filas: ", len(Datos_origen), "Columnas: ", len(Datos_origen.columns))
print("El número total de celdas (datos) del archivo Dataframe es: ", Datos_origen.size, "(filas x columnas)")
print()
print ("El número de datos en cada columna es:")
print (Datos_origen.count())
print()
print ("Este es el tipo de datos que contiene:")
print()
print (Datos_origen.dtypes)
print ()


# 4. ECHAMOS UN VISTAZO A UN SUBCONJUNTO DE DATOS:
# ------------------------------------------------
print ("UN VISTAZO A UN SUBCONJUNTO DE DATOS")
print ("------------------------------------")
# Los Dataframe son objetos en forma de tabla cuya primera columna es el índice
# de la fila (numeros naturales desde el 0 en orden creciente)
print (" Las etiquetas de las columnas son: ", Datos_origen.columns)
print()

# Para ver las 5 primeras filas del archivo utilizamos el método .head():
print("Éste es el aspecto de las primeras filas de datos:")
print (Datos_origen.head(5))
# Si aparecen puntos suspensivos (...) indica que hay muchos datos en ese
# intervalo y que resultaría incomo verlos en una misma pantalla.
print()

# Viendo las primeras fil filas y las primeras col columnas:
# El método .loc accede por etiquetas y el método .iloc accede por índices:
print ("Define la subtabla que deseas ver:")
fil = int(input ("¿Cuántas filas deseas imprimir?: "))
col = int(input ("¿Cuántas columnas deseas imprimir?: "))
columnas=[]
for x in range(col):
    columnas.append(Datos_origen.columns[x])   # El método .append() añade una
                                               # columna al datafame.
print (Datos_origen.loc[0:fil-1, columnas])

# Viendo otra subtabla:
print (Datos_origen.loc[5:8, ['BuildingArea', 'YearBuilt']])
print()

# Si queremos exportar esos datos a un archivo .csv o xls utilizaremos:
Subdatos=Datos_origen.loc[5:8, ['BuildingArea', 'YearBuilt']]
Subdatos.to_csv('C:\\Users\\Usuario\PYTHON\Data\\Subdatos.csv')
# Para exportar a Excel, es necesario tener instalada la librería xlwt:
Subdatos.to_excel('C:\\Users\\Usuario\PYTHON\Data\\Subdatos.xls')
# Los valores NaN se exportarán como celdas en blanco.


# 5. ESTADÍSTICA DESCRIPTIVA DE LOS DATOS GLOBALES
# ------------------------------------------------
# Un análisis estadístico descriptivo de los datos lo obtenemos con el método .describe()
# No es necesario hacer una limpieza de datos para obtener este estupendo resumen estadístico:
print ("RESUMEN ESTADÍSTICO DE LOS DATOS ORIGINALES:")
print ("--------------------------------------------")
print (Datos_origen.describe())


# 6. ESTADÍSTICA DESCRIPTIVA DE UNA COLUMNA
# -----------------------------------------
# Para visualizar gráficamente la estadística de algunas columnas, utilizarems la librería
# Seaborn y su método .distplot. Esto sólo puede hacerse con las columnas cuyos datos sean
# todos numéricos. Por ejemplo, elegimos la columna Rooms de los datos originales.

# Layout de la gráfica:
sns.set_style("darkgrid", {"axes.facecolor": ".9"})   # Cfr. documentación de Seaborn.
# Estos son otros temas de sns: darkgrid, whitegrid, dark, white y ticks.
# Comando para dibujar los datos:
print (Datos_origen.Rooms.describe())
sns.distplot(Datos_origen.Rooms.dropna(), kde=False, color=".2")
# El método dropna() elimina las filas con valores NaN.
# kde=False hace que sólo no aparezca una línea suavizada además de las barras.
# Si no se especifica axlabel='Nombre de la columa', aparecerá el nombre de la columna
# de datos.
plt.show()


# 7. VISUALIZACIÓN DE ESTADÍSTICA DESCRIPTIVA EN COLUMNAS NO NUMÉRICAS
# --------------------------------------------------------------------
# Gráfico de barras: Número de viviendas en cada suburbio
# Definimos una figura (que es un conjunto de gráficos)
plt.figure(figsize=(8, 5))

# Con subplot puede organizar gráficas en una cuadrícula regular. Es
# necesario especificar el número de filas, columnas y el número del gráfico.
# Primer gráfico
plt.subplot(3, 1, 1)
plt.xticks(())      # Elimina las marcas en el eje x.
plt.yticks(())      # Elimina las marcas en el eje y.
Datos_origen['Suburb'].value_counts().plot.bar()

# Segundo gráfico
plt.subplot(3, 1, 2)
plt.xticks(())
plt.yticks(())
(Datos_origen['Suburb'].value_counts()/len(Datos_origen)).plot.line()

# Tercer gráfico
plt.subplot(3, 1, 3)
plt.xticks(())
plt.yticks(())
Datos_origen['Suburb'].value_counts().sort_index().plot.area()

plt.tight_layout()
plt.show()

# Más info sobre formato de gráficos en:
# https://claudiovz.github.io/scipy-lecture-notes-ES/intro/matplotlib/matplotlib.html#figuras


# 8. SCATTER PLOTS
# ----------------
# También es muy fácil hacer un gráfico de dispersión de los datos de dos comunas que
# sean totalmente numéricas:
Datos_origen.plot.scatter('Rooms','Price')
plt.show()


# 9. OTRAS VISUALIZACIONES GRÁFICAS MUY INTERESANTES
# --------------------------------------------------
# Gráficos de cajas (boxplot)

sns.set_style("dark")
plt.figure(figsize=(8, 5))

# Primer gráfico - Boxplot de 2 variables
plt.subplot(2, 1, 1)
plt.xticks(())      # Elimina las marcas en el eje x.
plt.yticks(())      # Elimina las marcas en el eje y.
sns.boxplot(x='Rooms', y='Price', data=Datos_origen)

# Segundo gráfico - Boxplot de 3 variables
plt.subplot(2, 1, 2)
plt.xticks(())
plt.yticks(())
sns.boxplot(x='Rooms', y='Price', data=Datos_origen, hue='Type')

plt.tight_layout()
plt.show()


# 10.WEBERÍA
# ----------
# Para operaciones del tipo: añadir/eliminar columnas o filas, crear columnas calculadas
# a partir de los datos originales, etc:
# https://relopezbriega.github.io/blog/2016/09/18/visualizaciones-de-datos-con-python/
