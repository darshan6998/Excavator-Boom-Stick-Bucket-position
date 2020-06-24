import math as m
import matplotlib.pyplot as plt
x_cord=input("Enter X-Coordinates(in mm): ")
y_cord=input("Enter Y-Coordinates(in mm): ")
orientation=input("Enter Orientation with respect to positive X-Axis(in Degrees): ")
print("Calculating..........................")
x=float(x_cord)
y=float(y_cord)
angle=float(orientation)
l1=300
l2=200
l3=100
phi=m.radians(angle)
x1=x+l3*m.cos(phi)
y1=y+l3*m.sin(phi)
d=pow(x1,2)+pow(y1,2)
try:
  c2=((pow(l1,2)+pow(l2,2)-d)/(2*l1*l2))
  theta_2=m.acos(c2)
  theta_11=m.atan2(y1,x1)
  theta_12=m.acos((pow(l1,2)+d-pow(l2,2))/(2*l1*m.sqrt(d)))
  theta_1=theta_11+theta_12
  theta_3=2*3.14+phi-(theta_1+theta_2+3.14)
  s1=m.sqrt(pow(140,2)+pow(100,2)-2*140*100*m.cos(theta_1))
  s2=m.sqrt(pow(80,2)+pow(50,2)-2*80*50*m.cos(theta_2))
  s3=m.sqrt(pow(60,2)+pow(50,2)-2*60*50*m.cos(theta_3))
  print("Lenght of Actuator 1:",s1,"mm")
  print("Length of Actuator 2:",s2,"mm")
  print("Length of Actuator 3:",s3,"mm")
  print("Plotting Graph")
  x2=l1*m.cos(theta_1)
  y2=l1*m.sin(theta_1)
  plt.plot([0,x2], [0,y2],'b-')
  plt.plot([x2,x1],[y2,y1],'r-')
  plt.plot([x1,x],[y1,y],'g-')
  plt.show()
except:
  print("Area out of reach")
