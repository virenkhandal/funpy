function [root, iterations] = MullerMethod()
format long;
    function y = func(x)
     y = (16 * (x ^ 4)) + (88 * (x ^ 3)) + (159 * (x ^ 2)) + (79 * x) - 240;
    end
    
 bound1 = "Enter your first initial approximation: ";
 lower_bound = input(bound1);
 bound2 = "Enter your second initial approximation: ";
 upper_bound = input(bound2);
 bound3 = "Enter your third initial approximation: ";
 third_bound = input(bound3);
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 maxItprompt = "Enter the maximum number of iterations: ";
 n = input(maxItprompt);
 
 p0 = lower_bound;
 p1 = upper_bound;
 p2 = third_bound;
  
 h1 = p1 - p0;
 h2 = p2 - p1;
 delta1 = (func(p1) - func(p0))/h1;
 delta2 = (func(p2) - func(p1))/h2;
 d = (delta2 - delta1)/(h2 + h1);
 i = 3;
 while (i <= n)
     b = delta2 + (h2 * d);
     D = sqrt(((b^2) - (4 * func(p2) * d)));
     
     E = 0;
     if (abs(b - D) < abs(b + D))
         E = b + D;
     else
         E = b - d;
     end
     
     h = (-2 * func(p2)) / E;
     p = p2 + h;
     if (abs(h) < TOL)
         root = p;
         iterations = i;
         return;
     end
     
     p0 = p1;
     p1 = p2;
     p2 = p;
     h1 = p1 - p0;
     h2 = p2 - p1;
     delta1 = (func(p1) - func(p0))/h1;
     delta2 = (func(p2) - func(p1))/h2;
     d = (delta2 - delta1)/(h2 + h1);
     i = i + 1;
 end
 return
end