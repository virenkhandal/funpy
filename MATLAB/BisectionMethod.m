function [root, iterations] = BisectionMethod()
format long;
    function y = func(x)
     y = (600 * (x ^ 4)) - (550 * (x ^ 3)) + (200 * (x ^ 2)) - (20 * x) - 1;
    end

    function z = derivative(x)
     z = (2400 * (x ^ 3)) - (1650 * (x ^ 2)) + (400 * x) - 20;
    end
    
 bound1 = "Enter your lower bound: ";
 lower_bound = input(bound1);
 
 bound2 = "Enter your upper bound: ";
 upper_bound = input(bound2);
 
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 
 a = lower_bound;
 b = upper_bound;
 
 if (sign(func(a)) == sign(func(b)))
     return;
 else
     i = 0;
     p = a + ((b - a) / 2);
     while (abs(func(p)) > TOL)
         i = i + 1;
            p = a + ((b - a) / 2);
            curr = func(p);
            if (sign(curr) == sign(func(a)))
                a = p;
            else
                b = p;
            end
     end
     root = p;
     iterations = i;
     return;
 end
 
 
end
 
        
 
