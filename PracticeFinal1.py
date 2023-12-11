#practice code 1 - final exam review 
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("actors.csv")
#print(dir(df))
df["ratio"] = df["Oscars Won"]/df["Oscars Nominated"]
#get actor and actress ratios
avg_actor = df["ratio"][df["Occupation"] =="Actor"].mean()

avg_actress = df["ratio"][df["Occupation"] =="Actress"].mean()


#create bar chart

data = {"actor":avg_actor, "actress":avg_actress}
courses = list(data.keys()) 
values = list(data.values())

plt.bar(courses, values ,color = 'purple', width = 0.7)
plt.title("percent heart attack if exercising")
plt.show()

print(df)
print(avg_actress)
'''
from PracticeFinal2 import Frequent_Flyer

def main():
    capt_sully = Frequent_Flyer("Sully")
    capt_sully.flight("CID","JFK",1000)
    capt_sully.flight("JFK","ORD",800)
    print(capt_sully)
    
    
if __name__ == "__main__":
    main()

