import urllib2, urllib, BeautifulSoup as BS, subprocess, sys, random, re, os, time

AbsLocation = os.path.abspath(os.path.dirname(sys.argv[0]))

def getWallpapers(Category):
    ExistingImages = [Image for Image in os.listdir(AbsLocation) if re.match(re.escape(Category)+r"\d+\.jpg", Image)]
    flag = 0
    if ExistingImages:
        ShuffleExisting = subprocess.Popen(["./setExisting.py",Category,"&"],shell=True)
        flag = 1
    PhantomJS = "/usr/bin/phantomjs"
    CategoryPageLink = "http://500px.com/popular?categories="+Category
    CategoryProcess = subprocess.Popen([PhantomJS, "getpage.js", CategoryPageLink], stdout = subprocess.PIPE)
    (CategoryOutput, Error) = CategoryProcess.communicate()
    CategorySoup = BS.BeautifulSoup(CategoryOutput)
    WallpaperImgTags = CategorySoup.findAll("img", {"data-bind":"photo_img"})
    count = 1 
    for ImgTag in WallpaperImgTags:
        ImageLink = re.sub(r"/\d+\.jpg\?v=\d+","/2048.jpg",ImgTag["src"])
        print "Downloading",ImageLink,"..."
        subprocess.call(["wget","-O",Category+str(count)+".jpg",ImageLink])
        count += 1
    if flag is 1: ShuffleExisting.kill()
    subprocess.call(["./setExisting.py",Category])

print "Loading 500px ..."
Homepage = urllib2.urlopen("http://500px.com/popular").read()
HomepageSoup = BS.BeautifulSoup(Homepage)
CategoryUList = HomepageSoup.find("ul",{"class":"categories"})
Categories = []
for ListElement in CategoryUList.findAll('li'):
    Categories.append(ListElement.find('a').contents[0].replace(" ","+"))

if ((len(sys.argv) == 3) and (sys.argv[1] == "-c")) :
    RequestedCategory = sys.argv[2].replace(" ","+")
    if RequestedCategory in Categories:
        CurrentCategory = RequestedCategory
        print "Fetching the requested wallapers ..."
        getWallpapers(CurrentCategory)
    else:
        print "Requested Category not found in category catalogue ... \n Reverting to Random categories ..."
elif ((len(sys.argv) == 3) and (sys.argv[1] != "-c")):
    print "Usage : \n Check the source code and figure it out"
elif len(sys.argv) == 1 :
    print "Selecting a random category..."
    CurrentCategory = Categories[random.randint(0,len(Categories)-1)]
    print "Fetching ", CurrentCategory , " ..."
    getWallpapers(CurrentCategory)
