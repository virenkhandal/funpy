clear

%Set up test cases
%Highly recommend to check other cases in the paper.
tol = 1e-15; params.maxit = 100;
% func_tol does not need to be adjusted
params.func_tol = tol;
test_functions{1} = @(x) x+3*cos(x)-exp(x); test_intervals{1} = [0, 1.0]; test_it(1) = 6;
test_functions{2} = @(x) log(x - 1) + cos(x - 1); test_intervals{2} = [1.3, 2]; test_it(2) = 8;
test_functions{3} = @(x) 3*x - exp(x); test_intervals{3} = [1, 2]; test_it(3) = 10;
test_functions{4} = @(x) x^3 - x - 1; test_intervals{4} = [1.0, 2.0]; test_it(4) = 10;
test_functions{5} = @(x) (2-exp(-x)+x^2)/3-x; test_intervals{5} = [-5, 5]; test_it(5) = 15;

%%
% New test set
%%
test_functions{5} = @(x) exp(x) - (2 + 2*x.^2); test_intervals{5} = [0, 4]; test_it(5) = 12;
test_functions{6} = @(x) 10e-12*(exp(x) - x^2 -2); test_intervals{6} = [-1, 3]; test_it(6) = 12;
% Ignore this test case
%test_functions{4} = @(x) exp(sin(10e-7*x)) + sin(x) - 1; test_intervals{4} = [1e8, 2e8]; test_it(4) = 24;
% Use this instead
test_functions{7} = @(x) -x.^3-cos(x); test_intervals{7} = [-3.0,3.0]; test_it(7) = 13;
test_functions{8} = @(x) exp(x) + log(2+2*x^2)-x^2 -2; test_intervals{8} = [-4, 4]; test_it(8) = 12;



test_functions{9} = @(x) sqrt(x) - cos(x); test_intervals{9} = [0, 1]; test_it(9) = 8;
test_functions{10} = @(x) 3*(x+1)*(x-0.5)*(x-1); test_intervals{10} = [-1.2, 2.5]; test_it(10) = 8;
test_functions{11} = @(x) x^3 - 7*x^2 + 14*x - 6; test_intervals{11} = [0, 1]; test_it(11) = 8;
test_functions{12} = @(x) exp(x) - x^2 + 3*x - 2; test_intervals{12} = [0, 1]; test_it(12) = 7;
test_functions{13} = @(x) 2*x*cos(2*x) - (x + 1)^2; test_intervals{13} = [-3, -2]; test_it(13) = 8;
test_functions{14} = @(x) x^2 - 4*x + 4 - log(x); test_intervals{14} = [1, 2]; test_it(14) = 8;
test_functions{15} = @(x) x^2 - 4*x + 4 - log(x); test_intervals{15} = [2, 4]; test_it(15) = 10;
test_functions{16} = @(x) x + 1 - 2*sin(pi*x); test_intervals{16} = [0, 0.5]; test_it(16) = 8;
test_functions{17} = @(x) x + 1 - 2*sin(pi*x); test_intervals{17} = [0.5, 1]; test_it(17) = 10;
test_functions{18} = @(x) exp(x) - 2 - cos(exp(x) - 2); test_intervals{18} = [-1, 2]; test_it(18) = 11;
test_functions{19} = @(x) (x + 2) * (x + 1)^2 * x * (x - 1)^3 * (x - 2); test_intervals{19} = [-0.5, 2.4]; test_it(19) = 13;
test_functions{20} = @(x) (x + 2) * (x + 1)^2 * x * (x - 1)^3 * (x - 2); test_intervals{20} = [-0.5, 3]; test_it(20) = 15;
test_functions{21} = @(x) (x + 2) * (x + 1)^2 * x * (x - 1)^3 * (x - 2); test_intervals{21} = [-3, -0.5]; test_it(21) = 13;
test_functions{22} = @(x) (x + 2) * (x + 1) * x * (x - 1)^3 * (x - 2); test_intervals{22} = [-1.5, 1.8]; test_it(22) = 15;
test_functions{23} = @(x) x^4 - 3*x^2 - 3; test_intervals{23} = [1, 2]; test_it(23) = 8;
test_functions{24} = @(x) x^3 - x - 1; test_intervals{24} = [1, 2]; test_it(24) = 10;
test_functions{25} = @(x) pi + 5*sin(x/2) - x; test_intervals{25} = [0, 6.3]; test_it(25) = 7;
test_functions{26} = @(x) 2^(-x) - x; test_intervals{26} = [0.3, 1]; test_it(26) = 6;
test_functions{27} = @(x) (2 - exp(-x) + x^2)/3 - x; test_intervals{27} = [-5, 5]; test_it(27) = 15;
test_functions{28} = @(x) 5*x^(-2) + 2 - x; test_intervals{28} = [1, 5]; test_it(28) = 8;
test_functions{29} = @(x) sqrt(exp(x)/3) - x; test_intervals{29} = [2, 4]; test_it(29) = 9;
test_functions{30} = @(x) 5^(-x) - x; test_intervals{30} = [-2, 5]; test_it(30) = 9;
test_functions{31} = @(x) 5*(sin(x) + cos(x)) - x ; test_intervals{31} = [-2, 1]; test_it(31) = 7;
test_functions{32} = @(x) -x^3 - cos(x); test_intervals{32} = [-3, 3]; test_it(32) = 13;
test_functions{33} = @(x) x^3 - 2*x^2 - 5; test_intervals{33} = [1, 4]; test_it(33) = 9;
test_functions{34} = @(x) x^3 + 3*x^2 - 1; test_intervals{34} = [-3, -2]; test_it(34) = 8;
test_functions{35} = @(x) x - cos(x); test_intervals{35} = [0, 1.6]; test_it(35) = 7;
%test_functions{36} = @(x) x - 8 - 2*sin(x); test_intervals{36} = [0, 1.6]; test_it(36) = 7;
test_functions{36} = @(x) exp(x) + 2^(-x) + 2*cos(x) - 6; test_intervals{36} = [1, 2]; test_it(36) = 8;
test_functions{37} = @(x) log(x - 1) + cos(x - 1); test_intervals{37} = [1.3, 2]; test_it(37) = 8;
test_functions{38} = @(x) 2*x*cos(2*x) - (x - 2)^2; test_intervals{38} = [2, 3]; test_it(38) = 8;
test_functions{39} = @(x) exp(x) - 3*x^2; test_intervals{39} = [3, 5]; test_it(39) = 12;
test_functions{40} = @(x) sin(x) - exp(-x); test_intervals{40} = [0, 1]; test_it(40) = 7;




