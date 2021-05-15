function [root, iterations] = SecantMethod()
format long;
    function y = func(r)
     y = (4 * pi * (r + 0.25)) + (2000/(r^2)) - ((2000 * (2 * pi * r + 0.25))/(pi * r^3));
    end
    
 bound1 = "Enter your first initial approximation: ";
 lower_bound = input(bound1);
 
 bound2 = "Enter your second initial approximation: ";
 upper_bound = input(bound2);
 
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 
 maxItprompt = "Enter the maximum number of iterations: ";
 n = input(maxItprompt);
 
 p0 = lower_bound;
 p1 = upper_bound;
 
 i = 2;
 q0 = func(p0);
 q1 = func(p1);
 while (i <= n)
     p = p1 - (q1 * (p1 - p0))/(q1-q0);
     if (abs(p - p1) < TOL)
         root = p;
         iterations = i;
         return;
     end
     i = i + 1;
     p0 = p1;
     q0 = q1;
     p1 = p;
     q1 = func(p);
 end
 return
end