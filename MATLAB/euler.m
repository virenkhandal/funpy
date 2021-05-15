function [w,t] = Euler(Fcn, Intv,alpha, N)
a = Intv(1);
b = Intv(2);
h = 0.1;
t = a;
w = alpha;
w1 = 0.09516;
str1 = sprintf("t = %d, w = %d", t, w);
str1 = sprintf("t = %d, w = %d", t, w1);
disp(str1);
for i=1:N
// %     disp(Fcn(t, w));
// %     func_val = Fcn(t, w);
// %     disp(func_val)
// %     incr = h * func_val;
// %     disp(w + incr)
// %     upd = w + incr;
     w1 = (4 * w1) - (3 * w) - (2 * h * Fcn(t, w));
     w = w1;
// %     disp(w)
     t = a + (i * h);
     str1 = sprintf("t = %d, w = %d", t, w1);
     disp(str1);
end

end

