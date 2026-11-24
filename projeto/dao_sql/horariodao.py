from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM horario"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = []
        for (id, data, confirmado, id_cliente, id_servico, id_profissional) in rows:
            
            data = datetime.strptime(data, "%d/%m/%Y %H:%M")
            obj = Horario(id, data)
            obj.set_confirmado(confirmado)
            obj.set_id_cliente(id_cliente)
            obj.set_id_servico(id_servico)
            obj.set_id_profissional(id_profissional)
            objs.append(obj)
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            id, data, confirmado, id_cliente, id_servico, id_profissional = row
            data = datetime.strptime(data, "%d/%m/%Y %H:%M")

            obj = Horario(id, data)
            obj.set_confirmado(confirmado)
            obj.set_id_cliente(id_cliente)
            obj.set_id_servico(id_servico)
            obj.set_id_profissional(id_profissional)
        else:
            obj = None

        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()