
def main():
    print("Demostration of List")

    List = ["Shivam","PPA",75,3.14]

    print(List)
    print(List[0])
    print(List[1])
    print(List[-1])
    print(List[1:])
    print(List[2:])
    print(List[:1])
    print(List[:2])
    print(List[:3])
    
    # WE CAN STORE HETEROGENIOUS DATA
    data1 = [11,"Shivam",21]
    print(data1)
    data2 = [41,"Kadam",31]
    print(data2)
    
   # WE CAN CREATE LIST OF LIST
    combined = [data1,data2]
    print(combined)
    
    # THERE ARE MULTIPLE METHOD THAT WE CAN USE TO MANIPULATE LIST
    List.append("MEAN")
    print(List)
    
    List.insert(1,"Sunil")
    print(List)
    
    
if __name__ == "__main__":
    main()