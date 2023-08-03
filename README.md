<h1>Asciitizer</h1>

<p>This code will allow you to convert any PNG image into ASCII art. For example, the first image into the second.</p>

<h2>Original Image</h2>
<img src="https://github.com/edianibarrola/asciitizer/assets/13739419/76d31356-dade-4582-b3a7-656a02bd9921" width="300">

<div style="display: flex; flex-direction: row;">
  <div style="flex: 50%; padding-right: 10px;">
    <p>Greyscale / No</p>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/c6584bdc-673a-4b4a-9f3e-195366f8ae81" width="100%">
  </div>
  <div style="flex: 50%; padding-left: 10px;">
    <p>Color / No</p>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/63bb5461-529c-44b3-ab2e-3be527ae3fd6" width="100%">
  </div>
</div>

<div style="display: flex; flex-direction: row;">
  <div style="flex: 50%; padding-right: 10px;">
    <p>Greyscale / Yes</p>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/776b31e0-477e-46a7-b656-5a249c9bbe25" width="100%">
  </div>
  <div style="flex: 50%; padding-left: 10px;">
    <p>Color / Yes</p>
    <img src="https://github.com/edianibarrola/asciitizer/assets/13739419/dae9647a-9e73-45a0-bd8e-f461cb9a186b" width="100%">
  </div>
</div>

<h2>How to use:</h2>
<ol>
  <li>Type <code>pip install Pillow</code> in the terminal, then when it finishes, type <code>pip install numpy</code>.</li>
  <li>Place your input image wherever the python file is. (If you're using gitpod, just upload it in)</li>
  <li>Change the uploaded image name to 'test.png' (there is one already there as an example, you need to replace it).</li>
  <li>There are some variables you can modify at the top of the asci.py file.
    <ul>
      <li>You can change the output width (calculated by ASCII characters).</li>
      <li>You can change the actual ASCII characters used. You can add or subtract characters to change the shades, keep in mind they are ordered from darkest to lightest. (If you put them back in reverse order, you get an inverted image).</li>
      <li>You can change the font size.</li>
    </ul>
  </li>
  <li>Run the code by typing the python file name in the terminal. Make sure the input image is in the same place as the python file and it is named test.png. (Type <code>python asci.py</code> in the terminal)</li>
  <li>The code will run, depending on the variables, it could take a bit, so just wait. The file will appear in the same directory when it finishes.</li>
</ol>
