import os, sys, shutil
import tempfile, uuid
from subprocess import Popen,PIPE
from pathlib import Path
import cv2
from PIL import Image


def pdftoimage(input_file, img_format='jpeg', DPI='300'):
    output_images_path = []
    temp_path = tempfile.mkdtemp()
    if type(input_file) == str and Path(input_file).is_file():
        filename = os.path.basename(input_file)
        basename = os.path.basename(filename)
        pdf_path = input_file
    else:
        basename = str(uuid.uuid4())
        filename = basename + ".pdf"
        pdf_path = os.path.join(temp_path, filename)
        with open(pdf_path, 'wb') as fileObj:
            fileObj.write(input_file)

    des_img = os.path.join(temp_path, os.path.splitext(basename)[0] + '_page_%01d.jpg')
    proc = Popen(['gs', '-q', '-dBATCH', '-dNOPAUSE', '-sDEVICE={}'.format(img_format), '-o', des_img, '-r{}x{}'.format(DPI, DPI), pdf_path], stderr=PIPE)
    _, error = proc.communicate()
    p_status = proc.wait()
    if error:
        print('\33[31mERROR or WARNING at pdftoimage: {}\033[0m'.format(error))
    num_page = len([im_path for im_path in Path(temp_path).rglob(os.path.splitext(basename)[0]+'*.jpg')])

    for i in range(num_page):
        des_img_name = des_img[: -8] + str(i+1) + des_img[-4:]
        output_images_path.append(des_img_name)
    return output_images_path


def get_cvimages(input_file, cvFLAG=None):
    '''return a list of OpenCV images'''
    cv_lst = []
    img_lst = pdftoimage(input_file)
    for img_path in img_lst:
        cv_lst.append(cv2.imread(img_path, flags=cvFLAG))
    shutil.rmtree(str(Path(img_path).parents[0]))
    return cv_lst


def get_pilimages(input_file):
    '''return a list of images opened by PIL'''
    pil_lst = []
    img_lst = pdftoimage(input_file)
    for img_path in img_lst:
        pil_lst.append(Image.open(img_path))
    shutil.rmtree(str(Path(img_path).parents[0]))
    return pil_lst


def get_byteimages(input_file):
    '''return list of images in bytes'''
    byte_lst = []
    img_lst = pdftoimage(input_file)
    for img_path in img_lst:
        byte_lst.append(bytearray(open(img_path, 'rb').read()))
    shutil.rmtree(str(Path(img_path).parents[0]))
    return byte_lst


def save_to(input_file, out_path):
    '''
        input_file: path to the pdf
        out_path: path to the directory for saving the images
    '''
    filename_noex = os.path.splitext(os.path.basename(input_file))[0]
    if not os.path.exists(out_path):
        print('\33[33mOutput directory not exists, create ...\033[0m')
        os.mkdir(out_path)
    img_lst = pdftoimage(input_file)
    for i, img_path in enumerate(img_lst):
        new_name = filename_noex+'_page{}.jpg'.format(i+1) if len(img_lst) > 1 else filename_noex+'.jpg'
        img_dest_path = os.path.join(out_path, new_name)
        shutil.move(img_path, img_dest_path)
        print('\33[32mImage created at: {}\033[0m'.format(img_dest_path))
    shutil.rmtree(str(Path(img_path).parents[0]))



if __name__ == "__main__":
    pdf_path = sys.argv[1]
    if len(sys.argv) < 3:
        print('\33[33mOutput directory not defined, use the same directory with input PDF ...\033[0m')
        output_path = str(Path(pdf_path).parents[0])
    else:
        output_path = sys.argv[2]
    save_to(pdf_path, output_path)