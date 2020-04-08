from socket import *
import time 
startTime = time.time()




if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    first_Port = int(input("What port would you like to start with? "))
    last_Port = int(input("What is the ending port?"))
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)

    for i in range(first_Port, last_Port):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))

        if(conn == 0):
            print ('Port %d: OPEN' % (i,))

        s.close()

print('Time taken:', time.time() - startTime)

