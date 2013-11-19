tcpurpose(Checks that only three recipes may be added to Coffee Maker)
tcsatisfies(ID001.001.003)

**Steps**
1. Enter: Menu option 1, "Add a recipe "
1. Enter:   Name: Coffee
            Price: 50
            Coffee: 3
            Milk: 1
            Sugar: 1 
            Chocolate: 0
1. Return to main menu.  
1. **Expectation:** Coffee successfully added.
1. Enter: Menu option 1, "Add a recipe "
1. Enter:   Name: Mocha 
            Price: 60
            Coffee: 3
            Milk: 2
            Sugar: 2
            Chocolate: 3 
1. Return to main menu.  
1. **Expectation:** Coffee successfully added.
1. Enter: Menu option 1, "Add a recipe "
1. Enter:   Name: Latte 
            Price: 60
            Coffee: 3
            Milk: 3 
            Sugar: 2
            Chocolate: 0
1. Return to main menu.  
1. **Expectation:** Coffee successfully added.
