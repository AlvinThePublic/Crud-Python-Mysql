import mysql.connector
import os

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='crud_python'
)

def insertData(db):
    name = input("Masukkan Nama : " )
    nip = input("Masukkan Nip : ")
    alamat = input("Masukkan Alamat : ")
    mapel = input("Masukkan Mapel : ")
    cursor = db.cursor()
    val = (name,nip,alamat,mapel)
    sql = "INSERT INTO tb_guru (nama_guru,nip,alamat,mapel) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,val)
    db.commit()
    print ('{} Data Berhasil Disimpan '.format(cursor.rowcount))

def showData(db):
    cursor = db.cursor()
    sql = "SELECT * FROM tb_guru"
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<---------------------------- Data Guru Tahun Ajaran 2019 -------------------------->')
    if cursor.rowcount < 0:
        print ("Tdak Ada Data")
    else:
        for data in result:
            
            print("|",data[0],"|","Nama : ",data[1],"   Nip : ",data[2],"  Alamat : ",data[4])
            print('|-----------------------------------------------------------------------------------')
            

def updateData(db):
    cursor = db.cursor()
    showData(db)
    id_guru = input("Pilih Id Guru : ")
    name = input("Nama Baru : ")
    nip = input("Masukkan Nip Baru : ")
    alamat = input("Masukkan Alamat Baru : ")
    mapel = input("Masukkan Mapel Baru : ")
    sql = "UPDATE tb_guru SET nama_guru=%s, nip=%s, alamat=%s, mapel=%s WHERE id_guru=%s"
    val = (name,nip,alamat,mapel,id_guru)
    cursor.execute(sql,val)
    db.commit()
    print ("{} Data Berhasil Diubah ".format(cursor.rowcount))

def hapusData(db):
    cursor = db.cursor()
    showData(db)
    id_gr= input("Masukkan Id Guru : ")
    sql = "DELETE FROM tb_guru WHERE id_guru=%s"
    val = (id_gr,)
    cursor.execute(sql,val)
    db.commit()
    print("{} Data Berhasil Dihapus ".format(cursor.rowcount))

def searchData(db):
    cursor = db.cursor()
    keyword = input("Search data Guru...")
    sql = "SELECT * FROM tb_guru WHERE nama_guru LIKE %s OR nip LIKE %s OR alamat LIKE %s OR mapel LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword) , "%{}%".format(keyword),  "%{}%".format(keyword))
    cursor.execute(sql,val)
    result = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada hasil..")
    else:
        for data in result:
            print(data)

def showMenu(db):
    print('\n\n')
    print("<------- Python With Mysql ------->")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("<--------------------------------->")
    menuGuru = input("Pilih Menu : ")

    os.system('cls')

    if menuGuru == "1":
        print("<---------- Data Guru Tahun Ajaran 2019 ---------->")
        insertData(db)
    elif menuGuru == "2":
        showData(db)
    elif menuGuru == "3":
        updateData(db)
    elif menuGuru == "4":
        hapusData(db)
    elif menuGuru == "5":
        searchData(db)
    elif menuGuru == "0":
        exit()
    else:
        print("Menu yang anda pilih invalid")


if __name__ == '__main__':
    while (True):
        showMenu(db)
