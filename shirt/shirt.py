import sys, os
from PIL import Image, ImageOps

def main():
    file_names = get_file_names()
    join_images(file_names)

def get_file_names():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

    first_img, second_img = args[0].lower(), args[1].lower()
    first_ext = os.path.splitext(first_img)[1]
    second_ext = os.path.splitext(second_img)[1]

    if first_ext not in (".jpg", ".jpeg", ".png") or second_ext not in (".jpg", ".jpeg", ".png"):
        sys.exit("Invalid input")
    elif not first_ext == second_ext:
        sys.exit("Input and output have different extensions")
    else:
        return args

def join_images(images):
    input_image, output_image = images
    try:
        with Image.open(input_image) as img, Image.open("shirt.png") as shirt:
            img = ImageOps.fit(img, shirt.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            img.paste(shirt, (0,0), shirt)
            img.save(output_image)
    except FileNotFoundError:
        sys.exit("Input doesn't exist")

if __name__ == "__main__":
    main()
