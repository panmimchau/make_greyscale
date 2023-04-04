#python make_greyscale.pl --input color --output blackwite
from PIL import Image, ImageFilter
from glob import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='change image files to b&w')
parser.add_argument('--input', help='Folder which contains the original image files', required=True)
parser.add_argument('--output', help='Folder with modified image files', required=True)
args = parser.parse_args()


for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)
    
    with Image.open(path) as new_image:
        greyscaled = new_image.convert('L')
        modified_image = greyscaled.filter(ImageFilter.DETAIL)
        greyscaled.save(args.output + '/' + filename)
        modified_image.save(args.output + '/modified_' + filename)
        
    


