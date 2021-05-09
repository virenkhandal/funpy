function [w,t,hi,flg] = RKF(Fcn, Intv, alpha, tol, stepsize)
// %
// % Written by Ming Gu for Math 128A, Fall 2008
// % 
format long;
flg  = 0;
a    = Intv(1);
b    = Intv(2);
hmin = stepsize(1);
hmax = stepsize(2);
h    = min(hmax,b-a);
if (h<=0)
    msg = ['Illegal hmax or interval'];
    error('InvalidFUN',msg);
end
w    = alpha;
t    = a;
c    = [0;      1/4; 3/8;       12/13;      1;  1/2];
d    = [25/216  0    1408/2565  2197/4104 -1/5  0   ];
r    = [1/360   0   -128/4275  -2197/75240 1/50 2/55];
KC   = [zeros(1,5); 
        1/4,       zeros(1,4); 
        3/32       9/32       zeros(1,3);
        1932/2197 -7200/2197, 7296/2197, 0,         0;
        439/216   -8          3680/513  -845/4104,  0;
          -8/27    2         -3544/2565  1859/4104 -11/40];
K    = zeros(6,1);
%
% main loop
%
i = 0;
hi = h;
while (flg == 0)
%     print("t: ", t, "w: ", w, "h: ", h)
    ti   = t(end);
    wi   = w(end);
    for j = 1:6
        K(j) = h*Fcn(ti+c(j)*h,wi+KC(j,:)*K(1:5));
    end
%
% accept approximation
%
    R = max(eps,abs(r*K)/h);
    if (R <= tol)
        t = [t; ti+h];
        w = [w; wi+d*K];
        hi = [hi; h];
    end
%
% reset stepsize.
%
    delta = 0.84*(tol/R)^(1/4);
    delta = min(4,max(0.1,delta));
    h     = min(hmax, delta * h);
    h     = min(h, b-t(end));
    if (abs(h)<eps)
        return;
    end
    if (h < hmin)
        flg = 1;
        return;
    end 
    i = i + 1;
end