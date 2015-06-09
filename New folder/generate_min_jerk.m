function stretch = generate_min_jerk( xi, xf, dur, T )
%GENERATE_MIN_JERK Summary of this function goes here
%   Detailed explanation goes here

t = linspace(0, 1.0, dur / T);
stretch_minjerk = xi + (xi - xf) *( (15.0 * t.^4) - (6.0 * t.^5) - (10.0 * t.^3));



stretch_final = [   repmat(stretch_minjerk(1), 1, 200)...
                    stretch_minjerk ...
                    repmat(stretch_minjerk(end), 1, 200)];
time_final = [1:length(stretch_final)] * T;

stretch = [time_final; stretch_final]';



