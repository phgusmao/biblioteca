from tkinter import *
import psycopg2

janela = Tk()
janela.title("Biblioteca de Godric's Hollow")
janela.geometry("800x500+400+100")
janela["bg"] = "#088A85"

lbPrincipal = Label(janela, text = "Biblioteca de Godric's Hollow!", font=('Arial', 16, 'bold'), bg = "#088A85")
lbPrincipal.place(x = 200, y = 0)

#verificador

def display_usuario():
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="postgres",
        password="pedro2514q1",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    query = """SELECT * FROM usuario"""
    cursor.execute(query)

    row = cursor.fetchall()

    lista_usuario = Listbox(janela, width=30, height=25, bg='gray')
    #lista_usuario.place(x=5, y=150)

    for usuario in row:
        lista_usuario.insert(END, usuario[1])

    conn.commit()
    conn.close()

def verificador(cpf):
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="postgres",
        password="pedro2514q1",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    query = """SELECT * FROM usuario WHERE cpf = '{}'"""
    cursor.execute(query.format(cpf))

    row = cursor.fetchone()

    display_verificador(row)

    conn.commit()
    conn.close()

def display_verificador(row):
    if(row != None):
        label_verif = Label(janela, text="Id:", bg='#088A85', font='Arial')
        label_verif.place(x=10, y=140)
        pesquisa_verif = Listbox(janela, width=3, height=1, bg='#848484')
        pesquisa_verif.place(x=40, y=143)
        pesquisa_verif.insert(END, row[0])
        label_verif = Label(janela, text="Nome:", bg='#088A85', font='Arial')
        label_verif.place(x=80, y=140)
        pesquisa_verif = Listbox(janela, width=10, height=1, bg='#848484')
        pesquisa_verif.place(x=140, y=143)
        pesquisa_verif.insert(END, row[1])
        label_verif = Label(janela, text="CPF:", bg='#088A85', font='Arial')
        label_verif.place(x=10, y=165)
        pesquisa_verif = Listbox(janela, width=12, height=1, bg='#848484')
        pesquisa_verif.place(x=60, y=168)
        pesquisa_verif.insert(END, row[2])
        label_verif = Label(janela, text="Email:", bg='#088A85', font='Arial')
        label_verif.place(x=10, y=190)
        pesquisa_verif = Listbox(janela, width=30, height=1, bg='#848484')
        pesquisa_verif.place(x=60, y=193)
        pesquisa_verif.insert(END, row[3])
        bt_NovaJanela = Button(janela, text="Vamos aos livros!", width=20, command=lambda :janela_principal())
        bt_NovaJanela.place(x=10, y=230)
        label_apagar = Label(janela, text="", width = 30, height = 10, bg='#088A85')
        label_apagar.place(x = 10, y=270)
    else:
        lb_Nencontrado = Label(janela, text = "Usuário não encontrado", bg='#088A85', font='Arial', width=27, height=25)
        lb_Nencontrado.place(x=10, y=140)


#cadastro

def cadastrar(nome, cpf, email):
    conn = psycopg2.connect(
                     dbname = "biblioteca",
                     user = "postgres",
                     password = "pedro2514q1",
                     host = "localhost",
                     port = "5432"
    )
    cursor = conn.cursor()
    query = """INSERT INTO usuario(nome, cpf, email) VALUES (%s, %s, %s)"""
    cursor.execute(query, (nome, int(cpf), email))
    print("Data Saved")
    conn.commit()
    conn.close()
    display_usuario()


lbLogin = Label(janela, text="Nome:", font = "Arial", bg = "#088A85")
lbLogin.place(x = 255, y = 60)

entryLogin = Entry(janela)
entryLogin.place(x = 260, y = 85)

lbEmail = Label(janela, text = "Email:", font = "Arial", bg = "#088A85")
lbEmail.place(x = 255, y = 115)

entryEmail = Entry(janela)
entryEmail.place(x = 260, y = 140)

lbCpf = Label(janela, text = "CPF:", font = "Arial", bg = "#088A85")
lbCpf.place(x = 255, y = 165)

entryCpf = Entry(janela)
entryCpf.place(x = 260, y = 190)

btCadastro = Button(janela, text = "Cadastrar", width = 20, command = lambda:cadastrar(entryLogin.get(), entryCpf.get(), entryEmail.get()))
btCadastro.place(x = 250, y = 220)

