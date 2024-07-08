import random
import numpy as np
import matplotlib.pyplot as plt

def calcular_estructura_de_bandas(N, a, t, eps, valores_k):
    """
    Calcula la estructura de bandas para un modelo de tight-binding en 1D.

    Parámetros:
        N (int): Número de orbitales atómicos.
        a (float): Espaciado de la red.
        t (float): Parámetro de hopping.
        eps (float): Energía en el sitio.
        valores_k (np.ndarray): Array de valores de k.

    Retorna:
        lista de np.ndarray: Lista de arrays de autovalores para cada valor de k.
    """
    autovalores = []

    for k in valores_k:
        H = np.zeros((N, N), dtype=complex)

        # Término de energía en el sitio
        for i in range(N):
            H[i, i] = eps

        # Términos de hopping con condiciones de contorno periódicas
        for i in range(N):
            H[i, (i+1) % N] = -t * np.exp(1j * k * a)
            H[(i+1) % N, i] = -t * np.exp(-1j * k * a)

        evals = np.linalg.eigvalsh(H)
        autovalores.append(evals)

    return autovalores

def seleccionar_autovalores_aleatorios(autovalores):
    """
    Selecciona un conjunto arbitrario de autovalores de la estructura de bandas calculada.

    Parámetros:
        autovalores (lista de np.ndarray): Lista de arrays de autovalores para cada valor de k.

    Retorna:
        np.ndarray: Array de autovalores seleccionados.
    """
    indice_aleatorio = random.randint(0, len(autovalores) - 1)
    return autovalores[indice_aleatorio]

def aplicar_condiciones_de_contorno_periodicas(autovalores):
    """
    Aplica condiciones de contorno periódicas de manera que E(-k) = E(k).

    Parámetros:
        autovalores (np.ndarray): Array de autovalores.

    Retorna:
        np.ndarray: Array de autovalores con condiciones de contorno periódicas aplicadas.
    """
    return np.concatenate((np.flip(autovalores, 0), autovalores), axis=0)

def calcular_banda_analitica(valores_k, t, eps, a):
    return eps - 2 * t * np.cos(valores_k * a)

def graficar_estructura_de_bandas(valores_k, banda_numerica, t, eps, a, N):
    banda_analitica = calcular_banda_analitica(valores_k, t, eps, a)

    fig, axs = plt.subplots()
    axs.plot(valores_k, banda_numerica, 'o', label=f'Autovalores de H(k)')
    axs.plot(valores_k, banda_analitica, label=r'$E(k) = \epsilon_0 - 2t\cos(ka)$', linestyle='--', color='black')
    axs.set_yticks([eps-2.*t, eps-t, eps, eps+t, eps+2.*t])
    axs.set_yticklabels(['$\epsilon_0-2t$', '$\epsilon_0-t$', '$\epsilon_0$', '$\epsilon_0+t$', '$\epsilon_0+2t$'])
    axs.set_xlabel('k')
    axs.set_ylabel('E(k)')
    axs.set_title(f'Modelo de tight-binding con cadena atómica de N={N} celdas')
    axs.legend()
    axs.grid(True)

    fig.savefig('tight_binding.png')

# Parámetros
N = 50      # Número de orbitales atómicos
a = 1       # Espaciado de la red
t = 0.5     # Parámetro de hopping
eps = 0.0   # Energía en el sitio
max_iterations = 2 * N
valores_k = np.linspace(-np.pi/a, np.pi/a, max_iterations)  # Array de valores k

# Calcular la estructura de bandas
autovalores = calcular_estructura_de_bandas(N, a, t, eps, valores_k)

# Seleccionar un conjunto arbitrario de autovalores para graficar
autovalores_seleccionados = seleccionar_autovalores_aleatorios(autovalores)

# Aplicar las condiciones de contorno periódicas
autovalores_con_ccp = aplicar_condiciones_de_contorno_periodicas(autovalores_seleccionados)

# Graficar la estructura de bandas
graficar_estructura_de_bandas(valores_k, autovalores_con_ccp, t, eps, a, N)
