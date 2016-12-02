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


def resize_image(path_to_file, *args):
    img = Image.open(path_to_file)
    name, ext = os.path.splitext(path_to_file)
    width, height, scale, output = args[0], args[1], args[2],args[3]

    save_string = "{0}__{2}x{3}{1}"

    if output:
        save_string = "{4}{1}"

    write_image = lambda out_width, out_height: \
        img.resize((out_width, out_height)).save(save_string.format(name, ext, out_width, out_height, output))

    if scale:
        width, height = abs(int(img.size[0]*scale)), abs(int(img.size[1]*scale))
        write_image(width, height)
    else:
        if width and not height:
            exp = width/img.width
            width, height = abs(int(img.width*exp)), abs(int(img.height*exp))
            write_image(width, height)
        elif height and not width:
            exp = height/img.height
            width, height = abs(int(img.width*exp)), abs(int(img.height*exp))
            write_image(width, height)
        else:
            print('Notice: image proportions are probably not constrained')
            write_image(width, height)


def main():
    args = get_console_args()
    resize_image(args.source, args.width, args.height, args.scale, args.output)

if __name__ == '__main__':
    main()
