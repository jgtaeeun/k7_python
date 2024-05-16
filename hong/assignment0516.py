#person 객체, 상속받은 student객체, 합성 dept
#list로 객체들 다 묶어서 출력

class Person :
    def __init__(self, pid,pname, page):
        self.pid=pid
        self.pname=pname
        self.page=page
    def __str__(self) :
        return f"[Person정보(id,name,age)={self.pid},{self.pname},{self.page}]"
    
class Student(Person):
    def __init__(self,pid, pname, page,sid, syear ):
        super().__init__(pid, pname, page)
        self.sid=sid
        self.syear=syear
        self.sdept=Dept()

    def __str__(self) :
        # super().__str__()
        return  super().__str__()+f"[Student정보(id,year,dept)={self.sid},{self.syear},{self.sdept.sdept_type}]"
    

class Dept():
    def  __init__(self, sdept_type='python'):
        self.sdept_type=sdept_type

    def modify_type(self, department):
        self.sdept_type=department

# p1=Person( 'p1' ,'person1', 10)
# p2=Person( 'p2', 'person2', 20)
# p3=Person( 'p3' ,'person3', 30)
# p4=Person( 'p4', 'person4', 40)
# p5=Person( 'p5' ,'person5', 50)
# p6=Person( 'p6' ,'person6', 60)
# p7=Person( 'p7', 'person7', 70)
# p8=Person( 'p8', 'person8', 80)
# p9=Person( 'p9', 'person9', 90)
# p10=Person( 'p10' ,'person10', 100)

# person_list=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

# s1=Student( 'p1' ,'person1', 10,'s1' , 2010)
# s2=Student( 'p2' ,'person2', 20,'s2' , 2011) 
# s2.sdept.modify_type('Java')

# s3=Student( 'p3' ,'person3', 30,'s3' , 2012)
# s4=Student( 'p4' ,'person4', 40,'s4' , 2013)
# s4.sdept.modify_type('CSS')

# s5=Student( 'p5' ,'person5', 50,'s5' , 2014)
# s6=Student( 'p6' ,'person6', 60,'s6' , 2015)
# s6.sdept.modify_type('React')
# s7=Student( 'p7' ,'person7', 70,'s7' , 2016)
# s8=Student( 'p8' ,'person8', 80,'s8' , 2017)
# s9=Student( 'p9' ,'person9', 90,'s9' , 2018)
# s10=Student( 'p10' ,'person10', 100,'s10' , 2019)

# student_list=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]


# total_list=[*person_list,*student_list]    

# for i in total_list:
#      print(i)

p_list=[]
s_list=[]

for i in range(1,11):
   p_list.append( Person(f"p{i}",f"pname{i}",i*10))
   
   if i ==2 :
    temp=Student(f"p{i}",f"pname{i}",{i*10},f"s{i}",i+2012)
    temp.sdept.modify_type('java')
    s_list.append(temp)
   elif i==8:
    temp=Student(f"p{i}",f"pname{i}",{i*10},f"s{i}",i+2012)
    temp.sdept.modify_type('css')
    s_list.append(temp)   
   else:
    s_list.append( Student(f"p{i}",f"pname{i}",{i*10},f"s{i}",i+2012))
   
print()
total_list=[*p_list,*s_list]    
for i in total_list:
     print(i)