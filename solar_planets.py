import cv2 

img = cv2.imread("solar-system.jpg")
 
cv2.putText(
    img,
    "The Solar System - Harjith :)",
    (70,40),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Sun",
    (110,360),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (0,102,255)
)

cv2.putText(
    img,
    "Mercury",
    (125,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,255)
)

cv2.putText(
    img,
    "Venus",
    (200,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (25,68,100)
)

cv2.putText(
    img,
    "Earth",
    (300,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,0,0)
)

cv2.putText(
    img,
    "Moon",
    (320,160),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (400,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (0,29,54)
)

cv2.putText(
    img,
    "Jupiter",
    (500,300),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (650,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.8,
    (51,64,92)
)

cv2.putText(
    img,
    "Uranus",
    (950,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.6,
    (230,216,173)
)

cv2.putText(
    img,
    "Neptune",
    (1150,150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,0,0)
)

cv2.imshow("Display Image",img)

cv2.waitKey(10000)

