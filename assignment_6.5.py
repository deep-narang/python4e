text = "X-DSPAM-Confidence:    0.8475";

stpos=text.find(":")

data=str(text[stpos+1:])
data=data.strip()

no=float(data)
print(no)
