# Initial Dataset
# Methods = the different methods to check
# TP = True Positives
# FP = False Positives
# FN = False Negatives
# TN = True Negatives

import operator # Allow us to sort using a class attribute
import matplotlib.pyplot as plt # Plotting and figures
import numpy as np # numeric arrays

class Method:

    def __init__(self,MethodName, TruePos, FalsePos, FalseNeg, TrueNeg):
        self.Name = MethodName # Name of the Method
        self.TP = TruePos # True positive
        self.FP = FalsePos # False positive
        self.FN = FalseNeg # False negative
        self.TN = TrueNeg # True negative

        self.PR = None # Precision / Higher is better
        self.SP = None # Specificity / Higher is better
        self.RC = None # Recall / Higher is better
        self.FNR = None # False Negative Rate / Lower is better
        self.FPR = None # False Positive Rate / Lower is better
        self.ACC = None # Accuracy / Higher is better
        self.S = None # Spatial Accuracy / Higher is better
        self.FM = None # F-Measure / Higher is better

    def SolveMetrics(self):  # Function to solve every metric for a method
        if (self.TP + self.FP) != 0:
            self.PR = self.TP / (self.TP + self.FP)
        else:
            self.PR = 0
        self.SP = self.TN / (self.TN + self.FP)
        self.RC = self.TP / (self.TP + self.FN)
        self.FNR = self.FN / (self.TP + self.FN)
        self.FPR = self.FP / (self.FP + self.TN)
        self.ACC = (self.TN + self.TP) / (self.TP + self.FN + self.FP + self.TN)
        self.S = self.TP / (self.TP + self.FN + self.FP)
        if (self.PR + self.RC) != 0:
            self.FM = (2 * self.PR * self.RC) / (self.PR + self.RC)
        else:
            self.FM = 0



# Define every method and pass arguments (TP, FP, FN, TN)
List = []
List.append(Method("A", 100, 900, 0, 0))
List.append(Method("B", 80, 125, 20, 775))
List.append(Method("C", 25, 25, 75, 875))
List.append(Method("D", 50, 50, 50, 850))
List.append(Method("E", 0, 0, 100, 900))

# Print methods and values
print("\nMethods Values: \n")
print("Method | TP | FP | FN | TN")
for object in List:
    print("   " + object.Name + "    " + str(object.TP) + "  " + str(object.FP) + "   " + str(object.FN) + "    " + str(object.TN))

# Solve every metric
for method in List:
    method.SolveMetrics()

# Print metric in table
print("\nMetrics Results: \n")
print("Method | PR | SP | RC | FNR | FPR | ACC | S | FM")
for object in List:    
    print("  " + object.Name + "     " + str(round(object.PR,2)) + "  " + str(round(object.SP,2)) + "  " + str(round(object.RC,2)) + "  " + str(round(object.FNR,2)) + "  "\
         + str(round(object.FPR,2)) + "  " + str(round(object.ACC,2)) + "  " + str(round(object.S,2)) + "  " + str(round(object.FM,2)))
print("")
# Metrics comparison and sorting
PR_Sorted = sorted(List, key=operator.attrgetter('PR'))
SP_Sorted = sorted(List, key=operator.attrgetter('SP'))
RC_Sorted = sorted(List, key=operator.attrgetter('RC'))
FNR_Sorted = sorted(List, key=operator.attrgetter('FNR'))
FPR_Sorted = sorted(List, key=operator.attrgetter('FPR'))
ACC_Sorted = sorted(List, key=operator.attrgetter('ACC'))
S_Sorted = sorted(List, key=operator.attrgetter('S'))
FM_Sorted = sorted(List, key=operator.attrgetter('FM'))

# Print results
print("The best method in Precision is " + PR_Sorted[-1].Name + " with PR = " + str(PR_Sorted[-1].PR))
print("The best method in Specificity is " + SP_Sorted[-1].Name + " with SP = " + str(SP_Sorted[-1].SP))
print("The best method in Recall is " + RC_Sorted[-1].Name + " with RC = " + str(RC_Sorted[-1].RC))
print("The best method in False negative rate is " + FNR_Sorted[0].Name + " with FNR = " + str(FNR_Sorted[0].FNR))
print("The best method in False Positive rate is " + FPR_Sorted[0].Name + " with FPR = " + str(FPR_Sorted[0].FPR))

print("The best method in Accuracy is " + ACC_Sorted[-1].Name + " with ACC = " + str(ACC_Sorted[-1].ACC))
print("The best method in Spatial Accuracy is " + S_Sorted[-1].Name + " with S = " + str(S_Sorted[-1].S))
print("The best method in F-Measure is " + FM_Sorted[-1].Name + " with FM = " + str(FM_Sorted[-1].FM))
## Plots

# False Negatives Vs False Positives
xPoints = []
yPoints = []
List_FN = sorted(List, key=operator.attrgetter('FN'))
for i,object in enumerate(List_FN):
    xPoints.append(object.FN)
    yPoints.append(object.FP)

xPoints_a = np.array(xPoints)
yPoints_a = np.array(yPoints)

plt.scatter(xPoints, yPoints)
plt.plot(xPoints, yPoints)

for i, obj in enumerate(List_FN):
    plt.annotate(obj.Name, (xPoints[i], yPoints[i]))

# x-axis label
plt.xlabel('False Negatives')
# frequency label
plt.ylabel('False Positives')
# plot title
plt.title('False Negatives vs False Positives')
plt.show()

# Precision Vs Recall
xPoints = []
yPoints = []
for i,object in enumerate(PR_Sorted):
    xPoints.append(object.PR)
    yPoints.append(object.RC)

xPoints_a = np.array(xPoints)
yPoints_a = np.array(yPoints)

for i, obj in enumerate(PR_Sorted):
    plt.annotate(obj.Name, (xPoints[i], yPoints[i]))

plt.scatter(xPoints, yPoints)
plt.plot(xPoints, yPoints)
# x-axis label
plt.xlabel('Precision')
# frequency label
plt.ylabel('Recall')
# plot title
plt.title('Precision Vs Recall')
plt.show()

# Accuracy Vs F-Measure
xPoints = []
yPoints = []
for i,object in enumerate(ACC_Sorted):
    xPoints.append(object.ACC)
    yPoints.append(object.FM)

for i, obj in enumerate(ACC_Sorted):
    plt.annotate(obj.Name, (xPoints[i], yPoints[i]))

xPoints_a = np.array(xPoints)
yPoints_a = np.array(yPoints)

plt.scatter(xPoints, yPoints)
plt.plot(xPoints, yPoints)
# x-axis label
plt.xlabel('Accuracy')
# frequency label
plt.ylabel('F-Measure')
# plot title
plt.title('Accuracy Vs F-Measure')
plt.show()