
saving_amount = 1500000 #저축금액
total_principle = 1500000*12 #원금

Eza = 2.4 #이자율
year = 1
principal = saving_amount * 12
pre_tax_interest = (total_principle+saving_amount)*Eza*year/2/100 #세전이자
tax = int((pre_tax_interest * 15.4/100)) #세금
pre_tax_interest1 = int(pre_tax_interest)


print("[대마뱅크]")
print("좌*익님 자유적금이 만료되어 알려드립니다.")
print(f"원급합계 {total_principle: ,}원")
print(f"세전이자 {pre_tax_interest1:,}원")
print(f"이자과세(15.4%) {tax: ,}원")
print(f"세후 수령액 {total_principle+pre_tax_interest1-tax: ,}원")

