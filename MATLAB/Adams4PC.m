function [w,t] = Adams4PC(Fcn, Intv, alpha, N)

w(1) = alpha;
h2   = h/2;
for i = 1:3
    k1 = h* Fcn(t(i),w(i));
    k2 = h* Fcn(t(i)+h2,w(i)+k1/2);
    k3 = h* Fcn(t(i)+h2,w(i)+k2/2);
    k4 = h* Fcn(t(i)+h,w(i)+k3);
    w(i+1) = w(i) + (k1+2*k2+2*k3+k4)/6;
end
p = h*[-9/24  37/24 -59/24 55/24];
c = h*[ 1/24 -5/24   19/24 9/24 ];
f = Fcn(t(1:4), w(1:4)); 
for i = 4:N
    wp     = w(i) + p*f;
    fp     = Fcn(t(i+1),wp);
    w(i+1) = w(i) + c *[f(2:end);fp];
    f      =[f(2:end); Fcn(t(i+1),w(i+1))];
end
