# Testing code

import numpy as np 
import conversion_math


def test_strike(deltax, deltay, answer):
	strike = conversion_math.get_strike(deltax, deltay);
	print("Computed strike is : %.1f ; Correct strike is %.1f degrees" % (strike, answer) );
	return;

def test_rake(ss, ds, answer):
	rake=conversion_math.get_rake(ss,ds);
	print("Computed rake is : %.1f ; Correct rake is %.1f degrees" % (rake, answer) )
	return;


if __name__=="__main__":
	test_strike(1, 0.0, 90);  
	test_strike(-1, 0.0, 270); 
	test_strike(0.0, -1.0, 180); 
	angle = -160;
	test_strike(np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle)), 250);


	test_rake(1, 0, 0)
	test_rake(0,1,90);
	test_rake(0,-1,-90);
	test_rake(-1,0,180);