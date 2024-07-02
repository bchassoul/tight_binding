import numpy as np
import matplotlib.pyplot as plt


def construir_hamiltoniana(N, t, V_0, k, a):
    H = np.zeros((N, N)) 
    for i in range(N):
        H[i, i] = V_0 
        if i < N-1:
            H[i, i+1] = -t 
            H[i+1, i] = -t 
    H[0, N-1] = -t 
    H[N-1, 0] = -t 
    return H * np.exp(-1j * k * a)


def calcular_energias(N, t, V_0, valores_k, a):
    energias = []  
    for k in valores_k:
        H = construir_hamiltoniana(N, t, V_0, k, a) 
        eigvals = np.linalg.eigvalsh(H) 
        energias.append(eigvals)
    return np.array(energias) 



N = 1
t = 1.0  
V_0 = 0.0  
a = 1.0
valores_k = np.linspace(-np.pi/a, np.pi/a, 5000)
energias = calcular_energias(N, t, V_0, valores_k, a)


plt.plot(valores_k, energias, label='Banda 1')
plt.xlabel('k')
plt.ylabel('Energía')
plt.title('Estructura de Bandas')
plt.legend()
plt.show()
