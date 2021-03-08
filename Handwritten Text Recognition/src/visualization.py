import cv2
import matplotlib.pyplot as plt
import numpy as np


def visualize(img, aabbs):
    img = ((img + 0.5) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for aabb in aabbs:
        aabb = aabb.enlarge_to_int_grid().as_type(int)
        #cv2.rectangle(img, (aabb.xmin, aabb.ymin), (aabb.xmax, aabb.ymax), (0, 0, 0), 2)

    return img


def saveimages(img, aabbs):

    img = ((img + 0.5) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    count=1

    for aabb in aabbs:
        aabb = aabb.enlarge_to_int_grid().as_type(int)
        #cv2.rectangle(img, (aabb.xmin, aabb.ymin), (aabb.xmax, aabb.ymax), (255, 0, 255), 2)
        imgCropped=img[aabb.ymin:aabb.ymax,aabb.xmin:aabb.xmax]
        cv2.imwrite("../data/%d.png"%(count),imgCropped)
        count=count+1

    #for aabb in aabbs:
        #plt.plot([aabb.xmin, aabb.xmin, aabb.xmax, aabb.xmax, aabb.xmin],
                 #[aabb.ymin, aabb.ymax, aabb.ymax, aabb.ymin, aabb.ymin])

    #plt.show()