%% Get Results
failure_list = {};
it_buff = @(x) max(ceil(x*1.2), x+3);
fcalls2score = @(x, it) (40*(x <= it) + 20/it*(it*3 - x)*((x > it) & (x < 3*it)) + 0*(x >= 3*it))/40;
filename = 'modifiedbrent'; % your function name
profile on
for j = 1:40
    Int.a = test_intervals{j}(1); Int.b = test_intervals{j}(2);
    params.root_tol = max(max(abs(Int.a), abs(Int.b)),1.0)*tol;
    myfunctionstring = [filename, '(test_functions{j}, Int, params);'];
    try
        profile on
        [root, info] = eval(myfunctionstring);
        profile off

        %%%%%%%%%%%%%%%%%%%%%%%%
        % When root is not numeric, put an invalid value.
        if (isnumeric(root) == 0 || isempty(root))
            root = Int.b+10;
        end
        % Raehyun
        %%%%%%%%%%%%%%%%%%%%%%%%

        %Store Roots
        roots(1, j) = root;
        %Grade Roots
        if or(isnan(root), isinf(root))
            fcalls(1, j) = inf;
            roots_scores(1, j) = 0;
            fcalls_scores(1, j) = 0;
        else
            %%%%%%%%%%%%%%%%%%%%%%%%
            % Modified to use the relative error instead of the absolute eror
            % to cover the case that the root is huge.
            root_tol_check = abs(root - fzero(test_functions{j}, root)) < params.root_tol;
            func_tol_check = abs(test_functions{j}(root)) < params.func_tol;
            int_check = (root > Int.a) & (root < Int.b);
            % Raehyun
            %%%%%%%%%%%%%%%%%%%%%%%%
            %%%%%%%%%%%%%%%%%%%%%%%%
            % Modified to return 0 value when it can't find a proper root
            % root_tol_check OR func_tol_check
            if (root_tol_check || func_tol_check) && int_check
                roots_scores(1, j) = 12;
            else
                roots_scores(1, j) = 0;
            end
            % Raehyun
            %%%%%%%%%%%%%%%%%%%%%%%%
            %Store Number of Function Calls
            p = profile('info');
            blah = {p.FunctionTable.CompleteName};
            coo = strfind(blah, func2str(test_functions{j}));
            fcall_idx = find(~cellfun(@isempty, coo));
            fcalls(1, j) = p.FunctionTable(fcall_idx).NumCalls;
            %%%%%%%%%%%%%%%%%%%%%%%%
            % Modified to return 0 value when it can't find a proper root
            if (root_tol_check || func_tol_check) && int_check
                fcalls_scores(1, j) = fcalls2score(fcalls(1, j), it_buff(test_it(j)));
            else
                fcalls_scores(1, j) = 0;
            end
            % Raehyun
            %%%%%%%%%%%%%%%%%%%%%%%%
        end
    catch
        fprintf('failed: %s\n', filename);
        failed = 1;
    end
end
disp('total score')
disp(sum(fcalls_scores)+sum(roots_scores)*60/(40*12))
disp('fcalls_scores')
disp(fcalls_scores)
disp('roots_scores')
disp(roots_scores)