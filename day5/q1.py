
# class Temperature:

#     def __init__(self,temp=0):
#         self._temp = temp

#     @property
#     def temp(self):
#         print("Getting the Temperature")
#         return f"{self._temp} C"
    
#     @temp.setter
#     def temp(self,val):
        
#         if val < -273.15:
#             raise ValueError("Invalid Temperature.")
        
#         print("Setting the Temperature")
#         self._temp = val

#     def toFahrenheit(self):
#         return f"{(9/5)*(self._temp + 32)} F"


class T:
    def __init__(self,temp=0):
        self._temp = temp

    # def getter(self):
    #     return self._temp
    
    # def setter(self,val):
    #     self._temp = val

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self,val):
        self._temp = val
    
    


    
t = T()

# print(t.getter())
# t.setter(4)
# print(t.getter())

print(t.temp)
t.temp = 40
t.temp+=5
print(t.temp)
    