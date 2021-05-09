function [s, info] = modifiedbrent3034653805(Fcn, Intv, params)
// % On input: 
// %   Fcn is the name of function to find root of
// %   Intv is the interval that contains the root
// % 		- Intv.a is the lower interval
// %		- Intv.b is the upper interval
// %	params is the struct which holds all user parameters
// %		- params.func_tol is the tolerance for value of the root, Fcn(s)
// %		- params.root_tol is the tolerance for the root, s
// %		- params.maxit is is the maximum number of iterations to find s
// %
// %	The problem: Find a root, s, of Fcn on Intv such that
// %	a <= s <= b within params.maxit iterations. The root 
// %   should be accurate to params.root_tol
// %	and the value at the root (Fcn(s)) should be accurate to 
// %	params.func_tol.
// %	
// %	modifiedbrent3034653805 leverages the ideas discussed in 
// %	"A modified Brent’s method for finding zeros of functions"
// %	by Wilkins and Gu, by forcing a bisection step if
// %		- 5 consecutive interpolation steps fail to reduce the original 
// %			interval length by a factor of at least 2
// %		- An interpolation step produces a b such that abs(b)
// %			is not at least a factor of 2 smaller than the 
// %			previous best point.
// %
// %	These modifications to Brents Method reduce the number of
// %	function calls used in our calculation of the root, thus 
// %	leaving us with a much better root-finder than the default
// %	fzero method in MATLAB.
// %
// % On output:
// %	s is the root of Fcn on the given Intv that satisfies params
// %	info indicates whether or not the function successfully ran.
// %		- an info.flag value of 0 indicates success
// %		- an info.flag value of 1 indicates error
// %
// % Written by Viren Khandal for Math 128A, Spring 2021
// % Updated Spring 2021


format long
a = Intv.a;
b = Intv.b;
fa = Fcn(a);
fb = Fcn(b);
root_tol = params.root_tol;
func_tol = params.func_tol;
max_iterations = params.maxit;
if abs(fa) < abs(fb)
    temp = b;
    b = a;
    a = temp;
    temp = fa;
    fa = fb;
    fb = temp;
end
a0 = a;
b0 = b;
if fa*fb >= 0
    printf("root not bounded by a, b")
end

endb = fb;
fc = fa;
c = a;
i = 0;
counter = 0;
while (abs(b-a) > root_tol) && (i < max_iterations)
    if i == 0
%       secant
      s = secant(a, b, fa, fb);
    elseif (fa ~= fc) && (fb ~= fc)
%       iqi
      s = iqi(a, b, c, fa, fb, fc);
    else
%       secant
      s = secant(a, b, fa, fb);
    end
    
    i = i + 1;
    value = Fcn(s);
    curr_bound = abs(b-a);
    half_bound = 1/2*abs(b0 - a0);
%     five succesive steps of interpolation condition
    exceeding_counter = (counter >= 5);
%     weak interval condition
    exceeding_bound = (curr_bound > half_bound);
%     weak value condition
    exceeding_value = (abs(value) > 1/2*abs(endb));
    
%     bisect if new conditions are met
    if exceeding_counter && exceeding_bound || ...
            exceeding_value
%         bisection
        s = bisection(a, b);
        counter = 0;
    else
        counter = counter + 1;
    end
    
    if counter == 0
        value = Fcn(s);
    end
    if abs(value) < abs(fb)
        endb = value;
    end
    if abs(value) < func_tol
        info.flag = 0;
        return
    end 

    c = b;
    fc = fb;
    if fa * value > 0
        a = s;
        fa = value;
    else
        b = s;
        fb = value;
    end
    if abs(fa) < abs(fb)
        temp = b;
        b = a;
        a = temp;
        temp = fa;
        fa = fb;
        fb = temp;
    end
    if counter == 0
        a0 = a;
        b0 = b;
    end
end
if i >= max_iterations
    info.flag = 1;
    return
end
info.flag = 0;
end

function s = iqi(a, b, c, fa, fb, fc)
% Helper function to do IQI method
    s = a*fb*fc/((fa - fb)*(fa - fc)) + b*fa*fc/((fb - fa)*(fb - fc))...
            + c*fa*fb/((fc - fa)*(fc - fb));
end
function s = secant(a, b, fa, fb)
% Helper function to do secant method
    s = b - fb*(b - a)/(fb - fa);
end
function s = bisection(a, b)
% Helper function to do bisection method
    s = (a + b) / 2;
end