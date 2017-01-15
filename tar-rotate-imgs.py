#!/usr/bin/python3

# Script to tar, compress and rotate images

import os
import tarfile
import datetime
import shutil


picdir = "/home/ramsey/"
tar_loc = "/root/pic_backups"
pics = []
tar_files = []


def get_imgs():
    for image in os.listdir(picdir):
        if image.endswith(".jpg"):
            pics.append(picdir + image)
    return pics


def tar_imgs():
    pictures = get_imgs()
    today = str(datetime.date.today())
    filename = picdir + "archive" + today + ".tar.gz"
    tar = tarfile.open(filename, "w:gz")
    for jpeg in pictures:
        tar.add(jpeg)
    tar.close
            
def pic_cleanup():
    pictures = get_imgs()
    for pic in pictures:
        try:
            os.remove(pic)
        except:
            pass

def get_tarnames():
    for tar in os.listdir(picdir):
        if tar.endswith(".tar.gz"):
            tar_files.append(tar)
    return tar_files

def move_tarfiles():
    tarnames = get_tarnames()
    for filename in tarnames:
        source = picdir + filename
        dest = tar_loc
        shutil.move(source, dest)


tar_imgs()
pic_cleanup()
move_tarfiles()
