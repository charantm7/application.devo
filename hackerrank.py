if __name__ == '__main__':
    
    record = []
    scores = set()
    sec_lowest_name = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        scores.add(score) 
        
    second_lowest_score = sorted(scores)[1]
    
    for name,score in record:
        if score == second_lowest_score:
            sec_lowest_name.append(name)
            
    for name in sorted(sec_lowest_name):
        print(name)
        
