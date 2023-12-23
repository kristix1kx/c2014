#print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#try:
#    print("start code")
 #   print(10/0)
 #   print("No errors")
#except (TypeError, ZeroDivisionError):
#    print("we have an error")

#print("code after capsule")

#def checker(var_1):
  #  if type(var_1)!=str:
    #    raise TypeError(F"sorry, we can't work with {type(var_1)}," f"нам потрібний тип str")
 #   else:
  #      return var_1
 #   firsr_var=10
   # checker(firsr_var)

class BuildingError(Exception):
    def __str__(self):
        return  f"з такою кількістю матеріалів ми працювати не зможемо!"
def check_material(amount_of_material, limit_value):
    if amount_of_material>limit_value:
        return "materials достатньо"
    else:
        raise BuildingError((amount_of_material))
materials=123
check_material(materials,300)





















