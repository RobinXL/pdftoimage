import sys, os
from pdftoimage import save_to
from pathlib import Path
import time


if __name__ == "__main__":
    folder = sys.argv[1]
    if not Path(folder).is_dir():
        print('\33[31mError: Directory does not exist or invalid\033[0m')
        sys.exit()
    all_pdf = [str(p) for p in Path(folder).rglob('*.pdf')] + [str(p) for p in Path(folder).rglob('*.PDF')]
    print('\33[34mFound total {} PDFs\033[0m'.format(len(all_pdf)))
    tic = time.time()
    if len(sys.argv) < 3:
        print('\33[33mOutput directory not defined, use the same directory with input PDF ...\033[0m')
        output_path = os.path.join(str(Path(folder).parents[0]), os.path.basename(folder)+'_PDF_TO_IMAGES')
    else:
        output_path = sys.argv[2]
    for pdf in all_pdf:
        save_to(pdf, output_path)
    print('\33[34mJob finished! Total time takes: {}\033[0m'.format(time.time() - tic))