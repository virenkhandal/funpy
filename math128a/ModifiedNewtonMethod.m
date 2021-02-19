function [root, iterations] = ModifiedNewtonMethod()
format long;
    function y = func(x)
       y = ((x - 1) ^ 2) * (exp(x));
    end

    function z = derivative(x)
       z = ((x^2) - 1) * (exp(x));
    end
    
 initialprompt = "Enter your first initial approximation: ";
 p0 = input(initialprompt);
 
 multprompt = "Enter the multiplicity of your root: ";
 m = input(multprompt);
 
 maxTolprompt = "Enter your tolerance: ";
 TOL = input(maxTolprompt);
 
 maxItprompt = "Enter the maximum number of iterations: ";
 n = input(maxItprompt);
 
 str1 = sprintf("p_0 = %d, func(p_0) = %d", p0, func(p0));
 disp(str1);
 i = 1;
 while (i <= n)
    p = p0 - (m * (func(p0) / derivative(p0)));
    str = sprintf("p_%d = %d, func(p_%d) = %d", i, p, i, func(p));
    disp(str);
    if (abs(func(p)) <= TOL)
        root = p;
        iterations = i;
        return;
    end
    i = i + 1;
    p0 = p;
 end
end
 
