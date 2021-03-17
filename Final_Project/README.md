# Final Project
## Laptops

Ստեղծել jupyter notebook կամ python script, որը կկարդա csv ֆայլը և կտպի

1.  5 ամենաթանկ laptop-ները f’{brand} {model} {price}’ այս ֆորմատով
2.  5 ամենամատչելի laptop-ները f’{brand} {model} {price}’ այս ֆորմատով
3.  բոլոր օպերացիոն համակարգերը և իրենց laptop-երի քանակը(օրինակ՝ windows: 456, macOS:46, Linux: 876...)
4.  5 ամենածանր laptop-ները f’{brand} {model} {weight}’ այս ֆորմատով
5.  5 ամենահզոր RAM ունեցող laptop-ները f’{brand} {model} {ram}’ այս ֆորմատով
6.  բոլոր չափի RAM-երը և իրենց մոդելների քանակը(օրինակ՝ 4GB: 456, 8GB:46, 10GB: 876...)
7.  էկրանի չափսերը և իրենց մոդելների քանակը։ էկրանի չափսերը խմբավորել հետևյալ կերպ։ մինչև 10”, 10”-13”, 13”-15” և 15” կամ ավելի մեծ
8.  բոլոր brand-երը և իրենց մոդելների քանակը(օրինակ՝ apple: 11, Dell:80...)

### Here is the resault

```
*** Top 5 Laptops With The Highest Prices ***
  BRAND |         MODEL |     PRICE
  Razer |     Blade Pro |  6099,00€
  Razer |     Blade Pro |  5499,00€
 Lenovo |  Thinkpad P51 |  4899,00€
     HP |      Zbook 17 |  4389,00€
   Asus |    ROG G701VO |  3975,00€


*** Top 5 Laptops With The Lowest Prices ***
  BRAND |                 MODEL |    PRICE
   Acer |             C740-C9QX |  174,00€
   Asus |       Vivobook E200HA |  191,90€
   Vero |                  V131 |  196,00€
   Asus |         E402WA-GA010T |  199,00€
   Acer |  Chromebook C910-C2ST |  199,00€


*** Top 5 Laptops With The Highest Weights ***
  BRAND |               MODEL |    WEIGHT
   Asus |   ROG G703VI-E5062T |     4.7kg
 Lenovo |  IdeaPad Y910-17ISK |     4.6kg
 Lenovo |  IdeaPad Y900-17ISK |     4.6kg
    MSI |           GT80S 6QE |     4.5kg
   Dell |        Alienware 17 |    4.42kg


*** Top 5 Laptops With The Highest RAMs ***
  BRAND |              MODEL |    RAM
   Asus |         ROG G701VO |   64GB
  Razer |          Blade Pro |   32GB
   Asus |  ROG G703VI-E5062T |   32GB
   Dell |             XPS 15 |   32GB
Toshiba |  Portege X30-D-10L |   32GB


*** Number of Laptops For Each OS ***
       OS : COUNT
  Android :     2
Chrome OS :    27
    Linux :    62
   Mac OS :    21
    No OS :    66
  Windows :  1124
-- TOTAL COUNT: 1302 --


*** Number of Laptops For Each RAM size ***
RAM SIZE : COUNT
     2GB :    22
     4GB :   375
     6GB :    41
     8GB :   618
    12GB :    25
    16GB :   200
    24GB :     3
    32GB :    17
    64GB :     1
-- TOTAL COUNT: 1302 --


*** Number of Laptops For Each Screen Size ***
   SCREEN SIZE : COUNT
 less than 10" :     0
     10" - 13" :    88
     13" - 15" :   376
15" and bigger :   838
-- TOTAL COUNT: 1302 --


*** Number of Laptops For Each Brand ***
    BRAND : COUNT
     Acer :   103
    Apple :    21
     Asus :   157
    Chuwi :     3
     Dell :   297
  Fujitsu :     3
   Google :     3
       HP :   274
   Huawei :     2
       LG :     3
   Lenovo :   297
      MSI :    54
 Mediacom :     7
Microsoft :     6
    Razer :     7
  Samsung :     9
  Toshiba :    48
     Vero :     4
   Xiaomi :     4
-- TOTAL COUNT: 1302 --
```