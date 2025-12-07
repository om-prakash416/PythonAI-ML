#problem -
#product store

##design & create an online store for products (name,price),
#track total products being created
#create a static method to calculate discount on each product based on a % parameter 


# class Product:
#     count = 0
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Product.count += 1
        
#     @staticmethod
#     def calc_discount(price,discount):
#         final_price = price - (price * discount /100)
#         print(f"Final price after {discount}% discount is {final_price}")
        
# p1 = Product("laptop", 50000)
# p2 = Product("phone", 20000)
# p3 = Product("tablet", 15000)

# print(f"Total products created: {Product.count}")
# Product.calc_discount(p1.price, 10)
# Product.calc_discount(p2.price, 5)
# Product.calc_discount(p3.price, 15)



class Product:
    count =0
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1
        
    def get_info(self):
        print(f"Product Name: {self.name}, Price: {self.price}")    
        
    @classmethod
    def get_count(cls):
        print(f"Total products created: {cls.count}")
        
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Final price after {discount}% discount is {final_price}")
        
        
p1 = Product("laptop", 50000)
p2 = Product("phone", 20000)
p3 = Product("tablet", 15000)

Product.get_count()
p1.calc_discount(p1.price, 10)
p2.calc_discount(p2.price, 5)
p3.calc_discount(p3.price, 15)
