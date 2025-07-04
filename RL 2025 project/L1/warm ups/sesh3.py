from math import pi, sqrt

#E1
def circle_area(r):
    area = pi*(r**2)
    return area

radius = 1/sqrt(pi)
area = circle_area(radius)
print(area)

#E2
def circle_areas_ls(radii):
    area_ls = [pi*radius**2 for radius in radii]
    return area_ls

radii = [0,1,1/sqrt(pi)]
area_ls = circle_areas_ls(radii)
print(area_ls)

#E3
def is_pile_long(pile_lengths):
    bool_ls = [pile>=5 for pile in pile_lengths]
    return bool_ls

pile_lengths = [4.51, 6.12, 4.15, 7.31, 5.01, 4.99, 5.00]
bool_ls = is_pile_long(pile_lengths)
print(bool_ls)

#E4
def dist_point_to_line(x,y,x1,y1,x2,y2):
    distance_num = abs((y2-y1)*x-(x2-x1)*y + x2*y1 - y2*x1)
    distance_den = sqrt((x2-x1)**2 + (y2-y1)**2)
    distance = distance_num/distance_den
    return distance

d1 = dist_point_to_line(2, 1, 5, 5, 1, 6)
print(d1)

d2 = dist_point_to_line(1.4, 5.2, 10.1, 2.24, 34.142, 13.51)
print(d2)

#E5
x_coords = [4.1, 22.2, 7.7, 62.2, 7.8, 1.1]
y_coords = [0.3, 51.2, 3.5, 12.6, 2.7, 9.8]

dis_ls = [round(dist_point_to_line(x,y,2,3,8,7),2) for x,y in zip(x_coords, y_coords)]
print(dis_ls)

def shoelace(xv,yv,signed):
    n = len(xv)
    diff_ls = []
    for i in range(n-1):
        diff = xv[i]*yv[i+1] - xv[i+1]*yv[i]
        diff_ls.append(diff)
    
    area = 0.5*sum(diff_ls)
    if not signed:
        area = abs(area)
    return area

x = [3, 4, 7, 8, 8.5, 3]
y = [5, 3, 0, 1, 3, 5]

print(shoelace(x,y, signed=True))

#E7
def centroid(xv, yv):
    n = len(xv)
    area = shoelace(xv, yv, signed=True)
    diff_x_ls = []
    diff_y_ls = []
    for i in range(n-1):
        diff_x = (xv[i] + xv[i+1])*(xv[i]*yv[i+1] - xv[i+1]*yv[i])
        diff_y = (yv[i] + yv[i+1])*(xv[i]*yv[i+1] - xv[i+1]*yv[i])

        diff_x_ls.append(diff_x)
        diff_y_ls.append(diff_y)


    cx = round(sum(diff_x_ls)/(6*area), 3)
    cy = round(sum(diff_y_ls)/(6*area), 3)

    return (cx,cy)

x = [3, 4, 7, 8, 8.5, 3]
y = [5, 3, 0, 1, 3, 5]

print(centroid(x,y))
     