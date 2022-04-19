def run():
    my_list = [1, "Hola", True, 4.5]
    my_dict = {"firstname":"Felix","lastname":"Garzon"}
    super_list = [
        {"firstname":"Felix","lastname":"Garzon"},
        {"firstname":"Ana","lastname":"Torres"},
        {"firstname":"Alejo","lastname":"Garcia"},
        {"firstname":"Maria","lastname":"Perez"}
    ]

    super_dict = {
        "natural_num" :[1,2,3,4],
        "integer_num" :[-1,-2,0,1,2],
        "float_num" :[1.1,4.5,6.5,5.8]
    }

    #for key, value in super_dict.items():
    #    print(key, " - ", value)

    for item in super_list:
        print(item["firstname"] + " " + item["lastname"])

if __name__=='__main__':
    run()
