abjad= {
	
	"ا":1, "ب":2, "ج":3, "د":4, "ه":5, "و":6, "ز":7,
	"ح":8, "ط":9, "ي":10, "ك":20, "ل":30, "م":40, "ن":50,
	"س":60, "ع":70, "ف":80, "ص":90, "ق":100, "ر":200, "ش":300, 
	"ت":400, "ث":500, "خ":600, "ذ":700, "ض":800, "ظ":900, "غ":1000,
	"ّ":0, "أ":1, "إ":1, ",":0, "َ":0, "ً":0, "ُ":0, "ٌ":0, "ِ":0, "ٍ":0,"ء":1, "،":0, "ْ":0,
}
words=input("Enter your words to find the adad jumal. ")
count=0
newkeys=[]
for word in words:
	letters=word.split()
	for letter in letters:
		if letter in abjad.keys():
			num=abjad.get(letter)
			count=count+num
		else:
			newkeys.append(letter)
unidentified={}
for letter in newkeys:
	unidentified[letter]= unidentified.get(letter,0) +1

print (count)

if unidentified:
	print ("Some letters are not part of the abjad huroof, or don't fall under any of the 28 huroof with certainty.")
	for letter, freq in unidentified.items():
		print ("The character "+letter+ " appears " + str(freq) + " times.")
