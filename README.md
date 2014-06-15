WALLPAPER500px
--------------

**Goal:** Download high-res images from www.500px.com and shuffle wallpapers using Python

Installation
------------

    $ sudo apt-get install git
    $ git clone https://github.com/umang94/Wallpaper500px.git
    $ sudo apt-get install phantomjs

Usage
-----

Here's an example that will download the most popular images under the 
"Urban Exploration" category on 500px website:

    $ cd Wallpaper500px
    $ python extractdata.py -c "Urban Exploration" &

