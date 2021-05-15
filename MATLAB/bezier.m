function [bx,by] = Bezier(x,y,alphal,betal,alphar,betar)
    // % bezier curve 
    // % 
    n  = length(x);
    bx = zeros(n-1,4);
    by = zeros(n-1,4);
    bx = [x(1:n-1), alphal(1:n-1), x(2:n)-x(1:n-1) - alphal(1:n-1), 2*(x(2:n)-x(1:n-1))-(alphal(1:n-1)+alphar(2:n))];
    by = [y(1:n-1), betal(1:n-1),  y(2:n)-y(1:n-1) - betal(1:n-1),  2*(y(2:n)-y(1:n-1))-(betal(1:n-1)+betar(2:n))];
// %     for i = 1:4
// %         if i ~= 1
// %             if i ~= 4
// %                 bx(i) = 3 * bx(i);
// %                 by(i) = 3 * by(i);
// %             end
// %         end
// %     end
end

// %%
// % In order to get Bezier polynomial, uncomment for loops
// % Current code gives interpolation polynomials, not Bezier polynomial
// % Refer to page 183/918 (Example 2) to see interpolation polynomials
