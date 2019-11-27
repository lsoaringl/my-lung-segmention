import cv2
import numpy
import shutil
import os
import pydicom
from glob import glob

def dicomClassify():
    file_list = glob(scr_path + '*')
    for img_file in file_list:
            img_file = img_file.replace("\\", "/")
            file_name = str(img_file).split("/")[-1]
            dcm = pydicom.read_file(img_file)
            patientName = dcm.PatientName
            patientName = str(patientName)
            seriesTime = dcm.SeriesTime
            seriesDescription = dcm.SeriesDescription
            src = r'D:/dicomClassify/'
            dst = src + patientName
            if not os.path.exists(dst):
                os.mkdir(dst)
            dstFinal = src + patientName +"/"+seriesDescription
            if not os.path.exists(dstFinal):
                os.mkdir(dstFinal)
            if seriesDescription == "Fl_ThorAngio  0.75  I26f  3":
                dstFinalWithTime = src + patientName +"/"+seriesDescription + "/" +seriesTime
                if not os.path.exists(dstFinalWithTime):
                    os.mkdir(dstFinalWithTime)
                    shutil.copyfile(img_file, dstFinalWithTime + "/" + file_name)
                shutil.copyfile(img_file, dstFinalWithTime + "/" + file_name)
            shutil.copyfile(img_file, dstFinal + "/" + file_name)
            print(img_file + " classified Success!!")

    return None

if __name__ == '__main__':
    scr_path =  r"D:/dataConcentration/"
    dicomClassify()