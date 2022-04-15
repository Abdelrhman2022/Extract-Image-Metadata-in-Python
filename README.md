# Extract Image Metadata in Python

here are many reasons why you want to include the metadata of a video or any media file in your Python application. Video metadata is all available information about a video file, such as width, height, codec type, fps, duration, and many more.

``In order to review the properties of various common-format image files, I wrote a command-prompt script in Python that will display EXIF data and other properties of JPG, PNG, TIF, CR2 and NEF files.
``

I am routinely looking at images, so I wanted a Python script that could display the EXIF (Exchangeable image file format) data from any JPEG, PNG, TIF or RAW (CR2 and NEF) file, as well as summarise some key properties such as:

* Format
* Height and Width
* Data type
* Bit-depth
* Mode

Whilst there are many Python programmes available, most will only work with specific file types. This is a problem because JPEG and TIF files natively support EXIF data, whilst the information in PNG files (where present) is encapaulated differently. Then there are the two common proprietary RAW image formats (Canon’s CR2 and Nikon’s NEF) which store their metadata in yet another format.

What I wanted was a single piece of code that would work out what the file format is then extract the EXIF or metadata in a manner appropriate for that format.

It turns out that this is quite an ask.

Extracting EXIF data from JPEG and TIF
JPEG (Joint Photographic Experts Group) and TIF (Tagged Image Format) files natively support EXIF. In order to extract some of the properties of these files, I found that I had to use two Python modules:

```
  Imageio to determine the data type
  Pillow to extract some basic metadata
```
