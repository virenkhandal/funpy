function [w,t, flg] = Trapezoidal(Fcn, Dy, Intv, alpha, N, M, tol)
// % On input: 
// %   FunFcnIn is the name of function to be integrated
// %   FunDyFcnIn is the name of derivative function d(FunFcnIn)/dy
// %
// %   interv is the interval to be integrated over
// % 
// %   The problem: y = f(t,y), y(a) = alpha, a<= t <= b
// %   where Intv = [a b], and a call to FunFcnIn with 
// %   argument (t, y) returns f(t,y).
// %
// %   N is the number of equi-spaced mesh points on which to approximate 
// %   the unknown function, and tol is the tolerance of Newton iteration.
// %   M is the maximum number of Newton iterations per time step.
// %
// %   TrapNewton solve the ODE using implicity trapezoidal method, coupled 
// %   with Newton iteration to approximate y at N+1 equi-spaced points on [a, b].
// %
// % On output
// %   w contains the approximations at the mesh points.
// %   flg ~= 0 indicates failure.
// %
// % Written by Ming Gu for Math 128A, Fall 2008
// % 
[Fcn,msg] = fcnchk(Fcn,0);
if ~isempty(msg)
    error('InvalidFUN',msg);
end
[Dy,msg] = fcnchk(Dy,0);
if ~isempty(msg)
    error('InvalidFUN',msg);
end
a    = Intv(1);
b    = Intv(2);
h    = (b-a)/N;
w    = zeros(N+1,1);
w(1) = alpha;
t    = a + (0:N)'*h;
h2   = h / 2;
for i = 1:N
    k1 = w(i) + h2* Fcn(t(i),w(i));
    w0 = w(i);
%%
%% uncomment the line below for the initial guess suggested in the text
    w0 = k1;
%%
    flg= 1;
    for j = 1:M
        w0new   = w0 - (w0-h2* Fcn(t(i)+h,w0)-k1)/(1-h2*Dy(t(i)+h,w0));
        if (abs(w0new-w0)<tol)
            w(i+1) = w0new;
            flg = 0;
            break;
        end
        w0 = w0new;
    end
    if (flg == 1)
        return;
    end