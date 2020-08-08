# pdftoimage
A light weight python(3.6+) module for converting pdf to image. Wrapped with GhostScript

## dependant
Install `ghostscript 9.26`
### Mac
```
brew install ghostscript
```
### CentOS/Fedora
```
sudo dnf install ghostscript
```
### Ubuntu/Debian
```
apt install ghostscript
```
### Verify `ghostscript`
```
gs --version
# output: 9.26
```

## How to use
### Use as command line
```
python pdftoimage.py test.pdf test

# output:
Output directory not exists, create ...
Image created at: test/test_page1.jpg
Image created at: test/test_page2.jpg
```
### Bulk convert all PDF to image in the folder (includes all subfolders)
```
python bulkconvert.py test

# output:
Found total 3 PDFs
Output directory not defined, use the same directory with input PDF ...
Output directory not exists, create ...
Image created at: ./test_PDF_TO_IMAGES/20200109174921-0001.jpg
Error: Ignoring invalid annotation, output may be incorrect.
Image created at: ./test_PDF_TO_IMAGES/8-15-15 A320J158001-RW_page1.jpg
Image created at: ./test_PDF_TO_IMAGES/8-15-15 A320J158001-RW_page2.jpg
...
Image created at: ./test_PDF_TO_IMAGES/0012063430.jpg
Job finished! Total time takes: 7.694029092788696
```

## Working with PIL or OpenCV
OpenCV / PIL
```
import pdftoimage

myPDF = 'example.pdf' # or byte type pdf

# OpenCV
cv_images = pdftoimage.get_cvimages(myPDF)

# or PIL
pil_images = pdftoimage.get_pilimages(myPDF)
```

## Future work
- Image format flag
- DPI flag
- OpenCV flag
- more option on output image control (grayscale, denoise)
