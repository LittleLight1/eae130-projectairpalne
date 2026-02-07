import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Unit conversions


# Weight requirements

# Crew
num_pilots = 1
person_weight = 200/2.205# kg

# Payload
W_payload = 15000/2.205 #kg     

W_crew = num_pilots*person_weight
print("W_crew: " + str(W_crew) + " kg")
print("W_payload: " + str(W_payload) + " kg")

# Mission
R_cruise = 1000*1852 # m
R_strike = 50*1852 # m

E_loiter = 20 * 60 # s
E_comb = 5 * 60 # s

# Performance Inputs
c_tosi = 1/2.205 * 1/4.448 * 1/3600 #Unit change to SI for SFC
c_cruise = 0.8 * c_tosi # lb/(lbf hr)
c_strike = 0.85 * c_tosi# lb/(lbf hr)
c_comb = 1.85 * c_tosi# lb/(lbf hr)

V_cruise = 273.42 # m/s
V_strike = 306.27 # m/s
V_combat = 607.6 # m/s
L_D = 8


# W0 Initial Weight
# W0_W1 Warm-up, taxi, and take-off
# W1_W2 Climb
# W2_W3 Cruise
# W3_W4 Combat
# W4_W5 Cruise
# W5_W6 Loiter
# W6_W7 Descent/Two Landings
# W7 Final Weight

#Typical Fuel Fractions (From references)
W1_W0 = 0.99*0.99*0.99 # Warmup, taxi, take-off
W2_W1 = 0.96 # Climb
W3_W2 = np.exp((-R_cruise*c_cruise) / (V_cruise*L_D))  # cruise
W4_W3 = np.exp((-R_strike*c_strike) / (V_strike*L_D)) # strike
#W4_W3 = np.exp((-E_loiter*c_cruise) / (L_D)) # air-to-air combat
W5_W4 = np.exp((-R_cruise*c_cruise) / (V_cruise*L_D))  # cruise
W6_W5 = np.exp((-E_loiter*c_cruise) / (L_D))
W7_W6 = 0.99*0.995*0.995 # Descent/Two Landings

print("Warmup-Takeoff Fuel Fraction (W1/W0): ", str(round(W1_W0, 3)))
print("Climb Fuel Fraction (W2/W1): ", str(round(W2_W1, 3)))
print("Cruise Fuel Fraction (W3/W2): " + str(round(W3_W2**2, 3)))
print("Combat Fuel Fraction (W4/W3): " + str(round(W4_W3, 3)))
print("Loiter Fuel Fraction (W6/W5): " + str(round(W6_W5, 3)))

W7_W0 = W7_W6 * W6_W5 * W5_W4 * W4_W3 * W3_W2 * W2_W1 * W1_W0
print("Final Weight Fraction (W5/W0): " + str(round(W7_W0, 3)))

Wf_W0 = (1-W7_W0) * 1.06    # compute fuel fraction
print("Total Fuel Fraction Wf/W0: {:.3f}".format(Wf_W0))

W0 = 32081/2.205  # kg, initial empty weight guess
W0_history = []   # list of all W0 guesses for plot
err = 1e-6        # relative convergence tolerance
delta = 2*err     # any value greater than the tolerance

# Raymer's Regression Constants
A = 2.34          # From Raymer Table 3.1
C = -0.13         # From Raymer Table 3.1

while delta > err:
    W0_history.append(W0)                                 # add latest value to list
    We_W0 = A*W0**C                                       # kg, Compute empty weight ratio
    W0_new = (W_crew + W_payload) / (1 - Wf_W0 - We_W0)   # kg, compute new TOGW
    delta = abs(W0_new - W0) / abs(W0_new)                # find difference between last guess and current guess  
    W0 = W0_new                                           # kg, update TOGW value
    
W0_history = np.array(W0_history)  # convert list to array

# Plot Convergence
plt.figure(figsize=(8,4))
plt.title('Weight Estimate Convergence')
plt.xlabel("Iteration")
plt.ylabel("W0 (kg)")
plt.plot(W0_history, label='W0', linestyle='-', linewidth=2, marker=None, markersize=8)
plt.grid(True)
plt.legend(loc='best')
plt.show()
We = We_W0 * W0
print("Empty Weight: " + str(round(We)) + " kg")
print("Our regression's Empty Weight Fraction (We/W0): " + str(round(We/W0 ,3)))

print("Takeoff Gross Weight: " + str(round(W0)) + " kg")
print("Maximum Gross Weight: " + str(round(W0*2.205)) + " lb")
