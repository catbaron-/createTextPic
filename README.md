createTextPic
=============
用来生成字符图片的小工具。默认生成a-z,A-Z,0-9共62个字符的图片，包括不同的字体和透视变换。
create pictures of text of a-z,A-Z,0-9, with different fonts and perspective changing.

需要正确python的PIL 模块，以及zlib，freetype库(大概）。此外需要py-opencv支持。
need PIL module for python ,and zlib, freetype lib (i guess).Besides, py-opencv is used so try to intall it.

在pyCreateTextPic.py中，fonts和font_url可以设置字体路径。
letters是要生成的字母表。

transPic.py用来做透视变换。
