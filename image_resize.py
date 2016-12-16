from PIL import Image
import argparse
import os.path


def get_console_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to the source image")
    parser.add_argument("--width", "--w",  help="Width of the output file", type=int)
    parser.add_argument("--height", "--h",  help="Height of the output file", type=int)
    parser.add_argument("--scale", "--s",  help="Scale of the output file", type=float)
    parser.add_argument("--output", "--o", help="Path to image output")

    args = parser.parse_args()

    if args.scale and (args.width or args.height):
        print('Specify only scale or width/height')
        parser.print_usage()
    elif not args.width and not args.height and not args.scale:
        print('Specify either scale or width/height')
        parser.print_usage()

    return args


def calculate_sizes(img, width, height, scale):
    if scale:
        width, height = abs(int(img.size[0]*scale)), abs(int(img.size[1]*scale))
    else:
        if width and not height:
            exp = width/img.width
            width, height = abs(int(img.width*exp)), abs(int(img.height*exp))
        elif height and not width:
            exp = height/img.height
            width, height = abs(int(img.width*exp)), abs(int(img.height*exp))
        else:
            print('Notice: image proportions are probably not constrained')

    return width, height


def resize_image(path_to_file, res_width, res_height, output):
    img = Image.open(path_to_file)
    name, ext = os.path.splitext(path_to_file)

    save_string = "{0}__{2}x{3}{1}"

    if output:
        save_string = "{4}{1}"

    img.resize((res_width, res_height)).save(save_string.format(name, ext, res_width, res_height, output))


def main():
    args = get_console_args()

    img = Image.open(args.source)
    width, height, scale, output = args.width, args.height, args.scale, args.output

    res_width, res_height = calculate_sizes(img, width, height, scale)
    resize_image(args.source, res_width, res_height, output)

if __name__ == '__main__':
    main()
