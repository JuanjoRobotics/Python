# Initial Dataset
# Methods = the different methods to check
# TP = True Positives
# FP = False Positives
# FN = False Negatives
# TN = True Negatives
import operator
import matplotlib.pyplot as plt

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

# Metrics comparison and sorting
PR_Sorted = sorted(List, key=operator.attrgetter('PR'))
SP_Sorted = sorted(List, key=operator.attrgetter('SP'))
RC_Sorted = sorted(List, key=operator.attrgetter('RC'))
FNR_Sorted = sorted(List, key=operator.attrgetter('FNR'))
FPR_Sorted = sorted(List, key=operator.attrgetter('FPR'))
ACC_Sorted = sorted(List, key=operator.attrgetter('ACC'))
S_Sorted = sorted(List, key=operator.attrgetter('S'))
FM_Sorted = sorted(List, key=operator.attrgetter('FM'))



