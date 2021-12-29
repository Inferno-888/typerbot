import time

def wait(sec):
    print("Elapsed: 0s", end='')
    for i in range(sec):
        time.sleep(1)
        t = str(i + 1) + 's'
        print('\b'*(len(str(i))+1), end='')
        print(t, end='')
    print("\nResuming...\n")
