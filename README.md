# algoritma-tak-m-
soru çözümleri
nums = [1,2,2,3,1,4,2]
adet={}
birinciokuma={}
ensonokuma={}
for i, num in enumerate(nums):
    if num not in birinciokuma:
        birinciokuma[num]=i
    ensonokuma[num]=i
    adet[num]=adet.get(num, 0)+1
derece = max(adet.values())
print(derece)

uzunluk= len(nums)
for num in adet:
    if adet[num] == derece:
        uzunluk2 = ensonokuma[num] - birinciokuma[num]+1
        uzunluk = min(uzunluk, uzunluk2)
print(uzunluk)
