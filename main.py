from point import *
from figure import *

def drawPoint(t,p):
    t.up()
    t.width(10)
    t.pencolor(0, 0, 1)
    t.goto(p.get_cords()[0],p.get_cords()[1])
    t.dot()


def drawLine(t, p1, p2):
    t.up()
    t.width(10)
    t.pencolor(1, 0, 0)  # red
    t.goto(p1.get_cords()[0], p1.get_cords()[1])
    t.down()
    t.goto(p2.get_cords()[0], p2.get_cords()[1])


def drawFigure(t,figure):
    pts = figure.get_points()
    for i in range(0,len(pts)-1):
        drawLine(t,pts[i],pts[i+1])
    drawLine(t,pts[len(pts)-1],pts[0])

def isIntRec(p, figure):
        px = p.get_x()
        py = p.get_y()
        f_pts = figure.get_points()
        f_a_x = f_pts[0].get_x()
        f_b_x = f_pts[1].get_x()
        f_c_x = f_pts[2].get_x()
        f_d_x = f_pts[3].get_x()
        f_a_y = f_pts[0].get_y()
        f_b_y = f_pts[1].get_y()
        f_c_y = f_pts[2].get_y()
        f_d_y = f_pts[3].get_y()
        if (px <= f_b_x) and (px >= f_a_x) and (py <= f_c_y) and (py >= f_a_y):
            print('True')
        else:
            print ('False')

def main():
    # Generating figure and X-point:

    point1 = Point(0, 0)
    point2 = Point(20, 0)
    point3 = Point(30, 40)
    point4 = Point(0, 80)
    figure1 = Figure([point1, point2, point3, point4])
    X_point = Point(1,1)
    isIntRec(X_point, figure1)
    # Stage 2
    X_dots, Y_dots = [], []



if __name__ == '__main__':
    main()
