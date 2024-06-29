import numpy as np
import matplotlib.pyplot as plt

# Parámetros
E_0 = 0.0  # Energía en el sitio
t = 1.0    # Parámetro de hopping
a = 1.0    # Constante de red
N = 100    # Número de sitios
k_points = 100  # Número de puntos k

# Construir la matriz Hamiltoniana
def construir_hamiltoniana(N, E_0, t):
    H = np.zeros((N, N), dtype=complex)
    for i in range(N):
        H[i, i] = E_0  # Energía en el sitio
        if i > 0:
            H[i, i - 1] = -t  # Hopping a la izquierda
            H[i - 1, i] = -t  # Hopping a la derecha
    H[0, N - 1] = -t  # Condición periódica de contorno (izquierda)
    H[N - 1, 0] = -t  # Condición periódica de contorno (derecha)
    return H

# Calcular la energía en función de k
def calcular_energia(E_0, t, a, N, k_points):
    H = construir_hamiltoniana(N, E_0, t)
    valores_k = np.linspace(-np.pi/a, np.pi/a, k_points)
    energias = []
    for k in valores_k:
        H_k = H.copy()
        for i in range(N - 1):
            H_k[i, i + 1] *= np.exp(1j * k * a)  # Factor de fase para hopping a la derecha
            H_k[i + 1, i] *= np.exp(-1j * k * a)  # Factor de fase para hopping a la izquierda
        H_k[0, N - 1] *= np.exp(1j * k * a)  # Factor de fase para la condición periódica (izquierda)
        H_k[N - 1, 0] *= np.exp(-1j * k * a)  # Factor de fase para la condición periódica (derecha)

        # Diagonalizamos el Hamiltoniano para obtener los autovalores (energías)
        autovalores = np.linalg.eigvalsh(H_k)
        energias.append(autovalores[0])  # Solo la banda principal
    return valores_k, np.array(energias)

# Función principal
valores_k, energias = calcular_energia(E_0, t, a, N, k_points)

# Graficar la estructura de bandas
plt.figure(figsize=(8, 6))
plt.plot(valores_k, energias, label='Banda 1')
plt.xlabel('k')
plt.ylabel('Energía')
plt.title('Estructura de Bandas')
plt.legend()
plt.grid(True)
plt.show()
