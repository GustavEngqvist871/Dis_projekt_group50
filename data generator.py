l = ["jan","feb","mar","apr","maj","juni","juli","august","sep","okt","nov","dec"]
data = []
import numpy as np
dag = 0

for i in range(12):
    if l[i]=="jan":
        for i in range(31):
            print((dag,np.random.normal(4.1,2.5),np.random.normal(7,4)),",")
            dag = dag+1

    elif l[i]=="feb":
        for i in range(28):
            print((dag,np.random.normal(0.1,1.4),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="mar":
        for i in range(31):
            print((dag,np.random.normal(3.7,0.4),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="apr":
        for i in range(30):
            print((dag,np.random.normal(6.6,0.6),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="maj":
        for i in range(31):
            print((dag,np.random.normal(11.5,0.1),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="juni":
        for i in range(30):
            print((dag,np.random.normal(15,0.5),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="juli":
        for i in range(31):
            print((dag,np.random.normal(16.4,0.5),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="august":
        for i in range(31):
            print((dag,np.random.normal(15.7,1.2),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="sep":
        for i in range(30):
           print((dag,np.random.normal(14.5,0.9),np.random.normal(7,4)),",")
           dag = dag+1
    elif l[i]=="okt":
        for i in range(31):
            print((dag,np.random.normal(11.7,2.3),np.random.normal(7,4)),",")
            dag = dag+1
    elif l[i]=="nov":
        for i in range(30):
            print((dag,np.random.normal(6.8,1.3),np.random.normal(7,4)),",")
            dag = dag+1
            
    elif l[i]=="dec":
        for i in range(31):
            print((dag,np.random.normal(1.5,1.3),np.random.normal(7,4)),",")
            dag = dag+1
          
    