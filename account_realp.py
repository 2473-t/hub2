# this script is made for estimate a relatively accurate value of the  real interest rate .
import sys
 
sys.setrecursionlimit(1000)

side1=0.0000
side2=1.0000
cal_time=0


r=0.5000
n=float(input('please input the limit time (years):'))
bond_init=float(input('please input the Initial measurement value:'))
bond_face=float(input('please input the Face value:'))
bond_face_profit=float(input('please input the face interest per year:'))
dif_rate_limit=float(input('please input the max Difference rate acceptable (suggest 0.0000001) :'))
def func_bond():
    global r,side1,side2,cal_time
    cal_time=cal_time+1

    P_F=1/((1+r)**n)
    #num2=(1+r)**n
    #num1=1/(r*num2)
    P_A=(1-P_F)/r
    num=(P_F * bond_face) + (P_A * bond_face_profit)

    num=round(num,2)
    difference=abs(bond_init-num)
    differrate=difference/bond_init
    if differrate<=dif_rate_limit :
        print('The real interest rate is',r,'almost as %.2f'%(100*r),end='')
        print('%')
        print('total calculating times is',cal_time)
    elif num < bond_init :
        side2=r
        r=(side1+side2)/2
        func_bond()
    else :
        side1=r
        r=(side1+side2)/2
        func_bond()
func_bond()