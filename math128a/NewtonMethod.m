function [root, iterations] = NewtonMethod()
format long;
    function y = func(x)
       y = (exp(6 * x)) + (1.441 * exp(2 * x)) - (2.079 * exp(4 * x)) - 0.3330;
    end

    function z = derivative(x)
       z = (6 * exp(6 * x)) + (2.882 * exp(2 * x)) - (8.316 * exp(4 * x));
    end
    
 initialprompt = "Enter your first initial approximation: ";
 p0 = input(initialprompt);
 
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 
 maxItprompt = "Enter the maximum number of iterations: ";
 n = input(maxItprompt);
 
 
 i = 1;
 while (i <= n)
    p = p0 - (func(p0) / derivative(p0));
    str = sprintf("p_%d = %d", i, p);
    X = ["p_", num2str(i), " = ", num2str(p)];
    disp(str);
    if (abs(p - p0) <= TOL)
        root = p;
        iterations = i;
        return;
    end
    i = i + 1;
    p0 = p;
 end
end
 