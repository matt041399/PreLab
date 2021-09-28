import csv
def compare(thread_dict):
    with open('gold.csv', 'r') as file:
        reader = csv.reader(file)
        gold_dict = {}
        for row in reader:   
            gold_dict[row[0]] = row[1]
        totalMatch = 0
        counter = 1
        while counter < 51:
            if(int(thread_dict[str(counter)]) == int(gold_dict[str(counter)])):
                totalMatch += 1
            else:
                print("incorrect thread #:")
                print(counter)
                print("auto, gold")
                print(int(thread_dict[str(counter)]), int(gold_dict[str(counter)]))
            counter += 1
        print("Accuracy (%): ")
        print(totalMatch * 100 / 50)


def writeFile(threadDict, len):
    f = open('output.csv', 'a')
    writer = csv.writer(f)

    for i in sorted(threadDict.items()):
        writer.writerow(i)
    
    

def readFile():
    with open('file.csv', 'r') as file:
        reader = csv.reader(file)
        placeHolder = "1"
        thread_dict = {}
        for row in reader:   
            counter = row[0]
            if placeHolder != counter:
                placeHolder = counter
            if (thread_dict.has_key(placeHolder) == False):
                thread_dict[placeHolder] = 0
            if ("?" in row[3]):
                thread_dict[placeHolder] = thread_dict[placeHolder] + 1
        writeFile(thread_dict, placeHolder)
        compare(thread_dict)
                
            
            
    

f = open('output.csv', 'w')
writer = csv.writer(f)
writer.writerow(["thread", "Number of Questions"])
readFile()
