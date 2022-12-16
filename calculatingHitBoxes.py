#Calculating Hit Boxes 2:00pm, Nov. 15th 2022, Jaylin Moody, v0.9

#Hit Box Type
boxType = 0 # 1 = 2D Box, 2 = 3D Box
if boxType == 1:
    print("You have chosen a 2D hit box.\n")
elif boxType == 2:
    print("You have chosen a 3D hit box.\n")
else:
    print("Invalid box selection, please restart the program.\n")

# A Box
boxALength = 0
boxAWidth = 0
boxAHeight = 0

# B Box
boxBLength = 0
boxBWidth = 0
boxBHeight = 0

# Box A Measurements
boxALength = int(input("Please enter an interget value for Box A Length.\n")) 
boxAWidth = int(input("Please enter an interget value for Box A Width.\n")) 
boxAHeight = int(input("Please enter an interget value for Box A Height.\n")) 

# Box B Measurment
boxBLength = int(input("Please enter an interget value for Box B Length.\n"))
boxBWidth = int(input("Please enter an interget value for Box B Width.\n")) 
boxBHeight = int(input("Please enter an interget value for Box B Height.\n"))

# Box A Area Calcs.
boxA2D = boxAWidth * boxALength
boxA3D = boxAWidth * boxALength * boxAHeight

# Box B Area Calcs.
boxB2D = boxBWidth * boxBLength
boxB3D = boxBWidth * boxBLength * boxBHeight

# Verify Measurements
print(f"Box A Measurement -- Height: {boxAHeight} Width: {boxAWidth} Length {boxALength}")
print(f"Box B Measurement -- Height: {boxBHeight} Width: {boxBWidth} Length {boxBLength}")  

# Print Areas for Box A and Box B
if boxType == 1:
    print(f"Box A -- 2D Area: {boxA2D} 3D Area: {boxA2D}")
elif boxType == 2:
    print(f"Box B -- 2D Area: {boxB3D} 3D Area: {boxB3D}") 
else:
    print("Something has gone terribly wrong, please restart the program.\n")
    quit()

# Compare Which Is Larger, Print the % Difference
if boxType == 1 and boxA2D > boxB2D:
    print("Box A 2D is Larger than Box B 2D.")
    
    # Determine the Difference Between Larger Hit Box and Smaller Hit Box
    boxDiff = boxB2D - boxA2D 
   
    # Calculate Average Area
    avgArea = (boxA2D + boxB2D) / 2
    
    # Divide Differece by Average
    diffDivByAvg = boxDiff / avgArea
    
    # Divide Difference by Average
    percentDiff = diffDivByAvg * 100
    print(f"Box A 2D is {percentDiff:.2f}% larger than Box B.")

elif boxType == 1 and boxB2D > boxA2D: 
    print("Box A 2D is Larger to Box B 2D.")
   # Determine the Difference Between Larger Hit Box and Smaller Hit Box
    boxDiff = boxB2D > boxA2D 
   
    # Calculate Average Area
    avgArea = (boxA2D + boxB2D) / 2
    
    # Divide Differece by Average
    diffDivByAvg = boxDiff / avgArea
    
    # Divide Difference by Average
    percentDiff = diffDivByAvg * 100
    print(f"Box A 2D is {percentDiff:.2f}% larger than Box B.")

elif boxType == 1 and boxA2D == boxA2D:
    print("Box A 2D is Equal to Box B 2D.")
    boxDiff = boxA2D == boxB2D 
    avgArea = (boxA2D + boxB2D) / 2
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100
    print(f"Box A 2D is {percentDiff:.2f}% equal to Box B 2D.")
    
elif boxType == 2 and boxA3D > boxB3D:
    print("Box A 3D is Larger than Box B 3D.")
    boxDiff = boxA3D > boxB3D 
    avgArea = (boxA3D + boxB3D) / 2
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100
    print(f"Box A 3D is {percentDiff:.2f}% larger than Box B 3D.")

elif boxType == 2 and boxA3D > boxB3D:
    print("Box A 3D is Larger than Box B 3D.")
    boxDiff = boxA3D > boxB3D 
    avgArea = (boxA3D + boxB3D) / 2
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100
    print(f"Box A 3D is {percentDiff:.2f}% larger than Box B 3D.")
   
elif boxType == 2 and boxA3D == boxB3D:
    print("Box A 3D is Equal to Box B 3D.")
    boxDiff = boxA3D == boxB3D 
    avgArea = (boxA3D + boxB3D) / 2
    diffDivByAvg = boxDiff / avgArea
    percentDiff = diffDivByAvg * 100
    print(f"Box A 3D is {percentDiff:.2f}% equal to Box B 3D.")
else:
    print("Hit Box Type still not identified correctly. Please restart the program.\n")

