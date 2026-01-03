OOPS with python

* Class, Object, method
* Classes have data/attributes and methods/functions
* data/attributes are defined in the constructor/ dunder method (def __init__())
* when a class is assigned to an object, data/attributes get called/initialized automatically and methods should be called manually.
* Python is called OOP because everything in python is an object.
    * Data structures like list, set, tuple, dict
    * Data types like int, str, bool
* Advantages of OOPS
    * you can create your own data type
    * code reusability
    * debugging
    * easy to collab
* Function vs Method
    * Function is independent.
    * Method is a function that belongs to an object.
* Self - it refers to the current object(instance) of the class. Self tells the class which data/attributes to use based on the current instance or object.
* You can create an attribute outside the class as well


* Encapsulation - it hides(but can’t protect) the attributes or method from the user. This is done by adding a ‘__’ before the data/method. And this hidden thing is called by using ‘_classname__method/dataname’

* Getter is a method that helps us get/ prints the attibutes.
* Setter is a method that helps us set the attributes.

* Static method is something that is defined in the class without passing self. This is not called thorugh the object but through the class name itself because static methods are accessed at class level not at object level.



* Inheritance
    * When we are inheriting a parent class into a child class, then the child class gets both the attributes and methods of the parent class but parent class doesn’t get any attributes or methods from the child class.
    * Child gets the constructor method, non private attibutes and non private methods(i.e, no encapsulation)
    * Constructor overloading - If there is a constructor method in the child class then the parent attributes are nullified/ doesn’t work
    * Method overloading - If ther eis a method in teh child class with the same name as the parent class then calling the method gives the output of the child class.
* Super keyword
    * To overcome the attribute/constructor overloading we call super().__init__() - by this we bring all the attributes of parent class
    * To overcome the method overloading we call super().methodname() - through this we bring the method from parent class that has the same name of child class.
    * Super can only be used inside a child class and super is used only to bring methods to the child class either constructor or normal methods.
* Types of Inheritences
    * Single inheritance - child inherits from a parent
    * Multi level inheritance - child inherits from parent and parent inherit from grand parent
    * Hierarchical inheritance - two childs inherits from the same parent
    * Diamond/Multiple inheritance - If there is a same method in two child classes and these two child classes are inheriting from a parent class and another small/grand child class is inheriting these two child classes then if we call that method then first method from grand child gets executed and then the first mentioned child class and then the 2nd mentioned child class and at the last the method from parent class is executed. This inheritance diagram looks like a diamond shape.
    * Hybrid - Has all the types of inheritances discussed aboved and the order of exceution is the key concept here.
