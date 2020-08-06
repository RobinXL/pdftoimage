# pdftoimage
A light weight python3 module for converting pdf to image. Wrapped with GhostScript

## dependant
Install `ghostscript`
### Mac
```
brew install ghostscript
```
### CentOS
```
sudo dnf install ghostscript
```
### Ubuntu
```
apt install ghostscript
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
