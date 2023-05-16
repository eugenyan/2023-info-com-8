
import statistics

nums = input("Ingrese lista de numeros separados por comas (hasta 5): ")
nums_l = nums.split(",")

nums_i= [float(x) for x in nums_l]

mean = sum(nums_i)/len(nums_i)
print(mean)