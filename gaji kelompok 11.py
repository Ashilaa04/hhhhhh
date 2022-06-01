import streamlit as st

st.write(""" # Aplikasi Penghitung Gaji Karyawan """)
nip = st.number_input('Masukan NIP', 0)
nama = st.text_input('Masukan Nama')
st.write("1. Golongan I \n2. Golongan II \n3. Golongan III \n4. Golongan IV \n5. Golongan V \n6. Golongan Lain")
jabatan = st.text_input('Masukan jabatan karyawan', 0)
alamat = st.text_input('Masukan Alamat')
jml_anak = st.text_input('Masukan Jumlah Anak', 0)
lembur = st.text_input('Total jam lembur', 0)
ijin = st.text_input('Total hari ijin', 0)

    #fungsi gaji_pokok
if (jabatan=='1'):
    gaji_pokok=10000000
elif(jabatan=='2'):
    gaji_pokok=8500000
elif(jabatan=='3'):
    gaji_pokok=6000000
elif(jabatan=='4'):
    gaji_pokok=5000000
elif(jabatan=='5'):
    gaji_pokok=4000000
else:
    gaji_pokok=3000000

    #fungsi tunjangan
if(jml_anak=='5'):
    tunjangan=1000000
elif(jml_anak =='4'):
    tunjangan=750000
elif(jml_anak =='3'):
    tunjangan= 500000
elif(jml_anak =='2'):
    tunjangan=450000
elif(jml_anak =='1'):
    tunjangan=40000
else:
    tunjangan=300000

    #fungsi lembur
if(lembur == '1'):
    tambahan=10000
elif(lembur == '2'):
    tambahan=15000
elif(lembur == '3'):
    tambahan=30000
elif(lembur == '4'):
    tambahan=45000
elif(lembur == '5'):
    tambahan=50000
else:
    tambahan=0

    #fungsi ijin
if (ijin == '1'):
    pengurangan = 5000
elif(ijin == '2'):
    pengurangan = 10000
elif (ijin == '3'):
    pengurangan = 15000
elif (ijin == '4'):
    pengurangan = 100000
else:
    pengurangan =0

gaji_bersih = gaji_pokok+tunjangan+tambahan+pengurangan

if (st.button('HITUNG GAJI')):
    st.success('Gaji Bersih adalah {}.'.format(gaji_bersih))

    