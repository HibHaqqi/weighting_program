#!/usr/bin/python

import numpy as np
import argparse
import csv

#list of data
nama = []
kota =[]
penghasilan =[]
umur = []
kelamin = []
pekerjaan = []
tempat_tinggal = []
hutang = []

#load data
parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str)
args = parser.parse_args()
data= np.genfromtxt(args.file,delimiter='|',dtype=None)

#move data to list
for row in data:
   nama.append(str(row[0])) 
   kota.append(str(row[1]))
   penghasilan.append(float(row[2]))
   umur.append(float(row[3]))
   kelamin.append(str(row[4]))
   pekerjaan.append(str(row[5]))
   tempat_tinggal.append(str(row[6]))
   hutang.append(float(row[7]))

#Bobot Kota  
service = ['Jakarta','Bekasi', 'Bogor', 'Depok', 'Tangerang']    
bobot_kota = []   
for i in kota:
    if i  in service :
        i = 10 
        bobot_kota.append(i)
    elif i  == 'Surabaya':
        i = 5
        bobot_kota.append(i)
    else  :
        i = 2
        bobot_kota.append(i)
        
#Bobot Penghasilan
bobot_penghasilan = []   
null = [0,-1]
for i in penghasilan:
    if    1 < i <= 3000000:
        i = 3 
        bobot_penghasilan.append(i)
    elif   3000000 < i <= 6000000 :
        i = 8
        bobot_penghasilan.append(i)
    elif  i > 6000000 :
        i = 12
        bobot_penghasilan.append(i)
    elif i in null :
        i = 0
        bobot_penghasilan.append(i)   
    else  :
        i = 0
        bobot_penghasilan.append(i)
        
#Bobot Umur
bobot_umur = []  
def weight_by_age_and_sex(age,sex):
    if sex == "Wanita" and 21 <= age <= 25:
        return 15
    if (age <21):
        return 0
    if 21 <= age <= 40:      
        return 10
    if 40 <= age <= 65:
        return 12
    else :
        return 0
    
for age, sex in zip(umur, kelamin):
    weight = weight_by_age_and_sex(age,sex)
    bobot_umur.append(weight)  
    
        
#Bobot Kelamin        
bobot_kelamin = []   
for i in kelamin:
    if i  == 'Pria' :
        i = 3
        bobot_kelamin.append(i)
    else :
        i = 5
        bobot_kelamin.append(i)        
        
#Bobot Pekerjaan       
ibu_rumahtangga = ['Ibu Rumah tangga', 'Ibu Rumah Tangga', 'Ibu rumah tangga', 'ibu rumah tangga' ]        
bobot_pekerjaan = []   
for i in pekerjaan:
    if i  == 'Pegawai Swasta' :
        i = 8
        bobot_pekerjaan.append(i)
    elif i  == 'Wiraswasta':
        i = 4
        bobot_pekerjaan.append(i)
    elif i  in ibu_rumahtangga:
        i = 6
        bobot_pekerjaan.append(i)   
    else  :
        i = 0
        bobot_pekerjaan.append(i)  
        
#Bobot Tempat Tinggal        
bobot_tempat_tinggal = [] 
milik = ['Milik', 'Milik Sendiri', 'Milik sendiri', 'milik sendiri']  
for i in tempat_tinggal:
    if i  in milik :
        i = 15
        bobot_tempat_tinggal.append(i)
    elif i  == 'Kontrak':
        i = 10
        bobot_tempat_tinggal.append(i)
    elif i  == 'Kost':
        i = 5
        bobot_tempat_tinggal.append(i)   
    else  :
        i = 0
        bobot_tempat_tinggal.append(i)     

#Bobot Hutang 
bobot_hutang=[]
for i in hutang:
    if i > 5000000:
        i= -15
        bobot_hutang.append(i)
    elif 0 < i <= 5000000 :
        i= -5
        bobot_hutang.append(i)
    else :
        i= 0
        bobot_hutang.append(i)


#sum of rows
jumlah = []
for a, b, c, d, e, f, g in zip(bobot_kota, bobot_penghasilan, bobot_kelamin, bobot_pekerjaan, bobot_tempat_tinggal, bobot_hutang, bobot_umur):
      a =  a + b  + c + d + e + f + g
      jumlah.append(a)     
     
#save as output.txt
final= []
          
for a, b in zip (nama, jumlah):
    x=  a ,  b
    print x
    final.append(x)
with open('output.txt', 'wb') as output:
    o = csv.writer(output, delimiter = '|')
    o.writerows(final)
    
