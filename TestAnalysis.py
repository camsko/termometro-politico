import csv
'''
Esta clase analiza 2 inputs de CSV para hacer el analisis estadistico usando
Precision, Recall, Accuracy y F1
'''
with open('manual_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    matrix_man = [row for row in reader]
    matrix_man = [row[2:] for row in matrix_man[2:]]

with open('similitudes_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    matrix_auto = [row for row in reader]
    matrix_auto = [row[2:] for row in matrix_auto[2:]]
        

def classify(umbral_bajo, umbral_alto, m_auto):
    classified = []
    for r in range(len(m_auto)):
        classified.append([])
        for c in range(len(m_auto[r])):
            classified[r].append(2)
            if(float(m_auto[r][c]) < umbral_bajo):
                classified[r][c] = 0
            elif(float(m_auto[r][c]) < umbral_alto):
                classified[r][c] = 1                
    return classified

def calcular_confusion(umbral_bajo, umbral_alto, m_auto, m_man):
    confusion = [[0,0,0],[0,0,0],[0,0,0]] #matriz de confusion de clases 3x3, las columnas son 0 (none), 1(low), 2(high)
    auto_matrix_classified = classify(umbral_bajo, umbral_alto, m_auto)
    for i in range(len(auto_matrix_classified)):
        for j in range(len(auto_matrix_classified[i])):
            clase_real = m_man[i][j]
            clase_predicha = auto_matrix_classified[i][j]
            confusion[int(clase_real)][int(clase_predicha)] += 1
    print(confusion)
    return confusion

def calcular_metricas(confusion):
    total = sum(sum(row) for row in confusion)
    resultados = []

    for clase in range(3):
        tp = confusion[clase][clase]
        fp = sum(confusion[i][clase] for i in range(3) if i != clase)
        fn = sum(confusion[clase][j] for j in range(3) if j != clase)
        tn = total - tp - fp - fn

        precision = tp / (tp + fp) if (tp + fp) != 0 else 0
        recall = tp / (tp + fn) if (tp + fn) != 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
        accuracy = sum(confusion[i][i] for i in range(3)) / total if total != 0 else 0
        
        resultados.append({
            "clase": clase,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "accuracy": accuracy, 
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "tn": tn
        })


    return resultados


def imprimir_confusion(confusion, nombre="Matriz de Confusión"):
    print(f"\n{nombre}")
    print(" "*14 + "Predicha")
    print(" "*10 + "   0     1     2")
    print("         -------------------")
    for i, fila in enumerate(confusion):
        print(f"Real {i}  |  " + "  ".join(f"{x:>3}" for x in fila))

confusion_umbral_bajo = calcular_confusion(0.2, 0.5, matrix_auto, matrix_man)
confusion_umbral_medio = calcular_confusion(0.5, 0.7, matrix_auto, matrix_man)
confusion_umbral_alto = calcular_confusion(0.7, 0.8, matrix_auto, matrix_man)

imprimir_confusion(confusion_umbral_bajo, nombre="Bajo")
imprimir_confusion(confusion_umbral_medio, nombre="Medio")
imprimir_confusion(confusion_umbral_alto, nombre="Alto")

print("\nBajo:")
print(calcular_metricas(confusion_umbral_bajo))
print("\nMedio:")
print(calcular_metricas(confusion_umbral_medio))
print("\nAlto:")
print(calcular_metricas(confusion_umbral_alto))
