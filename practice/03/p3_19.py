weight = float(input('体重入力>>'))
stature = float(input('身長(cm)>>'))
statureM = (stature/100)
BMI = (weight / statureM ** 2)
print(f"BMI={BMI}")