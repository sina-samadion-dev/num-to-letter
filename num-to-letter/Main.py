number=input('inter only number:')
number=number[::-1]

yekan={'1':'و یک','2':'و دو','3':'و سه','4':'و چهار','5':'و پنج','6':'و شیش','7':'و هفت','8':'و هشت','9':'و نه'}
dahgan={'1':'و ده ','2':'و بیست ','3':'و سی ','4':'و چهل ','5':'و پنجاه ','6':'و شصت ','7':'و هفتاد ','8':'و هشتاد ','9':'و نود '}
sadgan={'1':'و صد ','2':'و دویست ','3':'و سیصد ','4':'و چهارصد ','5':'و پانصد ','6':'و شیشصد ','7':'و هفتصد ','8':'و هشتصد ','9':'و نهصد '}
pasvand={3:' هزار ',6:' میلیون ',9:' بیلیون ',12:' تریلیون ',15:' کوادریلیون ',18:' کوینتیلیون ',21:' سکستیلیون ',24:' سپتیلیون ',27:' اکتیلیون ',
         30:' نانیلیون ',33:' دسیلیون ',36:' اندسیلیون ',39:' دیودسیلیون ',42:' تریدسیلیون ',45:' کواتیوردسیلیون ',48:' کویندسیلیون ',51:' سکسدسیلیون ',
         54:' سپدسیلیون ',57:' اکتودسیلیون ',60:' نومدسیلیون '}
final=''
counter=0
zerocounter=0
for i in range (len(number)):
    counter += 1
    if zerocounter == 3 and counter > 6:
        final = final.replace(pasvand[counter - 4],'')      #fina.strip !!نمیدونم چرا در نوشتن(1100011) مشکل داشت
    if counter % 3 == 1 and counter != 1:
        zerocounter=0
        final = pasvand[counter-1] + final
    if number[i] == '0':
        zerocounter += 1
        continue

    if i % 3 == 0:
        final = yekan[number[i]] + final
    if i % 3 == 1:
        final = dahgan[number[i]] + final
    if i % 3 == 2:
        final = sadgan[number[i]] + final

final=final.replace('ده و دو','دوازده')
final=final.replace('ده و یک','یازده')
final=final.replace('ده و سه','سیزده')
final=final.replace('ده و چهار','چهارده')
final=final.replace('ده و پنج','پانزده')
final=final.replace('ده و شیش','شانزده')
final=final.replace('ده و هفت','هیفده')
final=final.replace('ده و هشت','هیجده')
final=final.replace('ده و نه','نوزده')
print(final.lstrip('و '))