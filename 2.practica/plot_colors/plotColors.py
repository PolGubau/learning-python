from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_colors(image_path, num_colors=5):
    """
    Extrae los colores principales de una imagen usando k-means.
    
    Args:
        image_path (str): Ruta de la imagen.
        num_colors (int): Número de colores principales a extraer.
        
    Returns:
        list: Lista de colores en formato RGB.
    """
    # Cargar la imagen y convertirla a formato RGB
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    # Aplanar la imagen a una matriz de píxeles
    pixels = image_array.reshape(-1, 3)

    # Usar k-means para agrupar colores
    kmeans = KMeans(n_clusters=num_colors, random_state=0)
    kmeans.fit(pixels)

    # Obtener los colores principales
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def plot_colors(colors):
    """
    Muestra una gráfica con los colores principales.
    
    Args:
        colors (list): Lista de colores en formato RGB.
    """
    plt.figure(figsize=(8, 2))
    plt.axis("off")
    plt.title("Colores principales")

    # Crear una barra para cada color
    for i, color in enumerate(colors):
        plt.fill_between([i, i+1], 0, 1, color=np.array(color)/255)
    
    plt.show()

# Ruta de la imagen
image_path = "./2.practica/plot_colors/img1.png"
 

# Extraer colores
num_colors = 5
colors = extract_colors(image_path, num_colors=num_colors)

# Mostrar los colores principales
print("Colores principales (RGB):", colors)
plot_colors(colors)
