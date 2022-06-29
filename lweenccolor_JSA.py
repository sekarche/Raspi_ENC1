import math
import timeit
from PIL import Image
import numpy as np
import random
#import cv2


def chaoticdif(x,img):
   x1=[]
   x1 = [0 for i in range(0,262144)]
   di=[]
   di = [0 for i in range(0,262144)]
   for i1 in range(0,262144):
      x1[i1] =math.ceil(x[i1]*pow(10,12))%256;
   for i2 in range(0,262144):
      di[i2]=img[i2]^x1[i2]
   # i1=i1+1;
   return di
def piecewise(yy):
    y=[]
    y = [0 for i in range(0,262144)]
    y[0]=yy
    p=0.256
    for i in range(0,262143):
        if (y[i]>0 and y[i]<=p):
            y[i+1]=y[i]/p
        if(y[i]>p and y[i]<=0.5):
            y[i+1]=(y[i]-p)/(0.5-p)
        if(y[i]>0.5 and y[i]<1):
            y[i+1]=1-y[i]
    return y   
        
   
def tent(x2):
  
   x3=[]
   x3 = [0 for i in range(262144)]
   x3[0]=x2
   u=3.999998
   for i in range(0,262143):
       if x3[i]<0.5:
        x3[i+1]=u*(x3[i]/2)
                  
        
       elif x3[i]>=0.5:
           x3[i+1]=u*((1-x3[i])/2)
   return x3
def bi2de(binary):
    
    binary1 = binary
    decimal = 0
    i = 0
    while(i!= 8):
     #   dec = binary1 % 10
        decimal = decimal + binary1[i] * pow(2, i)
        #binary = binary//10
        i += 1
    return decimal

# def pershu(x,img):
#     y1=0
#     yy=[]
#     yy = [0 for i in range(262144)]
#     x1=[]
#     x1 = [0 for i in range(262144)]
#     k=0
#     # res=''
#     # res1=0
#     for i2 in range(0,262144):
#        x1[i2]=math.ceil(x[i2]*pow(10,12))
    
#     for ii in range(0,262144):
#         y1=format(img[ii],'08b')
#         y1=''.join(reversed(y1))
#         digits = [int(xx) for xx in str(y1)]
#         r=(x1[k]%757)+1
#         z=(r%7)+1
#         for j in range(7,0,-1):
#               r1=(math.ceil(pow(r,z))%(j+1))
#               tmp=digits[r1];
#               digits[r1]=digits[j];
#               digits[j]=tmp;
#         yy[ii]=bi2de(digits)
#         k=k+1
#     return yy
def lwesi(x,img):
    z3=[0,0,0,0]
    z1=[]
    z1 = [0 for i in range(0,262144)]
    im=[]
    im = [0 for i in range(0,262144)]
    for i in range(262144):
      z1[i]=math.ceil(x[i]*pow(10,12))%256
    for ii in range(0,262144,4):
        z3=[img[ii],img[ii+1],img[ii+2],img[ii+3]]
        y=format(z1[ii],'08b')
        y1=format(z1[ii+1],'08b')
        y2 = [int(xx) for xx in str(y)]
        y3 = [int(xx) for xx in str(y1)]
        aa=[z1[ii],z1[ii+1],z1[ii+2],z1[ii+3]]
        bb=[[y2[7],-y2[6],y2[5],-y2[4]],[y2[3],-y2[2],y2[1],-y2[0]],[y3[7],-y3[6],y3[5],-y3[4]],[y3[3],-y3[2],-y3[1],y3[0]]]
        mat=np.matmul(aa,bb)
        for i in range(4):
            mat[i]=mat[i]%256
        mat1=[[mat[0],mat[1],(1-mat[0])%256,-mat[1]%256],[mat[2],mat[3],-mat[2]%256,(1-mat[3])%256],[(1+mat[0])%256,mat[1]%256,-mat[0]%256,-mat[1]%256],[mat[2]%256,(1+mat[3])%256,-mat[2]%256,-mat[3]%256]]
        zz=np.matmul(mat1,z3)
        for i in range(4):
            zz[i]=zz[i]%256
        for j in range(4):
              im[ii+j]=zz[j]
    return im
def chaostrans(img):
    j=0
    k=0
    bits1 = []
    bits1=[0 for i in range(262144)]
    img1 = []
    img1=[0 for i in range(262144)]
    with open('index.txt') as f:
              bits=f.read().split("k")
              f.close()
              for i in range(0,262144):
                  bits1[i]=int(bits[i])-1
              for i in range(262144):
                  j=bits1[i]
                  img1[k]=img[j]
                  k=k+1
              return img1
