import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
N = 100  # Número de sitios
t = 1.0  # Parámetro de hopping
E0 = 0.0  # Energía en los sitios
a = 1.0  # Parámetro de red

# Construir la matriz Hamiltoniana dependiente de k
def construir_hamiltoniana(N, t, E0, k, a):
    H = np.zeros((N, N), dtype=complex)  # Inicializar la matriz Hamiltoniana
    for i in range(N):
        H[i, i] = E0  # Energía en los sitios (diagonal)
        if i < N-1:
            H[i, i+1] = -t  # Hopping a la derecha
            H[i+1, i] = -t  # Hopping a la izquierda
    # Elementos que conectan el primer y último sitio (condiciones periódicas)
    H[0, N-1] = -t * np.exp(1j * k * a)
    H[N-1, 0] = -t * np.exp(-1j * k * a)
    return H

# Calcular la energía en función de k
def calcular_energias(N, t, E0, valores_k, a):
    energias = []  # Lista para almacenar las energías
    for k in valores_k:
        H = construir_hamiltoniana(N, t, E0, k, a)  # Construir Hamiltoniana para cada k
        eigvals = np.linalg.eigvalsh(H)  # Diagonalizar la matriz Hamiltoniana para obtener las energías
        energias.append(eigvals)
    return np.array(energias)  # Convertir la lista a un array de numpy

# Valores de k para los cuales se calcularán las energías
valores_k = np.linspace(-np.pi/a, np.pi/a, 100)

# Calcular las energías
energias = calcular_energias(N, t, E0, valores_k, a)

# Graficar la estructura de bandas (solo la primera banda para claridad)
plt.figure(figsize=(10, 6))
plt.plot(valores_k, energias[:, 0], label='Banda 1')  # Graficar la primera banda de energía
plt.xlabel('k')
plt.ylabel('Energía')
plt.title('Estructura de Bandas')
plt.legend(loc='upper right', fontsize='small', frameon=True)
plt.grid(True)
plt.show()
