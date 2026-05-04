def Hanoi(n,source, auxilary, destination):
    if n==1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    Hanoi(n-1,source,destination,auxilary)
    print(f"Move disk {n} from {source} to {destination}")
    Hanoi(n-1,auxilary,source,destination)
Hanoi(3,'A','B','C')