#fimCadastro

lbCPF = Label(janela, text = "CPF:", font = "Arial", bg = "#088A85")
lbCPF.place(x = 10, y = 60)

entry_verif_CPF = Entry(janela)
entry_verif_CPF.place(x = 10, y = 85)

bt_verif = Button(janela, text = "Verificar", width = 20, command = lambda :verificador(entry_verif_CPF.get()))
bt_verif.place(x = 10, y = 110)

def janela_principal():
    janela = Tk()
    janela.title("Biblioteca de Godric's Hollow")
    janela.geometry("1000x600+200+100")
    janela["bg"] = "#088A85"

    def display_livros():
        conn = psycopg2.connect(
            dbname="biblioteca",
            user="postgres",
            password="pedro2514q1",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        query = """SELECT * FROM livro"""
        cursor.execute(query)

        row = cursor.fetchall()

        lista_livro = Listbox(janela, width=30, height=30, bg='#848484')
        lista_livro.place(x=5, y=93)

        for livro in row:
            lista_livro.insert(END, livro[1])

        conn.commit()
        conn.close()

    def display_alugueis():
        conn = psycopg2.connect(
            dbname="biblioteca",
            user="postgres",
            password="pedro2514q1",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        query_two = """select usuario.cpf, livro.nome from alugueis, usuario, livro where alugueis.idusuario = usuario.idusuario 
                        AND livro.idlivro = alugueis.idlivro"""
        cursor.execute(query_two)

        row = cursor.fetchall()

        lista_aluguel = Listbox(janela, width=15, height=23, bg='#848484')
        lista_aluguel.place(x=625, y=200)

        label_alugueis = Label(janela, text = "CPF's alugados:", font = ('Arial', 12, 'bold'), bg='#088A85')
        label_alugueis.place(x = 625, y = 170)

        for aluguel in row:
            lista_aluguel.insert(END, aluguel[0])

        lista_aluguel = Listbox(janela, width=30, height=23, bg='#848484')
        lista_aluguel.place(x=760, y=200)

        label_alugueis = Label(janela, text="Livros alugados:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_alugueis.place(x=760, y=170)

        for aluguel in row:
            lista_aluguel.insert(END, aluguel[1])

        conn.commit()
        conn.close()

    def search_livro(nome):
        conn = psycopg2.connect(
            dbname="biblioteca",
            user="postgres",
            password="pedro2514q1",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        query = """SELECT * FROM livro WHERE nome = '{}'"""
        cursor.execute(query.format(nome))

        row = cursor.fetchone()

        query_two = """select autor.nome from livroautor, autor, livro WHERE livro.idlivro = livroautor.idlivro
                            AND livroautor.idautor = autor.idautor AND livro.nome = '{}'"""

        cursor.execute(query_two.format(nome))

        row_two = cursor.fetchone()

        query_three = """select editora.nome from livroeditora, editora, livro WHERE livro.idlivro = livroeditora.idlivro
                            AND livroeditora.ideditora = editora.ideditora AND livro.nome = '{}'"""

        cursor.execute(query_three.format(nome))

        row_three = cursor.fetchone()

        query_four = """select generoliterario.tipo from livrogenero, generoliterario, livro WHERE livro.idlivro = livrogenero.idlivro
                            AND livrogenero.idgenero = generoliterario.idgenero 
							AND livro.nome = '{}'"""

        cursor.execute(query_four.format(nome))

        row_four = cursor.fetchone()

        query_five = """select data_aluguel, data_entrega FROM alugueis, livro
                        WHERE livro.idlivro = alugueis.idlivro 
                        AND livro.nome = '{}'"""

        cursor.execute(query_five.format(nome))

        row_five = cursor.fetchone()

        display_search_result(row, row_two, row_three, row_four, row_five)

        conn.commit()
        conn.close()

    def display_search_result(row, row_two, row_three, row_four, row_five):
        if (row != None):
            label_idlivro = Label(janela, text="Id Livro:", bg='#088A85', font='Arial')
            label_idlivro.place(x=500, y=135)
            pesquisa_idlivro = Listbox(janela, width=5, height=1, bg='#848484')
            pesquisa_idlivro.place(x=565, y=140)
            pesquisa_idlivro.insert(END, row[0])
            label_livro = Label(janela, text="Livro:", bg='#088A85', font='Arial')
            label_livro.place(x=210, y=135)
            pesquisa_nome = Listbox(janela, width=35, height=1, bg='#848484')
            pesquisa_nome.place(x=270, y=140)
            pesquisa_nome.insert(END, row[1])
            label_pagina = Label(janela, text="Páginas:", bg='#088A85', font='Arial')
            label_pagina.place(x=200, y=170)
            pesquisa_pagina = Listbox(janela, width=10, height=1, bg='#848484')
            pesquisa_pagina.place(x=270, y=175)
            pesquisa_pagina.insert(END, row[2])
            label_data = Label(janela, text="Data de publicação:", bg='#088A85', font='Arial')
            label_data.place(x=390, y=170)
            pesquisa_data = Listbox(janela, width=10, height=1, bg='#848484')
            pesquisa_data.place(x=540, y=175)
            pesquisa_data.insert(END, row[3])
            label_autor = Label(janela, text="Autor:", font='Arial', bg='#088A85')
            label_autor.place(x=210, y=205)
            lista_autor = Listbox(janela, width=20, height=1, bg='#848484')
            lista_autor.place(x=270, y=205)
            lista_autor.insert(END, row_two)
            label_editora = Label(janela, text="Editora:", font='Arial', bg='#088A85')
            label_editora.place(x=210, y=240)
            lista_editora = Listbox(janela, width=20, height=1, bg='#848484')
            lista_editora.place(x=270, y=240)
            lista_editora.insert(END, row_three)
            label_genero = Label(janela, text="Gênero:", font='Arial', bg='#088A85')
            label_genero.place(x=210, y=275)
            lista_genero = Listbox(janela, width=20, height=1, bg='#848484')
            lista_genero.place(x=270, y=275)
            lista_genero.insert(END, row_four)
            if (row[6] == 1):
                label_disp = Label(janela, text="Disponível", bg='green', font=('Arial', 12, 'bold'), width=20)
                label_disp.place(x=220, y=300)
                bt_button = Button(janela, text="Alugar!", width=10, command=lambda: display_alugar())
                bt_button.place(x=400, y=300)
            else:
                label_disp = Label(janela, text="Indisponível", bg='red', font=('Arial', 12, 'bold'), width=20)
                label_disp.place(x=220, y=300)
                bt_button = Button(janela, text="Devolver!", width=10, command=lambda: devolver(row[0]))
                bt_button.place(x=400, y=300)
                label_genero = Label(janela, text="Data de aluguel:", font='Arial', bg='#088A85')
                label_genero.place(x=400, y=240)
                lista_genero = Listbox(janela, width=10, height=1, bg='#848484')
                lista_genero.place(x=530, y=243)
                lista_genero.insert(END, row_five[0])
                label_genero = Label(janela, text="Data de entrega:", font='Arial', bg='#088A85')
                label_genero.place(x=400, y=275)
                lista_genero = Listbox(janela, width=10, height=1, bg='#848484')
                lista_genero.place(x=530, y=278)
                lista_genero.insert(END, row_five[1])
        else:
            lb_Nencontrado = Label(janela, text="Livro não encontrado", bg='#088A85', font='Arial', width=44, height=20)
            lb_Nencontrado.place(x=203, y=120)

    def alugar(idlivro, idusuario, data_aluguel, data_entrega):
        conn = psycopg2.connect(
            dbname="biblioteca",
            user="postgres",
            password="pedro2514q1",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        query = """INSERT INTO alugueis (idlivro, idusuario, data_aluguel, data_entrega) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (idlivro, idusuario, data_aluguel, data_entrega))
        query = """UPDATE livro SET disponibilidade = '0' WHERE idlivro = '{}'"""
        cursor.execute(query.format(idlivro))

        conn.commit()
        conn.close()

        display_livros()

    def display_alugar():
        lb_alugar = Label(janela, text="Para alugar um livro, preencha os campos abaixo:", font="Arial", bg="#088A85")
        lb_alugar.place(x=200, y=340)

        lb_addlivro = Label(janela, text="ID do livro:", font="Arial", bg="#088A85")
        lb_addlivro.place(x=200, y=370)

        entry_idlivro = Entry(janela)
        entry_idlivro.place(x=285, y=373)

        lb_addusuario = Label(janela, text="ID do usuario:", font="Arial", bg="#088A85")
        lb_addusuario.place(x=200, y=400)

        entry_idusuario = Entry(janela)
        entry_idusuario.place(x=300, y=405)

        lb_adddataaluguel = Label(janela, text="Data de aluguel:", font="Arial", bg="#088A85")
        lb_adddataaluguel.place(x=200, y=430)

        entry_adddataaluguel = Entry(janela)
        entry_adddataaluguel.place(x=320, y=433)

        lb_addentrega = Label(janela, text="Data de entrega:", font="Arial", bg="#088A85")
        lb_addentrega.place(x=200, y=460)

        entry_addentrega = Entry(janela)
        entry_addentrega.place(x=320, y=463)

        bt_alugel = Button(janela, text="Alugar", width=20,
                           command=lambda: alugar(entry_idlivro.get(), entry_idusuario.get(), entry_adddataaluguel.get(), entry_addentrega.get()))
        bt_alugel.place(x=240, y=510)

    def devolver(idlivro):
        conn = psycopg2.connect(
            dbname="biblioteca",
            user="postgres",
            password="pedro2514q1",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        query = """DELETE FROM alugueis WHERE idlivro = '{}' """
        cursor.execute(query.format(idlivro))
        query = """UPDATE livro SET disponibilidade = '1' WHERE idlivro = '{}'"""
        cursor.execute(query.format(idlivro))
        conn.commit()
        conn.close()
        display_livros()

    def janela_addbook():
        janela = Tk()
        janela.title("Biblioteca de Godric's Hollow")
        janela.geometry("1100x500+200+100")
        janela["bg"] = "#088A85"

        lbPrincipal = Label(janela, text="Biblioteca de Godric's Hollow!", font=('Arial', 16, 'bold'), bg="#088A85")
        lbPrincipal.place(x=200, y=0)

        def display_autor():
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """SELECT * FROM autor"""
            cursor.execute(query)

            row = cursor.fetchall()

            label_autor_lista = Label(janela, text="Lista de autores: ", font="Arial", bg='#088A85')
            label_autor_lista.place(x=550, y=240)

            lista_autor = Listbox(janela, width=20, height=10, bg='#848484')
            lista_autor.place(x=550, y=265)

            for autor in row:
                lista_autor.insert(END, autor)

            conn.commit()
            conn.close()

        def adicionar_autor(nome, sexo):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO autor(nome, sexo) VALUES (%s, %s)"""
            cursor.execute(query, (nome, sexo))
            print("Data Saved")
            conn.commit()
            conn.close()

        def display_editora():
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """SELECT * FROM editora"""
            cursor.execute(query)

            row = cursor.fetchall()

            label_editora_lista = Label(janela, text="Lista de editoras: ", font="Arial", bg='#088A85')
            label_editora_lista.place(x=950, y=240)

            lista_editora = Listbox(janela, width=20, height=10, bg='#848484')
            lista_editora.place(x=950, y=265)

            for editora in row:
                lista_editora.insert(END, editora)

            conn.commit()
            conn.close()

        def adicionar_editora(nome):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO editora(nome) VALUES ('{}');"""
            cursor.execute(query.format(nome))
            print("Data Saved")
            conn.commit()
            conn.close()

        def display_genero():
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """SELECT * FROM generoliterario"""
            cursor.execute(query)

            row = cursor.fetchall()

            label_genero_lista = Label(janela, text="Lista de gêneros: ", font="Arial", bg='#088A85')
            label_genero_lista.place(x=750, y=240)

            lista_genero = Listbox(janela, width=20, height=10, bg='#848484')
            lista_genero.place(x=750, y=265)

            for genero in row:
                lista_genero.insert(END, genero)

            conn.commit()
            conn.close()

        def adicionar_genero(tipo):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO generoliterario(tipo) VALUES ('{}')"""
            cursor.execute(query.format(tipo))
            print("Data Saved")
            conn.commit()
            conn.close()

        # add Livro

        def salvar_livro(nome, puclibacao, pagina, nota, idioma, disponibilidade):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO livro(nome, puclibacao, pagina, nota, idioma, disponibilidade) VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (nome, puclibacao, pagina, nota, idioma, disponibilidade))
            print("Data Saved")
            conn.commit()
            conn.close()

        def adicionar_autor_ao_livro(idlivro, idautor):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            #query = """INSERT INTO livroautor(idlivro, idautor) VALUES ('{}', '{}')"""
            #cursor.execute(query.format(idlivro, idautor))
            cursor.execute(f"""INSERT INTO livroautor(idlivro, idautor) VALUES ('{(idlivro)}', '{idautor}')""")
            print("Data Saved")
            conn.commit()
            conn.close()

        def adicionar_genero_ao_livro(idlivro, idgenero):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO livrogenero(idlivro, idgenero) VALUES ('{}', '{}')"""
            cursor.execute(query.format(idlivro, idgenero))
            print("Data Saved")
            conn.commit()
            conn.close()

        def adicionar_editora_ao_livro(idlivro, ideditora):
            conn = psycopg2.connect(
                dbname="biblioteca",
                user="postgres",
                password="pedro2514q1",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            query = """INSERT INTO livroeditora(idlivro, ideditora) VALUES ('{}', '{}')"""
            cursor.execute(query.format(idlivro, ideditora))
            print("Data Saved")
            conn.commit()
            conn.close()

        # adicionar um autor

        label_autor = Label(janela, text="Adicionar autor:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_autor.place(x=550, y=50)

        label_nomeautor = Label(janela, text="Nome:", bg='#088A85')
        label_nomeautor.place(x=500, y=75)

        entry_nomeautor = Entry(janela, width=20)
        entry_nomeautor.place(x=545, y=75)

        label_sexoautor = Label(janela, text="Sexo:", bg='#088A85')
        label_sexoautor.place(x=500, y=100)

        entry_sexoautor = Entry(janela, width=20)
        entry_sexoautor.place(x=545, y=100)

        bt_addautor = Button(janela, text="Adicionar",
                             command=lambda: adicionar_autor(entry_nomeautor.get(), entry_sexoautor.get()))
        bt_addautor.place(x=545, y=125)

        # adicionar uma editora

        label_editora = Label(janela, text="Adicionar editora:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_editora.place(x=750, y=50)

        label_nomeeditora = Label(janela, text="Nome: ", bg='#088A85')
        label_nomeeditora.place(x=715, y=75)

        entry_nomeeditora = Entry(janela, width=20)
        entry_nomeeditora.place(x=760, y=75)

        bt_addeditora = Button(janela, text="Adicionar", command=lambda: adicionar_editora(entry_nomeeditora.get()))
        bt_addeditora.place(x=760, y=100)

        # adicionar um gênero

        label_genero = Label(janela, text="Adicionar gênero:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_genero.place(x=550, y=150)

        label_nomegenero = Label(janela, text="Nome: ", bg='#088A85')
        label_nomegenero.place(x=500, y=175)

        entry_nomegenero = Entry(janela, width=20)
        entry_nomegenero.place(x=545, y=175)

        bt_addgenero = Button(janela, text="Adicionar", command=lambda: adicionar_genero(entry_nomegenero.get()))
        bt_addgenero.place(x=545, y=200)

        # add Autor ao livro

        label_add_autor = Label(janela, text="Adicionar um autor ao livro:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_add_autor.place(x=10, y=215)

        label_idlivro = Label(janela, text="Id livro:", bg='#088A85')
        label_idlivro.place(x=10, y=240)

        entry_idlivro = Entry(janela, width=20)
        entry_idlivro.place(x=60, y=240)

        label_idautor = Label(janela, text="Id autor:", bg='#088A85')
        label_idautor.place(x=10, y=265)

        entry_idautor = Entry(janela, width=20)
        entry_idautor.place(x=60, y=265)

        bt_add_autor = Button(janela, text="Adicionar",command=lambda: adicionar_autor_ao_livro(entry_idlivro.get(), entry_idautor.get()))
        bt_add_autor.place(x=60, y=290)

        # add_genero ao livro

        label_add_genero = Label(janela, text="Adicionar um gênero ao livro:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_add_genero.place(x=10, y=325)

        label_idgenero = Label(janela, text="Id gênero:", bg='#088A85')
        label_idgenero.place(x=10, y=350)

        entry_idgenero = Entry(janela, width=20)
        entry_idgenero.place(x=75, y=350)

        label_idlivro = Label(janela, text="Id livro:", bg='#088A85')
        label_idlivro.place(x=10, y=375)

        entry_idlivro = Entry(janela, width=20)
        entry_idlivro.place(x=75, y=375)

        bt_add_genero = Button(janela, text="Adicionar", command=lambda :adicionar_genero_ao_livro(entry_idlivro.get(), entry_idgenero.get()))
        bt_add_genero.place(x=75, y=400)

        # add_editora ao livro

        label_add_editora = Label(janela, text = "Adicionar uma editora ao livro:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_add_editora.place(x = 250, y = 215)

        label_ideditora = Label(janela, text="Id editora:", bg='#088A85')
        label_ideditora.place(x=250, y=240)

        entry_ideditora = Entry(janela, width=20)
        entry_ideditora.place(x=310, y=240)

        label_idlivro = Label(janela, text="Id livro:", bg='#088A85')
        label_idlivro.place(x=250, y=265)

        entry_idlivro = Entry(janela, width=20)
        entry_idlivro.place(x=310, y=265)

        bt_add_editora = Button(janela, text="Adicionar", command=lambda: adicionar_editora_ao_livro(entry_idlivro.get(), entry_ideditora.get()))
        bt_add_editora.place(x=310, y=290)

        # ADICIONAR UM NOVO LIVRO

        label_add = Label(janela, text="Adicionar um novo livro:", font=('Arial', 12, 'bold'), bg='#088A85')
        label_add.place(x=150, y=50)

        label_nome = Label(janela, text="Nome:", bg='#088A85')
        label_nome.place(x=10, y=80)

        entry_nome = Entry(janela, width=20)
        entry_nome.place(x=60, y=80)

        label_publicacao = Label(janela, text="Data de publicação:", bg='#088A85')
        label_publicacao.place(x=190, y=80)

        entry_puclibacao = Entry(janela, width=20)
        entry_puclibacao.place(x=305, y=80)

        label_pagina = Label(janela, text="Páginas:", bg='#088A85')
        label_pagina.place(x=10, y=110)

        entry_pagina = Entry(janela, width=20)
        entry_pagina.place(x=60, y=110)

        label_nota = Label(janela, text="Nota:", bg='#088A85')
        label_nota.place(x=10, y=140)

        entry_nota = Entry(janela, width=20)
        entry_nota.place(x=60, y=140)

        label_idioma = Label(janela, text="Idioma:", bg='#088A85')
        label_idioma.place(x=190, y=110)

        entry_idioma = Entry(janela, width=20)
        entry_idioma.place(x=305, y=110)

        label_disponibilidade = Label(janela, text="Disponibilidade:", bg='#088A85')
        label_disponibilidade.place(x=190, y=140)

        entry_disponibilidade = Entry(janela, width=20)
        entry_disponibilidade.place(x=305, y=140)

        btPesquisar = Button(janela, text="Adicionar", width=20,
                             command=lambda: salvar_livro(entry_nome.get(), entry_puclibacao.get(), entry_pagina.get(),
                                                          entry_nota.get(), entry_idioma.get(),
                                                          entry_disponibilidade.get()))
        btPesquisar.place(x=180, y=170)

        display_editora()
        display_genero()
        display_autor()
        janela.mainloop()

    lbPrincipal = Label(janela, text="Biblioteca de Godric's Hollow!", font=('Arial', 16, 'bold'), bg='#088A85')
    lbPrincipal.place(x=185, y=0)

    lbLista = Label(janela, text="Lista do nosso acervo:", font="Arial", bg='#088A85')
    lbLista.place(x=5, y=60)

    lbPesquisar = Label(janela, text="Pesquisar por livro:", font="Arial", bg='#088A85')
    lbPesquisar.place(x=200, y=60)

    entry_livro_pesquisado = Entry(janela, width=20)
    entry_livro_pesquisado.place(x=210, y=93)

    btPesquisar = Button(janela, text="Pesquisar", width=20, command=lambda: search_livro(entry_livro_pesquisado.get()))
    btPesquisar.place(x=360, y=90)

    lb_janela_addbook = Label(janela, text="Adicionar livros à Biblioteca:", font="Arial", bg='#088A85')
    lb_janela_addbook.place(x=650, y=60)

    bt_janela_addbook = Button(janela, text="Adicionar", width=20, command=lambda: janela_addbook())
    bt_janela_addbook.place(x=650, y=90)

    display_alugueis()
    display_livros()
    janela.mainloop()

display_usuario()
janela.mainloop()








