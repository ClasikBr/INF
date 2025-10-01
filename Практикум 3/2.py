time=int(input())
hour= time//(60*60)
min= (time%(60*60))//60
sec= (time%(60*60))%60
print(hour,'hour ',min,'min ',sec,'sec ')