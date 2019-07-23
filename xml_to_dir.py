#modpification of xml_to_csv.py to crop input images based on xml and to output directory based structure

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse
import cv2
import numpy as np

def xml_to_dir(pathIn, pathImages,pathOut):
    xml_list = []
    i = 1
    for xml_file in glob.glob(pathIn + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            img = cv2.imread(pathImages+'/'+root.find('filename').text)
            crop = img[int(member[4][1].text):int(member[4][3].text),
                       int(member[4][0].text):int(member[4][2].text)]
            for i in range(0,3):
                if i==2:
                    kernel = np.ones((5,5),np.float32)/25
                    crop = cv2.filter2D(crop,-1,kernel)
                elif i==3:
                    crop = cv2.blur(crop,(5,5))
                try:
                    os.mkdir(pathOut+'/'+member[0].text)
                except:
                    pass
                cv2.imwrite(pathOut+'/'+member[0].text+'/'+str(i)+'.png',crop)
                i += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in-xml', '--input_xml', help='define the input xml file(s)', type=str, required=True)
    parser.add_argument('-in-img','--input_images',help='define the input image files()',type=str, required=True)
    parser.add_argument('-out', '--output_dir', help='define the output directories', type=str, required=True)
    args = parser.parse_args()

    xml_to_dir(args.input_xml,args.input_images,args.output_dir)
    print('Successfully converted xml to dir.')


main()
