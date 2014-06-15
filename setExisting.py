#!/usr/bin/python
import sys, os, re, subprocess, time
AbsLocation = os.path.abspath(os.path.dirname(sys.argv[0]))
ExistingImages = [Image for Image in os.listdir(AbsLocation) if re.match(re.escape(sys.argv[1])+r"\d+\.jpg", Image)]
while(1):
  for Image in ExistingImages:
    FileLink = "file://"+AbsLocation+"/"+Image
    subprocess.call(["/usr/bin/gsettings", "set", "org.gnome.desktop.background", "picture-uri", FileLink])
    time.sleep(20)

