from pytoimage import PyImage
from pathlib import Path


def pycode_to_img(file_path='main.py'):
    path = Path(file_path)
    
    if not path.is_file():
        return 'None, check a file path'

    code = PyImage(file_path, background=(255, 255, 255))
    palette = {
        'line': (255, 0, 255),
        'normal': (0, 0, 0),
    }

    code.set_color_palette(palette=palette)
    code.generate_image()
    image_name = f'{file_path.split(".")[0]}.png'
    code.save_image(image_name)

    return f'{image_name} saved successfully'


def main():
    file_path = input('Enter a filename - ')
    print(pycode_to_img(file_path=file_path))


if __name__ == '__main__':
    main()