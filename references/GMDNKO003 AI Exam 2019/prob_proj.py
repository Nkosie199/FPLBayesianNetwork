def main():
    i = 1 #iterator
    t = 2 #where t represents the current timestamp
    pr_lowHumidity = 0.3 #the probability of low humidity given that the humidifier is on
    pr_low_prev = pr_lowHumidity #stores the previous change in probability of low humidity
    pr_terminate = 0.0005 #terminate when the change in probability is less than 0.05%
    while pr_low_prev > pr_terminate:
        pr_low = pr_lowHumidity**t #calculate the current probability of a low humidity level
        print(i,") Probability of low humidity = ",pr_low)
        pr_change = pr_low_prev - pr_low #update the change value
        print(i,") New change in probability = ",pr_change)
        pr_low_prev = pr_low #update the previous change in probability of low humidity
        t = t+1 #update the timestamp
        i+=1 #update the iterator
        
    print("Terminated after",t,"iterations as change in probability <",pr_terminate)
    

if __name__=="__main__":
    main()