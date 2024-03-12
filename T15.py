class MyDate:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        months = {1: "Yanvar", 
                  2: "Fevral", 
                  3: "Mart", 
                  4: "Aprel", 
                  5: "May", 
                  6: "Iyun", 
                  7: "Iyul", 
                  8: "Avgust",
                  9: "Sentabr", 
                  10: "Oktabr", 
                  11: "Noyabr", 
                  12: "Dekabr"}
                  
        return f"{self.day} {months[self.month]} {self.year} yil"

    def isValidDate(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= self.day <= 31:
                return True
        elif self.month in [4, 6, 9, 11]:
            if 1 <= self.day <= 30:
                return True
        elif self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                if 1 <= self.day <= 29:
                    return True
            elif 1 <= self.day <= 28:
                return True
        return False

    def nextDay(self):
        if self.isValidDate():
            self.day += 1
            if self.day > self.days_in_month():
                self.day = 1
                self.nextMonth()
            return self
        else:
            return "Bunday kun mavjud emas!!!"

    def previousDay(self):
        if self.isValidDate():
            self.day -= 1
            if self.day == 0:
                self.previousMonth()
                self.day = self.days_in_month()
            return self
        return "Bunday kun mavjud emas!!!"
        
    def nextMonth(self):
        if self.isValidDate():
            self.month += 1
            if self.month == 13:
                self.month = 1
                self.nextYear()
            return self

    def previousMonth(self):
        if self.isValidDate():
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.previousYear()
            return self
        return "Bunday oy mavjud emas!!!"

    def nextYear(self):
        if self.isValidDate():
            self.year += 1
            return self

    def previousYear(self):
        if self.isValidDate():
            self.year -= 1
            return self
        return "Bunday yil mavjud emas!!!"

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                return 29
            else:
                return 28
        return 0

m = MyDate(28, 2, 2012)
print(m)           
print(m.nextDay())  
print(m.nextDay())
print(m.nextMonth())
print(m.nextYear(),'\n')

m1 = MyDate(2, 1, 2012)
print(m1)                  
print(m1.previousDay())    
print(m1.previousDay())    
print(m1.previousMonth())  
print(m1.previousYear(),'\n')   

m2 = MyDate(29, 2, 2012)
print(m2)
print(m2.previousDay())    
print(m2.previousYear(),'\n')   

m3 = MyDate(31, 11, 2099)
print(m3)
print(m3.previousDay())    
print(m3.previousMonth())  
print(m3.previousYear(),'\n')
   
m4 = MyDate(29, 2, 2011) 
print(m4)   
print(m4.previousDay())    
print(m4.previousMonth())  
print(m4.previousYear(),'\n')
