import mysql.connector
import os,sys,time

conn = mysql.connector.connect (
  host = "192.168.0.104",
  user = "root",
  password = "root",
  database = "crudpython"
)


def lihat(conn) :
  
  cursor = conn.cursor()
  val = "SELECT * FROM peserta"
  cursor.execute(val)
  result = cursor.fetchall()
  
  for i in result :
  
    print ("Nama : %s"%i[1])
    print ("Nomerhp : %s"%i[2])
    print ("Email : %s"%i[3])
    print ("Lomba : %s"%i[4])
    print ("------------------------------")
    
  

def tambah(conn) :
  nama = input("Masukkan nama : ")
  nomerhp = input("Masukkan nomerhp : ")
  email = input("Masukkan email : ")
  lomba = input("Lomba yang ingin diikuti : ")
  val = (nama, nomerhp, email, lomba)
  cursor = conn.cursor()
  sql = "INSERT INTO peserta (nama, nomerhp, email, lomba) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql,val)
  result = conn.commit()
  print(cursor.rowcount, "Data berhasil ditambah\n")
  time.sleep(1)
  lihat(conn)
  
def ubah(conn) :
  UbahNama = input("Masukkan nama peserta yang ingin diubah : ")
  nama = input("Ubah nama : ")
  nomerhp = input("Ubah nomerhp : ")
  email = input("Ubah email : ")
  lomba = input("Ubah lomba : ")
  
  sql = "UPDATE peserta SET nama = %s, nomerhp = %s, email = %s, lomba = %s WHERE nama=%s"
  val = (nama, nomerhp, email, lomba, UbahNama)
  cursor = conn.cursor()
  cursor.execute(sql, val)
  result = conn.commit()
  print(cursor.rowcount, "Data berhasil diubah\n")
  time.sleep(1)
  lihat(conn)
  
def hapus(conn) : 
  HapusNama = input("Masukkan nama yang ingin dihapus : ")
  sql = "DELETE FROM peserta WHERE nama = %s"
  val = (HapusNama,)
  konfirm = input("Yakin?Y/N : ")
  if konfirm.lower() == "y" :
    cursor = conn.cursor()
    cursor.execute(sql,val)
    result = conn.commit()
    print(cursor.rowcount, "Data berhasil dihapus\n")
    time.sleep(1)
    lihat(conn)
  elif konfirm.lower() == "n" :
    menu()
    lihat(conn)
  else:
    sys.exit()
    
  
  
  
  
  
  
  

def kembali() :
  kembali = input("Kembali?Y/N : ")
  if kembali.lower() == "y" :
    menu()
    main()
  elif kembali.lower() == "n" :
    sys.exit()
  else :
    sys.exit()
    


def menu() : 
  os.system('clear')
  print ("Data peserta lomba 2021")
  print ("1. Lihat data peserta")
  print ("2. Tambahkan data peserta")
  print ("3. Hapus data peserta")
  print ("4. Ubah data peserta")
  print ("5. Keluar")

def main() :
  try:
    pilih = input("Masukkan pilihan : ")
    if pilih == "1" :
      lihat(conn)
      kembali()
    elif pilih == "2" :
      tambah(conn)
      kembali()
    elif pilih == "3" :
      hapus(conn)
      kembali()
    elif pilih == "4" :
      ubah(conn)
    elif pilih == "5" :
      sys.exit()
      kembali()
    else :
      print ("Pilihan salah")
      menu()
    
  except:
    sys.exit()
    
menu() 
main()

