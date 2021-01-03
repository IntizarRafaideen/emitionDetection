import detector as dec



# converting emotions into numbers
if dec.result["dominant_emotion"] == "happy":
    dec.no = 1
elif dec.result["dominant_emotion"] == "sad":
    dec.no = 2
elif dec.result["dominant_emotion"] == "angry":
    dec.no = 3
else:
    dec.no = 4
print(dec.no)