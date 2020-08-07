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
```
python pdftoimage.py <example.pdf> <output path>
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
