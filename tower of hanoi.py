def tower_of_hanoi(n, src, dest, aux):
    if n==0:
        return
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    tower_of_hanoi(n - 1, src, aux, dest)
    print(f"Move disk {n} from {src} to {dest}")
    tower_of_hanoi(n - 1, aux, dest, src)

n = 3
tower_of_hanoi(n, "s", "d", "a") 
