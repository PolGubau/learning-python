from PIL import Image

def create_sample_image(filename="img1.png", size=(100, 100)):
    """
    Crea un archivo de imagen PNG con un degradado.

    Args:
        filename (str): Nombre del archivo a crear.
        size (tuple): Tamaño de la imagen (ancho, alto).
    """
    image = Image.new("RGB", size)
    pixels = image.load()

    for y in range(size[1]):
        for x in range(size[0]):
            # Crear un degradado horizontal
            r = int((x / size[0]) * 255)  # Rojo depende de x
            g = int((y / size[1]) * 255)  # Verde depende de y
            b = 123  # Azul constante
            pixels[x, y] = (r, g, b)

    image.save(filename)
    print(f"Imagen '{filename}' creada con éxito.")

# Crear el archivo img1.png con degradado
create_sample_image()