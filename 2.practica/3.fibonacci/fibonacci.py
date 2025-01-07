def getFibonacci(limit: int = 50) -> list[int]:
    f = [0, 1]  # Los dos primeros números de la secuencia
    while len(f) < limit:
        f.append(f[-1] + f[-2])  # La suma de los dos últimos números
    return f[:limit]  # Devolver solo hasta el límite indicado
 