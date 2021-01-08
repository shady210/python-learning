
import csv
fields = []

with open('files/course.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    fields = next(csv_reader)
    print(csv_reader)
    def studentByQualification(qualification):
            for row in csv_reader:
                if row[4]==qualification:
                    print(list(row))
                else:
                    pass

    def countStudentPlaced():
        count = 0
        for row in csv_reader:
            if row[3] == 'Y':
                count += 1
            else: 
                pass       
        print(f'Number of Student placed is: {count}')    
    
    def countStudentbyQualification(qualifications):
        cnt = 0
        for row in csv_reader:
            if row[4] == qualifications:
                cnt +=1
            else:
                pass
        print(f'Student count of {qualifications} is {cnt}')

    def countStudentPlacedAndCourse():
        cnt = 0
        for row in csv_reader:
            if row[2] == 'Y' and row [3] == 'Y':
                cnt +=1
            else:
                pass
        print(f'Number of student who placed and completed the course successfully: {cnt}')

    def countStudentplacedorNotplaced(placed_or_not):
        cnt = 0 
        cnt1 = 0
        for row in csv_reader:
            if row[3] =='Y':
                cnt +=1
              
            elif row[3] == 'N':
                cnt1 +=1
               
            else:
                pass
        print(f'Number of student who got placed are: {cnt}')
        print(f'Number of student not got placed: {cnt1}')


    def searchName(name):
        for row in csv_reader:
            
            if row[0]==name:
                print(f'{row[0]} Name found in the file.')
            else:
                pass
        

    def studentName():
        for row in csv_reader:
            print(f'{row[0]}')    
  
    
    def studentNameandScore():
        for row in csv_reader:
            print(f'{row[0]} {row[4]} {row[5]}')


    def avgSuccessRate(batch):
        batchSuccess = 0
        batchStudent = 0
        for row in csv_reader:
            if row[1] == batch:
                if row[3] == 'Y':
                    batchSuccess += 1
                batchStudent +=1
        print(batchStudent, batchSuccess)
        print(f'{batch} Success rate: {float(100*(batchSuccess/batchStudent))}')


    def maximumPercent():
        prcnt = 0 
        for row in csv_reader:
            if float(row[5]) > float(prcnt):
                prcnt = row[5]
        for row in csv_reader:
            if float(row[5]) == float(prcnt):
                print(f'Student details is: {row}')
    
    
    
    
    
    if __name__ == "__main__":

        print("1. Student by qualification\n2. Student count by placed student\n3. Student count by Qualification\n4. Student count who completed course but not placed\n5. Student count of placed and not placed student\n6. Search student by the given name\n7. Get all the student name only\n8. Get all the student name,qualification,score\n9. Get average success rate of the given batch\n10. Get max percentage scored Student details")
        num = int(input("Enter the choices? "))
        if num == 1:
            qualification = input("Enter the qualifications ")
            studentByQualification(qualification)
        elif num == 2:
            countStudentPlaced()
        elif num == 3:
            qualifications = input("Enter the qualifications ")
            countStudentbyQualification(qualifications)
        elif num == 4:
            countStudentPlacedAndCourse()
        elif num == 5:
            placed_or_not = input("Enter Y or N for count")
            countStudentplacedorNotplaced(placed_or_not)
        elif num == 6:
            name = input('Enter first name of student: ')
            searchName(name)
        elif num == 7:
            studentName()
        elif num == 8:
            studentNameandScore()
        elif  num == 9:
            batch = input('Enter batch: ') 
            avgSuccessRate(batch)
        elif num == 10:
            maximumPercent()
          
        
   

    


            


    

    
       
    
        
