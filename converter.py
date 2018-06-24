# -*- coding: utf-8 -*-
import re
text="ဝီကီပီးဒီးယားသည်ဝီကီပီးဒီးယားသည် သုံးစွဲသူများက ပူးပေါင်း၍ ရေးသားတည်းဖြတ်သော စွယ်စုံကျမ်းဖြစ်ပါသည်။ ကဏ္ဍဝီကီပီးဒီးယား မြန်မာယူနီကုဒ် ၁၁၃၄၂၀ပအ၀afafpa"
#text=raw_input()#for user input
text=text.decode('utf-8')


def converter(a):

    a=re.sub(u'\u1033',u'\u102f',a)#1 chaung nyin
    a=re.sub(u'\u1034',u'\u1030',a)#2 chaung nyin
    a=re.sub(u'\u1086',u'\u103f',a)#tha a kyi
    a=re.sub(u'\u103d',u'\u103e',a)#ha htoe
    a=re.sub(u'\u103c',u'\u103d',a)#wa swal
    a=re.sub(u'\u103b',u'\u103c',a)#ya yit
    a=re.sub(u'\u103a',u'\u103b',a)#ya pin
    a=re.sub(u'\u1039',u'\u103a',a)#a thet
    a=re.sub(u'\u104e',u'\u104e'u'\u1004'u'\u103a'u'\u1038',a)#lal kaung
    a=re.sub(u'\u105a',u'\u102b'u'\u103a',a)#yay cha shay htoe
    a=re.sub(u'\u108f',u'\u1014',a)#na nge a thay
    a=re.sub(u'\u1090',u'\u101b',a)#ya kout a thay

    #  u1039patsint
    a=re.sub(u'\u1060',u'\u1039'u'\u1000',a)
    a=re.sub(u'\u1061',u'\u1039'u'\u1001',a)
    a=re.sub(u'\u1062',u'\u1039'u'\u1002',a)
    a=re.sub(u'\u1063',u'\u1039'u'\u1003',a)
    a=re.sub(u'\u1064',u'\u1004'u'\u103a'u'\u1039',a)
    a=re.sub(u'\u1065',u'\u1039'u'\u1005',a)
    a=re.sub(u'\u1066',u'\u1039'u'\u1006',a)
    a=re.sub(u'\u1067',u'\u1039'u'\u1006',a)
    a=re.sub(u'\u1068',u'\u1039'u'\u1007',a)
    a=re.sub(u'\u1069',u'\u1039'u'\u1008',a)
    a=re.sub(u'\u106a',u'\u1009',a)
    a=re.sub(u'\u106b',u'\u100a',a)
    a=re.sub(u'\u106c',u'\u1039'u'\u100b',a)
    a=re.sub(u'\u106d',u'\u1039'u'\u100c',a)
    a=re.sub(u'\u106e',u'\u100d'u'\u1039'u'\u100b',a)
    a=re.sub(u'\u106f',u'\u100d'u'\u1039'u'\u100e',a)
    a=re.sub(u'\u1070',u'\u1039'u'\u100f',a)
    a=re.sub(u'\u1071',u'\u1039'u'\u1010',a)
    a=re.sub(u'\u1072',u'\u1039'u'\u1010',a)
    a=re.sub(u'\u1073',u'\u1039'u'\u1011',a)
    a=re.sub(u'\u1074',u'\u1039'u'\u1011',a)
    a=re.sub(u'\u1075',u'\u1039'u'\u1012',a)
    a=re.sub(u'\u1076',u'\u1039'u'\u1013',a)
    a=re.sub(u'\u1077',u'\u1039'u'\u1014',a)
    a=re.sub(u'\u1078',u'\u1039'u'\u1015',a)
    a=re.sub(u'\u1079',u'\u1039'u'\u1016',a)
    a=re.sub(u'\u107a',u'\u1039'u'\u1017',a)
    a=re.sub(u'\u107b',u'\u1039'u'\u1018',a)
    a=re.sub(u'\u107c',u'\u1039'u'\u1019',a)
    a=re.sub(u'\u1085',u'\u1039'u'\u101c',a)
    a=re.sub(u'\u1091',u'\u100f'u'\u1039'u'\u100d',a)
    a=re.sub(u'\u1092',u'\u100b'u'\u1039'u'\u100c',a)
    a=re.sub(u'\u1093',u'\u1039'u'\u1018',a)
    a=re.sub(u'\u1093',u'\u103b'u'\u1039',a)
    #Ya pin
    a=re.sub(u'\u107d',u'\u103b',a)

    #ya YIT
    a=re.sub(u"[\u107e-\u1084]",u'\u103c',a)

    #ha htoe
    a=re.sub(u'\u1087',u'\u103e',a)
    a=re.sub(u'\u1088',u'\u103e'u'\u102f',a)
    a=re.sub(u'\u1089',u'\u103e'u'\u1030',a)
    a=re.sub(u'\u108a',u'\u103d'u'\u103e',a)

    #kinzi
    a=re.sub(u'\u108b',u'\u1004'u'\u103a'u'\u1039'u'\u102d',a)
    a=re.sub(u'\u108c',u'\u1004'u'\u103a'u'\u1039'u'\u102e',a)
    a=re.sub(u'\u108d',u'\u1004'u'\u103a'u'\u1039'u'\u1036',a)

    #lone gyi tin thay thay tin
    a=re.sub(u'\u108e',u'\u102d'u'\u1036',a)

    #out ka myint
    a=re.sub(u'\u1094',u'\u1037',a)
    a=re.sub(u'\u1095',u'\u1037',a)

    #reoredering
    a=re.sub(u"([\u1000-\u1021])(\u102f)(\u102d)", r"\1\3\2",a)#longe gyi tin 1 chaung ngin
    a=re.sub(u"([\u1000-\u1021])(\u102f)(\u103b)", r"\1\3\2",a)#longe gyi tin 1 chaung ngin
    a=re.sub(u"([\u1000-\u1021])(\u103b)(\u102f)(\u102d)", r"\1\2\4\3",a)#longe gyi tin 1 chaung ngin
    #a=re.sub(u"(\u103c)([\u1000-\u1021])", r"\2\1",a)#vowel yayit
   return a.encode('utf-8')

   def main():

       b=converter(text)
       print(b)

   main()
