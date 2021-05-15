function [w,t] = AdamsAdaptPC(Fcn, Intv, alpha, tol,stepsize)
% On input: 
%   Fcn is the name of function to be integrated
%   interv is the interval to be integrated over
% 
%   The problem: y' = f(t,y), y(a) = alpha, a<= t <= b
%   where Intv = [a b], and a call to Fcn with 
%   argument (t, y) returns f(t,y).
%
%   AdamsAdaptPC uses the Adams Variable Step-size PC method to solve
%   the above problem, to a given tolerance. 
%   hmin and hmax are the minimum and maximum step sizes.
%
% On output
%   t contains the (unequi-spaced) mesh points, w the
%   function values at these points. 
%
% Written by Ming Gu for Math 128A, Fall 2008
% Updated Spring 2021
%
format long;
flg  = 0;
a    = Intv(1);
b    = Intv(2);
hmin = stepsize(1);
hmax = stepsize(2);
h    = min(hmax,(b-a)/5);
if (h<=0)
    msg = ['Illegal hmax or interval'];
    error('InvalidFUN',msg);
end
p = [25/720  -1274/720 2616/720 -2774/720 1901/720];
c = [-19/720 106/720 -264/720 646/720 251/720];
%
% RK4 for the first 3 steps
%
nflg      = 1;
[f, w, t] = RK(Fcn, a,h,alpha);
%
% main loop
%
flg = 0;
i   = 5;
last= 0;
while (flg == 0)
    wi   = w(i);
    ti   = t(i);
    tnew = ti + h;
    wp   = wi + h*(p*f(i-4:i));
    fp   = Fcn(tnew,wp);
    wc   = wi + h*(c*[f(i-3:i);fp]);
    sigma= max(eps,19*abs(wc-wp)/(270*h));
    if (sigma <= tol)
        i    = i + 1;
        t(i) = tnew;
        w(i) = wc;
        f(i) = Fcn(tnew,wc);
        if (last == 1)
            return;
        end

        nflg = 0;
        if (sigma <= 0.1*tol || tnew+h>b)
            q  = (tol/(2*sigma))^(1/4);
            h  = min(hmax,min(q,5)*h);
            if (tnew + 5 * h > b)
                h = (b-tnew)/5;
                last = 1;
            end
            nflg = 1;
            [f1, w1, t1] = RK(Fcn, t(i), h, w(i));
            f = [f(1:i);f1(2:end)];
            w = [w(1:i);w1(2:end)];
            t = [t(1:i);t1(2:end)];
            i = i + 4;
        end
    else
        q  = (tol/(2*sigma))^(1/4);
        h  = max(q,0.1)*h;
        if (h < hmin)
            disp(['hmin exceeded']);
            flg = 1;
            return;
        end
        if (nflg == 1)
            i = i - 4;
        end
        nflg = 1;
        [f1, w1, t1] = RK(Fcn, t(i), h, w(i));
        f = [f(1:i);f1(2:end)];
        w = [w(1:i);w1(2:end)];
        t = [t(1:i);t1(2:end)];
        i = i + 4;
    end
end
function [f,w, t] = RK(Fcn, a,h,alpha)
%
% performs 3 steps of RK4
%
w    = zeros(5,1);
f    = zeros(5,1);
w(1) = alpha;
h2   = h/2;
t    = a+(0:4)'*h;
for i = 1:4
    f(i) = Fcn(t(i),w(i));
    k1 = h* f(i);
    k2 = h* Fcn(t(i)+h2,w(i)+k1/2);
    k3 = h* Fcn(t(i)+h2,w(i)+k2/2);
    k4 = h* Fcn(t(i)+h,w(i)+k3);
    w(i+1) = w(i) + (k1+2*k2+2*k3+k4)/6;
end
f(5) = Fcn(t(5),w(5));