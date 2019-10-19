from circ_lib import *
import time
# c1 = (46, 46)
# c2 = (48 + 4, 46)
# r1 = 4
# r2 = 4
# ci = (c1,r1,c2,r2)
# input_image = create_2circs(c1,c2,r1,r2) # for testing purpose
# sho(input_image,'ip')
# #print(ci)
'''
Program to check if two circles in an 100x100 image intersect and find points of intersection
lib : opencv2, numpy
uncomment sho(...) to view the image
Jeevan K
'''
#t = time.clock()
#print(t)

ip_img_path = 'input.png'    #specify path to the input image
input_image = cv2.imread(ip_img_path, cv2.IMREAD_GRAYSCALE)

input_image = amp(input_image)
#sho(input_image,'n ip')

time.clock()
def main(img) :
    ip_copy = img.copy()

    first_circle_inf = find_cirx(img)
    first_circle_img = create_circ(first_circle_inf[0],first_circle_inf[1])
    #sho(first_circle_img,"first "+str(first_circle_inf))

    subed_img = sub_img(ip_copy,first_circle_img)
    #sho(subed_img,'sub image')

    second_circle_inf1 = find_cirx(subed_img)
    second_circle_img1 = create_circ(second_circle_inf1[0], second_circle_inf1[1])
    score1 = compare_img(img, second_circle_img1)
    #sho(second_circle_img1,'second1 '+str(score1))

    second_circle_inf2 = find_ciry(subed_img)
    second_circle_img2 = create_circ(second_circle_inf2[0],second_circle_inf2[1])
    score2 = compare_img(img, second_circle_img2)
    #sho(second_circle_img2,'second2 '+str(score2))

    if score1 > score2 :
        second_circle_img = second_circle_img1
        second_circle_inf = second_circle_inf1     #((center),radius)
    else :
        second_circle_img = second_circle_img2
        second_circle_inf = second_circle_inf2

    #sho(second_circle_img, 'secnd '+str(second_circle_inf))

    intersec_img = and_img(first_circle_img, second_circle_img)

    #sho(intersec_img, 'inter '+str(find_pt(intersec_img)==1))
    print(str(find_pt(intersec_img)==1))

main(input_image)

#print(time.clock())