def calc():
    ops = {
        "+":lambda x,y:x+y,
        "-":lambda x,y:x-y,
        "*":lambda x,y:x*y,
        "/":lambda x,y:0 if x == 0 or y == 0 else x/y,
    }
    history = {
        "+":0,
        "-":0,
        "*":0,
        "/":0
    }
    while 1:
        print(f"""
    History:
    + = {history['+']}
    - = {history['-']}
    * = {history['*']}
    / = {history['/']}
    """)
        op = input("Mathematic operator (x to exit): ")
        if ops.get(op):
            while 1:
                try:
                    x = int(input("First num: "))
                    y = int(input("Second num: "))
                    break
                except:
                    print("Invalid datatype")
            print(f"Result: {ops[op](x,y)}")
            history[op] += 1
        elif op == "x":
            exit()
        else:
            print("Not an valid operator (+,-,*,/)")