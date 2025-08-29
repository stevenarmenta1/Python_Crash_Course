def make_car(manufacturer, model_name, **kargs):
    '''This funciton stores information about a selected car'''
    kargs['manufacturer']= manufacturer
    kargs['model_name']= model_name
    return kargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)