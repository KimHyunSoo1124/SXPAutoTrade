import pyupbit
access = "r0BOkOfbChPvNn75NHEcirndGbNTdoxrUfQWIs24"          # 본인 값으로 변경
secret = "K1IBxWB9F3TBQo9STIzxBeEkYV9XHFGaxbZYbLnx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-SXP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회