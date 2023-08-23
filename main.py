from mahasiswa import *

def main():
    connection = create_connection()
    while True:
        read_records(connection)
        print("Menu:")
        print("1 - Create | 2 - Edit | 3 - Delete | 4 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            nim = input("Enter NIM: ")
            nama = input("Enter Nama: ")
            jk = input("Enter Jenis Kelamin: ")
            prodi = input("Enter Prodi: ")
            create_record(connection, nim, nama, jk, prodi)
        elif choice == "2":
            kode = input("Enter NIM of the record to update: ")
            id, nim, nama, jk, prodi = get_record(connection, kode)
            print("Data Mahasiswa")
            print("================\n")
            print("ID:", id)
            print("NIM:", nim)
            print("Nama:", nama)
            print("Jenis Kelamin:", jk)
            print("Prodi:", prodi)
            print(" ")
            print("Edit Mahasiswa")
            print("================\n")
            new_nama = input("Enter new Nama: ")
            new_jk = input("Enter new Gender: ")
            new_prodi = input("Enter new Prodi: ")
            update_record(connection, kode, new_nama, new_jk, new_prodi)
        elif choice == "3":
            id = input("Enter ID of the record to delete: ")
            delete_record(connection, id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")

    close_connection(connection)

if __name__ == "__main__":
    main()
