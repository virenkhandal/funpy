function [root, iterations] = SteffensenMethod()
format long;
    function y = func(x)
     y = sqrt((x+1)/x);
    end
    
 bound1 = "Enter your initial approximation: ";
 lower_bound = input(bound1);
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 maxItprompt = "Enter the maximum number of iterations: ";
 n = input(maxItprompt);
 
 p0 = lower_bound;
  
 i = 1;
 while (i <= n)
     p1 = func(p0);
     p2 = func(p1);
     p = p0 - ((p1 - p0)^2)/(p2-(2 * p1)+p0);
     
     if (abs(p - p0) < TOL)
         root = p;
         iterations = i;
         return;
     end
     
     p0 = p;
     i = i + 1;
 end
 return
end
 
        