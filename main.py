from mahasiswa import *

def main():
    connection = create_connection()

    while True:
        print("Menu:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            nim = input("Enter NIM: ")
            nama = input("Enter Nama: ")
            jk = input("Enter Jenis Kelamin: ")
            prodi = input("Enter Prodi: ")
            create_record(connection, nim, nama, jk, prodi)
        elif choice == "2":
            read_records(connection)
        elif choice == "3":
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
        elif choice == "4":
            id = input("Enter ID of the record to delete: ")
            delete_record(connection, id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose again.")

    close_connection(connection)

if __name__ == "__main__":
    main()
