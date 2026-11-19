from collections import Counter

def solution(str1, str2):
    answer = 0
    
    A, B = [], []
    
    for i in range(1, len(str1)):
        if str1[i-1:i].isalpha() and str1[i:i+1].isalpha():
            A.append(str1[i-1:i].lower() + str1[i:i+1].lower())
            
    for i in range(1, len(str2)):
        if str2[i-1:i].isalpha() and str2[i:i+1].isalpha():
            B.append(str2[i-1:i].lower() + str2[i:i+1].lower())
            
    A = Counter(A)
    B = Counter(B)
    
    intersection = A & B
    union = A | B
    
    def jaccard(intersection, union):
        if not intersection and not union:
            return 1
        else:
            return sum(intersection.values()) / sum(union.values())
    
    jaccard_similarity = jaccard(intersection, union)
    
    answer = int(65536 * jaccard_similarity)
    
    return answer