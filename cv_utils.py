"""
copyright 2013-2014 Talin Salway

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy
import cv2

def img_from_buffer(buffer):
    np_arr = numpy.fromstring(buffer,'uint8')
    np_mat = cv2.imdecode(np_arr,0)
    return np_mat

def show_scaled(win, img):
    minVal, maxVal, pt1, pt2 = cv2.minMaxLoc(img)
    cols, rows = img.shape
    #tmp = cv.CreateMat(rows, cols,cv.CV_32FC1)
    tmp = cv2.convertScaleAbs(img, 1.0/(maxVal-minVal), 1.0*(-minVal)/(maxVal-minVal))
    cv2.imshow(win,tmp)

def float_version(img):
    #tmp = cv.CreateImage( cv.GetSize(img), 32, 1)
    #tmp = cv2.convertScaleAbs(img, 1/255.0)
    tmp = img/255.0
    return tmp

def sum_squared(img1, img2):
    #tmp = cv.CreateImage(cv.GetSize(img1), 8,1)
    tmp = cv2.subtract(img1,img2)
    tmp = cv2.pow(tmp,2.0)
    return cv2.sumElems(tmp)[0]

def ccoeff_normed(img1, img2):
    size = img1.shape
    tmp1 = float_version(img1)
    tmp2 = float_version(img2)
    
    #print(tmp1)
    mean1 = cv2.mean(tmp1)
    mean2 = cv2.mean(tmp2)
    #print('mean: '+str(mean1)+' '+str(mean2))
    tmp1 = cv2.subtract(tmp1, cv2.mean(tmp1))
    tmp2 = cv2.subtract(tmp2, cv2.mean(tmp2))


    #norm1 = cv.CloneImage(tmp1)
    #norm2 = cv.CloneImage(tmp2)
    norm1 = cv2.pow(tmp1, 2.0)
    norm2 = cv2.pow(tmp2, 2.0)

    #cv.Mul(tmp1, tmp2, tmp1)
    dot = numpy.dot(tmp1.flat,tmp2.flat)
    sum1 = cv2.sumElems(norm1)[0]
    sum2 = cv2.sumElems(norm2)[0]
    sums = (sum1*sum2)**0.5
    #print(dot,sum1,sum2,sums)

    return dot / sums

