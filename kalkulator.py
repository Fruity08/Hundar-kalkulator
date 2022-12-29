import decimal
import time

mår = input("Hur många människo-år är din hund?""\n")

hår = decimal.Decimal(mår)

hår = hår/31

round(hår, 8)

hår = str(hår)

print("Svaret är : "+hår+" : Hund-år")

exit