def chaosblkscr(img):
   bits2 =[]
   bits2=[0 for i in range(16384)]
   bits3 =[]
   bits3=[0 for i in range(16384)]
   with open('index1.txt') as f:
              bits2=f.read().split("k")
              f.close()
   for i in range(0,16384):
      bits3[i]=int(bits2[i])-1
   k=0
   a =[]
   a=[0 for i in range(262144)]
   b =[]
   b=[0 for i in range(16384)]
   a1 =[]
   a1=[0 for i in range(16384)]

   for i in range(0,262144,16):
      a1[k]=img[i:i+16]
      #[a[i],a[i+1],a[i+2],a[i+3]]
      k=k+1
   k=0    
   for i in range(0,16384):
    j=bits3[i]
    b[k]=a1[j]
    k=k+1
   k=0
   for i in range(0,262144,16):
     a[i:i+16]=b[k]
     k=k+1    
   return a      

  
if __name__ == "__main__":
    im = Image.open('C:/Users/NIT CSE/Desktop/desktop 2/comp comm python code/lenacolor.jpg')
    
    im1 = Image.Image.split(im)
    pixa = im1[0].load()
    pixb=im1[1].load()
    pixc=im1[2].load()
    pix1=[]
    pix1 = [0 for i in range(0,262144)]
    k=0
    for i1 in range(512):
        for j1 in range(512):
            pix1[k]=pixa[i1,j1]
            k=k+1
    pix2=[]
    pix2 = [0 for i in range(0,262144)]
    k=0
    for i1 in range(0,512):
        for j1 in range(0,512):
            pix2[k]=pixb[i1,j1]
            k=k+1
    pix3=[]
    pix3 = [0 for i in range(0,262144)]
    k=0
    for i1 in range(0,512):
        for j1 in range(0,512):
            pix3[k]=pixc[i1,j1]
            k=k+1
    r=random.random()
    r1=random.random()
    start = timeit.default_timer() 
    arr=tent(0.1236)
    arr1=piecewise(0.2345)
    a1=chaosblkscr(pix1)
    a2=chaostrans(a1)
    a3=chaoticdif(arr,a2)
    #a4=pershu(arr,a3)
    a4=lwesi(arr1,a3)
    #stop = timeit.default_timer()
    #Time=start-stop
    pixr=np.zeros((512, 512))
    pixr1=np.zeros((512, 512))
    k=0
    for i in range(512):
        for j in range(512):
            pixr[i][j]=a4[k]
            k=k+1
    pixr1 = np.array(pixr, dtype=np.uint8)
    imr= Image.fromarray(pixr1)
    r=random.random()
    r1=random.random()
    arr=tent(0.3456)
    arr1=piecewise(0.5647)
    a1=chaosblkscr(pix2)
    a2=chaostrans(a1)
    a3=chaoticdif(arr,a2)
    #a4=pershu(arr,a3)
    a5=lwesi(arr1,a3)
    #stop = timeit.default_timer()
    #Time=start-stop
    pixb=np.zeros((512, 512))
    pixb1=np.zeros((512, 512))
    k=0
    for i in range(512):
        for j in range(512):
            pixb[i][j]=a5[k]
            k=k+1
    pixb1 = np.array(pixb, dtype=np.uint8)
    imb= Image.fromarray(pixb1)
    r=random.random()
    r1=random.random()
    arr=tent(0.4567)
    arr1=piecewise(0.9845)
    a1=chaosblkscr(pix3)
    a2=chaostrans(a1)
    a3=chaoticdif(arr,a2)
    #a4=pershu(arr,a3)
    a5=lwesi(arr1,a3)
    #stop = timeit.default_timer()
    #Time=start-stop
    pixg=np.zeros((512, 512))
    pixg1=np.zeros((512, 512))
    k=0
    for i in range(512):
        for j in range(512):
            pixg[i][j]=a5[k]
            k=k+1
    pixg1 = np.array(pixg, dtype=np.uint8)
    img= Image.fromarray(pixg1)
    stop = timeit.default_timer()
    Time=stop-start
    # im.save('enc2.png')
    merged=Image.merge("RGB",(imr,imb,img))
    merged.save('C:/Users/NIT CSE/Desktop/desktop 2/comp comm python code/lenaencclr.png')
    merged.show()
    
    
