import cv2
import numpy as np
def create_2circs(c1,c2,r1,r2) :
    img = np.zeros((100,100), np.uint8)
    cv2.circle(img, c1, r1, 1, 1)
    cv2.circle(img, c2, r2, 1, 1)
    return img
  
def amp(img) :
    for i in range(100) :
        for j in range(100) :
            img[i][j] = img[i][j] and 255 
    return img

def sho(img,txt) :
    cv2.imshow(txt,img)
    cv2.waitKey()

def pointsx(img) :
    pts = []
    for i in range(1,100) :
        p = []
        for j in range(0, 100) :
            if img[i][j] > 0  :
                p.append((j,i))
        if len(p) > 1 :
            pts.append(p)
    return pts
      
def pointsy(img) :
    pts = []
    for j in range(0,100) :
        p = []
        for i in range(1, 100) :
            if img[i][j] > 0  :
                p.append((j,i))
        if len(p) > 1 :
            pts.append(p)
    return pts
      
def find_centerx(p1,p2) :
    return ((int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)),int((p2[0] - p1[0]) / 2))
      
def find_centery(p1,p2) :
    return ((int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)),int((p2[1] - p1[1]) / 2))
      
def draw_circ(img, c, r) :
    cv2.circle(img, c, r, 255, 1)

def create_circ(c,r) :
    img = np.zeros((100,100), np.uint8)
    cv2.circle(img, c, r, 255, 1)
    return img
    
def compare_img(im1, im2) :
    count = 0
    for i in range(100) :
        for j in range(100) :
            if im1[i][j] > 0 :
                if im1[i][j] == im2[i][j] :
                    count = count + 1
    return count

def sub_img(img1, img2) :
    for i in range(100) :
        for j in range(100) :
            if img2[i][j] > 0 :
                img1[i][j] = 0 
    return img1

def and_img(im1, im2) :
    for i in range(100) :
      for j in range(100) :
        im2[i][j] = im1[i][j] and im2[i][j]
    return im2

def find_pt(img) :
    f = 0
    for i in range(0,100) :
      for j in range(0, 100) :
        if img[i][j] > 0  :
          f = 1
          print("intersection point :  ", end = '')
          print("x:",j," y:",i)
    return f

def find_cirx(img) :
    #print("processing...")
    pts = pointsx(img)
    w = {}
    score = 0
    for p in pts :
      for j in range(len(p) - 1) :
        cir = find_centerx(p[0],p[j+1])
        if cir[1] <= 0 or cir[1] >= 50 :
          continue
        else :
          tst = np.zeros((100,100), np.uint8)
          draw_circ(tst,cir[0],cir[1])
          m = compare_img(img, tst)
          if score <= m :
            score = m
            w[score] = cir
    #print('done')
    return w[max(w)]
  
def find_ciry(img) :
    #print("processing...")
    pts = pointsy(img)
    w = {}
    score = 0
    for p in pts :
      for j in range(len(p) - 1) :
        cir = find_centery(p[0],p[j+1])
        if cir[1] <= 0 or cir[1] >= 50 :
          continue
        else :
          tst = np.zeros((100,100), np.uint8)
          draw_circ(tst,cir[0],cir[1])
          m = compare_img(img, tst)
          if score <= m :
            score = m
            w[score] = cir
    #print('done')
    return w[max(w)]