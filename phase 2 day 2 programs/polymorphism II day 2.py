class vizag():
    def placename(self):
        print("vizag placename is KLU")
    def student(self):
        print("Yes - vizag")
    def which_year(self):
        print("3rd year")
class hyd():
    
    def placename(self):
        print("hyd placename is HYD-KLU")
    def student(self):
        print("Yes - hyd")
    def which_year(self):
        print("3rd year-hyd")

obj_vig=vizag()
obj_hyd=hyd()
for details in (obj_vig,obj_hyd):
    details.placename()
    details.student()
    details.which_year()
