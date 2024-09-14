class Catalog:
    """This class represents the categories and the devices of each one"""
    
    
    def __init__(self):
        self._category = ["Computers", "Smartphones", "Cameras"]
        self._Computers =[["Mac", "Lenovo", "Acer", "Asus"],[20,15, 20, 45]]
        self._Smartphones = [[ "iPhone 14 Pro","Samsung Galaxy S22 Ultra", "Xiaomi Mi 11 Ultra","OnePlus 10 Pro"], [20,15, 20, 45]]  
        self._Cameras = [["Nikon Z7 II", "Sony Alpha A7 IV","Fujifilm X-T4", "Panasonic Lumix GH6",], [12,45,23,41]]
      
      
    
      
    def category(self):
        return self._category[0]
    
    def computer_names(self):
        return self._Computers[1]
    
    def computer_quantities(self):
        return self._Computers[1]
    
   
    def smartphone_names(self):
        return self._Smartphones[0]
    
    def smartphone_quantities(self):
        return self._Smartphones[1]
    
   
    def camera_names(self):
        return self._Cameras[0]
    
    def camera_quantities(self):
        return self._Cameras[1]


#get for ba product by index 

    def get_computer_by_index(self, index):
        return self._Computers[0][index], self._Computers[1][index]

    def get_smartphone_by_index(self, index):
        return self._Smartphones[0][index], self._Smartphones[1][index]

    def get_camera_by_index(self, index):
        return self._Cameras[0][index], self._Cameras[1][index]

# Example usage
catalog = Catalog()

# Get all computer names and quantities
computer_names = catalog.computer_names()
computer_quantities = catalog.computer_quantities()

# Get a specific computer by index (e.g., first computer)
first_computer_name, first_computer_quantity = catalog.get_computer_by_index(0)



print("Computer Names:", computer_names)
print("Computer Quantities:", computer_quantities)
print(f"First Computer: {first_computer_name}, Quantity: {first_computer_quantity}")
        
 
    
    
    
    
