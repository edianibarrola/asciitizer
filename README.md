# Asciitizer

This code will allow you to convert any PNG image into ASCII art. For example, the first image into the second.

<div style="float: left;">
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/c6584bdc-673a-4b4a-9f3e-195366f8ae81" width="300">
    <p><strong>Greyscale / No</strong></p>
</div>
<div style="float: left; padding-left: 20px;">
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/63bb5461-529c-44b3-ab2e-3be527ae3fd6" width="300">
    <p><strong>Color / No</strong></p>
</div>
<div style="clear: both;"></div>

<div style="float: left;">
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/776b31e0-477e-46a7-b656-5a249c9bbe25" width="300">
    <p><strong>Greyscale / Yes</strong></p>
</div>
<div style="float: left; padding-left: 20px;">
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/dae9647a-9e73-45a0-bd8e-f461cb9a186b" width="300">
    <p><strong>Color / Yes</strong></p>
</div>
<div style="clear: both;"></div>

## How to use:

1. Type `pip install Pillow` in the terminal, then when it finishes, type `pip install numpy`.
2. Place your input image wherever the python file is. (If you're using gitpod, just upload it in)
3. Change the uploaded image name to 'test.png' (there is one already there as an example, you need to replace it).
4. There are some variables you can modify at the top of the asci.py file.
    - You can change the output width (calculated by ASCII characters).
    - You can change the actual ASCII characters used. You can add or subtract characters to change the shades, keep in mind they are ordered from darkest to lightest. (If you put them back in reverse order, you get an inverted image).
    - You can change the font size.
5. Run the code by typing the python file name in the terminal. Make sure the input image is in the same place as the python file and it is named test.png. (Type `python asci.py` in the terminal)
6. The code will run, depending on the variables, it could take a bit, so just wait. The file will appear in the same directory when it finishes.
