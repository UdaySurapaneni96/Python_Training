#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy.interpolate import CubicSpline
# Q1. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
def product_except_self(nums):
    n = len(nums)
    right_product = np.ones(n)
    answer = np.ones(n)

# Calculate the product of all elements to the left of each element
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]

    # Calculate the product of all elements to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

lst=[2,4,6,8,10]
ans=product_except_self(lst)
print(ans)

# Q2. Assume you are given a dictionary pnl_grid with they keys representing issuer id and values being a tuple of (shock_list, pnl_list). pnl_list corresponds to pnl obtained by shocks from shock_list. shocks gives us the shocks applied to each issuer.
# Task: Find the pnl for each issuer using the shock from the shocks by interpolating between shock_list and pnl_list. Use CubicSpline from scipy, refer for arguments: https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html
# Example: pnl_grid = {1: ([1.5, 0, 1.0, 2.0], [-100, 0, -50, 250]), 2: ([10.0, 0, 4.0, 4.0], [-500, 10, -150, 300])} The output should be (only an illustrative example, not accurate): {1: 20, 2: -200}

shocks = {
    506: 0.486,
    258: 0.661,
    358: 0.371,
    735: 0.293,
    166: 0.203,
    781: 0.633,
    789: 0.529,
    822: 0.86,
    728: 0.038,
    725: 0.886
}

pnl_grid = {
    506: ([0.465,0.05,0.345,0.629,0.289,0.05,0.243,0.822,0.665,0.856], [-220.983,-217.841,-220.074,-222.224,-219.65,-217.841,np.nan,-223.685,np.nan,-223.942]),
    258: ([0.473,0.232,0.649,0.19,0.962,0.93,0.639,0.059,0.831,0.837], [-653.225,-654.91,-651.994,-655.203,-649.806,-650.03,-652.064,np.nan,-650.722,-650.68]),
    358: ([0.97,0.836,0.031,0.831,0.634,0.56,0.046,0.094,0.202,0.198], [687.434,686.908,683.749,686.888,686.115,685.825,683.808,683.997,684.42,684.405]),
    735: ([0.949,0.326,0.205,0.952,0.543,0.032,0.926,0.826,0.875,0.846], [-426.147,-428.488,-428.943,-426.136,-427.673,-429.593,-426.234,-426.609,np.nan,-426.534]),
    166: ([0.041,0.48,0.575,0.09,0.412,0.12,0.584,0.306,0.981,0.649], [769.374,762.653,761.199,768.624,763.694,np.nan,761.061,np.nan,754.983,760.066]),
    781: ([0.569,0.334,0.102,0.744,0.685,0.546,0.85,0.097,0.791,0.249], [-449.069,-448.246,np.nan,-449.682,np.nan,-448.989,-450.054,-447.416,-449.847,-447.948]),
    789: ([0.864,0.536,0.223,0.578,0.646,0.147,0.401,0.535,0.51,0.69], [477.718,472.913,468.328,473.528,474.525,467.215,470.936,472.899,472.532,475.169]),
    822: ([0.051,0.068,0.386,0.224,0.618,0.969,0.581,0.616,0.405,0.573], [-999.429,-999.695,-1004.679,-1002.14,-1008.315,-1013.816,-1007.735,-1008.284,-1004.977,-1007.61]),
    728: ([0.605,0.18,0.575,0.316,0.723,0.911,0.98,0.291,0.823,0.63], [336.468,332.996,336.223,334.107,np.nan,338.968,339.531,333.903,338.249,336.672]),
    725: ([0.76,0.703,0.223,0.785,0.211,0.48,0.644,0.551,0.871,0.275], [-204.815,-205.658,-212.755,np.nan,-212.933,-208.955,-206.53,-207.905,-203.174,-211.986]),
}

def calculate_pnl(shock_list, pnl_list, shocks):
    cleaned_data = [(shock, pnl) for shock, pnl in zip(shock_list, pnl_list) if not np.isnan(pnl)]
    cleaned_data.sort(key=lambda x: x[0])
    
    eps = 1e-8
    shock_list, pnl_list = zip(*cleaned_data)
    shock_list = np.array(shock_list)
    shock_list[1:] = np.maximum(shock_list[1:], shock_list[:-1] + eps)
    
    cs = CubicSpline(shock_list, pnl_list, extrapolate=True)
    pnl = cs(shocks)
    return pnl

pnl_results = {}

for issuer_id, (shock_list, pnl_list) in sorted(pnl_grid.items()):
    if issuer_id in shocks:
        shock = shocks[issuer_id]
        pnl = calculate_pnl(shock_list, pnl_list, shock)
        pnl_results[issuer_id] = pnl

print(pnl_results)
for issuer_id, pnl in pnl_results.items():
    print(f"Issuer {issuer_id}: {pnl}")


# Q3) Task: Calulate the expected default pnl over the next year for each issuer by follwing the simulation(use 1000 sims) below: 
# Generate shock for every issuer at each timestep, shocks must lie between 0 and 1 and use issuer id as the seed
# find the scenarios where the issuer defaults
# if an issuer defaults, calculate the deault pnl at that timestep using the shock and the pnl_grid defined above, use your function from Q2
# if an issuer does not default at a timestep, default pnl is zero at that timestep
# if an issuer has defaulted in any of the previous timesteps, default pnl is zero in subsequent timesteps.
# Expected pnl for each issuer is average default pnl across all simulations


cutoffs = {
    506: 0.4,
    258: 0.6,
    358: 0.3,
    735: 0.3,
    166: 0.2,
    781: 0.6,
    789: 0.5,
    822: 0.8,
    728: 0.4,
    725: 0.4
}

def simulate_default_pnl(pnl_grid, cutoffs, shocks, num_simulations=1000, num_timesteps=4):
    default_pnl_results = {}

    for issuer_id, cutoff in sorted(cutoffs.items()):
        total_default_pnl = 0

        for sim in range(num_simulations):
            np.random.seed(issuer_id)
            issuer_shocks = np.random.uniform(0, 1, num_timesteps)

            issuer_defaulted = False
            issuer_default_pnl = 0

            for timestep in range(num_timesteps):
                if not issuer_defaulted and issuer_shocks[timestep] > cutoff:
                    issuer_defaulted = True
                    issuer_default_pnl = calculate_pnl(shock_list,pnl_list,issuer_shocks[timestep])
                
                total_default_pnl += issuer_default_pnl
        
        expected_default_pnl = total_default_pnl / num_simulations
        default_pnl_results[issuer_id] = expected_default_pnl

    return default_pnl_results

default_pnl_results = simulate_default_pnl(pnl_grid, cutoffs, shocks)
print(default_pnl_results)
for issuer_id, default_pnl in default_pnl_results.items():
    print(f"Issuer {issuer_id}: Expected Default P&L - {default_pnl}")

