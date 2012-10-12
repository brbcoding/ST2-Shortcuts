s = raw_input("Shall I shut down Commander?")

def shut_down(s):

lower = s.lower()
upper = s.upper()
if s == 'Yes':
return "Shutting down..."
elif lower == 'yes':
return "Shutting down..."
elif upper == 'YES':
return "Shutting down..."
elif s == 'No':
return "Shutdown aborted!"
elif lower == 'no':
return "Shutdown aborted!"
elif upper == 'NO':
return "Shutdown aborted!"
else:
return "Sorry, I didn't understand you."

print shut_down(s) 
