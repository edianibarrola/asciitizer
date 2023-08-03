# Asciitizer

![Original Image](https://github.com/edianibarrola/asciitizer/assets/13739419/76d31356-dade-4582-b3a7-656a02bd9921)

## Preview

<div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <div style="flex: 0 0 45%; max-width: 45%; text-align: center;">
    <h3>Greyscale / No</h3>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/c6584bdc-673a-4b4a-9f3e-195366f8ae81" style="width: 100%; border-radius: 4px;">
  </div>
  <div style="flex: 0 0 45%; max-width: 45%; text-align: center;">
    <h3>Color / No</h3>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/63bb5461-529c-44b3-ab2e-3be527ae3fd6" style="width: 100%; border-radius: 4px;">
  </div>
  <div style="flex: 0 0 45%; max-width: 45%; text-align: center;">
    <h3>Greyscale / Yes</h3>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/776b31e0-477e-46a7-b656-5a249c9bbe25" style="width: 100%; border-radius: 4px;">
  </div>
  <div style="flex: 0 0 45%; max-width: 45%; text-align: center;">
    <h3>Color / Yes</h3>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/dae9647a-9e73-45a0-bd8e-f461cb9a186b" style="width: 100%; border-radius: 4px;">
  </div>
</div>

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
