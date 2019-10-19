Statement:

Write a program which takes a 100x100 binary image as an input which has two circles in it, where pixels on the circles have value 1 and rest have value 0. 
The program should return TRUE if the two circles intersect and FALSE otherwise.
In the event the circles intersect, the program should also return the point(s) of the intersection.


Solution:

Written in        : Python 3
Libraries used    : opencv2, numpy
main program file : 2cirkels.py
Basic explanation :

-The given 100x100 image is scanned line by line to find the points of circle in the image.
-For every two points in a line, another image with a circle(with those two points) is created.
-The image is compared with the i/p image to find the circles in the image.
-The first circle is subtracted form the image.
-The image of second circle is obtained.
-Two images of first and second circles are put through AND operation.
-The intersection point are found.

-Most of the edge cases are handled.
-May fail for very small intersecting circles.


* Put the i/p image in the same directory as the program
* Name the i/p image - "input.png" [should be 100x100 with circle boundary of width 1px]
* Uncomment sho() functions to view image. (press any key to continue after viewing the image)
* Wait when the console shows "processing..."
* o/p : False 			              ; circles don't intersect
	    True and intersection points  ; circles intersect

		--------------------------------------xxx---------------------------------------------
	