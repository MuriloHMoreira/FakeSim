def K(P_v, T):
    A = 0.7341
    B = 2.7
    C = 100
    K_val = A*T**2 + B*P_v/10 + C
    return K_val